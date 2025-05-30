# tests/khora_adapter/llm/test_gemini.py

from typing import Any
from unittest import mock

import pytest


@pytest.mark.parametrize(
    "response_text,expected",
    [
        ("Response from Gemini", "Response from Gemini"),
        (None, ""),
    ],
)
def test_gemini_model_complete_response(
    monkeypatch: Any, response_text: Any, expected: Any
) -> Any:
    monkeypatch.setenv("GEMINI_API_KEY", "test-key")
    mock_client = mock.Mock()
    mock_response = mock.Mock()
    mock_response.text = response_text
    mock_client.models.generate_content.return_value = (
        mock_response
    )
    with mock.patch(
        "khora_adapter.llm.gemini.model.genai.Client",
        return_value=mock_client,
    ):
        from khora_adapter.llm.config import GeminiConfig
        from khora_adapter.llm.gemini.model import (
            GeminiModel,
        )

        config = GeminiConfig(
            model="gemini-2.0", temperature=0.8
        )
        model = GeminiModel(config)

        result = model.complete("Tell me something.")
        assert result == expected

        mock_client.models.generate_content.assert_called_once_with(
            model="gemini-2.0",
            contents="Tell me something.",
        )
