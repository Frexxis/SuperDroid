---
description: Code analysis for quality, patterns, and improvements
argument-hint: <file, directory, or scope> [--focus security|performance|quality]
---

# /analyze - Code Analysis

Analyze `$ARGUMENTS` for quality and improvements:

## Analysis Areas

### Code Quality
- Code complexity metrics
- Duplication detection
- Naming conventions
- Documentation coverage

### Security
- Vulnerability patterns
- Input validation
- Authentication/authorization
- Sensitive data handling

### Performance
- Algorithmic complexity
- Memory usage patterns
- Database query efficiency
- Caching opportunities

### Architecture
- Design pattern usage
- Dependency structure
- Module coupling
- SOLID principles

## Analysis Process

1. **Scan**: Read and parse target code
2. **Analyze**: Apply analysis rules
3. **Prioritize**: Rank findings by severity
4. **Report**: Provide actionable recommendations

## Output Format

```
📊 Analysis Report: [target]

🔴 Critical Issues (fix immediately)
├── [issue description]
└── [recommended fix]

🟡 Warnings (should fix)
├── [issue description]
└── [recommended fix]

🟢 Suggestions (nice to have)
├── [improvement idea]
└── [benefit]

📈 Metrics
├── Complexity: [score]
├── Maintainability: [score]
└── Test Coverage: [percentage]
```

## Examples

```
/analyze src/auth/ --focus security
/analyze components/Dashboard.tsx --focus performance
/analyze . --focus quality
```

## Focus Areas

| Focus | Checks |
|-------|--------|
| `security` | OWASP, input validation, secrets |
| `performance` | O(n), memory, queries |
| `quality` | Complexity, duplication, style |
