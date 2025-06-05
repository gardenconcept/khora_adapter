# src/khora_adapter/llm/gemini.py

from typing import Any

from khora_adapter.llm.base import LLM
from khora_adapter.llm.gemini.config import GeminiConfig
from khora_adapter.llm.gemini.parse import (
    parse_gemini_response,
)
from khora_adapter.llm.types import LLMResponse
from khora_adapter.llm.utils import with_elapsed


class GeminiModel(LLM):
    def __init__(self, config: GeminiConfig) -> None:
        from google import genai

        self.config = config
        self.client = genai.Client(api_key=config.api_key)

    def complete(self, prompt: str) -> LLMResponse:
        def call() -> Any:
            return self.client.models.generate_content(
                model=self.config.model,
                contents=prompt,
            )

        response, elapsed = with_elapsed(call)
        result = parse_gemini_response(
            response, model=self.config.model
        )
        result.elapsed = elapsed
        return result
