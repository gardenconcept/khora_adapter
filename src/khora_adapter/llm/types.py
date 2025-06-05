# src/khora_adapter/llm/types.py

from dataclasses import dataclass
from typing import Any


@dataclass
class LLMResponse:
    text: str
    prompt_tokens: int | None = None
    completion_tokens: int | None = None
    model: str | None = None
    elapsed: float | None = None  # Seconds
    raw: dict[str, Any] | None = None
