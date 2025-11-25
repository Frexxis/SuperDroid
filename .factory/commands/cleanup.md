---
description: Code refactoring and cleanup
argument-hint: <file or directory> [--scope formatting|imports|dead-code|all]
---

# /cleanup - Refactoring

Clean up `$ARGUMENTS`:

## Cleanup Scopes

### Formatting
- Consistent indentation
- Line length
- Whitespace normalization
- Code style alignment

### Imports
- Remove unused imports
- Sort imports
- Group by type
- Fix import paths

### Dead Code
- Remove unused variables
- Remove unused functions
- Remove commented code
- Remove unreachable code

### All
- Apply all cleanup scopes

## Cleanup Process

1. **Scan** - Identify cleanup opportunities
2. **Preview** - Show proposed changes
3. **Apply** - Make changes
4. **Verify** - Run tests

## Examples

```
/cleanup src/ --scope imports
/cleanup components/Header.tsx --scope formatting
/cleanup utils/ --scope dead-code
/cleanup . --scope all
```

## Safety

- Changes are non-breaking
- Functionality is preserved
- Tests remain passing
- Git diff shows all changes

## Output

```
🧹 Cleanup Report: [target]

## Changes
- Removed X unused imports
- Fixed Y formatting issues
- Removed Z dead code lines

## Files Modified
- file1.ts
- file2.ts

## Next Steps
- Run tests to verify
- Review changes before commit
```
