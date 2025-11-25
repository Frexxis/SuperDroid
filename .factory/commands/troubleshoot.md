---
description: Debugging and issue resolution
argument-hint: <error or issue description>
---

# /troubleshoot - Debugging

Debug and resolve `$ARGUMENTS`:

## Troubleshooting Process

### 1. Understand the Problem
- What is the expected behavior?
- What is the actual behavior?
- When did it start happening?
- Can it be reproduced?

### 2. Gather Information
- Error messages
- Stack traces
- Logs
- Environment details

### 3. Investigate
- Identify potential causes
- Check recent changes
- Analyze related code
- Search for similar issues

### 4. Root Cause Analysis
- Why did this happen?
- What is the underlying issue?
- Are there related problems?

### 5. Resolve
- Implement fix
- Verify solution
- Prevent recurrence

## Investigation Tools

| Tool | Purpose |
|------|---------|
| `Read` | Examine source code |
| `Grep` | Search for patterns |
| `Execute` | Run diagnostic commands |
| `WebSearch` | Find similar issues |

## Output Format

```
🔍 Troubleshooting: [issue]

## Problem
[Clear description of the issue]

## Investigation
[Steps taken to investigate]

## Root Cause
[Identified cause]

## Solution
[How to fix it]

## Prevention
[How to prevent recurrence]
```

## Examples

```
/troubleshoot "TypeError: Cannot read property 'map' of undefined"
/troubleshoot build failing on CI
/troubleshoot slow database queries
/troubleshoot memory leak in production
```

## Tips

- Provide full error messages
- Include relevant file paths
- Describe recent changes
- Share environment details
