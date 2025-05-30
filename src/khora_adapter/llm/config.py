# src/khora_adapter/llm/config.py
from dataclasses import dataclass


@dataclass
class OpenAIConfig:
    api_key: str | None = None
    model: str = "gpt-4.1-nano"
    temperature: float = 0.7


@dataclass
class GeminiConfig:
    api_key: str | None = None
    model: str = "gemini-2.5-flash-preview-05-20"
    temperature: float = 0.7
