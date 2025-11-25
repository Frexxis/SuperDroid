---
description: Git operations and workflow assistance
argument-hint: <operation> [options]
---

# /git - Git Operations

Execute git operations for `$ARGUMENTS`:

## Supported Operations

### Status & Info
```
/git status           # Show working tree status
/git log              # Show commit history
/git diff             # Show changes
```

### Branching
```
/git branch new-feature       # Create branch
/git checkout main            # Switch branch
/git merge feature-branch     # Merge branch
```

### Commits
```
/git commit "message"         # Commit changes
/git amend                    # Amend last commit
```

### Remote
```
/git pull                     # Pull changes
/git push                     # Push changes (requires confirmation)
```

## Commit Message Convention

```
<type>: <description>

Types:
- feat: New feature
- fix: Bug fix
- docs: Documentation
- refactor: Code refactoring
- test: Tests
- chore: Maintenance
```

## Safety Guidelines

1. **Always check status first** - Know what you're committing
2. **Review diff before commit** - Verify changes
3. **Never force push shared branches** - Protect team history
4. **Use descriptive branch names** - feature/, fix/, docs/

## Examples

```
/git status
/git commit "feat: add user authentication"
/git branch feature/payment-integration
/git merge --no-ff feature/payment
```

## Protected Operations

These require explicit confirmation:
- `git push` - Modifies remote
- `git push --force` - Destructive
- `git reset --hard` - Loses changes
- `git clean -fd` - Deletes files
