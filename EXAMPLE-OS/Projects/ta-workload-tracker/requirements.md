# TA Workload Tracker - Product Requirements Document

## Document Info

| Field | Value |
|-------|-------|
| Author | Alex Chen |
| Status | In Review |
| Version | 1.2 |
| Last Updated | Jan 28, 2025 |
| Reviewers | Marcus Kim (Eng), Priya Patel (Design), Jordan Wright (CS) |

---

## 1. Problem Statement

### 1.1 Background

GradeFlow serves 340+ universities with our AI-assisted grading platform. A significant portion of our users are professors who manage teams of Teaching Assistants (TAs). Currently, professors have no systematic way to understand how grading work is distributed among their TAs.

### 1.2 Current State Pain Points

Based on 12 user interviews conducted in January 2025:

1. **Visibility Gap** - "I have no idea who's doing what until the end of the semester when I look at the gradebook" - Prof. Martinez, UC Davis

2. **Inequitable Distribution** - TAs report significant variance in workload. In our sample, the busiest TA graded 3.2x more submissions than the least busy TA in the same course.

3. **Burnout Risk** - 4 of 7 TAs interviewed mentioned feeling "overwhelmed" at least once per semester. Two were considering not returning.

4. **Planning Difficulty** - Professors struggle to determine how many TA hours they need for upcoming semesters without historical data.

### 1.3 Business Impact

- **Retention:** 23% of churned accounts in Q4 cited "TA management challenges" as a factor
- **Expansion:** Enterprise deals often stall on "department-level reporting" requirements
- **Support:** ~180 tickets/month related to TA workload questions (est. $14K support cost)

---

## 2. Solution Overview

### 2.1 Product Vision

Give professors instant, actionable visibility into TA workload so they can ensure equitable distribution, prevent burnout, and make data-driven staffing decisions.

### 2.2 Core Value Propositions

1. **See at a glance** - Dashboard shows real-time workload distribution
2. **Spot problems early** - Alerts notify when imbalance exceeds threshold
3. **Act with confidence** - Historical data supports staffing decisions

### 2.3 Key Features (v1)

| Feature | Priority | Status |
|---------|----------|--------|
| Workload Distribution View | P0 | Design in progress |
| Time Period Selector | P0 | Design in progress |
| TA Detail Drill-down | P0 | Design in progress |
| Imbalance Alerts | P1 | Spec complete |
| Export to CSV/PDF | P1 | Not started |
| Email Digest (weekly) | P2 | Backlog |

---

## 3. User Stories

### 3.1 Primary Persona: Professor Patricia

> Patricia is a CS professor teaching a 200-student intro course with 4 TAs. She wants to be a good manager but is stretched thin with research and committee work.

**Stories:**

| ID | Story | Acceptance Criteria |
|----|-------|---------------------|
| US-1 | As Patricia, I want to see how many submissions each TA has graded this week so I can spot if anyone is falling behind | Dashboard shows bar chart of grading volume per TA for selected time period |
| US-2 | As Patricia, I want to see average grading time per TA so I can identify who might need support | Metrics panel shows avg time-to-grade per TA |
| US-3 | As Patricia, I want to be alerted if one TA is doing 2x+ the work of another so I can rebalance | Alert appears when variance exceeds configurable threshold (default 2x) |
| US-4 | As Patricia, I want to see trends over the semester so I can plan for next term | Line chart shows weekly volumes for past 16 weeks |
| US-5 | As Patricia, I want to export data for my department chair so I can justify TA budget requests | Export button generates CSV with all metrics |

### 3.2 Secondary Persona: Department Chair Doug

> Doug oversees 15 courses with 40+ TAs. He needs aggregate visibility for budgeting and resource allocation.

**Stories:**

| ID | Story | Acceptance Criteria |
|----|-------|---------------------|
| US-6 | As Doug, I want to see workload across all courses I oversee so I can reallocate TAs if needed | Department view shows aggregated data (v1.1 - not in initial scope) |
| US-7 | As Doug, I want to export reports for budget meetings so I can demonstrate utilization | Export includes department-level rollup |

*Note: US-6 and US-7 are stretch goals for v1.1 based on enterprise customer feedback.*

---

## 4. Detailed Requirements

### 4.1 Dashboard Layout

```
+------------------------------------------+
|  TA Workload Dashboard     [Time Period] |
+------------------------------------------+
|                                          |
|  +----------------+  +----------------+  |
|  | Total Graded   |  | Avg per TA     |  |
|  | 847            |  | 212            |  |
|  +----------------+  +----------------+  |
|                                          |
|  +------------------------------------+  |
|  |     Grading Volume by TA           |  |
|  |     [Bar Chart]                    |  |
|  |     Sarah: 287 ||||||||||||        |  |
|  |     Marcus: 243 ||||||||||         |  |
|  |     Jin: 198 ||||||||              |  |
|  |     Taylor: 119 |||||   [!]        |  |
|  +------------------------------------+  |
|                                          |
|  +------------------------------------+  |
|  |     Weekly Trend                   |  |
|  |     [Line Chart - 8 weeks]         |  |
|  +------------------------------------+  |
|                                          |
+------------------------------------------+
```

