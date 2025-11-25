---
description: Index and analyze repository structure
argument-hint: [directory] [--depth shallow|deep]
---

# /index-repo - Repository Indexing

Index and analyze the repository:

## Indexing Process

### 1. Structure Analysis
- Directory tree
- File types distribution
- Size metrics

### 2. Code Analysis
- Languages detected
- Frameworks identified
- Dependencies listed

### 3. Pattern Detection
- Coding conventions
- Architecture patterns
- Test structure

## Output Format

```
📂 Repository Index

## Structure
├── src/           (45 files)
├── tests/         (23 files)
├── docs/          (12 files)
└── config/        (5 files)

## Languages
- TypeScript: 65%
- JavaScript: 20%
- CSS: 10%
- Other: 5%

## Frameworks
- React 18.2.0
- Express 4.18.0
- Jest 29.0.0

## Key Files
- Entry: src/index.ts
- Config: tsconfig.json, package.json
- Tests: tests/

## Patterns Detected
- Component-based architecture
- Service layer pattern
- Unit + integration tests

## Statistics
- Total files: 85
- Lines of code: ~12,500
- Test coverage: 78%
```

## Depth Levels

| Depth | Analysis |
|-------|----------|
| `shallow` | Structure only |
| `deep` | Full analysis with patterns |

## Examples

```
/index-repo
/index-repo src/ --depth deep
/index-repo --depth shallow
```

## Use Cases

- Onboarding to new project
- Understanding codebase structure
- Finding patterns and conventions
- Documentation generation
