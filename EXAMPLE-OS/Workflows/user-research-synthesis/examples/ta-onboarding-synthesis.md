# TA Onboarding Experience - Synthesis

**Date:** January 15, 2026
**Researcher:** Alex Chen
**Participants:** 6 Teachers (new to GradeFlow, 1-3 months)
**Research Question:** Why do some teachers activate quickly while others stall during onboarding?

---

## Executive Summary

- **Time-to-first-grade is the critical moment**: Teachers who graded their first assignment within 48 hours had 3x higher retention than those who waited longer.
- **Setup friction causes early abandonment**: 4 of 6 teachers described the class setup process as "overwhelming" with too many options upfront.
- **Template discovery is broken**: Teachers who found the assignment templates activated faster, but only 2 of 6 discovered them without help.
- **Recommendation**: Simplify first-run experience to get teachers to their first grade within 30 minutes, not 2 hours.

---

## Research Context

### Objective
Understand why Teacher Activation rate (teachers who grade 5+ assignments in first 14 days) is stuck at 55% despite improvements to core grading features.

### Methodology
- 6 interviews conducted January 8-12, 2026
- 45 minutes each, video call via Zoom
- Participants: Teachers who signed up in past 90 days, mix of activated and non-activated

### Participants Overview
| ID | Role | Experience | School Type | Activated? |
|----|------|------------|-------------|------------|
| P1 | HS Math | 8 years | Public | Yes |
| P2 | MS English | 3 years | Charter | No |
| P3 | HS Science | 12 years | Private | Yes |
| P4 | ES All Subjects | 2 years | Public | No |
| P5 | HS History | 6 years | Public | Yes |
| P6 | MS Math | 1 year | Charter | No |

---

## Key Findings

### Finding 1: First 48 Hours Are Make-or-Break

**Strength:** Strong (6 of 6 participants)

Teachers who graded their first assignment within 48 hours of signup went on to become active users. Those who didn't grade within 48 hours either churned or became sporadic users.

**Evidence:**
> "I remember the first time I saw the AI feedback suggestion, I was like 'okay, this is actually useful.' But I almost didn't get there because setting up my first class took forever." - P1 (activated)

> "I signed up on a Sunday, spent 20 minutes trying to figure out rubrics, then had to make dinner. By the time I came back to it a week later, I'd kind of forgotten why I signed up." - P2 (not activated)

**Nuance:** The 48-hour window isn't about the calendar time - it's about maintaining momentum. Teachers who set aside dedicated time (e.g., a prep period) succeeded; those who tried to do it "in spare moments" failed.

---

### Finding 2: Setup Overwhelm Causes Abandonment

**Strength:** Strong (4 of 6 participants)

The initial class setup flow presents too many choices (rubric style, grading scale, AI feedback preferences, student roster import) before teachers have context for what matters.

**Evidence:**
> "It asked me what grading scale I wanted, and I was like, do I pick the school's scale? My personal scale? I didn't even know what the AI would do with that. I just wanted to grade something." - P4

> "I spent 30 minutes on rubrics before I even created an assignment. In hindsight, I should have just picked anything and fixed it later." - P6

**Nuance:** Experienced teachers (P1, P3, P5) powered through setup because they had strong mental models. Newer teachers without established workflows got stuck in decision paralysis.

---

### Finding 3: Template Discovery Is Broken

**Strength:** Strong (5 of 6 participants)

Assignment templates dramatically reduce time-to-first-grade, but they're buried in a submenu. Only 2 teachers found them without help.

**Evidence:**
> "Templates? I didn't know there were templates until Sarah in my department showed me. That would have saved me hours." - P2

> "I clicked around for a while and eventually found them, but it was like a hidden feature. Why isn't that front and center?" - P5

**Nuance:** The templates that exist are good - teachers loved them once discovered. The problem is purely discovery, not quality.

---

### Finding 4: "Aha Moment" Is First AI Feedback

**Strength:** Moderate (4 of 6 participants)

The moment teachers see AI-generated feedback on real student work is when they understand the product's value. Everything before that feels like "setup."

**Evidence:**
> "The first time the AI suggested feedback on a student essay, I literally said 'whoa' out loud. It was like having a teaching assistant." - P1

> "I was skeptical until I saw it actually grade something. Then I got it." - P3

**Nuance:** 2 teachers (P2, P4) never reached this moment because they churned during setup. The AI feedback is the hook, but we're not getting people there fast enough.

---

## Contradictions & Edge Cases

### Self-Service vs. Guided Setup
- 3 teachers wanted a "just let me explore" experience
- 3 teachers wanted a "tell me exactly what to do" guided flow
- **Explanation:** This split loosely correlated with tech comfort level. More experienced users wanted autonomy; less experienced wanted guidance.
- **Implication:** May need two paths, or smart detection of user type.

---

## Opportunities

Based on these findings, we see opportunities to:

1. **Streamlined First-Grade Flow**: Skip most setup, get teachers to grade one real assignment within 10 minutes of signup. Let them configure settings after they've experienced the AI feedback.

2. **Template-First Onboarding**: Surface templates as the default way to create first assignment, not as a power-user feature buried in menus.

3. **"Quick Start" Mode**: Offer a "skip setup, use defaults" option for teachers who just want to try the product before committing to configuration.

4. **Progressive Disclosure**: Instead of showing all settings upfront, reveal complexity as teachers use the product more.

---

## Recommendations

### Immediate (This Quarter)
- [ ] Redesign first-run experience to achieve "first grade in 30 minutes" target
- [ ] Move templates to primary navigation, add "Start with a template" CTA to dashboard
- [ ] Add "Quick Start" bypass option that uses sensible defaults

### Explore Further
- [ ] A/B test guided vs self-serve onboarding paths
- [ ] Interview churned users to validate setup as primary cause

### Parking Lot
- Onboarding video content (mentioned by 2 users as nice-to-have)
- Peer mentorship program for new teachers

---

## Next Steps

1. Share with product team for Monday discussion - Alex
2. Create design brief for streamlined onboarding - Alex, by Jan 22
3. Schedule follow-up interviews with churned users - Alex, next sprint

---

## Appendix

### Interview Guide
1. Walk me through how you first heard about GradeFlow
2. Describe your first day using the product
3. What was the hardest part of getting started?
4. When did you first feel like "this is useful"?
5. What almost made you give up?
6. How does GradeFlow fit into your current workflow?

### Raw Themes
- time-pressure, setup-overwhelm, template-discovery, ai-feedback-aha, decision-paralysis, workflow-fit, trust-in-ai, grade-anxiety, student-roster-import, rubric-confusion, mobile-needs, colleague-recommendations
