---
description: Documentation generation for code and APIs
argument-hint: <file or component> [--type readme|api|jsdoc|inline]
---

# /document - Documentation Generation

Generate documentation for `$ARGUMENTS`:

## Documentation Types

### README
- Project overview
- Installation instructions
- Usage examples
- API reference

### API Documentation
- Endpoint descriptions
- Request/response formats
- Authentication details
- Error codes

### JSDoc/Docstrings
- Function documentation
- Parameter descriptions
- Return value documentation
- Usage examples

### Inline Comments
- Complex logic explanation
- Algorithm documentation
- Decision rationale

## Documentation Process

1. **Analyze** - Understand the code
2. **Structure** - Organize documentation
3. **Write** - Generate clear documentation
4. **Review** - Ensure accuracy

## Output Format

Depends on --type flag:

- `readme`: Markdown README file
- `api`: OpenAPI/Swagger spec
- `jsdoc`: JSDoc/TSDoc comments
- `inline`: Code comments

## Examples

```
/document src/api/ --type api
/document components/Button.tsx --type jsdoc
/document utils/helpers.js --type inline
/document . --type readme
```

## Best Practices

1. **Be concise** - Clear and to the point
2. **Include examples** - Show, don't just tell
3. **Keep updated** - Docs should match code
4. **Target audience** - Write for the reader
