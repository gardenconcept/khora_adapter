# src/khora_adapter/llm/openai/model.py

from typing import Any

from khora_adapter.llm.base import LLM
from khora_adapter.llm.openai.config import OpenAIConfig
from khora_adapter.llm.openai.parse import (
    parse_openai_response,
)
from khora_adapter.llm.types import LLMResponse
from khora_adapter.llm.utils import with_elapsed


class OpenAIModel(LLM):
    def __init__(self, config: OpenAIConfig) -> None:
        from openai import OpenAI

        self.config = config
        self.client = OpenAI(api_key=config.api_key)

    def complete(self, prompt: str) -> LLMResponse:
        def call() -> Any:
            return self.client.chat.completions.create(
                model=self.config.model,
                messages=[
                    {"role": "user", "content": prompt}
                ],
                temperature=self.config.temperature,
            )

        response, elapsed = with_elapsed(call)
        result = parse_openai_response(response)
        result.elapsed = elapsed
        return result
