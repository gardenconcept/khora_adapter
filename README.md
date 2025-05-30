# Khora Adapter

**Khora Adapter** provides a unified interface for interacting with multiple large language model (LLM) APIs. It abstracts away provider-specific quirks, allowing your orchestration tools to speak a consistent prompt-and-response protocol—even as underlying LLMs evolve.

---

## ✨ Features

- ✅ Provider abstraction (OpenAI, Gemini, etc.)
- ☐ Role-aware, multi-message prompts 
- ☐ Consistent metadata in responses
- ✅ Lazy import and dynamic API key resolution
- ☐ Streaming support
- ✅ Fully typed and test-covered
- ✅ Extensible with new models and protocols

---

## 📦 Installation

```bash
poetry install
cp .env.example .env  # Then add your API keys
````

---

## 🚀 Usage

```bash
poetry run khora_adapter --provider openai --model gpt-4 --text "What's the capital of France?"
```

If `--text` is omitted, it will prompt you interactively.

### Example: Multi-role Chat Prompt

```bash
poetry run khora_adapter --provider openai --model gpt-4
```

Then enter a structured prompt when prompted:

```plaintext
>>> [system] You are a helpful assistant.
>>> [user] What's the capital of France?
>>> [assistant] The capital of France is Paris.
>>> [user] And what's the capital of Germany?
```

Multi-turn prompts and roles are parsed internally or passed as structured messages from an upstream client.

---

## 🧱 Python API

```python
from khora_adapter.prompt import run
from khora_adapter.llms.registry import get_factory
from khora_adapter.messages import PromptMessage

factory = get_factory(args)
model = factory.build()

response = run(
    messages=[
        PromptMessage(role="system", content="You are a helpful assistant."),
        PromptMessage(role="user", content="Explain photosynthesis."),
    ],
    model=model,
)

print(response.text)
print(response.usage)  # Optional metadata like token count
```

---

## 💬 Structured Prompt Format

Prompts are internally converted to a list of messages like:

```python
[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What's 2 + 2?"},
]
```

These are supported natively by OpenAI, Gemini, and others.

---

## 🌊 Streaming Support

For models and clients that support it:

```python
for chunk in model.stream(messages):
    print(chunk, end="", flush=True)
```

Streaming lets downstream UIs or tools render partial output in real time.

---

## 📊 Structured Output

Responses return structured metadata:

```python
@dataclass
class LLMResponse:
    text: str
    usage: dict[str, Any] | None = None  # tokens, cost, etc.
    raw: Any = None  # Original provider response
```

> For advanced formatting (Markdown, JSON, HTML), use dedicated rendering tools or downstream formatters. Khora only provides clean, structured output.

---

## 🛠 Extending with New Providers

To add a new model:

1. Create `khora_adapter/llms/<provider>/model.py` and `factory.py`
2. Implement the `LLM` protocol
3. Register the factory in `khora_adapter.llms.registry`

Khora handles the rest.

---

## 🧪 Testing

```bash
poetry run pytest --cov
```

---

## 🧠 Philosophy

Khora is designed to stay small and stable. It **does not** attempt prompt engineering, retries, formatting, or tool use — these are the job of orchestration layers built *on top* of Khora.

Instead, Khora ensures:

* One interface to talk to any LLM
* Strong typing and safety
* Easy extension
* Predictable behavior

---

## 📁 Project Structure

```
khora_adapter/
├── cli.py                  # CLI entrypoint
├── prompt.py               # Main invocation logic
├── protocols/              # Interfaces (LLM, LLMFactory)
├── llms/                   # Provider implementations
│   ├── config.py
│   ├── registry.py
│   ├── gemini/
│   └── openai/
tests/
scripts/
```

---

## 🗝 Environment Variables

Place your API keys in `.env`:

```
OPENAI_API_KEY=sk-...
GEMINI_API_KEY=...
```

---

## 📬 Coming Soon

* ☐ Prompt templating (Jinja-like)
* ☐ Token counting utility
* ☐ Retry/backoff middleware
* ☐ Tool use + function calling support
* ☐ More providers (Claude, Mistral, Groq, Llama.cpp)

---

## License

This project is licensed under the [GNU Affero General Public License v3.0](https://www.gnu.org/licenses/agpl-3.0.html).

AGPLv3 is a strong copyleft license designed to ensure end users can access the full source code of server-side software.

### Commercial Licensing

If you are a for-profit company interested in a commercial license that permits use without AGPL obligations, please [contact the author](mailto:sudoku-king-gender@duck.com).

(Note: Dual licensing is not currently offered, but we reserve the right to do so in the future.)
