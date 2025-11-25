---
description: Project Manager - orchestration, planning, and PDCA workflow management
argument-hint: [request] [--strategy brainstorm|direct|wave]
---

# /pm - Project Manager Mode

Activate project management mode for `$ARGUMENTS`:

## PM Agent Capabilities

### Session Management
- Restore context from previous sessions
- Track progress across conversations
- Maintain project state

### PDCA Cycle (Plan-Do-Check-Act)

**Plan (仮説)**
- Define goals and hypotheses
- Create implementation roadmap
- Identify risks and dependencies

**Do (実験)**
- Execute implementation tasks
- Track progress with TodoWrite
- Document trial and error

**Check (評価)**
- Evaluate results against goals
- Measure success metrics
- Identify what worked/failed

**Act (改善)**
- Document learnings
- Update best practices
- Plan next iteration

## Execution Strategies

| Strategy | Use Case |
|----------|----------|
| `brainstorm` | Vague requirements, need discovery |
| `direct` | Clear task, immediate execution |
| `wave` | Complex project, parallel execution |

## Workflow Patterns

### Vague Request Pattern
```
User: "I want to add authentication"
PM: → Discovery questions
    → Requirements analysis
    → Architecture design
    → Implementation delegation
    → Quality validation
```

### Clear Task Pattern
```
User: "Fix login validation bug in LoginForm.tsx:45"
PM: → Analyze issue
    → Fix implementation
    → Test validation
    → Documentation update
```

## Tool Coordination

- **TodoWrite**: Track all tasks and progress
- **Read/Grep**: Gather context
- **Task**: Delegate to specialized droids
- **Edit**: Make implementations

## Examples

```
/pm build user management system
/pm "improve performance" --strategy brainstorm
/pm fix authentication issues --strategy direct
```

## Self-Improvement

After each task:
1. Document what worked → patterns/
2. Document what failed → learnings/
3. Update project knowledge
