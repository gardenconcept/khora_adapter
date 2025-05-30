# tests/test_prompt.py

import argparse
from typing import Any
from unittest import mock

from khora_adapter import cli
from khora_adapter.cli import get_prompt, parse_args
from khora_adapter.prompt import run


def test_parse_args_defaults(monkeypatch: Any) -> None:
    monkeypatch.setattr("sys.argv", ["kh-prompt"])
    args = parse_args()
    assert args.provider == "openai"
    assert args.model == "gpt-4.1-nano"
    assert args.temperature == 0.7
    assert args.text is None


def test_parse_args_with_text(monkeypatch: Any) -> None:
    monkeypatch.setattr(
        "sys.argv", ["kh-prompt", "--text", "hello"]
    )
    args = parse_args()
    assert args.text == "hello"


def test_get_prompt_from_arg() -> None:
    args = argparse.Namespace(text="What is khôra?")
    prompt = get_prompt(args)
    assert prompt == "What is khôra?"


def test_get_prompt_from_input(monkeypatch: Any) -> None:
    monkeypatch.setattr(
        "builtins.input", lambda _: "typed input"
    )
    args = argparse.Namespace(text=None)
    prompt = get_prompt(args)
    assert prompt == "typed input"


def test_run_calls_model_complete() -> None:
    mock_model = mock.Mock()
    mock_model.complete.return_value = "Mocked response"
    result = run("What's up?", mock_model)
    assert result == "Mocked response"
    mock_model.complete.assert_called_once_with(
        "What's up?"
    )


@mock.patch(
    "khora_adapter.llm.openai.model.OpenAIModel.__init__",
    return_value=None,
)
@mock.patch(
    "khora_adapter.llm.openai.model.OpenAIModel.complete",
    return_value="hello",
)
def test_main_smoke(
    mock_complete: Any,
    mock_init: Any,
    monkeypatch: Any,
    capsys: Any,
) -> None:
    monkeypatch.setattr(
        "sys.argv", ["kh-prompt", "--text", "Hi there!"]
    )
    cli.main()
    out = capsys.readouterr().out
    assert "hello" in out
