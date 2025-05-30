# src/khora_adapter/llm/gemini.py


from google import genai

from khora_adapter.llm.base import LLM
from khora_adapter.llm.config import GeminiConfig


class GeminiModel(LLM):
    def __init__(self, config: GeminiConfig) -> None:

        self.config = config
        self.client = genai.Client(api_key=config.api_key)

    def complete(self, prompt: str) -> str:
        response = self.client.models.generate_content(
            model=self.config.model,
            contents=prompt,
        )
        return (
            response.text.strip() if response.text else ""
        )
