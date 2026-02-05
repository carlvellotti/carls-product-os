# Marcus Wong - 1:1

**Role:** Engineering Lead, TA Experience Team
**Cadence:** Weekly, Mondays 3pm
**Preferred Style:** Efficient, technical. Appreciates when I've done my homework. Prefers async for small stuff.

## Context

Marcus leads the 5-person eng team that builds my features. Great partner - pushes back when needed but always constructive. Been at GradeFlow 18 months, came from Stripe.

We've built good trust. He'll tell me early if something's going off track. In return, I try to protect his team from scope creep and give him advance notice on priority shifts.

**His concerns right now:**
- Tech debt in grading service (wants to refactor, I'm trying to find room)
- Team capacity - lost one eng to AI team last month
- Sprint predictability

**What works well:**
- I write detailed specs, he appreciates it
- We do quick async check-ins on Slack
- Joint backlog grooming Thursdays

---

## 2026-01-27

**Notes:**

Sprint planning for the next two weeks. Committed to:
- Rubric versioning (5 pts)
- Grading history MVP (8 pts)
- Bug fixes from last release (3 pts)

Grading history is the risk. Data migration is gnarly. Marcus is putting two engs on it to derisk. He wants me to be available for quick decisions this week if they hit edge cases.

Re: tech debt - I told him I'm trying to carve out 20% of Q2 for refactoring. He seemed skeptical but appreciative. Will need David's buy-in.

**Blockers:**
- Design for grading history not final - Tom is working on it, said EOD Tuesday
- Need decision on whether to support deleted assignments in history (I'm leaning no for MVP)

**Action items:**
- Confirm deleted assignment decision with David (async)
- Ping Tom on design timing
- Be available for edge case questions

---

## 2026-01-20

**Notes:**

Retro on the rubric builder release. Overall went well but some learnings:

What worked:
- Feature flags let us control rollout
- QA caught the weird Safari bug before launch

What didn't:
- Last-minute design change caused 2 extra days
- I didn't communicate the change well to his team

Marcus was direct about the design change thing. Fair feedback. I apologized and said I'd push back harder on late changes or at least flag the impact immediately.

**Action items:**
- Add "design freeze" checkpoint to our process
- I'll write up the retro for the team

---

## 2026-01-13

**Notes:**

Capacity planning for Q1. We're down one eng (Jamie moved to AI team). Going to be tight.

Walked through my roadmap. Marcus thinks we can hit the March deadline for TA portal v2 but it's aggressive. Suggested we identify one feature to cut if needed. I'm thinking the advanced filtering can slip to fast-follow.

Discussed AI integration dependency. He wants Sarah's team to provide a clear API contract by mid-Feb or we'll have to plan around it.

**Action items:**
- Identify cut candidate for portal v2
- Get API contract timeline from Sarah's eng lead
- Update roadmap with realistic dates

---

## Standing topics

- Sprint health / velocity
- Blockers and dependencies
- Team capacity
- Upcoming priorities
