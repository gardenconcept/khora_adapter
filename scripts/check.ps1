function Time-Command {
    param (
        [string]$Name,
        [scriptblock]$Command
    )

    Write-Host "`nRunning $Name..."
    $start = Get-Date
    & $Command
    $end = Get-Date
    $elapsed = ($end - $start).TotalSeconds
    Write-Host "$Name took $elapsed seconds.`n"
}

Time-Command "Ruff" {
    ruff check .
}

Time-Command "Black" {
    black .
}

Time-Command "Mypy" {
    mypy src tests --cache-dir=.mypy_cache --ignore-missing-imports
}

Time-Command "Pytest" {
#    pytest --cov=khora_adapter
    pytest --cov=khora_adapter --cov-report=html:artifacts/coverage
}

