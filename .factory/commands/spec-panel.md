---
description: Multi-expert specification analysis and requirements review
argument-hint: <requirements or spec document>
---

# /spec-panel - Specification Analysis

Analyze specifications for `$ARGUMENTS` from multiple expert perspectives:

## Expert Panel

### 🏗️ Architect
- System design implications
- Scalability concerns
- Integration requirements

### 🔒 Security Engineer
- Security requirements
- Threat modeling
- Compliance needs

### 🎨 UX Designer
- User experience flow
- Accessibility requirements
- Interface patterns

### 🧪 QA Engineer
- Testability assessment
- Edge cases
- Acceptance criteria

### 📊 Product Manager
- Business value
- Priority assessment
- Success metrics

## Analysis Process

1. **Review** - Each expert reviews the spec
2. **Identify** - Gaps, risks, and opportunities
3. **Discuss** - Cross-functional concerns
4. **Recommend** - Actionable improvements

## Output Format

```
📋 Spec Panel Review: [topic]

## Architect Assessment
[Findings and recommendations]

## Security Review
[Findings and recommendations]

## UX Evaluation
[Findings and recommendations]

## QA Assessment
[Findings and recommendations]

## Product Perspective
[Findings and recommendations]

## Consolidated Recommendations
1. [Priority item]
2. [Priority item]
3. [Priority item]

## Open Questions
- [Question 1]
- [Question 2]
```

## Examples

```
/spec-panel "User should be able to reset password via email"
/spec-panel review PRD.md
/spec-panel payment integration requirements
```
