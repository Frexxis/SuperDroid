# Droids Guide

SuperDroid includes 16 specialized droids (subagents) for focused tasks.

## What are Droids?

Droids are specialized AI assistants with:
- Domain expertise
- Focused tool access
- Specific responsibilities
- Consistent behavior

## Using Droids

### Via Natural Language
```
Use the security-engineer droid to audit this code
Ask the frontend-architect to review this component
Delegate to deep-research-agent for market research
```

### Via /agent Command
```
/agent security-engineer "audit authentication"
/agent frontend-architect "review UI patterns"
```

### Via Task Delegation
The pm-agent automatically delegates to appropriate droids.

## Available Droids

### Project Management

#### pm-agent
**Purpose**: Project orchestration and PDCA cycles
**Tools**: Full access
**Use for**: 
- Complex multi-step projects
- Workflow coordination
- Progress tracking

### Engineering

#### frontend-architect
**Purpose**: UI/UX, accessibility, React/Vue
**Tools**: Read, Grep, Edit, Create, WebSearch
**Use for**:
- Component design
- Accessibility review
- Performance optimization

#### backend-architect
**Purpose**: APIs, databases, server logic
**Tools**: Read, Grep, Edit, Execute, WebSearch
**Use for**:
- API design
- Database schema
- Server architecture

#### system-architect
**Purpose**: System design and patterns
**Tools**: Read, Grep, WebSearch
**Use for**:
- Architecture decisions
- Technology selection
- Scalability planning

#### devops-architect
**Purpose**: CI/CD, infrastructure
**Tools**: Read, Grep, Edit, Execute
**Use for**:
- Pipeline setup
- Deployment automation
- Infrastructure design

### Quality & Security

#### security-engineer
**Purpose**: Vulnerability assessment, compliance
**Tools**: Read, Grep, WebSearch
**Use for**:
- Security audits
- Threat modeling
- Compliance checks

#### quality-engineer
**Purpose**: Testing, QA processes
**Tools**: Read, Grep, Edit, Execute
**Use for**:
- Test strategy
- Test automation
- Quality metrics

#### performance-engineer
**Purpose**: Optimization, profiling
**Tools**: Read, Grep, Execute, WebSearch
**Use for**:
- Performance analysis
- Bottleneck identification
- Optimization

### Analysis & Research

#### deep-research-agent
**Purpose**: Autonomous web research
**Tools**: Read, WebSearch, FetchUrl
**Use for**:
- Comprehensive research
- Competitive analysis
- Technology evaluation

#### requirements-analyst
**Purpose**: Requirements gathering
**Tools**: Read, Grep, WebSearch
**Use for**:
- Requirements documentation
- Stakeholder analysis
- Specification writing

#### root-cause-analyst
**Purpose**: Problem investigation
**Tools**: Read, Grep, Execute, WebSearch
**Use for**:
- Bug investigation
- 5 Whys analysis
- Prevention planning

#### business-analyst
**Purpose**: Business process analysis
**Tools**: Read, Grep, WebSearch
**Use for**:
- Process mapping
- Business requirements
- Value analysis

### Development Support

#### refactoring-expert
**Purpose**: Code improvement
**Tools**: Read, Grep, Edit, MultiEdit, Execute
**Use for**:
- Code cleanup
- Technical debt
- Pattern application

#### technical-writer
**Purpose**: Documentation
**Tools**: Read, Grep, Edit, Create
**Use for**:
- API documentation
- Guides and tutorials
- README updates

#### python-expert
**Purpose**: Python development
**Tools**: Read, Grep, Edit, Execute
**Use for**:
- Python best practices
- Framework guidance
- Code review

### Education

#### learning-guide
**Purpose**: Concept explanation
**Tools**: Read, WebSearch
**Use for**:
- Learning paths
- Concept breakdown
- Resource curation

#### socratic-mentor
**Purpose**: Guided discovery
**Tools**: Read, Grep, WebSearch
**Use for**:
- Problem-solving guidance
- Critical thinking
- Self-discovery

## Creating Custom Droids

Create `.md` files in `.factory/droids/`:

```yaml
---
name: my-custom-droid
description: What this droid does
model: inherit
tools: ["Read", "Grep", "Edit"]
---

You are a specialized assistant that...
[System prompt here]
```

### Tool Options

| Category | Tools |
|----------|-------|
| Read-only | Read, LS, Grep, Glob |
| Edit | Create, Edit, MultiEdit |
| Execute | Execute |
| Web | WebSearch, FetchUrl |

## Best Practices

1. **Choose the right droid** for the task
2. **Provide context** in your request
3. **Let pm-agent delegate** for complex tasks
4. **Create custom droids** for repeated patterns
