# tests/khora_adapter/llm/test_openai_model.py

from typing import Any
from unittest import mock

import pytest


@pytest.mark.parametrize(
    "response_text,expected",
    [
        ("Response from OpenAI", "Response from OpenAI"),
        (None, ""),
    ],
)
def test_openai_model_complete_response(
    monkeypatch: Any,
    response_text: Any,
    expected: Any,
) -> Any:
    monkeypatch.setenv(
        "OPENAI_API_KEY",
        "test-key",
    )

    mock_client = mock.Mock()
    mock_response = mock.Mock()
    mock_response.choices = [
        mock.Mock(message=mock.Mock(content=response_text))
    ]
    mock_client.chat.completions.create.return_value = (
        mock_response
    )

    with mock.patch(
        "openai.OpenAI", return_value=mock_client
    ):
        from khora_adapter.llm.openai.config import (
            OpenAIConfig,
        )
        from khora_adapter.llm.openai.model import (
            OpenAIModel,
        )

        config = OpenAIConfig(
            model="gpt-4.1",
            temperature=0.9,
        )
        model = OpenAIModel(config)

        result = model.complete("Explain khôra.")
        assert result.text == expected

        mock_client.chat.completions.create.assert_called_once_with(
            model="gpt-4.1",
            messages=[
                {
                    "role": "user",
                    "content": "Explain khôra.",
                }
            ],
            temperature=0.9,
        )
