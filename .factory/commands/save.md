---
description: Save current session or context
argument-hint: [session-name]
---

# /save - Save Session

Save current session as `$ARGUMENTS`:

## What Gets Saved

- Current task progress
- TodoWrite state
- Project context
- Recent decisions
- Active goals

## Save Locations

| Location | Use For |
|----------|---------|
| `~/.factory/sessions/` | Personal sessions |
| `.factory/sessions/` | Project sessions |

## Examples

```
/save                     # Auto-named with timestamp
/save auth-feature        # Named session
/save checkpoint-1        # Checkpoint save
```

## Output Format

```
💾 Saving session: [name]

## Session Contents
- Tasks: 5 (2 completed, 1 in progress, 2 pending)
- Files touched: 12
- Duration: 45 minutes

## Saved To
~/.factory/sessions/auth-feature.json

## To Resume
/load auth-feature

Session saved successfully!
```

## Auto-Save

Sessions are automatically saved:
- On session end
- Every 30 minutes
- Before major operations

## Best Practices

1. **Name meaningfully** - Describe the work
2. **Save at checkpoints** - Before risky changes
3. **Save before breaks** - Resume easily later
4. **Clean up old sessions** - Remove unneeded saves

## Related Commands

- `/load` - Load saved session
- `/pm` - Project management with auto-save
