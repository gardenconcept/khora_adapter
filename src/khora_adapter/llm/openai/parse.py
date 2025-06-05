# src/khora_adapter/llm/openai/parse.py

from openai.types.chat import ChatCompletion

from khora_adapter.llm.types import LLMResponse


def parse_openai_response(
    response: ChatCompletion,
) -> LLMResponse:
    choice = response.choices[0]
    usage = getattr(response, "usage", None)

    return LLMResponse(
        text=(choice.message.content or "").strip(),
        prompt_tokens=getattr(
            usage, "prompt_tokens", None
        ),
        completion_tokens=getattr(
            usage, "completion_tokens", None
        ),
        model=getattr(response, "model", None),
        raw=response.model_dump(),
    )
