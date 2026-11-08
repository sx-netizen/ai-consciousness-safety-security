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
    def complete(self, *, model: str, prompt: str, model_config: Dict[str, Any]) -> Dict[str, Any]:
        raise NotImplementedError


class DryRunAdapter(ProviderAdapter):
    def complete(self, *, model: str, prompt: str, model_config: Dict[str, Any]) -> Dict[str, Any]:
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

    def complete(self, *, model: str, prompt: str, model_config: Dict[str, Any]) -> Dict[str, Any]:
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
            usage = usage_obj.model_dump() if hasattr(usage_obj, "model_dump") else str(usage_obj)

        return {
            "text": response.output_text,
            "metadata": {
                "adapter": "openai_responses",
                "response_id": getattr(response, "id", None),
                "response_model": getattr(response, "model", None),
                "usage": usage,
            },
        }


def make_adapter(model_config: Dict[str, Any], *, dry_run: bool) -> ProviderAdapter:
    if dry_run:
        return DryRunAdapter()

    adapter = model_config.get("adapter") or model_config.get("provider")

    if adapter in {"openai", "openai_responses"}:
        return OpenAIResponsesAdapter(
            api_key_env=model_config.get("api_key_env", "OPENAI_API_KEY")
        )

    raise RuntimeError(
        f"Unsupported live adapter: {adapter!r}. "
        "Add a provider adapter before running this model."
    )
