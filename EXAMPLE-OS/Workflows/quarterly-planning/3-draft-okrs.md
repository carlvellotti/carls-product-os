# Step 3: Draft OKRs

## Purpose

Translate gathered inputs into clear, measurable OKRs that will guide the quarter's work.

## OKR Principles

### Objectives
- **Qualitative and inspirational** - What do we want to achieve?
- **Ambitious but achievable** - Stretch goals, not sandbagging
- **Clear direction** - Team knows what "good" looks like
- **Limited quantity** - 3-4 max per team

### Key Results
- **Quantitative and measurable** - How will we know we achieved it?
- **Outcome-based** - Measure results, not activities
- **Specific** - No ambiguity about what counts
- **Time-bound** - Achievable within the quarter

### Bad vs. Good Examples

| Bad | Good | Why |
|-----|------|-----|
| O: Improve onboarding | O: Make every teacher successful in their first week | Clear, inspiring, specific |
| KR: Launch new onboarding flow | KR: Increase 7-day activation rate from 55% to 70% | Outcome vs output |
| KR: Do 10 user interviews | KR: Achieve NPS of 40+ among new teachers | Measures impact, not effort |

## Drafting Process

### 1. Review Input Summary

From Step 2, identify:
- Top strategic priorities
- Biggest user pain points
- Technical constraints
- Cross-team dependencies

### 2. Identify 3-4 Themes

Cluster inputs into major themes that could become Objectives:
- Each theme should be significant (worth a quarter's focus)
- Themes should be distinct (not overlapping)
- Together they should cover the most important work

### 3. Draft Objectives

For each theme, write an Objective:
- Use active language
- Make it memorable
- Ensure it resonates with the team

**Formula:** `[Action verb] + [what we're trying to achieve] + [for whom/why]`

Examples:
- "Make teachers fall in love with grading again"
- "Build an unshakeable foundation for scale"
- "Turn happy teachers into our best salespeople"

### 4. Define Key Results

For each Objective, define 2-4 Key Results:
- Each KR should be independently valuable
- Together they should fully describe success
- At least one should be easily measurable (leading indicator)

**Formula:** `[Metric] from [baseline] to [target]`

Examples:
- "Increase Teacher Activation Rate from 55% to 70%"
- "Reduce time-to-first-grade from 120 min to 30 min"
- "Achieve NPS of 50+ among activated teachers"

### 5. Sanity Check

For each OKR set, ask:
- [ ] Is the Objective inspirational and clear?
- [ ] Are Key Results measurable with current instrumentation?
- [ ] Do we know the baseline for each KR?
- [ ] Is the target ambitious but achievable?
- [ ] Does this ladder up to company goals?
- [ ] Is it within our control (not dependent on external factors)?

### 6. Map to Roadmap

For each Key Result:
- What initiatives/projects will move this metric?
- What's the expected contribution of each?
- Do we have capacity for these initiatives?

## Draft OKR Template

See `okr-template.md` for the full format.

```markdown
## Objective 1: [Objective statement]

**Theme:** [What input theme this addresses]
**Owner:** Alex Chen
**Strategic alignment:** [Which company goal this supports]

| Key Result | Baseline | Target | Confidence |
|------------|----------|--------|------------|
| [KR1] | X | Y | High/Med/Low |
| [KR2] | X | Y | High/Med/Low |
| [KR3] | X | Y | High/Med/Low |

**Initiatives:**
- [Initiative 1] → Primarily moves KR1
- [Initiative 2] → Primarily moves KR2, also KR1

**Dependencies:**
- [Any cross-team or external dependencies]

**Risks:**
- [Risk and mitigation]
```

## Common Mistakes to Avoid

| Mistake | Fix |
|---------|-----|
| Too many OKRs | Cut to 3-4 objectives, 2-4 KRs each |
| Output-based KRs | Rewrite as outcomes ("ship X" → "achieve Y impact") |
| Unmeasurable KRs | Find a proxy metric or reconsider the KR |
| No baseline | Get the baseline before finalizing (or don't include) |
| Sandbagging | Ask "would I be proud to hit 70% of this?" |
| Kitchen sink | Each KR should be critical, not nice-to-have |

## Getting Baseline Data

For each KR, you need current state:

| Metric | Source | How to Pull |
|--------|--------|-------------|
| Activation Rate | Amplitude | "Teacher Funnel" dashboard |
| Time-to-first-grade | Amplitude | Event timing analysis |
| NPS | Delighted | Current score from dashboard |
| Trial Conversion | Stripe | Subscription funnel report |

If baseline doesn't exist, either:
1. Instrument it now (if quick)
2. Set up measurement and set target next quarter
3. Use a proxy metric
