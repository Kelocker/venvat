# Path to the virtual environment activation script
$venvPath = ".\venv\Scripts\activate"

# Check if the activation script exists
if (Test-Path $venvPath) {
    Write-Host "Activating virtual environment..."
    & $venvPath
} else {
    Write-Host "Virtual environment activation script not found."
}
