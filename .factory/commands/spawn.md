---
description: Spawn parallel tasks for efficient execution
argument-hint: <task list>
---

# /spawn - Parallel Task Execution

Execute tasks in parallel for `$ARGUMENTS`:

## Wave Pattern

SuperDroid uses Wave → Checkpoint → Wave pattern:

```
Wave 1: [Task A, Task B, Task C]  ← Parallel
         ↓
Checkpoint: Analyze results
         ↓
Wave 2: [Task D, Task E]  ← Parallel (based on Wave 1)
         ↓
Final: Consolidate
```

## When to Use Parallel

### Good for Parallel
- Reading multiple files
- Searching different patterns
- Independent API calls
- Separate test suites

### Requires Sequential
- Dependent operations
- Order-sensitive changes
- State-dependent tasks

## Spawn Syntax

```
/spawn [
  "read src/auth/*.ts",
  "read src/api/*.ts",
  "search for deprecated patterns"
]
```

## Examples

```
/spawn [
  "analyze frontend code",
  "analyze backend code",
  "check security patterns"
]

/spawn [
  "run unit tests",
  "run integration tests",
  "check linting"
]
```

## Output Format

```
🚀 Spawning 3 parallel tasks

[1/3] ✅ Analyze frontend code (2.3s)
[2/3] ✅ Analyze backend code (1.8s)
[3/3] ✅ Check security patterns (3.1s)

Total time: 3.1s (vs 7.2s sequential)
Speedup: 2.3x

## Results Summary
[Consolidated findings]
```

## Performance Tips

- Group independent operations
- Limit to ~5 parallel tasks
- Use for read-heavy operations
- Checkpoint before writes
