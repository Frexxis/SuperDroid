---
description: Code improvements and optimizations
argument-hint: <file or component> [--focus readability|performance|maintainability]
---

# /improve - Code Improvements

Improve `$ARGUMENTS` with targeted enhancements:

## Improvement Areas

### Readability
- Clearer variable names
- Better function structure
- Improved comments
- Consistent formatting

### Performance
- Algorithm optimization
- Memory efficiency
- Caching opportunities
- Lazy loading

### Maintainability
- Reduce complexity
- Extract reusable functions
- Improve error handling
- Better abstractions

## Improvement Process

1. **Analyze** - Understand current code
2. **Identify** - Find improvement opportunities
3. **Prioritize** - Rank by impact
4. **Implement** - Make changes
5. **Validate** - Ensure tests pass

## Output Format

```
🔧 Improvements for [target]

## Changes Made
1. [Change description]
   - Before: [old code snippet]
   - After: [new code snippet]
   - Reason: [why this improves the code]

## Metrics
- Complexity: [before] → [after]
- Lines: [before] → [after]

## Recommendations
- [Additional improvement idea]
```

## Examples

```
/improve src/utils/helpers.js --focus readability
/improve components/DataTable.tsx --focus performance
/improve services/api.js --focus maintainability
```

## Guidelines

- Preserve existing functionality
- Make incremental changes
- Keep tests passing
- Document significant changes
