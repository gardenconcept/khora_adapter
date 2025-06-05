# src/khora_adapter/llm/base.py
from typing import Protocol

from khora_adapter.llm.types import LLMResponse


class LLM(Protocol):
    def complete(self, prompt: str) -> LLMResponse: ...
