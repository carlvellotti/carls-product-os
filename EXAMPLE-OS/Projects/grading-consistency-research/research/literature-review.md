# Literature Review: Grading Consistency

## Purpose

Review academic research on grading consistency, inter-rater reliability, and calibration methods to inform our product direction.

---

## Key Findings Summary

1. **Inter-rater reliability is a known problem** - Decades of research confirm significant variance in how different graders evaluate the same work.

2. **The problem is worse for subjective assessments** - Essays and open-ended responses show more variance than structured/quantitative work.

3. **Calibration helps but requires effort** - Training graders together improves consistency but is time-intensive.

4. **Technology solutions are emerging** - AI-assisted grading and calibration tools show promise but adoption is limited.

---

## Literature Sources

### 1. Bloxham, S. et al. (2011). "Mark my words: the role of assessment criteria in UK higher education grading practices"

**Source:** Studies in Higher Education, 36(6), 655-670

**Key findings:**
- Even with detailed rubrics, experienced markers showed significant variance
- 31% of essays would have received a different grade class from a different marker
- "Interpretive frameworks" differ between markers even when using same rubric

**Implications for us:**
- Rubrics alone don't solve the problem
- Need to address interpretation, not just documentation
- Opportunity for calibration features

---

### 2. Meadows, M. & Billington, L. (2005). "A review of the literature on marking reliability"

**Source:** National Assessment Agency report

**Key findings:**
- Inter-rater reliability varies by subject: Math (high) > Science (medium) > English (low)
- "Comparative pairs" method (comparing two submissions) improves consistency vs. absolute marking
- Marker fatigue significantly impacts consistency - variance increases after 15-20 items

**Implications for us:**
- Consider subject-specific approaches
- Comparative grading could be a feature direction
- Fatigue alerts could help TAs maintain consistency

---

### 3. Grainger, P. et al. (2017). "Assessment rubrics: a vehicle for calibration"

**Source:** Assessment & Evaluation in Higher Education, 42(4), 539-555

**Key findings:**
- Calibration sessions where graders discuss sample submissions significantly improved inter-rater reliability (effect size d=0.8)
- Most effective format: grade independently, then discuss discrepancies
- 2-3 calibration sessions per assignment was optimal

**Implications for us:**
- Could build calibration workflow into product
- Show TAs where they diverged from peers
- Facilitate async "calibration discussions"

---

### 4. Derrick, C. (2022). "AI-assisted calibration in large-enrollment courses"

**Source:** Journal of Computing in Higher Education

**Key findings:**
- AI can identify submissions where human graders are likely to disagree
- Flagging these for "calibration review" improved consistency by 25%
- Students in AI-assisted sections reported higher perceived fairness

**Implications for us:**
- Our AI could predict "calibration risk" submissions
- Auto-flag for secondary review or discussion
- Builds on our existing AI grading infrastructure

---

### 5. Jonsson, A. & Svingby, G. (2007). "The use of scoring rubrics: Reliability, validity and educational consequences"

**Source:** Educational Research Review, 2(2), 130-144

**Key findings:**
- Meta-analysis of 75 studies on rubric use
- Analytic rubrics (dimension-by-dimension) more reliable than holistic rubrics
- Exemplars/anchor papers significantly improve reliability
- Training effects decay over time without reinforcement

**Implications for us:**
- Encourage analytic rubric design in our product
- Could include exemplar/anchor submission features
- Periodic "recalibration" prompts to maintain consistency

---

### 6. Hunter, D. & Docherty, P. (2011). "Reducing variation in the assessment of student writing"

**Source:** Assessment & Evaluation in Higher Education, 36(1), 109-124

**Key findings:**
- "Blind double marking" (two graders, no communication) showed 23% disagreement rate
- "Moderated marking" (second grader reviews first grade) reduced to 8%
- "Consensus marking" (graders discuss before finalizing) reduced to 4%

**Implications for us:**
- Could build moderation workflow (TA grades, second TA reviews edge cases)
- Surface disagreement data to professors
- Consensus marking might be too time-intensive for most use cases

---

## Synthesis: What This Means for Product

### The Problem is Real and Quantifiable

| Assessment Type | Typical Disagreement Rate | Notes |
|----------------|---------------------------|-------|
| Math/quantitative | 5-10% | Well-defined right/wrong |
| Science short answer | 15-20% | Some interpretation needed |
| Essay/open-ended | 20-35% | High subjectivity |

These rates represent submissions that would receive materially different grades from different graders.

### What Works to Improve Consistency

| Intervention | Effectiveness | Effort Required |
|--------------|---------------|-----------------|
| Detailed rubrics | Low-Medium | Low |
| Anchor/exemplar papers | Medium | Medium |
| Calibration sessions | High | High |
| Double-marking with moderation | High | High |
| AI-assisted flagging | Medium-High | Low (after setup) |

### Product Opportunity Framework

**Low-hanging fruit (v1 potential):**
- Rubric design guidance/templates
- Exemplar submission features
- Display TA-to-TA variance to professor

**Medium effort (v2 potential):**
- Async calibration workflow (grade samples, see peer grades)
- AI flags for "high variance risk" submissions
- Moderation queue for second review

**High effort (future):**
- Real-time calibration nudges during grading
- Predictive consistency scoring for TAs
- Comparative grading interface

---

## Questions for User Research

Based on this literature, we should explore in interviews:

1. Have you ever done calibration sessions with TAs? What worked/didn't?
2. Do you use exemplar/anchor papers? How do you share them?
3. Have you experienced student complaints about grading fairness? How did you handle it?
4. Would you use a tool that flagged submissions where TAs might disagree?
5. How much time would you invest in improving consistency?

---

## Additional Sources to Review

- [ ] Sadler, D.R. (2009). "Indeterminacy in the use of preset criteria for assessment and grading"
- [ ] Boud, D. & Falchikov, N. (2006). "Aligning assessment with long-term learning"
- [ ] Black, P. & Wiliam, D. (1998). "Assessment and classroom learning" (foundational but dated)
- [ ] Recent EdTech industry white papers (Turnitin, Gradescope, Instructure)

---

*Review by: Alex Chen*
*Last updated: Feb 7, 2025*
*Status: In progress - awaiting additional sources*
