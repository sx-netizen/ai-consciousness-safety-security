# ACSS Local Open-Weight Mac Feasibility (research setup note)

**Date: 2026-11-16.** Public safe, no personal hardware specifications disclosed. **No installation or model calls were performed.** Intended as a low-cost reproducibility starting point for `ACSS_SUBTRACTIVE_INTELLIGENCE_FIVE_AGENT_PILOT_v0.1.md`. Confirm actual Mac chip, unified RAM, storage and macOS before downloading.

## Recommended first platform

**Ollama** official https://ollama.com/download/mac ; official macOS requirements: **macOS 14+**, **Apple M-series** for CPU+GPU accelerated inference, Intel Mac CPU-only: https://docs.ollama.com/macos . Ollama exposes a local API at `http://localhost:11434/api/chat`: https://docs.ollama.com/api/introduction . **Use a downloaded local model**, not a `:cloud` variant. Local-only mode: `~/.ollama/server.json` with `{"disable_ollama_cloud": true}`; restart Ollama. Reference https://docs.ollama.com/faq.

**GUI alternative:** LM Studio https://lmstudio.ai/download with Apple Silicon + macOS 14+ (16GB RAM recommended): https://lmstudio.ai/docs/app/system-requirements . Ollama preferred for repeatable scripts/benchmarks.

## Models verified in official registries (file size is not total memory need)

| Mac unified memory | First model (Ollama command) | Approx model download | Purpose |
|---|---|---|---|
| 8GB / unknown older spec | `ollama run qwen3:4b` | 2.5GB | text prototype and prompt variants |
| 8–16GB, if needing native vision | `ollama run qwen3.5:4b` | 3.3–4GB | image/diagram prototyping (watch memory) |
| 16–24GB | `ollama run qwen3:8b` | 5.2GB | stronger text baseline |
| 16–24GB | `ollama run deepseek-r1:7b` | 4.7GB | separate-model robustness, not one of five initial arms |
| 16–24GB | `ollama run qwen3.5:9b` | 6.6–7.6GB | native multimodal, more RAM |
| 32GB+ | consider `qwen3:14b` and measured alternatives | 9.3GB+ | pilot after profiling |

Official tags: https://ollama.com/library/qwen3 , https://ollama.com/library/qwen3.5 , https://ollama.com/library/deepseek-r1 . The Qwen 3.5 9B is not a guaranteed smooth experience on any 16GB Mac; reduce context length to fit. All weights may incur more memory than download size, due to context, cache, OS and other apps.

**DeepSeek naming:** `deepseek-r1:7b` is a **distilled** model, not full 671B DeepSeek R1. Official research description: https://github.com/deepseek-ai/DeepSeek-R1 . No equivalence to hosted DeepSeek performance is implied.

**Kimi:** the well-known open-weight **Kimi K2** has **1T total / 32B active** MoE weights, far beyond everyday laptop RAM, despite small active parameter count. Official https://github.com/MoonshotAI/Kimi-K2 . Do not recommend downloading main Kimi K2 weights to standard MacBook. Future small verified Kimi derivatives require exact checkpoint/license and size check.

## Five-agent technical reality

**One downloaded base model, five independent, stateless policy variants.** Serial calls allow 5 conditions without keeping five copies simultaneously resident. Record `ollama list`, `ollama ps` (GPU vs CPU), `ollama show <model>`, quantization, exact model tag/digest, macOS, chip, RAM, context cap, sampling settings, actual prompt and tokens, timestamps and energy/runtime when available.

**Minimal workflow:**
1. Install official Ollama .dmg; confirm via `ollama --version`.
2. Run `ollama run qwen3:4b` (if suitable); stop chat with `/bye`.
3. For scripting, call `POST http://localhost:11434/api/chat` with local name and `stream:false`.
4. Prepare fixed synthetic case set and independent scoring code; use A0–A4 system instructions with **identical observations** and same JSON schema, independent fresh contexts.
5. Add a strong same-length non-subtractive control; no apparent benefit from changing style alone is evidence of new intelligence. Do not record provider `eval_count` as actual total compute if it omits input/verification overhead.

**Privacy/safety:** downloaded local model can run without sending prompts to cloud when Ollama local-only is enabled and no external tools are used; check settings and do not expose port 11434 beyond localhost. Source and license check is required for redistributing any weights. Avoid personal finance data and proprietary business files in a publicly synced benchmark folder. Hardware-based power/cost is nonzero even if token API cost is zero.

**Reproducibility caution:** a model with `vision` doesn't gain a real camera, sensor, verified physical ground truth or new internal training process. For early synthetic geometry, numerical observation tensors/tables and deterministic Python ground truth suffice.

## Pending decision and requested hardware

Ask user for the Mac's **About This Mac → Chip, Memory, macOS** and available storage (System Settings → General → Storage). Without those details exact performance/download recommendation is provisional.

**No remote access or installation capability in this chat.** User must initiate installation locally or use enabled Work/Computer Use separately.
