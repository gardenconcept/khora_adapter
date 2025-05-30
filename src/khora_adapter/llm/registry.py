# src/khora_adapter/llm/factory_registry.py

from argparse import Namespace

from khora_adapter.llm.factory import LLMFactory
from khora_adapter.llm.gemini.factory import (
    GeminiModelFactory,
)
from khora_adapter.llm.openai.factory import (
    OpenAIModelFactory,
)


def get_factory(args: Namespace) -> LLMFactory:
    match args.provider:
        case "openai":
            return OpenAIModelFactory(
                model=args.model,
                temperature=args.temperature,
            )
        case "gemini":
            return GeminiModelFactory(
                model=args.model,
                temperature=args.temperature,
            )
        case _:
            raise NotImplementedError(
                f"Unsupported provider '{args.provider}'"
            )
