#!/bin/bash

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print status messages
print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

# Function to print success messages
print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

# Function to print error messages
print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Function to check if command was successful
check_error() {
    if [ $? -ne 0 ]; then
        print_error "$1"
        exit 1
    fi
}

# Main installation process
main() {
    print_status "Starting installation process..."

    # Check if uv is installed
    if ! command -v uv &> /dev/null; then
        print_error "uv is not installed. Please install it first:"
        echo "curl -LsSf https://astral.sh/uv/install.sh | sh"
        exit 1
    fi

    # Create virtual environment
    print_status "Creating virtual environment..."
    uv venv
    check_error "Failed to create virtual environment"
    print_success "Virtual environment created successfully"

    # Activate virtual environment
    print_status "Activating virtual environment..."
    source .venv/bin/activate
    check_error "Failed to activate virtual environment"
    print_success "Virtual environment activated"

    # Install MCP CLI
    print_status "Installing MCP CLI..."
    uv add "mcp[cli]"
    check_error "Failed to install MCP CLI"
    print_success "MCP CLI installed successfully"

    # Install main.py
    print_status "Installing main.py..."
    uv run mcp install main.py
    check_error "Failed to install main.py"
    print_success "main.py installed successfully"

    print_success "Installation completed successfully!"
}

# Run main function
main