# 10x Marketing & Sales Skill - Windows Installation Script
# Usage: irm https://raw.githubusercontent.com/AnitChaudhry/10x-marketing-and-sales-skill/main/.claude/skills/10x-team/install.ps1 | iex

$ErrorActionPreference = "Stop"

Write-Host "🚀 10x Marketing & Sales Skill Installer" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check for required tools
function Check-Requirements {
    Write-Host "Checking requirements..." -ForegroundColor Yellow

    # Check git
    if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
        Write-Host "Error: git is not installed" -ForegroundColor Red
        exit 1
    }

    # Check Node.js (warning only)
    if (-not (Get-Command node -ErrorAction SilentlyContinue)) {
        Write-Host "Warning: Node.js not found. Visual canvas won't work." -ForegroundColor Yellow
    }

    # Check Python (warning only)
    if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
        Write-Host "Warning: Python not found. Some scripts won't work." -ForegroundColor Yellow
    }

    Write-Host "✓ Requirements checked" -ForegroundColor Green
}

# Setup directories
function Setup-Directories {
    Write-Host "Setting up directories..." -ForegroundColor Yellow

    $claudeSkillsDir = "$env:USERPROFILE\.claude\skills"
    $workspaceDir = "$env:USERPROFILE\10x-skill-workspace"

    New-Item -ItemType Directory -Force -Path $claudeSkillsDir | Out-Null
    New-Item -ItemType Directory -Force -Path "$workspaceDir\input" | Out-Null
    New-Item -ItemType Directory -Force -Path "$workspaceDir\output" | Out-Null
    New-Item -ItemType Directory -Force -Path "$workspaceDir\projects" | Out-Null
    New-Item -ItemType Directory -Force -Path "$workspaceDir\credentials" | Out-Null

    Write-Host "✓ Directories created" -ForegroundColor Green
}

# Clone repository
function Clone-Repo {
    Write-Host "Downloading 10x Marketing & Sales Skill..." -ForegroundColor Yellow

    $tempDir = New-TemporaryFile | ForEach-Object { Remove-Item $_; New-Item -ItemType Directory -Path $_ }

    git clone --depth 1 https://github.com/AnitChaudhry/10x-marketing-and-sales-skill.git $tempDir 2>$null

    # Copy skill
    $skillSource = Join-Path $tempDir ".claude\skills\10x-team"
    $skillDest = "$env:USERPROFILE\.claude\skills\10x-team"

    if (Test-Path $skillSource) {
        Copy-Item -Path $skillSource -Destination $skillDest -Recurse -Force
    }

    # Copy canvas
    $canvasSource = Join-Path $tempDir "canvas"
    $canvasDest = "$env:USERPROFILE\10x-skill-workspace\canvas"

    if (Test-Path $canvasSource) {
        Copy-Item -Path $canvasSource -Destination $canvasDest -Recurse -Force
    }

    # Cleanup
    Remove-Item -Recurse -Force $tempDir

    Write-Host "✓ Skill installed" -ForegroundColor Green
}

# Install canvas dependencies
function Install-Canvas {
    if (Get-Command node -ErrorAction SilentlyContinue) {
        Write-Host "Installing visual canvas dependencies..." -ForegroundColor Yellow

        $canvasDir = "$env:USERPROFILE\10x-skill-workspace\canvas"

        if (Test-Path $canvasDir) {
            Push-Location $canvasDir
            npm install --silent 2>$null
            Pop-Location
            Write-Host "✓ Canvas dependencies installed" -ForegroundColor Green
        }
    }
}

# Create environment template
function Create-EnvTemplate {
    Write-Host "Creating environment template..." -ForegroundColor Yellow

    $envFile = "$env:USERPROFILE\10x-skill-workspace\.env.example"

    if (-not (Test-Path $envFile)) {
        @"
# 10x Marketing & Sales Skill - Environment Variables

# Gmail OAuth2 (for email features)
GOOGLE_CLIENT_ID=your_client_id
GOOGLE_CLIENT_SECRET=your_secret
SENDER_EMAIL=your@gmail.com
SENDER_NAME=Your Name

# Exa AI (for discovery)
EXA_API_KEY=your_exa_key

# Canva API (for design features)
CANVA_CLIENT_ID=your_client_id
CANVA_CLIENT_SECRET=your_client_secret
CANVA_ACCESS_TOKEN=your_token

# Gemini API (for multimodal)
GEMINI_API_KEY=your_gemini_key

# Rate Limits (optional)
LINKEDIN_CONNECTIONS_PER_DAY=20
TWITTER_FOLLOWS_PER_DAY=50
INSTAGRAM_FOLLOWS_PER_DAY=30
"@ | Out-File -FilePath $envFile -Encoding UTF8

        Write-Host "✓ Environment template created" -ForegroundColor Green
    }
}

# Main installation
function Main {
    Write-Host ""
    Check-Requirements
    Setup-Directories
    Clone-Repo
    Install-Canvas
    Create-EnvTemplate

    Write-Host ""
    Write-Host "========================================" -ForegroundColor Cyan
    Write-Host "✓ Installation complete!" -ForegroundColor Green
    Write-Host ""
    Write-Host "Next steps:" -ForegroundColor Yellow
    Write-Host "  1. cd ~\10x-skill-workspace"
    Write-Host "  2. copy .env.example .env"
    Write-Host "  3. Edit .env with your API keys"
    Write-Host "  4. Run 'claude' to start Claude Code"
    Write-Host "  5. Use '/10x' to begin"
    Write-Host ""
    Write-Host "Visual Canvas (optional):" -ForegroundColor Yellow
    Write-Host "  cd ~\10x-skill-workspace\canvas; npm run dev"
    Write-Host ""
}

Main
