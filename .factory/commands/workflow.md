---
description: Workflow automation and process management
argument-hint: <workflow-name> [options]
---

# /workflow - Workflow Automation

Execute workflow for `$ARGUMENTS`:

## Built-in Workflows

### Development Workflow
```
/workflow dev
```
1. Pull latest changes
2. Install dependencies
3. Run linter
4. Run tests
5. Start dev server

### Release Workflow
```
/workflow release --version 1.2.0
```
1. Run all tests
2. Build production
3. Update changelog
4. Create git tag
5. Prepare release notes

### Review Workflow
```
/workflow review
```
1. Check code style
2. Run static analysis
3. Run tests
4. Generate coverage report
5. Summarize findings

### CI Workflow
```
/workflow ci
```
1. Install dependencies
2. Lint code
3. Type check
4. Run tests
5. Build

## Custom Workflows

Create custom workflows in `.factory/commands/`:

```yaml
---
description: My custom workflow
---

# Steps:
1. [Step 1]
2. [Step 2]
...
```

## Examples

```
/workflow dev
/workflow release --version 2.0.0
/workflow review
/workflow ci
```

## Workflow Output

```
🔄 Workflow: [name]

Step 1/5: Pull latest changes
✅ Complete

Step 2/5: Install dependencies
✅ Complete

Step 3/5: Run linter
⚠️ 2 warnings

Step 4/5: Run tests
✅ 42 tests passed

Step 5/5: Start dev server
✅ Running on http://localhost:3000

Summary: 5/5 steps complete
```