### 4.2 Data Requirements

**Metrics to display:**

| Metric | Calculation | Update Frequency |
|--------|-------------|------------------|
| Total Submissions Graded | Count of graded submissions in period | Real-time |
| Submissions per TA | Count grouped by grader | Real-time |
| Avg Time to Grade | Mean(submit_time - grade_time) | Hourly |
| Workload Variance | Max(TA volume) / Min(TA volume) | Real-time |
| Trend Data | Weekly aggregates | Daily refresh |

**Data retention:** 2 years of historical data

### 4.3 Alert Logic

**Trigger conditions:**
- Workload variance exceeds threshold (default: 2x, configurable 1.5x - 3x)
- Any TA grades 0 submissions in 7+ days while others are active
- Weekly volume for any TA exceeds 150% of their historical average

**Alert delivery:**
- In-app notification (always)
- Email notification (opt-in, default on)

### 4.4 Permissions

| Role | Can View | Can Configure | Can Export |
|------|----------|---------------|------------|
| Professor (course owner) | Own courses | Yes | Yes |
| Co-instructor | Shared courses | No | Yes |
| Department Admin | All dept courses | Dept-wide | Yes |
| TA | None (v1) | No | No |

---

## 5. Success Metrics

### 5.1 Primary Metrics

| Metric | Current | Target | Timeline |
|--------|---------|--------|----------|
| Dashboard WAU (professors w/ 3+ TAs) | N/A | 60% | 30 days post-launch |
| TA Management NPS | 32 | 45 | 60 days post-launch |
| Support tickets (TA workload) | 180/mo | 108/mo | 90 days post-launch |

### 5.2 Leading Indicators

- Dashboard page loads per user per week
- Time spent on dashboard
- Export feature usage
- Alert click-through rate

### 5.3 Guardrail Metrics

- Overall platform NPS (should not decrease)
- TA satisfaction (survey planned for v1.1)

---

## 6. Technical Considerations

### 6.1 Dependencies

- Grading events pipeline (exists)
- User role system (exists, may need extension for dept admin)
- Notification service (exists)
- Export service (needs capacity check)

### 6.2 Performance Requirements

- Dashboard load time < 2s (p95)
- Data freshness < 5 minutes for real-time metrics
- Support courses with up to 20 TAs

### 6.3 Open Questions for Eng

1. Can we reuse the analytics dashboard infrastructure or need new?
2. What's the incremental data storage cost for 2-year retention?
3. Do we need a new microservice or extend existing grading service?

*See [[technical-spec-review]] for notes from spec review meeting.*

---

## 7. Go-to-Market

### 7.1 Launch Plan

- **Beta:** 15 professors from design partner list (Mar 10)
- **GA:** All professors with 2+ TAs (Mar 24)
- **Enterprise:** Department-level features in v1.1 (Apr)

### 7.2 Enablement

- CS team training: Mar 17
- Help center articles: Mar 20
- In-app onboarding tooltip: Mar 24

### 7.3 Pricing

No change to existing pricing. Feature available on Pro and Enterprise tiers.

---

## 8. Risks & Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Professors don't adopt | Medium | High | Strong onboarding, in-app prompts, email campaign |
| Performance issues at scale | Low | High | Load testing, progressive rollout |
| TAs feel surveilled | Medium | Medium | v1.1 includes TA self-service view; comms emphasize equity not surveillance |
| Scope creep delays launch | Medium | Medium | Strict P0/P1 prioritization, weekly scope review |

---

## 9. Appendix

### 9.1 Research References

- [[ta-workload-tracker/research/interview-sarah-ta|Interview: Sarah (TA)]]
- [[ta-workload-tracker/research/interview-marcus-ta|Interview: Marcus (TA)]]
- [[ta-workload-tracker/research/interview-prof-martinez|Interview: Prof. Martinez]]
- [[ta-workload-tracker/user-research-synthesis|Research Synthesis]]
- [[ta-workload-tracker/competitive-analysis|Competitive Analysis]]

### 9.2 Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | Jan 15 | Alex Chen | Initial draft |
| 1.1 | Jan 22 | Alex Chen | Added user stories from research |
| 1.2 | Jan 28 | Alex Chen | Updated metrics after stakeholder review |

---

*Questions? Reach out to Alex Chen (@alexc) in #product-ta-excellence*
