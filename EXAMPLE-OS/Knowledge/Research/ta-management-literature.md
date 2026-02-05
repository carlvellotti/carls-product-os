# TA Management Literature Review

*Research synthesis for TA Coordination product features*
*Last updated: December 2025*

## Key Papers & Findings

### 1. "Teaching Assistant Effectiveness in Large Enrollment Courses"
*Johnson & Park, 2024, Journal of Higher Education*

**Study:** Surveyed 1,200 TAs and 340 professors across 45 universities

**Key findings:**
- TAs spend 34% of time on administrative tasks (scheduling, coordination)
- Only 41% of TAs receive formal training before starting
- Professor-TA communication happens primarily through email (68%), which TAs find inefficient
- TAs in courses with clear workload expectations report 2.3x higher satisfaction

**Implications for GradeFlow:**
- Workload visibility is high-value feature
- Training/onboarding module could be differentiator
- In-product communication could replace email

**Quote to use:** "The administrative burden on TAs has increased 40% over the past decade while preparation time has remained flat."

---

### 2. "Grading Consistency in Multi-Grader Environments"
*Chen et al., 2023, Educational Measurement Journal*

**Study:** Analyzed 50,000 grades across 200 courses with multiple graders

**Key findings:**
- Inter-rater reliability averages 0.67 (below acceptable 0.80 threshold)
- Calibration exercises improve reliability to 0.81 average
- Real-time feedback during grading ("you're grading harsher than peers") improves consistency 23%
- First 10 assignments graded have 31% more variance than subsequent assignments

**Implications for GradeFlow:**
- Calibration tools are validated by research
- Real-time "grading drift" alerts could be powerful
- "Warm-up" period matters - maybe shuffle assignment order

**Already shipped:** Calibration tool v1 (Q4 2025) - results align with this research

---

### 3. "The Hidden Curriculum of TA Work"
*Williams, 2024, PhD Dissertation, Stanford*

**Study:** Ethnographic study of 30 TAs over one academic year

**Key findings:**
- TAs learn most of their skills from other TAs, not professors
- "Shadow work" (unreported hours) averages 4.2 hours/week
- TAs often make grading decisions without consulting rubrics due to time pressure
- Peer support networks among TAs reduce burnout significantly

**Implications for GradeFlow:**
- Rubric accessibility during grading is critical
- Time tracking could expose/reduce shadow work
- Peer features (TA-to-TA) could be interesting
- Professor often doesn't know what TAs actually do

**Product opportunity:** "TA insights for professors" - help professors understand what's really happening

---

### 4. "Office Hours Attendance Patterns and Student Outcomes"
*Martinez & Liu, 2023, Learning Analytics Journal*

**Study:** Tracked 15,000 students' office hours attendance and correlated with grades

**Key findings:**
- Students who attend office hours 3+ times score 0.4 GPA points higher
- 67% of office hours time is spent on assignment clarification (not conceptual help)
- Scheduling friction is #1 barrier to attendance
- Virtual office hours have 2.1x attendance vs. in-person only

**Implications for GradeFlow:**
- Office hours scheduling is validated priority
- Assignment clarity could reduce office hours load
- Hybrid (virtual + in-person) scheduling needed
- Tracking attendance could predict at-risk students

**Feature idea:** Pre-office-hours triage - student describes issue, TA can prepare or redirect

---

### 5. "Workload Distribution in Teaching Teams"
*Garcia & Thompson, 2024, Higher Education Quarterly*

**Study:** Analyzed workload distribution across 150 courses with TA teams

**Key findings:**
- Workload distribution is typically uneven: top 20% of TAs do 45% of work
- Professors underestimate TA hours by average of 38%
- Explicit workload caps reduce burnout without reducing quality
- Assignment-based (vs. section-based) TA allocation is more efficient

**Implications for GradeFlow:**
- Workload dashboards should be visible to both professors AND TAs
- Auto-assignment should optimize for balance, not just completion
- Historical workload data helps planning
- Per-assignment allocation is right model

**Validates:** Our auto-assignment algorithm and workload dashboard (shipped Q4 2025)

---

### 6. "TA Training Programs: What Works?"
*O'Brien, 2023, Teaching in Higher Education*

**Study:** Meta-analysis of 45 TA training program evaluations

**Key findings:**
- Just-in-time training (during semester) outperforms front-loaded training
- Grading-specific training has highest ROI (improves consistency, reduces time)
- Video-based training preferred 2:1 over text-based
- Peer feedback on grading samples is most effective calibration method

**Implications for GradeFlow:**
- Training module should be ongoing, not onboarding-only
- Grading-focused training is the priority
- Video content investment could pay off
- Peer calibration features (TAs reviewing each other) valuable

**Feature idea:** "First week grading bootcamp" - guided grading with feedback

---

## Synthesis: TA Pain Points (Research-Backed)

| Pain Point | Frequency | Research Support | Our Solution |
|------------|-----------|------------------|--------------|
| Unclear expectations | High | Johnson & Park, Williams | Workload dashboard |
| Inconsistent grading guidance | High | Chen et al. | Calibration tools |
| Time tracking/shadow work | Medium | Williams | Future: time tracking |
| Poor communication with professor | Medium | Johnson & Park | In-product messaging |
| Workload imbalance | Medium | Garcia & Thompson | Auto-assignment |
| Inadequate training | Medium | O'Brien | Future: training module |
| Office hours scheduling friction | Low-Medium | Martinez & Liu | Office hours scheduling |

## Competitive Research Gap Analysis

**What competitors don't address (based on our research):**
1. TA-to-TA communication and peer learning
2. Professor visibility into actual TA workload
3. Just-in-time training during the semester
4. Grading drift alerts
5. Shadow work visibility

## Recommended Reading

For deeper dives on specific topics:
- TA effectiveness: Johnson & Park 2024 (most comprehensive)
- Grading consistency: Chen et al. 2023 (quantitative, defensible)
- Qualitative insights: Williams 2024 (rich stories for personas)
- Office hours: Martinez & Liu 2023 (analytics-focused)

## Research To Do

1. Interview TAs at our customer universities to validate literature findings
2. Analyze our own data on grading consistency pre/post calibration tool
3. Survey professors on TA visibility pain points
4. Competitive analysis of TA-specific features (Gradescope, Canvas, etc.)
