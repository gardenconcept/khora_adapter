# scripts/check.ps1
Write-Host "Running Ruff..."
poetry run ruff check .

Write-Host "Checking formatting with Black..."
poetry run black .

Write-Host "Running Mypy..."
poetry run mypy src tests --cache-dir=.mypy_cache --ignore-missing-imports

Write-Host "Running Pytest..."
poetry run pytest --cov=khora_adapter --cov-report=html:artifacts/coverage
