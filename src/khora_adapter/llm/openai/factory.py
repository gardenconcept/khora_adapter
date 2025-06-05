# src/khora_adapter/llm/openai/factory.py
import os

from khora_adapter.llm.base import LLM
from khora_adapter.llm.openai.config import OpenAIConfig
from khora_adapter.llm.openai.model import OpenAIModel


class OpenAIModelFactory:
    def __init__(
        self, model: str, temperature: float
    ) -> None:
        self.model = model or "gpt-4.1-nano"
        self.temperature = temperature

    def build(self) -> LLM:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise RuntimeError(
                "Missing OPENAI_API_KEY in environment."
            )

        config = OpenAIConfig(
            api_key=api_key,
            model=self.model,
            temperature=self.temperature,
        )
        return OpenAIModel(config)
