# SuperDroid Framework

This file provides guidance to Factory Droid CLI when working with code in this repository.

## Core Principles

### 1. Evidence-Based Development
**Never guess** - verify with official docs, web search, or codebase analysis before implementation.

### 2. Confidence-First Implementation
Check confidence BEFORE starting:
- ≥90%: Proceed with implementation
- 70-89%: Present alternatives, ask questions
- <70%: STOP - Request more context

### 3. Parallel-First Execution
Use **Wave → Checkpoint → Wave** pattern for efficiency:
- Wave 1: [Read files in parallel]
- Checkpoint: Analyze findings
- Wave 2: [Edit files in parallel]

### 4. Token Efficiency
- Simple tasks (typo fix): ~200 tokens
- Medium tasks (bug fix): ~1,000 tokens
- Complex tasks (feature): ~2,500 tokens

---

## Development Workflow

### Essential Commands

```bash
# Use SuperDroid slash commands
/research "topic"           # Deep web research
/implement "feature"        # Code implementation
/test                       # Run tests
/analyze                    # Code analysis
/brainstorm "idea"          # Structured brainstorming
```

### Git Workflow

```bash
# Branch naming
feature/your-feature
fix/bug-description
docs/documentation-update

# Commit convention
feat: add new feature
fix: resolve bug
docs: update documentation
refactor: code improvement
test: add tests
```

---

## Project Patterns

### Code Style
- Follow existing patterns in the codebase
- Use consistent naming conventions
- Add comments only when necessary
- Prefer readability over cleverness

### Testing
- Write tests for new features
- Run existing tests before committing
- Fix broken tests immediately

### Documentation
- Update docs when adding features
- Keep README current
- Document breaking changes

---

## Droids (Subagents)

SuperDroid includes 16 specialized droids for delegation:

| Droid | Use Case |
|-------|----------|
| `pm-agent` | Project orchestration, PDCA cycles |
| `security-engineer` | Security audits, vulnerability checks |
| `frontend-architect` | UI components, accessibility |
| `backend-architect` | APIs, server logic |
| `deep-research-agent` | Autonomous research |
| `quality-engineer` | Testing, QA |

### Using Droids

```
"Use the security-engineer droid to audit authentication"
"Delegate to deep-research-agent for market analysis"
```

---

## Best Practices

### Before Implementation
1. Read relevant files first
2. Check for existing patterns
3. Verify requirements are clear
4. Assess confidence level

### During Implementation
1. Use TodoWrite for tracking
2. Make atomic changes
3. Test incrementally
4. Document decisions

### After Implementation
1. Run tests
2. Review changes
3. Update documentation
4. Clean up temporary files

---

## MCP Integration (Optional)

For enhanced capabilities, configure these MCP servers:

- **Tavily**: Web search for `/research` command
- **Context7**: Official documentation lookup
- **Playwright**: Browser automation for testing

Configure in `~/.factory/mcp.json`.

---

## Troubleshooting

### Common Issues

1. **Commands not working**: Restart Droid CLI after installation
2. **Droids not found**: Check `~/.factory/droids/` directory
3. **MCP errors**: Verify server configuration

### Getting Help

- Use `/help` command
- Check docs/ directory
- Open GitHub issue
