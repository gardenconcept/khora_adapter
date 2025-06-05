from collections.abc import Callable
from time import time
from typing import TypeVar

T = TypeVar("T")


def with_elapsed[T](
    func: Callable[[], T],
) -> tuple[T, float]:
    start = time()
    result = func()
    return result, time() - start
