# tests/khora_adapter/llm/test_factory_registry.py

from argparse import Namespace

import pytest

from khora_adapter.llm.gemini.factory import (
    GeminiModelFactory,
)
from khora_adapter.llm.openai.factory import (
    OpenAIModelFactory,
)
from khora_adapter.llm.registry import get_factory


def make_args(provider: str) -> Namespace:
    return Namespace(
        provider=provider,
        model="test-model",
        temperature=0.5,
    )


def test_get_factory_openai() -> None:
    args = make_args("openai")
    factory = get_factory(args)
    assert isinstance(factory, OpenAIModelFactory)


def test_get_factory_gemini() -> None:
    args = make_args("gemini")
    factory = get_factory(args)
    assert isinstance(factory, GeminiModelFactory)


def test_get_factory_unsupported() -> None:
    args = make_args("plarghhh")
    with pytest.raises(
        NotImplementedError,
        match="Unsupported provider 'plarghhh'",
    ):
        get_factory(args)
