# User Research Synthesis: TA Workload Tracker

## Research Overview

| Field | Value |
|-------|-------|
| Research Period | January 8-24, 2025 |
| Lead Researcher | Alex Chen |
| Method | Semi-structured interviews (45 min) |
| Participants | 12 total (7 TAs, 5 professors) |
| Institutions | 6 universities (UC Davis, UW, Northwestern, Georgia Tech, Boston University, Stanford) |

---

## Executive Summary

Our research confirmed strong demand for TA workload visibility tools. **100% of professors** interviewed expressed interest in a dashboard solution, and **6 of 7 TAs** wanted their professors to have better visibility (1 was neutral, none opposed).

### Key Finding

**The workload equity problem is invisible to professors but painfully obvious to TAs.** This creates a trust asymmetry where TAs feel unseen and professors feel helpless. Simple visibility would solve most issues.

---

## Participant Summary

### Professors Interviewed (5)

| ID | Institution | Course Size | # TAs | GradeFlow Tenure |
|----|-------------|-------------|-------|------------------|
| P1 - Prof. Martinez | UC Davis | 180 | 4 | 3 semesters |
| P2 - Prof. Johnson | UW | 240 | 5 | 2 semesters |
| P3 - Prof. Williams | Northwestern | 95 | 2 | 1 semester |
| P4 - Prof. Nakamura | Georgia Tech | 320 | 6 | 4 semesters |
| P5 - Prof. Foster | Boston University | 150 | 3 | 2 semesters |

### TAs Interviewed (7)

| ID | Institution | Role | Experience |
|----|-------------|------|------------|
| T1 - Sarah | UC Davis | Grad TA | 3 semesters |
| T2 - Marcus | UW | Undergrad TA | 4 semesters |
| T3 - Jin | Northwestern | Grad TA | 2 semesters |
| T4 - Taylor | Georgia Tech | Grad TA | 1 semester |
| T5 - Amanda | Georgia Tech | Undergrad TA | 2 semesters |
| T6 - Chris | Boston University | Grad TA | 5 semesters |
| T7 - Priya | Stanford | Undergrad TA | 3 semesters |

---

## Key Themes

### Theme 1: The Invisible Inequity Problem

**Finding:** Professors have near-zero visibility into workload distribution. Every professor interviewed admitted they don't track this.

**Evidence:**
- 0/5 professors actively monitor TA workload
- 5/5 professors suspect imbalances exist
- 5/7 TAs reported significant workload variance in their courses

**Quantitative data point:** In courses where we had multiple TAs interviewed, the self-reported workload variance was 2.5x-3.5x between highest and lowest contributors.

**Implication:** The data exists in GradeFlow. Professors just need it surfaced.

---

### Theme 2: Social Dynamics Prevent Self-Correction

**Finding:** TAs won't raise workload concerns, and professors won't ask directly. The problem festers.

**Evidence:**
- 0/7 TAs had raised workload concerns with their professor
- Reasons given: "don't want to throw anyone under the bus," "seems petty," "afraid of seeming like I'm complaining"
- 4/5 professors said they've "heard rumblings" but never direct complaints

**Key quote (T1 - Sarah):**
> "If I could see what everyone else is doing, at least I'd know if I'm being paranoid or if there's actually an imbalance."

**Implication:** The tool needs to provide objective data that removes the social discomfort of raising the issue.

---

### Theme 3: Professors Would Act If They Knew

**Finding:** Professors care about fairness and would address imbalances - they just don't have information.

**Evidence:**
- 5/5 professors expressed genuine concern about TA wellbeing
- 4/5 said they would have a direct conversation if shown data
- 1/5 said they might implement automatic assignment changes

**Key quote (P1 - Prof. Martinez):**
> "Sarah is amazing. I hope she's not doing more than her share. I would feel terrible."

**Implication:** The dashboard needs to make intervention easy - not just show data, but prompt action.

---

### Theme 4: Time is the Blocker

**Finding:** Professors want to manage TAs better but are stretched too thin. Any solution must be effortless.

**Evidence:**
- Avg time professors currently spend on TA management: ~20 min/week (logistics only)
- 3/5 professors mentioned attempting manual tracking but abandoning it
- Desired time investment for new tool: "30 seconds to glance at" (multiple responses)

