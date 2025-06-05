# tests/khora_adapter/llm/test_gemini_factory.py

import os
from typing import Any
from unittest import mock

import pytest

from khora_adapter.llm.gemini.factory import (
    GeminiModelFactory,
)
from khora_adapter.llm.gemini.model import GeminiModel


@mock.patch("google.genai.Client")
def test_gemini_model_factory_build(
    mock_client: Any,
) -> None:

    os.environ["GEMINI_API_KEY"] = "fake-key"
    factory = GeminiModelFactory(
        model="gemini-test", temperature=0.3
    )

    model = factory.build()

    assert isinstance(model, GeminiModel)
    assert model.config.api_key == "fake-key"
    assert model.config.model == "gemini-test"
    assert model.config.temperature == 0.3
    mock_client.assert_called_once_with(api_key="fake-key")


def test_gemini_factory_raises_if_no_api_key(
    monkeypatch: Any,
) -> None:
    # Ensure the environment variable is not set
    monkeypatch.delenv("GEMINI_API_KEY", raising=False)

    factory = GeminiModelFactory(
        model="test-model", temperature=0.5
    )

    with pytest.raises(
        RuntimeError,
        match="Missing GEMINI_API_KEY in environment.",
    ):
        factory.build()
