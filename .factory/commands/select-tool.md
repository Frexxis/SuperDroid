---
description: Help selecting the right tool for a task
argument-hint: <task description>
---

# /select-tool - Tool Selection

Select optimal tool for `$ARGUMENTS`:

## Available Tools

### Read Operations
| Tool | Use For |
|------|---------|
| `Read` | View file contents |
| `LS` | List directory contents |
| `Grep` | Search patterns in files |
| `Glob` | Find files by pattern |

### Write Operations
| Tool | Use For |
|------|---------|
| `Create` | Create new files |
| `Edit` | Modify existing files |
| `MultiEdit` | Multiple edits in one file |

### Execution
| Tool | Use For |
|------|---------|
| `Execute` | Run shell commands |

### Web
| Tool | Use For |
|------|---------|
| `WebSearch` | Search the web |
| `FetchUrl` | Get URL content |

### Management
| Tool | Use For |
|------|---------|
| `TodoWrite` | Task tracking |

## Selection Guide

### "I want to find..."
- Code pattern → `Grep`
- File by name → `Glob`
- File contents → `Read`
- Directory structure → `LS`

### "I want to change..."
- Single edit → `Edit`
- Multiple edits → `MultiEdit`
- New file → `Create`

### "I want to run..."
- Command → `Execute`
- Tests → `Execute`
- Build → `Execute`

### "I want to research..."
- Web search → `WebSearch`
- Specific URL → `FetchUrl`

## Examples

```
/select-tool "find all files using deprecated API"
→ Grep with pattern search

/select-tool "update version in multiple files"
→ Edit with change_all: true

/select-tool "understand project structure"
→ LS + Glob + Read
```
