# src/khora_adapter/llm/openai/config.py

from dataclasses import dataclass


@dataclass
class OpenAIConfig:
    api_key: str | None = None
    model: str = "gpt-4.1-nano"
    temperature: float = 0.7
