# tests/conftest.py

from typing import (
    Any,
)
from unittest.mock import (
    patch,
)

import pytest


@pytest.fixture(
    autouse=True,
    scope="session",
)
def patch_openai_import() -> Any:
    with patch("openai.OpenAI") as mock_openai:
        yield mock_openai
