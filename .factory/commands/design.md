---
description: System architecture and design with patterns
argument-hint: <system or feature> [--type architecture|api|database|ui]
---

# /design - System Design

Design architecture for `$ARGUMENTS`:

## Design Process

### 1. Requirements Analysis
- Functional requirements
- Non-functional requirements (scalability, performance)
- Constraints and limitations

### 2. Architecture Design
- System components
- Data flow
- Integration points
- Technology selection

### 3. Documentation
- Architecture diagrams (ASCII/Mermaid)
- Component specifications
- API contracts
- Data models

## Design Types

| Type | Focus |
|------|-------|
| `architecture` | Overall system structure |
| `api` | REST/GraphQL API design |
| `database` | Schema and data modeling |
| `ui` | Component hierarchy and state |

## Output Format

```
📐 Design Document: [system]

## Overview
[High-level description]

## Architecture
[Diagram and explanation]

## Components
[List with responsibilities]

## Data Flow
[How data moves through system]

## API Contracts
[Endpoint definitions]

## Trade-offs
[Decisions and rationale]
```

## Examples

```
/design user authentication system
/design payment processing --type api
/design user data model --type database
/design dashboard layout --type ui
```

## Design Principles

1. **Separation of Concerns**
2. **Single Responsibility**
3. **Loose Coupling**
4. **High Cohesion**
5. **YAGNI** - Don't over-engineer
