if (-not (Test-Path ".venv")) {
    Write-Host "Criando o ambiente virtual (.venv)..." -ForegroundColor Yellow
    python -m venv .venv
}
Write-Host "Instalando dependências do requirements.txt..." -ForegroundColor Yellow
.\.venv\Scripts\pip install -r requirements.txt

Write-Host "Ativando o ambiente virtual..." -ForegroundColor Green
.\.venv\Scripts\Activate.ps1
