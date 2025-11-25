<div align="center">

# 🤖 SuperDroid Framework

### **Transform Factory Droid CLI into a Structured Development Platform**

<p align="center">
  <img src="https://img.shields.io/badge/version-1.0.0-blue" alt="Version">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License">
  <img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg" alt="PRs Welcome">
  <img src="https://img.shields.io/badge/Factory_Droid-CLI-purple" alt="Factory Droid CLI">
</p>

<p align="center">
  <a href="#-quick-installation">Quick Start</a> •
  <a href="#-features">Features</a> •
  <a href="#-commands">Commands</a> •
  <a href="#-droids">Droids</a> •
  <a href="#-contributing">Contributing</a>
</p>

</div>

---

## 📊 Framework Statistics

| **Commands** | **Droids** | **Tool Categories** |
|:------------:|:----------:|:-------------------:|
| **30** | **16** | **5** |
| Slash Commands | Specialized Subagents | read-only, edit, execute, web, mcp |

30 slash commands covering the complete development lifecycle from brainstorming to deployment.

---

## 🎯 Overview

SuperDroid is a **meta-programming configuration framework** that transforms [Factory Droid CLI](https://docs.factory.ai) into a structured development platform through behavioral instruction injection and component orchestration. It provides systematic workflow automation with powerful slash commands and intelligent subagents (droids).

> **Inspired by**: [SuperClaude Framework](https://github.com/SuperClaude-Org/SuperClaude_Framework) - Adapted for Factory Droid CLI

## Disclaimer

This project is not affiliated with or endorsed by Factory AI.
Factory Droid CLI is a product built and maintained by [Factory AI](https://factory.ai).

---

## ⚡ Quick Installation

```bash
# Clone the repository
git clone https://github.com/Frexxis/SuperDroid.git
cd SuperDroid

# Run the installation script
./install.sh

# Or install manually
cp -r .factory/commands/* ~/.factory/commands/
cp -r .factory/droids/* ~/.factory/droids/
```

After installation, restart Droid CLI to use 30 commands including:
- `/research` - Deep web research
- `/brainstorm` - Structured brainstorming
- `/implement` - Code implementation
- `/test` - Testing workflows
- `/pm` - Project management

---

## ✨ Features

### 🎯 30 Slash Commands

Organized by category for the complete development lifecycle:

| Category | Commands |
|----------|----------|
| 🧠 **Planning** | `/brainstorm`, `/design`, `/estimate`, `/spec-panel` |
| 💻 **Development** | `/implement`, `/build`, `/improve`, `/cleanup`, `/explain` |
| 🧪 **Testing** | `/test`, `/analyze`, `/troubleshoot`, `/reflect` |
| 📚 **Documentation** | `/document`, `/help` |
| 🔧 **Version Control** | `/git` |
| 📊 **Project Management** | `/pm`, `/task`, `/workflow` |
| 🔍 **Research** | `/research`, `/business-panel` |

### 🤖 16 Specialized Droids (Subagents)

Each droid is a specialized AI assistant with domain expertise:

| Droid | Purpose |
|-------|---------|
| `pm-agent` | Project orchestration and PDCA cycles |
| `security-engineer` | Vulnerability assessment and compliance |
| `frontend-architect` | UI/UX and accessibility |
| `backend-architect` | APIs and server-side logic |
| `deep-research-agent` | Autonomous web research |
| `system-architect` | System design and patterns |
| `quality-engineer` | Testing and QA |
| `devops-architect` | CI/CD and infrastructure |
| ... and 8 more |

---

## 📋 Commands

### Planning & Design

```bash
/brainstorm "feature idea"     # Structured brainstorming with Socratic questioning
/design "system architecture"  # System design with patterns
/estimate "project scope"      # Time and effort estimation
/spec-panel "requirements"     # Multi-expert specification analysis
```

### Development

```bash
/implement "feature" --type component   # Code implementation
/build                                  # Build workflows
/improve "code section"                 # Code improvements
/cleanup                                # Refactoring
/explain "complex code"                 # Code explanation
```

### Testing & Quality

```bash
/test "feature"           # Test generation
/analyze "codebase"       # Code analysis
/troubleshoot "issue"     # Debugging assistance
/reflect                  # Retrospectives
```

### Research

```bash
/research "query" --depth deep    # Deep web research
/business-panel "analysis"        # Multi-expert business analysis
```

---

## 🤖 Droids

Droids are specialized subagents that can be delegated tasks. They run with focused context and specific tool access.

### Using Droids

```bash
# Ask droid to use a specific subagent
"Run the security-engineer droid to audit this code"
"Use the deep-research-agent to investigate this topic"
```

### Managing Droids

```bash
/droids              # Open droids manager
# Press 'C' to create new droid
# Press 'E' to edit existing droid
# Press 'D' to delete droid
```

### Creating Custom Droids

Create a `.md` file in `.factory/droids/`:

```yaml
---
name: my-custom-droid
description: What this droid does
model: inherit
tools: ["Read", "Grep", "Glob", "Edit"]
---

You are a specialized assistant that...
```

---

## 📁 Project Structure

```
SuperDroid/
├── .factory/
│   ├── commands/           # 30 slash commands
│   │   ├── research.md
│   │   ├── implement.md
│   │   └── ...
│   └── droids/             # 16 specialized droids
│       ├── pm-agent.md
│       ├── security-engineer.md
│       └── ...
├── AGENTS.md               # Project configuration
├── README.md
├── LICENSE
├── install.sh
└── docs/
    ├── getting-started/
    ├── user-guide/
    └── reference/
```

---

## 🔧 Configuration

### AGENTS.md

Copy `AGENTS.md` to your project root to customize behavior:

```bash
cp /path/to/SuperDroid/AGENTS.md ./AGENTS.md
```

### MCP Servers (Optional)

For enhanced capabilities, configure MCP servers in `~/.factory/mcp.json`:

- **Tavily** - Web search for research
- **Context7** - Official documentation lookup
- **Playwright** - Browser automation

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

| Priority | Area | Description |
|:--------:|------|-------------|
| 📝 **High** | Commands | Add new slash commands |
| 🤖 **High** | Droids | Create specialized droids |
| 📚 **Medium** | Documentation | Improve guides and examples |
| 🧪 **Medium** | Testing | Test and validate features |

### Development

```bash
# Clone the repo
git clone https://github.com/Frexxis/SuperDroid.git
cd SuperDroid

# Make changes to commands or droids
# Test locally by copying to ~/.factory/

# Submit a PR
```

---

## ⚖️ License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Credits

- Inspired by [SuperClaude Framework](https://github.com/SuperClaude-Org/SuperClaude_Framework)
- Built for [Factory Droid CLI](https://factory.ai)

---

<div align="center">

### 🚀 Built with passion for the Factory Droid community

<p align="center">
  <sub>Made with ❤️ for developers who push boundaries</sub>
</p>

</div>
