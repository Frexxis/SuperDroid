---
description: Feature and code implementation with systematic approach
argument-hint: <feature-description> [--type component|api|service|feature] [--with-tests]
---

# /implement - Feature Implementation

Implement `$ARGUMENTS` following this systematic approach:

## Implementation Flow

### 1. Analyze (10% effort)
- Examine implementation requirements
- Detect technology context and existing patterns
- Identify affected files and dependencies

### 2. Plan (15% effort)
- Choose implementation approach
- Break down into atomic tasks
- Identify potential risks

### 3. Implement (60% effort)
- Generate code following existing patterns
- Apply framework-specific best practices
- Maintain consistency with codebase style

### 4. Validate (15% effort)
- Run existing tests
- Add new tests if --with-tests specified
- Verify integration with existing code

## Implementation Types

| Type | Focus |
|------|-------|
| `component` | UI components, React/Vue/Angular |
| `api` | REST/GraphQL endpoints |
| `service` | Business logic, utilities |
| `feature` | Full-stack feature |

## Best Practices

1. **Read First**: Always analyze existing code patterns
2. **Atomic Changes**: Make small, focused changes
3. **Test Coverage**: Ensure tests pass after changes
4. **Documentation**: Update docs if needed

## Tool Usage

- **Read/Grep/Glob**: Analyze existing patterns
- **Edit/MultiEdit**: Make code changes
- **Execute**: Run tests and builds
- **TodoWrite**: Track progress for complex implementations

## Examples

```
/implement user authentication with JWT
/implement dashboard component --type component --with-tests
/implement payment processing API --type api
/implement full user profile feature --type feature
```

## Boundaries

**Will:**
- Implement features following existing patterns
- Apply security best practices
- Provide comprehensive implementation

**Won't:**
- Make breaking changes without warning
- Skip testing for complex changes
- Introduce new dependencies without explanation
