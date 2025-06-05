# src/khora_adapter/llm/gemini/parse.py

from typing import Any

from khora_adapter.llm.types import LLMResponse


def parse_gemini_response(
    response: Any, model: str
) -> LLMResponse:
    return LLMResponse(
        text=(
            response.text.strip() if response.text else ""
        ),
        model=model,
        raw=response.__dict__,
    )
