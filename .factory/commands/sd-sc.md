---
name: sc
description: SuperDroid command dispatcher - Use /sc [command] to access all SuperDroid features
---

# SuperDroid Command Dispatcher

🚀 **SuperDroid Framework** - Main command dispatcher

## Usage

All SuperDroid commands use the `/` prefix:

```
/command [args...]
```

## Available Commands

### Research & Analysis
```
/research [query]         - Deep web research with parallel search
```

### Repository Management
```
/index-repo              - Index repository for context optimization
```

### AI Agents
```
/agent [type]            - Launch specialized AI agents
```

### Recommendations
```
/recommend [context]     - Get command recommendations
```

### Help
```
/sc                         - Show this help (all available commands)
```

## Command Namespace

All commands are namespaced under `sc:` to keep them organized:
- ✅ `/research query`
- ✅ `/index-repo`
- ✅ `/agent type`
- ✅ `/recommend`
- ✅ `/sc` (help)

## Examples

### Research
```
/research React 18 new features
/research LLM agent architectures 2024
/research Python async best practices
```

### Index Repository
```
/index-repo
```

### Agent
```
/agent deep-research
/agent self-review
/agent repo-index
```

### Recommendations
```
/recommend
```

## Quick Reference

| Command | Description | Example |
|---------|-------------|---------|
| `/research` | Deep web research | `/research topic` |
| `/index-repo` | Repository indexing | `/index-repo` |
| `/agent` | Specialized AI agents | `/agent type` |
| `/recommend` | Command suggestions | `/recommend` |
| `/sc` | Show help | `/sc` |

## Features

- **Parallel Execution**: Research runs multiple searches in parallel
- **Evidence-Based**: All findings backed by sources
- **Context-Aware**: Uses repository context when available
- **Token Efficient**: Optimized for minimal token usage

## Help

For help on specific commands:
```
/research --help
/agent --help
```

Or use the main help command:
```
/sc
```

Check the documentation:
- PLANNING.md - Architecture and design
- TASK.md - Current tasks and priorities
- KNOWLEDGE.md - Tips and best practices

## Version

SuperDroid v4.1.7
- Python package: 0.4.0
- Pytest plugin included
- PM Agent patterns enabled

---

💡 **Tip**: All commands use the `/` prefix - e.g., `/research`, `/agent`

🔧 **Installation**: Run `superclaude install` to install/update commands

📚 **Documentation**: https://github.com/SuperDroid-Org/SuperDroid_Framework

⚠️ **Important**: Restart Factory Droid CLI after installing commands to use them!
