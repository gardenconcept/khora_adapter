import argparse

from dotenv import load_dotenv

from khora_adapter.cli import get_prompt, parse_args
from khora_adapter.llm.registry import get_factory
from khora_adapter.prompt import run

# from khora_adapter.messages import PromptMessage

def main() -> None:
    load_dotenv()
    args = parse_args()
    prompt = get_prompt(args)
    model = get_factory(args).build()
    print(run(prompt, model))


if __name__ == "__main__":
    main()
