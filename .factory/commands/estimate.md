---
description: Time and effort estimation for features and tasks
argument-hint: <feature or task description>
---

# /estimate - Effort Estimation

Estimate effort for `$ARGUMENTS`:

## Estimation Process

### 1. Scope Analysis
- Break down into subtasks
- Identify dependencies
- Assess complexity

### 2. Effort Calculation
- Development time
- Testing time
- Review/integration time
- Buffer for unknowns

### 3. Risk Assessment
- Technical risks
- Dependency risks
- Knowledge gaps

## Estimation Framework

| Complexity | Time | Description |
|:----------:|:----:|-------------|
| **Trivial** | < 1h | Simple fix, typo, config |
| **Simple** | 1-4h | Single component change |
| **Medium** | 4-16h | Multiple components |
| **Complex** | 2-5 days | New feature, integration |
| **Epic** | 1-4 weeks | Major system change |

## Output Format

```
📊 Estimation: [task]

## Breakdown
├── Task 1: [X hours]
├── Task 2: [X hours]
├── Testing: [X hours]
└── Buffer: [X hours]

## Total: [X hours/days]

## Confidence: [High/Medium/Low]

## Risks
├── [Risk 1]: [Mitigation]
└── [Risk 2]: [Mitigation]

## Assumptions
├── [Assumption 1]
└── [Assumption 2]
```

## Examples

```
/estimate adding OAuth2 authentication
/estimate migrating database to PostgreSQL
/estimate building admin dashboard
```

## Tips

- Add 20-30% buffer for unknowns
- Higher buffer for less familiar tech
- Consider testing in estimates
- Account for code review time
