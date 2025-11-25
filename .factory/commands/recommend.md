---
description: Get command recommendations based on context
argument-hint: [what you want to do]
---

# /recommend - Command Recommendations

Get recommendations for `$ARGUMENTS`:

## How It Works

Based on your description, I'll recommend:
1. Best matching command(s)
2. Usage examples
3. Related commands

## Common Scenarios

### "I want to..."

| Goal | Recommended Command |
|------|---------------------|
| Build a feature | `/implement` |
| Fix a bug | `/troubleshoot` |
| Understand code | `/explain` |
| Write tests | `/test` |
| Improve code | `/improve` or `/cleanup` |
| Research something | `/research` |
| Plan a project | `/brainstorm` or `/pm` |
| Review security | `/analyze --focus security` |
| Generate docs | `/document` |
| Estimate effort | `/estimate` |

## Examples

```
/recommend "I need to add authentication"
→ /implement, /design, /security-engineer droid

/recommend "code is slow"
→ /analyze --focus performance, /improve

/recommend "not sure what to build"
→ /brainstorm, /spec-panel

/recommend "prepare for release"
→ /workflow release, /test, /document
```

## Output Format

```
💡 Recommendations for: [goal]

## Primary Command
/command-name
[Why this is recommended]

## Usage
/command-name [example usage]

## Related Commands
- /related-1: [when to use]
- /related-2: [when to use]

## Droids to Consider
- droid-name: [expertise]
```
