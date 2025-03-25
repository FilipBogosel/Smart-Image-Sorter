<#
.SYNOPSIS
Installation script for Smart Image Sorter with GPU support option

.DESCRIPTION
This script will:
1. Install Python 3.12 if needed
2. Clone GitHub repository
3. Set up virtual environment
4. Install dependencies
5. Download RetinaNet model
6. Run the organizer program

.PARAMETER GpuSupport
Type "GPU" to enable CUDA acceleration (requires compatible NVIDIA GPU)

.EXAMPLE
.\install.ps1 GPU
#>

param(
    [Parameter(Mandatory=$false)]
    [string]$GpuSupport
)

# Error handling setup
$ErrorActionPreference = "Stop"

# 1. Python installation check
function Install-Python {
    Write-Host "Checking Python installation..."
    try {
        $python = (Get-Command python -ErrorAction SilentlyContinue).Path
        if (-not $python) {
            Write-Host "Installing Python 3.12..."
            $installer = "$env:TEMP\python-3.12.0-amd64.exe"
            Invoke-WebRequest -Uri "https://www.python.org/ftp/python/3.12.0/python-3.12.0-amd64.exe" -OutFile $installer
            Start-Process -Wait -FilePath $installer -ArgumentList "/quiet InstallAllUsers=1 PrependPath=1"
            Remove-Item $installer
        }
    }
    catch {
        Write-Host "Error installing Python: $_"
        exit 1
    }
}


# 2. Dependency installation
function Install-Dependencies {
    param([bool]$UseCuda)
    
    Write-Host "Creating virtual environment..."
    python -m venv venv
    .\venv\Scripts\activate

    Write-Host "Installing base dependencies..."
    pip install imageai opencv-python tqdm pillow

    if ($UseCuda) {
        Write-Host "Installing CUDA-enabled PyTorch..."
        pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
    }
    else {
        Write-Host "Installing CPU-only PyTorch..."
        pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
    }
}

# 3. Model download
function Download-Model {
    Write-Host "Downloading RetinaNet model..."
    $modelDir = ".\models"
    $modelPath = "$modelDir\retinanet_resnet50_fpn_coco-eeacb38b.pth"
    
    if (-not (Test-Path $modelPath)) {
        New-Item -ItemType Directory -Path $modelDir -Force | Out-Null
        Invoke-WebRequest -Uri "https://github.com/OlafenwaMoses/ImageAI/releases/download/3.0.0-pretrained/retinanet_resnet50_fpn_coco-eeacb38b.pth" -OutFile $modelPath
    }
}

# 4.Main execution flow
try {
    $useCuda = ($GpuSupport -eq "GPU")
    
    # Installation steps
    Install-Python
    Clone-Repository
    Install-Dependencies -UseCuda $useCuda
    Download-Model

    # Run the program
    Write-Host "Starting image organization..."
    .\venv\Scripts\activate
    cd .\src
    python organise_photos.py
    
    Write-Host "Operation completed successfully!" -ForegroundColor Green
}
catch {
    Write-Host "Error occurred: $_" -ForegroundColor Red
    exit 1
}
