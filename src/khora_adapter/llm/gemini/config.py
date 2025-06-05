# src/khora_adapter/llm/gemini/config.py

from dataclasses import dataclass


@dataclass
class GeminiConfig:
    api_key: str | None = None
    model: str = "gemini-2.5-flash-preview-05-20"
    temperature: float = 0.7
