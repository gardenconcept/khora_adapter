# src/khora_adapter/llm/base.py
from typing import Protocol


class LLM(Protocol):
    def complete(self, prompt: str) -> str:
        raise NotImplementedError
