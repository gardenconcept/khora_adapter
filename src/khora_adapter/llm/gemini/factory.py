# src/khora_adapter/llm/gemini/factory.py
import os

from khora_adapter.llm.base import LLM
from khora_adapter.llm.gemini.config import GeminiConfig
from khora_adapter.llm.gemini.model import GeminiModel


class GeminiModelFactory:
    def __init__(
        self, model: str, temperature: float
    ) -> None:
        self.model = (
            model or "gemini-2.5-flash-preview-05-20"
        )
        self.temperature = temperature

    def build(self) -> LLM:
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise RuntimeError(
                "Missing GEMINI_API_KEY in environment."
            )

        config = GeminiConfig(
            api_key=api_key,
            model=self.model,
            temperature=self.temperature,
        )
        return GeminiModel(config)
