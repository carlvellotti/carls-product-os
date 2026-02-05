# Step 2: Pattern Extraction

## Goal

Identify patterns across interviews that reveal genuine insights, not just isolated opinions.

## Pattern Extraction Process

### 1. Gather All Themes

Collect all tags/themes from individual interview reviews:
- List every theme that appeared
- Note which participants mentioned each
- Include the count (e.g., "5 of 6 participants")

### 2. Cluster Related Themes

Group themes that are related:
- Some themes might merge (same idea, different words)
- Some might be sub-themes of a larger pattern
- Keep them separate if the nuance matters

Example clustering:
```
GRADING EFFICIENCY
├── time-pressure (6/6)
├── batch-grading-desire (4/6)
└── grading-during-prep (3/6)

FEEDBACK QUALITY
├── student-feedback-quality (5/6)
├── personalization-desire (4/6)
└── feedback-templates (3/6)
```

### 3. Assess Evidence Strength

Rate each pattern:

| Strength | Criteria | How to Report |
|----------|----------|---------------|
| **Strong** | 5-6 of 6 participants, consistent | "Teachers consistently reported..." |
| **Moderate** | 3-4 of 6, some variation | "Several teachers mentioned..." |
| **Emerging** | 2 of 6, worth noting | "A few teachers described..." |
| **Outlier** | 1 of 6, might be unique | "One teacher uniquely..." |

### 4. Identify Contradictions

Document where participants disagreed:
- What was the nature of the disagreement?
- Can you explain it by segment (new vs experienced, school type, etc.)?
- Is it a genuine split in needs, or just different language?

Example:
```
CONTRADICTION: Automation preferences
- 4 teachers wanted more automation in grading
- 2 teachers worried about "losing control" of grades
- Explanation: The 2 concerned teachers both had < 1 year experience
  and seemed to have lower trust in AI generally
```

### 5. Look for Unexpected Patterns

The best insights often come from:
- Things that surprised you
- Behaviors that contradict stated preferences
- Workarounds that reveal unmet needs
- Emotional intensity around specific topics

## Pattern Documentation Format

For each major pattern:

```markdown
## Pattern: [Name]

**Strength:** Strong/Moderate/Emerging
**Participants:** X of Y

**Summary:** [1-2 sentences describing the pattern]

**Supporting Evidence:**
- P1: "[Quote]"
- P3: "[Quote]"
- P5: "[Quote]"

**Variation/Nuance:**
- [Any important differences between participants]

**Contradicting Evidence:**
- [If any participants said the opposite, note it here]

**Implication:** [What this might mean for the product]
```

## Connecting Patterns to Opportunities

For each strong pattern, ask:
1. What job is the user trying to do?
2. What's preventing them from doing it well today?
3. How might we address this?
4. What's the potential impact if we solve it?

## Red Flags in Pattern Extraction

Watch out for:
- **Forcing patterns**: Not every theme becomes a pattern
- **Ignoring outliers**: Sometimes the outlier has the real insight
- **Conflating correlation**: Two things appearing together doesn't mean one causes the other
- **Leading question artifacts**: If you asked leading questions, the pattern might be artificial
