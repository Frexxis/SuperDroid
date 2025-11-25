---
description: Build and compilation workflows
argument-hint: [--env development|staging|production] [--clean]
---

# /build - Build Workflows

Execute build process for the project:

## Build Process

### 1. Pre-build
- Clean previous artifacts (if --clean)
- Verify dependencies
- Check environment configuration

### 2. Build
- Compile/transpile code
- Bundle assets
- Generate artifacts

### 3. Post-build
- Run build validation
- Report build metrics
- Prepare for deployment

## Build Environments

| Environment | Optimizations | Source Maps |
|-------------|---------------|-------------|
| `development` | None | Full |
| `staging` | Partial | Limited |
| `production` | Full | None |

## Common Build Commands

The command will detect and use the appropriate build system:

| Tool | Command |
|------|---------|
| npm/yarn | `npm run build` |
| pnpm | `pnpm build` |
| make | `make build` |
| cargo | `cargo build` |
| go | `go build` |

## Examples

```
/build
/build --env production
/build --clean --env staging
```

## Build Troubleshooting

If build fails:
1. Check dependency versions
2. Verify environment variables
3. Clear caches and rebuild
4. Check for syntax/type errors

## Output

- Build status (success/failure)
- Build time
- Output size
- Warnings/errors if any
