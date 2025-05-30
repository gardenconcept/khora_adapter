# show_clean_structure.ps1

$excludeDirs = @(
    '__pycache__',
    '.venv',
    'env',
    'venv',
    '.mypy_cache',
    '.pytest_cache',
    '.vscode',
    '.idea',
    '.git',
    '.coverage',
    'htmlcov',
    '.cache',
    'artifacts',
    '.ruff_cache',
    'qol_scripts',
    'docs'
    '.poetry'
)

Get-ChildItem -Recurse -File | Where-Object {
    $full = $_.FullName
    $excludeDirs -notcontains ($_.Directory.Name) -and
    ($excludeDirs | Where-Object { $full -notmatch "\\$_(\\|$)" }).Count -eq $excludeDirs.Count
} | ForEach-Object {
    $_.FullName.Replace((Get-Location).Path + "\", "")
}
