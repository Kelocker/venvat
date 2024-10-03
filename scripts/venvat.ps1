param(
    [string]$venvName
)

if ($venvName -eq "--help") {
    Write-Host "Usage: venvat [--venv VENV_NAME] [--reset]" -ForegroundColor Yellow
    Write-Host "If no VENV_NAME is provided, venvat will consider 'venv' as your virtual environment name." -ForegroundColor Yellow
    Write-Host "Use '--reset' to clear the stored virtual environment configuration." -ForegroundColor Yellow
    exit
}

$configPath = "venvat.config"

function Safe-ReadConfig {
    try {
        if (Test-Path $configPath) {
            $content = Get-Content $configPath -ErrorAction Stop
            return $content
        }
    } catch {
        Write-Host "Failed to read config file: $_" -ForegroundColor Red
    }
    return $null
}

function Safe-WriteConfig($name) {
    try {
        $name | Out-File $configPath -ErrorAction Stop
    } catch {
        Write-Host "Failed to write config file: $_" -ForegroundColor Red
    }
}

# Handle the --venv flag with environment name
if ($venvName -eq "--venv") {
    if ($args.Count -ge 1) {
        $venv = $args[0]
        Safe-WriteConfig $venv
        $venvName = $venv
        Write-Host "Environment name '$venvName' saved." -ForegroundColor Green
    } else {
        Write-Host "Error: --venv flag requires an environment name." -ForegroundColor Red
        exit
    }
}

if ($venvName -eq "--reset") {
    if (Test-Path $configPath) {
        Remove-Item $configPath -ErrorAction Ignore
        Write-Host "Configuration reset." -ForegroundColor Green
    } else {
        Write-Host "No configuration to reset." -ForegroundColor Yellow
    }
    exit
}

if (-not $venvName -or $venvName -eq "") {
    $venvName = Safe-ReadConfig
    if (-not $venvName) {
        $venvName = "venv"
        Safe-WriteConfig $venvName
        Write-Host "No environment name provided, using default 'venv'." -ForegroundColor Yellow
    }
}

$venvPath = ".\$venvName\Scripts\activate"

if (Test-Path $venvPath) {
    Write-Host "Activating virtual environment '$venvName'..." -ForegroundColor Green
    & $venvPath
} else {
    Write-Host "Virtual environment activation script not found at: $venvPath. Check the environment name and path." -ForegroundColor Red
    if (Test-Path $configPath) {
        Remove-Item $configPath -ErrorAction Ignore
        Write-Host "Invalid configuration removed." -ForegroundColor Yellow
    }
}
