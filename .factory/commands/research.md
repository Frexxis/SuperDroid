---
description: Deep web research with adaptive planning and intelligent search
argument-hint: <query> [--depth quick|standard|deep|exhaustive]
---

# /research - Deep Research Command

Perform comprehensive web research on `$ARGUMENTS` with the following approach:

## Research Process

### 1. Understand (5-10% effort)
- Assess query complexity and ambiguity
- Identify required information types
- Define success criteria

### 2. Plan (10-15% effort)
- Decompose research question into sub-queries
- Identify parallelization opportunities
- Create investigation milestones

### 3. Execute (50-60% effort)
- **Parallel searches**: Batch similar queries together
- **Multi-hop exploration**: Follow entity and concept chains
- **Evidence collection**: Track sources and confidence levels

### 4. Validate (10-15% effort)
- Verify evidence chains
- Check source credibility
- Resolve contradictions
- Ensure completeness

## Depth Levels

| Depth | Sources | Time | Best For |
|:-----:|:-------:|:----:|----------|
| **quick** | 5-10 | ~2min | Quick facts |
| **standard** | 10-20 | ~5min | General research (default) |
| **deep** | 20-40 | ~8min | Comprehensive analysis |
| **exhaustive** | 40+ | ~10min | Academic-level research |

## Output Format

Provide research results with:
1. **Executive Summary** - Key findings in 2-3 sentences
2. **Detailed Findings** - Organized by topic/theme
3. **Sources** - List all references with URLs
4. **Confidence Level** - Overall confidence in findings
5. **Knowledge Gaps** - What couldn't be determined

## Example Usage

```
/research "latest developments in quantum computing 2024"
/research "competitive analysis of AI coding assistants" --depth deep
/research "best practices for distributed systems"
```

Use WebSearch and FetchUrl tools for gathering information. Always cite sources.
