# Technical Spec Review Notes

## Meeting Info

| Field | Value |
|-------|-------|
| Date | January 27, 2025 |
| Attendees | Alex Chen (PM), Marcus Kim (Eng Lead), Priya Patel (Design), Wei Zhang (Backend), Lisa Torres (Data) |
| Duration | 60 minutes |
| Doc Reviewed | [Eng Spec v0.3](https://docs.google.com/document/d/xxx) |

---

## Summary

Reviewed the engineering spec for TA Workload Tracker. Overall alignment on approach. Key decisions made on data architecture and performance targets. A few open questions escalated to architecture review.

---

## Architecture Overview (from Eng)

### Proposed Approach

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  Grading Events │────▶│  Analytics DB   │────▶│  Dashboard API  │
│   (existing)    │     │   (new table)   │     │   (new service) │
└─────────────────┘     └─────────────────┘     └─────────────────┘
                                                         │
                                                         ▼
                                                ┌─────────────────┐
                                                │   Frontend UI   │
                                                │  (React comp)   │
                                                └─────────────────┘
```

**Key decisions:**
1. New `ta_workload_metrics` table, not modifying existing schema
2. Hourly aggregation job (not real-time streaming)
3. Separate API endpoint, not extending grading API
4. React component embedded in existing course dashboard

### Why This Approach

Marcus explained the tradeoffs:

**Option A: Real-time streaming**
- Pros: Immediate data
- Cons: Complex infrastructure, expensive at scale

**Option B: Hourly batch (CHOSEN)**
- Pros: Simple, cost-effective, uses existing pipeline
- Cons: Data is up to 1 hour stale

**Decision:** Hourly is fine. Professors don't need second-by-second accuracy. Revisit if user feedback indicates otherwise.

---

## Data Schema Discussion

### Proposed Metrics Table

```sql
CREATE TABLE ta_workload_metrics (
    id BIGSERIAL PRIMARY KEY,
    course_id BIGINT NOT NULL,
    ta_user_id BIGINT NOT NULL,
    time_period DATE NOT NULL,
    submissions_graded INT DEFAULT 0,
    avg_grading_time_seconds INT,
    assignment_ids JSONB,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW(),
    UNIQUE(course_id, ta_user_id, time_period)
);
```

### My Questions & Eng Responses

**Q1: Why daily granularity?**
A: Aggregating to daily reduces storage significantly. Can roll up to weekly/monthly in queries. Going more granular (hourly) 10x's storage with minimal user benefit.

**Decision:** Daily is fine. Approved.

**Q2: What about assignment type data?**
A: Not in v1 schema. Adding `assignment_type` column would require joining to assignments table on every aggregation. Significant complexity.

**Decision:** Defer to v1.1. Document as known limitation.

**Q3: Data retention?**
A: Proposing 2 years. After that, roll up to monthly aggregates only.

**Decision:** Approved. Aligns with PRD.

**Q4: Can we track time-to-grade per submission?**
A: Yes, we already have timestamps. `avg_grading_time_seconds` captures this at daily level.

**Decision:** Include in v1. Good for future "efficiency" metrics.

---

## Performance Discussion

### Targets

| Metric | Target | Notes |
|--------|--------|-------|
| Dashboard load time | < 2s (p95) | Current course dashboard is 1.2s |
| Data freshness | < 1 hour | Hourly aggregation job |
| Supported TAs per course | Up to 20 | Covers 99% of courses |
| Supported time range | 2 years | Storage constraint |

### Load Testing Plan

Wei proposed:
1. Test with synthetic data for course with 20 TAs, 2 years of history
2. Target: query returns in < 200ms
3. Add caching layer if needed (Redis)

**My question:** What's the largest course we have today?
**Answer:** 18 TAs (Georgia Tech intro CS course). So 20 is reasonable ceiling.

---

## Frontend Discussion

### Integration Point

Priya confirmed design calls for new tab in course settings:
- Course Settings > "TA Workload" tab (new)
- Only visible to course instructors and admins
- Permission check on API side

### Chart Library

Lisa (data) recommended Chart.js over D3 for simplicity. Marcus agreed.

**Decision:** Use Chart.js. We already use it elsewhere. Consistency > perfection.

### Mobile Responsiveness

Priya asked about mobile. Current course dashboard is not mobile-optimized.

**Decision:** Match current behavior (desktop-first). Add mobile to v1.1 backlog.

---

## Open Questions (Escalated)

### 1. Multi-tenant Data Isolation

**Question:** Our analytics DB serves multiple customers. How do we ensure data isolation?

**Current state:** Row-level security on `organization_id`.

**Concern:** New table adds another surface. Need architecture review.

**Action:** Marcus to schedule 30-min review with Security team. Target: Feb 3.

### 2. GDPR Implications

**Question:** Are TA workload metrics considered personal data under GDPR?

**My take:** Probably yes - it's performance data about identifiable individuals.

**Action:** Alex to consult with Legal. Need answer before beta launch.

### 3. Export Service Capacity

**Question:** Export service currently handles ~100 exports/day. Dashboard could 10x this.

**Action:** Wei to run capacity analysis. Report back Feb 5.

---

## Timeline Impact

Original timeline:
- Design: Jan 27 - Feb 7
- Build: Feb 10 - Mar 7

Eng assessment: **Timeline is achievable** assuming:
1. No major changes from architecture review
2. GDPR question doesn't require data model changes
3. Design is finalized by Feb 7

**Risk:** If architecture review requires changes to data isolation approach, could add 1 week.

---

## Action Items

| Owner | Action | Due |
|-------|--------|-----|
| Marcus | Schedule architecture review with Security | Jan 28 |
| Alex | Consult Legal on GDPR | Jan 30 |
| Wei | Export service capacity analysis | Feb 5 |
| Priya | Finalize designs, share with eng | Feb 7 |
| Alex | Update PRD with schema decisions | Jan 29 |
| Lisa | Create test dataset (20 TAs, 2 years) | Feb 7 |

---

## My Takeaways

1. **Eng is aligned** - No pushback on feasibility. Good sign.
2. **Hourly refresh is fine** - Was worried about this, but professor use case doesn't need real-time.
3. **Assignment-type weighting is hard** - Need to manage expectations on v1 limitations.
4. **GDPR is a real risk** - Should have thought of this earlier. Flagging for board deck.
5. **Team is excited** - Marcus said "this is the most useful feature we've built in a while."

---

## Next Steps

1. Complete action items above
2. Reconvene after architecture review (Feb 3)
3. Kick off build on Feb 10 assuming no blockers

---

*Notes by: Alex Chen*
*Last updated: January 27, 2025*
