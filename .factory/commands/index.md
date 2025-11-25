---
description: Quick index/overview of current directory or file
argument-hint: [path]
---

# /index - Quick Index

Quick overview of `$ARGUMENTS`:

## For Directories

Shows:
- File count by type
- Directory structure
- Key files identified
- Size summary

## For Files

Shows:
- File type and size
- Structure overview
- Key sections/functions
- Dependencies

## Examples

```
/index                    # Current directory
/index src/               # Specific directory
/index src/auth/login.ts  # Specific file
```

## Output Format

### Directory Index
```
📁 Index: src/

Files: 45 total
├── TypeScript: 30
├── CSS: 10
├── JSON: 5

Structure:
├── components/  (15 files)
├── utils/       (8 files)
├── hooks/       (5 files)
└── services/    (7 files)

Key Files:
- index.ts (entry point)
- App.tsx (main component)
- router.ts (routing)
```

### File Index
```
📄 Index: auth/login.ts

Type: TypeScript
Size: 2.4 KB
Lines: 85

Exports:
- LoginForm (component)
- useLogin (hook)
- validateCredentials (function)

Dependencies:
- react
- ./auth-context
- ../utils/validation

Sections:
- Imports (1-10)
- Types (12-20)
- Component (22-70)
- Hook (72-85)
```

## Related Commands

- `/index-repo` - Full repository analysis
- `/explain` - Detailed explanation
- `/analyze` - Quality analysis
