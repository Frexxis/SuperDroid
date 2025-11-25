#!/bin/bash
################################################################################
# SuperDroid Framework Installation Script
################################################################################
#
# This script installs SuperDroid Framework for Factory Droid CLI.
# It performs the following steps:
#   1. Creates necessary directories
#   2. Installs 30 slash commands to ~/.factory/commands/
#   3. Installs 16 droids to ~/.factory/droids/
#   4. Optionally copies AGENTS.md to current project
#
# Usage:
#   ./install.sh            # Interactive installation
#   ./install.sh --yes      # Non-interactive (auto-yes)
#   ./install.sh --help     # Show help
#
################################################################################

set -e

# Colors
readonly RED='\033[0;31m'
readonly GREEN='\033[0;32m'
readonly YELLOW='\033[1;33m'
readonly BLUE='\033[0;34m'
readonly CYAN='\033[0;36m'
readonly NC='\033[0m'

# Paths
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
FACTORY_DIR="$HOME/.factory"
COMMANDS_DIR="$FACTORY_DIR/commands"
DROIDS_DIR="$FACTORY_DIR/droids"

# Options
AUTO_YES=false

################################################################################
# Helper Functions
################################################################################

print_header() {
    printf "\n%b\n" "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    printf "%b\n" "${CYAN}$1${NC}"
    printf "%b\n" "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
}

print_success() {
    printf "%b\n" "${GREEN}✅ $1${NC}"
}

print_error() {
    printf "%b\n" "${RED}❌ $1${NC}"
}

print_warning() {
    printf "%b\n" "${YELLOW}⚠️  $1${NC}"
}

print_info() {
    printf "%b\n" "${BLUE}ℹ️  $1${NC}"
}

print_step() {
    printf "%b\n" "${CYAN}🔹 $1${NC}"
}

confirm() {
    if [ "$AUTO_YES" = true ]; then
        return 0
    fi
    local prompt="$1"
    read -p "$prompt [Y/n]: " -r response
    response=${response:-y}
    [[ "$response" =~ ^[Yy]$ ]]
}

################################################################################
# Installation Functions
################################################################################

check_factory_cli() {
    print_step "Checking Factory Droid CLI..."
    
    if [ -d "$FACTORY_DIR" ]; then
        print_success "Factory directory found: $FACTORY_DIR"
    else
        print_warning "Factory directory not found. Creating..."
        mkdir -p "$FACTORY_DIR"
        print_success "Created $FACTORY_DIR"
    fi
}

create_directories() {
    print_step "Creating directories..."
    
    mkdir -p "$COMMANDS_DIR"
    mkdir -p "$DROIDS_DIR"
    
    print_success "Directories ready"
}

install_commands() {
    print_step "Installing slash commands..."
    
    local source_dir="$SCRIPT_DIR/.factory/commands"
    
    if [ ! -d "$source_dir" ]; then
        print_error "Commands source directory not found: $source_dir"
        return 1
    fi
    
    local count=0
    for file in "$source_dir"/*.md; do
        if [ -f "$file" ]; then
            cp "$file" "$COMMANDS_DIR/"
            ((count++))
        fi
    done
    
    print_success "Installed $count slash commands to $COMMANDS_DIR"
}

install_droids() {
    print_step "Installing droids (subagents)..."
    
    local source_dir="$SCRIPT_DIR/.factory/droids"
    
    if [ ! -d "$source_dir" ]; then
        print_error "Droids source directory not found: $source_dir"
        return 1
    fi
    
    local count=0
    for file in "$source_dir"/*.md; do
        if [ -f "$file" ]; then
            cp "$file" "$DROIDS_DIR/"
            ((count++))
        fi
    done
    
    print_success "Installed $count droids to $DROIDS_DIR"
}

enable_custom_droids() {
    print_step "Checking custom droids setting..."
    
    local settings_file="$FACTORY_DIR/settings.json"
    
    if [ -f "$settings_file" ]; then
        if grep -q '"enableCustomDroids"' "$settings_file"; then
            if grep -q '"enableCustomDroids": true' "$settings_file"; then
                print_success "Custom droids already enabled"
            else
                print_warning "Custom droids is disabled in settings"
                print_info "Enable it via /settings or edit $settings_file"
            fi
        else
            print_warning "enableCustomDroids not found in settings"
            print_info "Enable custom droids via /settings in Droid CLI"
        fi
    else
        print_warning "Settings file not found"
        print_info "Run droid CLI once to create settings, then enable custom droids"
    fi
}

show_summary() {
    print_header "🎉 Installation Complete!"
    
    echo ""
    print_success "SuperDroid Framework installed successfully!"
    echo ""
    
    print_info "Installed components:"
    echo "  • Commands: $COMMANDS_DIR"
    echo "  • Droids:   $DROIDS_DIR"
    echo ""
    
    print_info "Next steps:"
    echo "  1. Restart Droid CLI to load new commands"
    echo "  2. Enable custom droids: /settings → Custom Droids → On"
    echo "  3. Try a command: /help"
    echo "  4. Use a droid: 'Use the pm-agent droid'"
    echo ""
    
    print_info "Available commands:"
    echo "  /research    - Deep web research"
    echo "  /implement   - Code implementation"
    echo "  /brainstorm  - Structured brainstorming"
    echo "  /test        - Testing workflows"
    echo "  /pm          - Project management"
    echo "  ... and 25 more!"
    echo ""
    
    print_info "Documentation:"
    echo "  • README.md"
    echo "  • docs/getting-started/quick-start.md"
    echo ""
    
    print_success "Happy coding with SuperDroid! 🤖"
}

################################################################################
# Main
################################################################################

show_help() {
    cat << EOF
SuperDroid Framework Installation Script

Usage:
    ./install.sh [OPTIONS]

Options:
    --yes, -y    Non-interactive mode (auto-yes)
    --help, -h   Show this help message

Description:
    Installs SuperDroid Framework for Factory Droid CLI.
    - 30 slash commands
    - 16 specialized droids

Requirements:
    - Factory Droid CLI installed
    - ~/.factory directory exists (or will be created)

Examples:
    ./install.sh          # Interactive installation
    ./install.sh --yes    # Non-interactive

For more information:
    https://github.com/Frexxis/SuperDroid
EOF
    exit 0
}

parse_args() {
    while [[ $# -gt 0 ]]; do
        case $1 in
            --yes|-y)
                AUTO_YES=true
                shift
                ;;
            --help|-h)
                show_help
                ;;
            *)
                print_error "Unknown option: $1"
                echo "Run './install.sh --help' for usage"
                exit 1
                ;;
        esac
    done
}

main() {
    parse_args "$@"
    
    clear
    print_header "🤖 SuperDroid Framework Installation"
    echo ""
    print_info "This will install SuperDroid Framework for Factory Droid CLI"
    print_info "Source: $SCRIPT_DIR"
    print_info "Target: $FACTORY_DIR"
    echo ""
    
    if [ "$AUTO_YES" != true ]; then
        if ! confirm "Continue with installation?"; then
            print_info "Installation cancelled"
            exit 0
        fi
    fi
    
    echo ""
    
    # Phase 1: Check prerequisites
    print_header "📋 Phase 1: Prerequisites"
    check_factory_cli
    create_directories
    
    # Phase 2: Install commands
    print_header "⚙️  Phase 2: Installing Commands"
    install_commands
    
    # Phase 3: Install droids
    print_header "🤖 Phase 3: Installing Droids"
    install_droids
    
    # Phase 4: Configuration
    print_header "🔧 Phase 4: Configuration"
    enable_custom_droids
    
    # Summary
    show_summary
}

main "$@"
