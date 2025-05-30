# fix.ps1
Write-Host "Running Ruff..."
ruff check --fix .

Write-Host "Running Black..."
black .
