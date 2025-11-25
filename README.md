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
  <a href="#-documentation">Docs</a> •
  <a href="#-contributing">Contributing</a>
</p>

</div>

---

<div align="center">

## 📊 **Framework Statistics**

| **Commands** | **Droids** | **Modes** | **MCP Servers** |
|:------------:|:----------:|:---------:|:---------------:|
| **30** | **20** | **7** | **8** |
| Slash Commands | Specialized AI | Behavioral | Integrations |

30 slash commands covering the complete development lifecycle from brainstorming to deployment.

</div>

---

<div align="center">

## 🎯 **Overview**

SuperDroid is a **meta-programming configuration framework** that transforms [Factory Droid CLI](https://docs.factory.ai) into a structured development platform through behavioral instruction injection and component orchestration. It provides systematic workflow automation with powerful tools and intelligent droids (subagents).

> **Inspired by**: [SuperClaude Framework](https://github.com/SuperClaude-Org/SuperClaude_Framework) - Adapted for Factory Droid CLI

## Disclaimer

This project is not affiliated with or endorsed by Factory AI.
Factory Droid CLI is a product built and maintained by [Factory AI](https://factory.ai).

</div>

---

## ⚡ **Quick Installation**

### **Option 1: pipx (Recommended for Python users)**

```bash
# Install from PyPI
pipx install superdroid

# Install commands, droids, and modes
superdroid install

# Verify installation
superdroid doctor
```

### **Option 2: npm (Recommended for Node.js users)**

```bash
# Install globally from npm
npm install -g @frexxis/superdroid

# Install commands, droids, and modes
superdroid install

# Verify installation
superdroid doctor
```

### **Option 3: Install Script**

```bash
# Clone and install
git clone https://github.com/Frexxis/SuperDroid.git
cd SuperDroid
./install.sh
```

### **Option 4: Manual Installation**

```bash
# Clone the repository
git clone https://github.com/Frexxis/SuperDroid.git
cd SuperDroid

# Copy commands
cp -r .factory/commands/* ~/.factory/commands/

# Copy droids
cp -r .factory/droids/* ~/.factory/droids/

# Copy modes
cp -r .factory/modes/* ~/.factory/modes/
```

After installation:
1. **Restart Droid CLI** to load new commands
2. **Enable Custom Droids**: `/settings` → Custom Droids → Enable
3. **Verify**: Type `/help` to see all commands

### **Available Commands After Installation**

- `/research` - Deep web research (enhanced with Tavily MCP)
- `/brainstorm` - Structured brainstorming
- `/implement` - Code implementation
- `/test` - Testing workflows
- `/pm` - Project management
- `/sd` - Show all 30 available commands

### **Enhanced Performance (Optional MCPs)**

For **2-3x faster** execution and **30-50% fewer tokens**, configure MCP servers in `~/.factory/mcp.json`:

```bash
# Recommended MCP servers:
# - Tavily: Web search for Deep Research
# - Context7: Official documentation lookup
# - Sequential: Token-efficient reasoning
# - Playwright: Browser automation
```

**Performance Comparison:**
- **Without MCPs**: Fully functional, standard performance ✅
- **With MCPs**: 2-3x faster, 30-50% fewer tokens ⚡

---

<div align="center">

## 🎉 **Features**

</div>

<table>
<tr>
<td width="50%">

### 🤖 **20 Specialized Droids**
Domain expertise on demand:
- PM Agent for project orchestration
- Deep Research agent for web research
- Security engineer for vulnerability checks
- Frontend/Backend architects
- Quality & Performance engineers
- And 15 more specialists

</td>
<td width="50%">

### ⚡ **Optimized Performance**
Efficient framework design:
- Reduced token footprint
- More context for your code
- Longer conversations possible
- Complex operations enabled

</td>
</tr>
<tr>
<td width="50%">

### 🔧 **MCP Server Integration**
**8 powerful servers** supported:

- **Tavily** → Primary web search
- **Context7** → Documentation lookup
- **Sequential** → Multi-step reasoning
- **Playwright** → Browser automation
- **Serena** → Session persistence
- And more...

</td>
<td width="50%">

### 🎯 **7 Behavioral Modes**
Adaptive modes for different contexts:
- **Brainstorming** → Discovery questions
- **Business Panel** → Multi-expert analysis
- **Deep Research** → Autonomous research
- **Orchestration** → Tool coordination
- **Token-Efficiency** → Context savings
- **Task Management** → Organization
- **Introspection** → Meta-analysis

</td>
</tr>
</table>

---

## 🔬 **Deep Research Capabilities**

### **Autonomous Web Research**

SuperDroid includes comprehensive Deep Research capabilities:

<table>
<tr>
<td width="50%">

### 🎯 **Adaptive Planning**
- **Planning-Only**: Direct execution
- **Intent-Planning**: Clarification first
- **Unified**: Collaborative refinement

</td>
<td width="50%">

### 🔄 **Multi-Hop Reasoning**
- Entity expansion
- Concept deepening
- Temporal progression
- Causal chains

</td>
</tr>
</table>

### **Research Command Usage**

```bash
# Basic research
/research "latest AI developments 2024"

# Deep research
/research "quantum computing breakthroughs" --depth exhaustive

# Domain-filtered (with Tavily MCP)
/research "React patterns" --domains reactjs.org,github.com
```

### **Research Depth Levels**

| Depth | Sources | Time | Best For |
|:-----:|:-------:|:----:|----------|
| **Quick** | 5-10 | ~2min | Quick facts |
| **Standard** | 10-20 | ~5min | General research |
| **Deep** | 20-40 | ~8min | Comprehensive |
| **Exhaustive** | 40+ | ~10min | Academic-level |

---

<div align="center">

## 📚 **Documentation**

### **Complete Guide to SuperDroid**

<table>
<tr>
<th align="center">🚀 Getting Started</th>
<th align="center">📖 User Guides</th>
<th align="center">📋 Reference</th>
</tr>
<tr>
<td valign="top">

- 📝 [**Quick Start**](docs/getting-started/quick-start.md)
- 💾 [**Installation**](docs/getting-started/quick-start.md)

</td>
<td valign="top">

- 🎯 [**Commands**](docs/user-guide/commands.md)
- 🤖 [**Droids**](docs/user-guide/droids.md)
- 🔧 [**MCP Servers**](docs/user-guide/mcp-servers.md)

</td>
<td valign="top">

- 📓 [**Commands List**](docs/reference/commands-list.md)

</td>
</tr>
</table>

</div>

---

## 📋 **All 30 Commands**

<details>
<summary><b>Click to expand full command list</b></summary>

### 🧠 Planning & Design (4)
- `/brainstorm` - Structured brainstorming
- `/design` - System architecture
- `/estimate` - Time/effort estimation
- `/spec-panel` - Specification analysis

### 💻 Development (5)
- `/implement` - Code implementation
- `/build` - Build workflows
- `/improve` - Code improvements
- `/cleanup` - Refactoring
- `/explain` - Code explanation

### 🧪 Testing & Quality (4)
- `/test` - Test generation
- `/analyze` - Code analysis
- `/troubleshoot` - Debugging
- `/reflect` - Retrospectives

### 📚 Documentation (2)
- `/document` - Doc generation
- `/help` - Command help

### 🔧 Version Control (1)
- `/git` - Git operations

### 📊 Project Management (3)
- `/pm` - Project management
- `/task` - Task tracking
- `/workflow` - Workflow automation

### 🔍 Research & Analysis (2)
- `/research` - Deep web research
- `/business-panel` - Business analysis

### 🎯 Utilities (9)
- `/agent` - Invoke droids
- `/index-repo` - Repository indexing
- `/index` - Quick indexing
- `/recommend` - Command recommendations
- `/select-tool` - Tool selection
- `/spawn` - Parallel tasks
- `/load` - Load sessions
- `/save` - Save sessions
- `/sd` - Show all commands

[**📖 View Detailed Command Reference →**](docs/reference/commands-list.md)

</details>

---

<div align="center">

## 🤝 **Contributing**

### **Join the SuperDroid Community**

We welcome contributions of all kinds!

| Priority | Area | Description |
|:--------:|------|-------------|
| 📝 **High** | Commands | Add new slash commands |
| 🤖 **High** | Droids | Create specialized droids |
| 📚 **Medium** | Documentation | Improve guides & examples |
| 🧪 **Medium** | Testing | Test and validate features |

</div>

---

<div align="center">

## ⚖️ **License**

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

<p align="center">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="MIT License">
</p>

</div>

---

<div align="center">

## 🙏 **Credits**

- Inspired by [SuperClaude Framework](https://github.com/SuperClaude-Org/SuperClaude_Framework)
- Built for [Factory Droid CLI](https://factory.ai)

</div>

---

<div align="center">

### **🤖 Built with passion for the Factory Droid community**

<p align="center">
  <sub>Made with ❤️ for developers who push boundaries</sub>
</p>

<p align="center">
  <a href="#-superdroid-framework">Back to Top ↑</a>
</p>

</div>
