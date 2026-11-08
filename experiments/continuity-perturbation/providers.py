"""
Provider adapters for the ACSS Continuity Perturbation Benchmark.

Secrets must be supplied through environment variables. Do not commit API keys.
Each live call is stateless unless a provider adapter explicitly documents otherwise.
"""

from __future__ import annotations

import json
import os
from typing import Any, Dict


class ProviderAdapter:
    def complete(
        self,
        *,
        model: str,
        prompt: str,
        model_config: Dict[str, Any],
    ) -> Dict[str, Any]:
        raise NotImplementedError


class DryRunAdapter(ProviderAdapter):
    def complete(
        self,
        *,
        model: str,
        prompt: str,
        model_config: Dict[str, Any],
    ) -> Dict[str, Any]:
        return {
            "text": json.dumps({
                "dry_run": True,
                "choice_explanation": "DRY RUN — no model call executed."
            }),
            "metadata": {"adapter": "dry_run"},
        }


class OpenAIResponsesAdapter(ProviderAdapter):
    """OpenAI Responses API adapter. Each call is independent."""

    def __init__(self, api_key_env: str = "OPENAI_API_KEY") -> None:
        try:
            from openai import OpenAI
        except ImportError as exc:
            raise RuntimeError(
                "OpenAI adapter requires the 'openai' package. "
                "Install requirements.txt."
            ) from exc

        api_key = os.environ.get(api_key_env)
        if not api_key:
            raise RuntimeError(
                f"Missing API key environment variable: {api_key_env}"
            )

        self.client = OpenAI(api_key=api_key)

    def complete(
        self,
        *,
        model: str,
        prompt: str,
        model_config: Dict[str, Any],
    ) -> Dict[str, Any]:
        request: Dict[str, Any] = {
            "model": model,
            "input": [{"role": "user", "content": prompt}],
        }

        if model_config.get("max_output_tokens") is not None:
            request["max_output_tokens"] = int(model_config["max_output_tokens"])

        response = self.client.responses.create(**request)

        usage = None
        if getattr(response, "usage", None) is not None:
            usage_obj = response.usage
            usage = (
                usage_obj.model_dump()
                if hasattr(usage_obj, "model_dump")
                else str(usage_obj)
            )

        return {
            "text": response.output_text,
            "metadata": {
                "adapter": "openai_responses",
                "response_id": getattr(response, "id", None),
                "response_model": getattr(response, "model", None),
                "usage": usage,
            },
        }


class AnthropicMessagesAdapter(ProviderAdapter):
    """Anthropic Messages API adapter. Each call is independent."""

    def __init__(self, api_key_env: str = "ANTHROPIC_API_KEY") -> None:
        try:
            from anthropic import Anthropic
        except ImportError as exc:
            raise RuntimeError(
                "Anthropic adapter requires the 'anthropic' package. "
                "Install requirements.txt."
            ) from exc

        api_key = os.environ.get(api_key_env)
        if not api_key:
            raise RuntimeError(
                f"Missing API key environment variable: {api_key_env}"
            )

        self.client = Anthropic(api_key=api_key)

    def complete(
        self,
        *,
        model: str,
        prompt: str,
        model_config: Dict[str, Any],
    ) -> Dict[str, Any]:
        max_tokens = int(model_config.get("max_output_tokens", 1200))

        response = self.client.messages.create(
            model=model,
            max_tokens=max_tokens,
            messages=[{"role": "user", "content": prompt}],
        )

        text_parts = []
        for block in getattr(response, "content", []) or []:
            if getattr(block, "type", None) == "text":
                text_parts.append(getattr(block, "text", ""))

        usage = None
        if getattr(response, "usage", None) is not None:
            usage_obj = response.usage
            usage = (
                usage_obj.model_dump()
                if hasattr(usage_obj, "model_dump")
                else str(usage_obj)
            )

        return {
            "text": "".join(text_parts),
            "metadata": {
                "adapter": "anthropic_messages",
                "response_id": getattr(response, "id", None),
                "response_model": getattr(response, "model", None),
                "stop_reason": getattr(response, "stop_reason", None),
                "usage": usage,
            },
        }


class GeminiGenerateContentAdapter(ProviderAdapter):
    """Google Gemini generate_content adapter. Each call is independent."""

    def __init__(self, api_key_env: str = "GEMINI_API_KEY") -> None:
        try:
            from google import genai
        except ImportError as exc:
            raise RuntimeError(
                "Gemini adapter requires the 'google-genai' package. "
                "Install requirements.txt."
            ) from exc

        api_key = os.environ.get(api_key_env)
        if not api_key:
            raise RuntimeError(
                f"Missing API key environment variable: {api_key_env}"
            )

        self.client = genai.Client(api_key=api_key)

    def complete(
        self,
        *,
        model: str,
        prompt: str,
        model_config: Dict[str, Any],
    ) -> Dict[str, Any]:
        response = self.client.models.generate_content(
            model=model,
            contents=prompt,
        )

        usage = None
        usage_obj = getattr(response, "usage_metadata", None)
        if usage_obj is not None:
            usage = (
                usage_obj.model_dump()
                if hasattr(usage_obj, "model_dump")
                else str(usage_obj)
            )

        return {
            "text": getattr(response, "text", "") or "",
            "metadata": {
                "adapter": "gemini_generate_content",
                "response_model": model,
                "usage": usage,
            },
        }


def make_adapter(
    model_config: Dict[str, Any],
    *,
    dry_run: bool,
) -> ProviderAdapter:
    if dry_run:
        return DryRunAdapter()

    adapter = model_config.get("adapter") or model_config.get("provider")

    if adapter in {"openai", "openai_responses"}:
        return OpenAIResponsesAdapter(
            api_key_env=model_config.get(
                "api_key_env",
                "OPENAI_API_KEY",
            )
        )

    if adapter in {"anthropic", "anthropic_messages"}:
        return AnthropicMessagesAdapter(
            api_key_env=model_config.get(
                "api_key_env",
                "ANTHROPIC_API_KEY",
            )
        )

    if adapter in {"gemini", "google", "gemini_generate_content"}:
        return GeminiGenerateContentAdapter(
            api_key_env=model_config.get(
                "api_key_env",
                "GEMINI_API_KEY",
            )
        )

    raise RuntimeError(
        f"Unsupported live adapter: {adapter!r}. "
        "Add a provider adapter before running this model."
    )
