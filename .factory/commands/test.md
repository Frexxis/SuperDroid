---
description: Test generation and execution workflows
argument-hint: <feature or file> [--type unit|integration|e2e] [--coverage]
---

# /test - Testing Workflows

Generate and run tests for `$ARGUMENTS`:

## Testing Approach

### 1. Analyze
- Identify testable components
- Detect existing test patterns
- Find testing framework in use

### 2. Generate
- Create test cases based on functionality
- Follow existing test conventions
- Include edge cases and error scenarios

### 3. Execute
- Run generated tests
- Verify all pass
- Report coverage if requested

## Test Types

| Type | Purpose | Tools |
|------|---------|-------|
| `unit` | Individual functions/components | Jest, pytest, etc. |
| `integration` | Component interactions | Testing library |
| `e2e` | Full user workflows | Playwright, Cypress |

## Test Structure

```
describe('Feature', () => {
  it('should handle normal case', () => {});
  it('should handle edge case', () => {});
  it('should handle error case', () => {});
});
```

## Best Practices

1. **Test behavior, not implementation**
2. **One assertion per test when possible**
3. **Use descriptive test names**
4. **Mock external dependencies**
5. **Test edge cases and errors**

## Examples

```
/test user authentication --type unit
/test payment flow --type integration
/test checkout process --type e2e --coverage
/test src/components/Button.tsx
```

## Coverage Guidelines

| Coverage | Quality |
|:--------:|---------|
| < 50% | Needs improvement |
| 50-70% | Acceptable |
| 70-85% | Good |
| > 85% | Excellent |

## Output

- Generated test files
- Test execution results
- Coverage report (if --coverage)
- Recommendations for improvement
