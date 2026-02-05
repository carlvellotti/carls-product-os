# Customer Escalation: Acme University

**Date:** January 15, 2026
**Attendees:** Alex Chen (PM), Rachel Torres (CS Lead), Mike Patterson (Account Exec), Prof. Williams (Acme, customer)
**Context:** Acme University (enterprise customer, $85k ARR) escalated an issue with grading sync. Prof. Williams threatened to cancel if not resolved.

---

## Background

Acme has been a customer for 2 years. Prof. Williams runs the largest course on platform (800 students, Intro to Economics). Last week, grades failed to sync to their Canvas LMS for ~200 students.

This caused:
- Manual rework for TAs (4 hours)
- Student complaints to Prof. Williams
- Prof. Williams emailed CEO directly (not great)

Rachel looped me in Monday. Mike joined because of renewal risk.

---

## Meeting Notes

**Prof. Williams' concerns:**
- This is the second sync issue in 3 months
- His TAs don't trust the system anymore
- He's evaluating Gradescope as an alternative
- "I love the product but I can't keep dealing with this"

**Root cause (we explained):**
The sync failed due to a Canvas API timeout during peak usage. Our retry logic didn't handle this case well. James identified the bug and we shipped a fix Tuesday.

**What we committed to:**
1. **Immediate:** Manual grade push for the 200 affected students (done before this meeting)
2. **Short-term:** Add monitoring alerts for sync failures (shipping this week)
3. **Medium-term:** Improve retry logic + add manual "re-sync" button for TAs (on roadmap for Feb)
4. **Communication:** Weekly status updates to Prof. Williams until he's confident

**Prof. Williams' response:**
Appreciated the quick fix and transparency. Said he'd give us until end of Q1 to prove reliability. Still concerned but not actively looking at competitors. "Just don't make me look bad to my students."

---

## Action Items

- [x] Manual grade push (James - done)
- [ ] Sync failure alerts - shipping Jan 17 (Kevin)
- [ ] Manual re-sync button - add to Feb sprint (Alex)
- [ ] Weekly updates to Prof. Williams (Rachel, cc Alex)
- [ ] Post-mortem doc for internal review (Alex)
- [ ] Brief David on the situation (Alex - today)

---

## Follow-up Notes

**Jan 17:** Alerts shipped. Rachel sent first weekly update. Prof. Williams replied "thank you, appreciated."

**Jan 22:** No sync issues this week. Rachel's update was well-received. Mike says renewal risk is lower but we need a clean February.

---

## Learnings

1. Should have had sync failure alerts from the start - adding to tech debt list
2. Need better escalation path so issues don't go to CEO
3. Enterprise customers need faster response SLA - discuss with David
4. The manual re-sync button idea is good - should prioritize this for all enterprise customers
