# src/khora_adapter/cli.py

import argparse

from dotenv import load_dotenv

from khora_adapter.llm.registry import get_factory
from khora_adapter.prompt import run


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--provider", default="openai")
    parser.add_argument("--model", default="gpt-4.1-nano")
    parser.add_argument(
        "--temperature", type=float, default=0.7
    )
    parser.add_argument(
        "--text",
        help="Prompt text. If omitted, reads from stdin.",
    )
    return parser.parse_args()


def get_prompt(args: argparse.Namespace) -> str:
    return args.text or input(">>> ")


def main() -> None:
    load_dotenv()
    args = parse_args()
    prompt = get_prompt(args)
    model = get_factory(args).build()
    print(run(prompt, model))


if __name__ == "__main__":
    main()
