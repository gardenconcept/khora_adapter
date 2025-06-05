# prompt.py

import json

from khora_adapter.llm.base import LLM
from khora_adapter.llm.types import LLMResponse


def generate(prompt: str, model: LLM) -> LLMResponse:
    return model.complete(prompt)


def format_response(
    response: LLMResponse, format: str
) -> str:
    if format == "json":
        return json.dumps(
            {
                "text": response.text,
                "model": response.model,
                "prompt_tokens": response.prompt_tokens,
                "completion_tokens": response.completion_tokens,
                "elapsed": response.elapsed,
            },
            indent=2,
        )

    if format == "full":
        return json.dumps(
            response.__dict__, indent=2, default=str
        )

    return response.text


def run(
    prompt: str, model: LLM, format: str = "text"
) -> str:
    response = generate(prompt, model)
    return format_response(response, format)
