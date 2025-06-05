# src/khora_adapter/cli.py

import argparse
from typing import Any

from khora_adapter.llm.registry import get_factory
from khora_adapter.prompt import run


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--provider", default="openai")
    parser.add_argument(
        "--model", help="Model name to use"
    )
    parser.add_argument(
        "--temperature", type=float, default=0.7
    )
    parser.add_argument(
        "--text",
        help="Prompt text. If omitted, reads from stdin.",
    )
    parser.add_argument(
        "--text-file",
        help="Path to a text file containing the prompt.",
    )
    parser.add_argument(
        "--output-format",
        choices=["text", "json", "full"],
        default="text",
        help="Format for output: plain text (default), json metadata, or full debug.",
    )
    return parser.parse_args()


def get_prompt(args: argparse.Namespace) -> Any:
    if getattr(args, "text_file", None):
        with open(args.text_file, encoding="utf-8") as f:
            return f.read()
    elif getattr(args, "text", None):
        return args.text
    else:
        return input(">>> ")


def main() -> None:
    from dotenv import load_dotenv

    load_dotenv()
    args = parse_args()
    prompt = get_prompt(args)
    model = get_factory(args).build()
    print(run(prompt, model, args.output_format))


if __name__ == "__main__":
    main()
