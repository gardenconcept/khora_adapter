from typing import Any

import pytest

from khora_adapter.llm.openai.factory import (
    OpenAIModelFactory,
)


def test_openai_factory_missing_api_key(
    monkeypatch: Any,
) -> None:
    monkeypatch.delenv(
        "OPENAI_API_KEY", raising=False
    )  # ensure the env var is absent

    factory = OpenAIModelFactory(
        model="gpt-4.1-nano", temperature=0.7
    )

    with pytest.raises(
        RuntimeError,
        match="Missing OPENAI_API_KEY in environment.",
    ):
        factory.build()
