# Grading Consistency & Bias Research

*Research synthesis for AI grading and calibration features*
*Last updated: November 2025*

## The Problem: Grading Is Unreliable

Foundational studies show that grading, especially for subjective assignments, is remarkably inconsistent:

- **Starch & Elliott (1912, 1913):** Classic studies showed the same English paper received grades ranging from 50 to 98 from different teachers
- **Modern replication (Meadows & Billington, 2005):** Found similar variability persists despite rubrics
- **Current estimate:** Inter-rater reliability for essay grading averages 0.60-0.70 (below the 0.80 threshold for "acceptable")

## Key Research Findings

### 1. Sources of Grading Bias

**Order effects**
*Study: Spear, 1997*
- Papers graded first in a batch receive harsher scores
- Papers following a poor paper receive inflated scores
- Effect size: 0.3-0.5 grade points

**Our feature response:** Randomize grading order in batch interface

---

**Name/identity bias**
*Study: Malouff & Thorsteinsson, 2016*
- Graders give higher scores to students they like or know
- Gender-associated names affect scores in STEM fields
- Prestigious-sounding names receive benefit of doubt

**Our feature response:** Anonymous grading mode (shipped Q2 2025)

---

**Fatigue effects**
*Study: Danziger et al., 2011 (judicial decisions, applicable to grading)*
- Decision quality degrades over time
- Breaks restore decision quality
- Effect is unconscious - graders don't notice it

**Our feature response:** Suggested break reminders after 45 min (not yet shipped)

---

**Handwriting bias**
*Study: Chase, 1986*
- Neat handwriting receives 0.5-1.0 grade point advantage
- Effect persists even when content is identical
- More pronounced for subjective assignments

**Our feature response:** Digital submission normalization; AI grading doesn't see handwriting

---

**Anchoring on first impression**
*Study: Hughes et al., 2011*
- First paragraph disproportionately affects overall grade
- Graders often decide grade early, then confirm
- Rubric-based grading reduces but doesn't eliminate

**Our feature response:** Component-by-component grading enforced by rubric tool

---

### 2. What Improves Consistency

**Rubric design**
*Study: Jonsson & Svingby, 2007 (meta-analysis)*
- Analytic rubrics (component-based) beat holistic rubrics
- More specific descriptors = higher reliability
- Training on rubric use is essential
- Sweet spot: 4-6 performance levels

**Reliability improvements:**
| Rubric Type | Average Reliability |
|-------------|---------------------|
| No rubric | 0.52 |
| Holistic rubric | 0.65 |
| Analytic rubric | 0.78 |
| Analytic + training | 0.85 |

**Our feature response:** Rubric builder emphasizes analytic rubrics with specific descriptors

---

**Calibration/norming sessions**
*Study: Chen et al., 2023*
- Grading sample assignments together improves alignment
- Discussing disagreements is key mechanism
- Effect lasts ~2 weeks before drift returns
- Most effective at start of assignment, not just start of semester

**Our feature response:** Calibration tool v1 (shipped Q4 2025)

---

**Real-time feedback**
*Study: Graesser et al., 2018*
- Showing graders how they compare to peers improves consistency
- "Drift alerts" (you're trending harsher) are effective
- Works best when immediate, not post-hoc

**Our feature response:** Grading analytics dashboard shows patterns; real-time alerts on roadmap

---

**Double grading with reconciliation**
*Study: Various, meta-analyzed by Meadows & Billington, 2005*
- Having two graders improves reliability to 0.90+
- But doubles workload
- Sampling approach (double-grade 20%) can work
- Key: Clear reconciliation process for disagreements

**Our feature response:** AI as "second grader" for verification (v2 feature)

---

### 3. AI Grading Research

**Current state of AI grading accuracy**
*Study: Automated Student Assessment Prize (ASAP) competition data + recent replications*

| Assignment Type | AI vs Human Agreement | Notes |
|-----------------|----------------------|-------|
| Short answer | 0.80-0.90 | Near human level |
| Essay (structured) | 0.70-0.85 | Good for clear rubrics |
| Essay (creative) | 0.55-0.70 | Still challenging |
| Code | 0.85-0.95 | Strongest area |
| Math (process) | 0.75-0.85 | Depends on partial credit |

**Our current performance:** 89% suggestion acceptance rate, comparable to research benchmarks

---

**Student/faculty acceptance of AI grading**
*Study: Bearman et al., 2022*

**Student perspectives:**
- 62% comfortable with AI grading if transparent
- 78% want human review available
- Biggest concern: AI missing nuance/creativity
- Biggest benefit they see: Faster feedback

**Faculty perspectives:**
- 48% would use AI for first pass
- 71% want AI as "assistant" not "replacement"
- Concerns: Academic integrity, liability
- Benefits they see: Time savings, consistency

**Our design implication:** "AI suggests, human confirms" is right model

---

**Bias in AI grading systems**
*Study: Mayfield & Black, 2020*

**Key findings:**
- AI systems can perpetuate biases in training data
- Dialectal differences (AAVE, non-native English) often penalized
- Mitigation: Diverse training data, bias auditing, human oversight

**Our approach:**
- Regular bias audits (quarterly)
- Diverse training data sourcing
- Easy override when AI might be biased
- Never use AI as sole grader for high-stakes assessments

---

### 4. Grade Inflation Research

**Trend data**
*Study: Rojstaczer & Healy, 2012, updated through 2024*

- Average GPA at US colleges: 3.15 (up from 2.93 in 2003)
- Grade inflation accelerated during COVID, hasn't retreated
- Inflated grades correlate with student evaluations of teaching
- STEM departments inflate less than humanities

**Implications:**
- "Calibration to past courses" can perpetuate inflation
- AI trained on inflated grades will suggest inflated grades
- Consider absolute standards, not just relative

---

## Synthesis: Design Principles for Grading Features

Based on research, our grading features should:

1. **Encourage analytic rubrics** with specific descriptors (4-6 levels)
2. **Randomize grading order** to reduce order effects
3. **Support anonymous grading** to reduce identity bias
4. **Build in breaks** to combat fatigue
5. **Require component-by-component scoring** before overall grade
6. **Facilitate calibration** at assignment start
7. **Show grading patterns** to make drift visible
8. **Position AI as assistant** - suggest, don't decide
9. **Maintain transparency** - students know when AI is used
10. **Enable easy override** - humans have final say

## Metrics We Should Track

Based on research, key metrics for grading quality:

| Metric | Target | Current |
|--------|--------|---------|
| Inter-rater reliability (Krippendorff's alpha) | >0.80 | 0.74 |
| AI suggestion acceptance rate | >80% | 89% |
| Time to feedback (hours) | <72 | 68 |
| Grading time per assignment (minutes) | Reduce 50% | 47% reduction |
| Grade distribution variance across graders | Low | Not tracked |
| Student grade appeals | Reduce | Not tracked |

## Research Gaps / Future Reading

1. Long-term effects of AI grading on student learning
2. Best practices for AI grading in creative assignments
3. Cultural differences in grading expectations
4. AI grading in non-English languages
