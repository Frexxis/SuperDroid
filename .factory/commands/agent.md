---
description: Invoke specific specialized droids (subagents)
argument-hint: <droid-name> <task>
---

# /agent - Droid Invocation

Invoke specialized droid for `$ARGUMENTS`:

## Available Droids

### Engineering
| Droid | Expertise |
|-------|-----------|
| `frontend-architect` | UI/UX, accessibility, React/Vue |
| `backend-architect` | APIs, databases, server logic |
| `system-architect` | System design, patterns |
| `devops-architect` | CI/CD, infrastructure |

### Quality
| Droid | Expertise |
|-------|-----------|
| `security-engineer` | Vulnerabilities, compliance |
| `quality-engineer` | Testing, QA |
| `performance-engineer` | Optimization |

### Analysis
| Droid | Expertise |
|-------|-----------|
| `deep-research-agent` | Web research |
| `requirements-analyst` | Requirements gathering |
| `root-cause-analyst` | Problem investigation |

### Support
| Droid | Expertise |
|-------|-----------|
| `pm-agent` | Project management |
| `technical-writer` | Documentation |
| `refactoring-expert` | Code improvement |

## Usage

```
/agent security-engineer "audit authentication code"
/agent frontend-architect "review component structure"
/agent deep-research-agent "research GraphQL best practices"
```

## Direct Invocation

You can also invoke droids conversationally:

```
"Use the security-engineer droid to check this code"
"Ask the frontend-architect to review this component"
```

## Creating Custom Droids

See `/droids` command or create `.md` files in:
- `.factory/droids/` (project)
- `~/.factory/droids/` (personal)
