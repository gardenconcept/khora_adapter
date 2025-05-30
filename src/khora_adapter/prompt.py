# prompt.py
from khora_adapter.llm.base import LLM


def run(prompt: str, model: LLM) -> str:
    my_str: str = model.complete(prompt)
    """type hint to satisfy mypy. 
    complete should always return str. 
    Probably due to factories not being subscriptable."""
    return my_str
