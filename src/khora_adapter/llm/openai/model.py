from khora_adapter.llm.base import LLM
from khora_adapter.llm.config import OpenAIConfig


class OpenAIModel(LLM):
    def __init__(self, config: OpenAIConfig) -> None:
        from openai import OpenAI

        self.config = config
        self.client = OpenAI(api_key=config.api_key)

    def complete(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model=self.config.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=self.config.temperature,
        )

        content: str | None = response.choices[
            0
        ].message.content
        return content.strip() if content else ""
