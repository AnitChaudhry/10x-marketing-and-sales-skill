#!/bin/bash
# 10x Marketing & Sales Skill - Installation Script
# Usage: curl -fsSL https://raw.githubusercontent.com/AnitChaudhry/10x-marketing-and-sales-skill/main/.claude/skills/10x-team/install.sh | bash

set -e

echo "🚀 10x Marketing & Sales Skill Installer"
echo "========================================"
echo ""

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check for required tools
check_requirements() {
    echo "Checking requirements..."

    if ! command -v git &> /dev/null; then
        echo -e "${RED}Error: git is not installed${NC}"
        exit 1
    fi

    if ! command -v node &> /dev/null; then
        echo -e "${YELLOW}Warning: Node.js not found. Visual canvas won't work.${NC}"
    fi

    if ! command -v python3 &> /dev/null; then
        echo -e "${YELLOW}Warning: Python 3 not found. Some scripts won't work.${NC}"
    fi

    echo -e "${GREEN}✓ Requirements checked${NC}"
}

# Create directories
setup_directories() {
    echo "Setting up directories..."

    mkdir -p ~/.claude/skills
    mkdir -p ~/10x-skill-workspace/{input,output,projects,credentials}

    echo -e "${GREEN}✓ Directories created${NC}"
}

# Clone or update repository
clone_repo() {
    echo "Downloading 10x Marketing & Sales Skill..."

    TEMP_DIR=$(mktemp -d)
    git clone --depth 1 https://github.com/AnitChaudhry/10x-marketing-and-sales-skill.git "$TEMP_DIR"

    # Copy skill to Claude skills directory
    cp -r "$TEMP_DIR/.claude/skills/10x-team" ~/.claude/skills/

    # Copy canvas to workspace (optional)
    if [ -d "$TEMP_DIR/canvas" ]; then
        cp -r "$TEMP_DIR/canvas" ~/10x-skill-workspace/
    fi

    # Cleanup
    rm -rf "$TEMP_DIR"

    echo -e "${GREEN}✓ Skill installed${NC}"
}

# Install canvas dependencies
install_canvas() {
    if command -v node &> /dev/null; then
        echo "Installing visual canvas dependencies..."

        if [ -d ~/10x-skill-workspace/canvas ]; then
            cd ~/10x-skill-workspace/canvas
            npm install --silent
            echo -e "${GREEN}✓ Canvas dependencies installed${NC}"
        fi
    fi
}

# Create .env template
create_env_template() {
    echo "Creating environment template..."

    if [ ! -f ~/10x-skill-workspace/.env ]; then
        cat > ~/10x-skill-workspace/.env.example << 'EOF'
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
EOF
        echo -e "${GREEN}✓ Environment template created${NC}"
    fi
}

# Main installation
main() {
    echo ""
    check_requirements
    setup_directories
    clone_repo
    install_canvas
    create_env_template

    echo ""
    echo "========================================"
    echo -e "${GREEN}✓ Installation complete!${NC}"
    echo ""
    echo "Next steps:"
    echo "  1. cd ~/10x-skill-workspace"
    echo "  2. cp .env.example .env"
    echo "  3. Edit .env with your API keys"
    echo "  4. Run 'claude' to start Claude Code"
    echo "  5. Use '/10x' to begin"
    echo ""
    echo "Visual Canvas (optional):"
    echo "  cd ~/10x-skill-workspace/canvas && npm run dev"
    echo ""
}

main
