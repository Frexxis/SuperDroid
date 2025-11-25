---
description: Task tracking and management with TodoWrite
argument-hint: <action> [task description]
---

# /task - Task Tracking

Manage tasks for `$ARGUMENTS`:

## Task Actions

### Create Tasks
```
/task add "implement user login"
/task add "fix navigation bug" --priority high
```

### Update Tasks
```
/task start 1              # Mark as in_progress
/task complete 1           # Mark as completed
/task update 1 "new desc"  # Update description
```

### View Tasks
```
/task list                 # Show all tasks
/task list --status pending
```

## Task States

| State | Description |
|-------|-------------|
| `pending` | Not started |
| `in_progress` | Currently working |
| `completed` | Finished |

## Priority Levels

| Priority | Use For |
|----------|---------|
| `high` | Urgent, blocking issues |
| `medium` | Normal priority (default) |
| `low` | Nice to have |

## Best Practices

1. **One task in progress** - Focus on one thing
2. **Break down large tasks** - Smaller = manageable
3. **Update status** - Keep list current
4. **Complete immediately** - Mark done when done

## Integration with TodoWrite

Tasks are managed via TodoWrite tool:
- Automatically tracked
- Persisted across session
- Visible in UI

## Examples

```
/task add "refactor auth module" --priority high
/task list
/task start 1
/task complete 1
/task add "write unit tests"
```

## Output Format

```
📋 Tasks

[1] 🔴 HIGH | in_progress | Refactor auth module
[2] 🟡 MED  | pending     | Write unit tests
[3] 🟢 LOW  | pending     | Update documentation

Progress: 0/3 completed
```
