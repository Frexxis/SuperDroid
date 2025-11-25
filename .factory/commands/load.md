---
description: Load saved session or context
argument-hint: <session-name>
---

# /load - Load Session

Load session or context for `$ARGUMENTS`:

## Session Types

### Project Context
Load project-specific context and preferences:
```
/load project
```

### Previous Session
Resume from a saved session:
```
/load session-2024-01-15
```

### Custom Context
Load custom context file:
```
/load context/feature-auth.md
```

## What Gets Loaded

- Task progress (TodoWrite state)
- Project understanding
- Recent decisions
- Active goals
- Custom preferences

## Session Storage

Sessions are stored in:
- `~/.factory/sessions/` (personal)
- `.factory/sessions/` (project)

## Examples

```
/load                     # Load default/last session
/load project             # Load project context
/load auth-feature        # Load named session
/load context/sprint-5.md # Load context file
```

## Output Format

```
📂 Loading session: [name]

## Restored Context
- Project: MyApp
- Branch: feature/auth
- Last activity: 2 hours ago

## Active Tasks
- [x] Setup authentication
- [ ] Implement login form
- [ ] Add JWT validation

## Continuing from
[Last checkpoint description]

Ready to continue!
```

## Related Commands

- `/save` - Save current session
- `/pm` - Project management mode