**Implication:** Dashboard must be scannable in under 30 seconds. Alerts are more valuable than dashboards.

---

### Theme 5: Volume Alone Doesn't Tell the Story

**Finding:** Counting submissions graded is a good start, but assignment complexity matters.

**Evidence:**
- T2 (Marcus) raised this strongly: "An essay should count as 5 submissions"
- T6 (Chris) mentioned "cherry-picking" behavior - TAs grab easy assignments
- P4 (Prof. Nakamura) independently suggested "weighted workload" as an improvement

**Quantitative example:** In one course, TA #1 graded 200 quiz responses (avg 1 min each), TA #2 graded 80 essays (avg 8 min each). Raw count suggests #1 did 2.5x more work. Actual effort was reversed.

**Implication:** v1 can launch with volume, but v1.1 should explore weighted metrics based on assignment type or actual time data.

---

### Theme 6: TA Self-Service is a Future Opportunity

**Finding:** TAs want visibility into their own performance, even if they don't see others'.

**Evidence:**
- 6/7 TAs expressed interest in seeing their own stats
- Use cases: track progress toward "fair share," document contribution for recommendation letters, personal accountability
- 2/7 TAs asked if they could eventually see aggregate (anonymized) comparison

**Key quote (T1 - Sarah):**
> "When I ask for recommendations, I want to show I did way more than average."

**Implication:** TA self-service view should be on v2 roadmap. Consider "TA impact report" for recommendation letters.

---

## Persona Validation

Our research validated two primary personas:

### Persona 1: Professor Patricia (Primary)

Confirmed characteristics:
- Manages 3-6 TAs across 1-2 courses
- Values fairness but lacks time to manage actively
- Trust-based management style by default
- Would act on data if presented clearly

### Persona 2: Overwhelmed TA Oliver

Emerged pattern:
- High-performing TAs pick up slack without recognition
- Feel resentment but won't self-advocate
- At risk of burnout and reduced engagement
- Want objective data as "proof"

### Emerging Persona: Department Chair Doug

Three institutions mentioned department-level visibility needs:
- Budget justification for TA hours
- Cross-course resource optimization
- Accreditation reporting

**Recommendation:** Add department admin features to v1.1 roadmap for enterprise tier.

---

## Design Implications

| Research Finding | Design Implication |
|------------------|-------------------|
| Professors scan in 30 seconds | Dashboard must surface key insight immediately - bar chart, not tables |
| Alerts more valuable than dashboards | Email alerts for variance threshold; in-app secondary |
| Social dynamics prevent raising issues | Frame as "fairness tool" not "surveillance"; provide conversation starters |
| Assignment complexity varies | Label as "v1: volume" with v1.1 weighted metrics |
| Historical data for planning | Include semester trend view and export for budget discussions |
| TAs want self-visibility eventually | Design TA-facing view in v2; ensure dashboard architecture supports it |

---

## Competitive Validation

See [[ta-workload-tracker/competitive-analysis|Competitive Analysis]] for full details.

**Summary:** No direct competitor offers robust TA workload visibility. This is a differentiation opportunity.

- Canvas: No workload dashboard
- Gradescope: Basic "grading progress" but no TA-level breakdown
- Top Hat: No relevant features
- Brightspace: Admin reports only, not accessible to professors

---

## Recommended Next Steps

1. **Proceed with current design direction** - Research strongly validates the problem and solution approach
2. **Prioritize alerts over dashboard polish** - Proactive notifications are higher value
3. **Plan v1.1 features now** - Weighted workload metrics and TA self-service are validated needs
4. **Include 3 professors and 2 TAs in beta** - Participants expressed strong interest

---

## Appendix: Interview Links

- [[ta-workload-tracker/research/interview-sarah-ta|T1: Sarah (TA)]]
- [[ta-workload-tracker/research/interview-marcus-ta|T2: Marcus (TA)]]
- [[ta-workload-tracker/research/interview-prof-martinez|P1: Prof. Martinez]]
- Additional transcripts available in research repository

---

*Synthesis completed: January 24, 2025*
*Author: Alex Chen*
