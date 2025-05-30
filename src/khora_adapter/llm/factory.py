# src/khora_adapter/llm/factory.py
from typing import Protocol

from khora_adapter.llm.base import LLM


class LLMFactory(Protocol):
    def build(self) -> LLM: ...
