# GradeFlow Product Overview

## What We Build

GradeFlow is a course operations platform that handles everything between "syllabus created" and "final grades submitted." We're not an LMS - we integrate with Canvas, Blackboard, and Moodle.

## Product Pillars

### 1. Grading Workflow
The core product. Streamlines assignment submission, grading, and feedback delivery.

**Key features:**
- Rubric builder with reusable components
- AI-assisted grading suggestions (launched Q3 2025)
- Batch grading interface
- Inline annotation tools
- Plagiarism flagging (Turnitin integration)
- Grade calibration tools for multi-grader consistency

**Metrics:**
- Avg grading time reduced by 47%
- 89% of AI suggestions accepted without modification
- NPS: 62

### 2. TA Coordination
Helps professors manage teaching assistant teams.

**Key features:**
- TA assignment distribution (auto and manual)
- Workload dashboard
- Office hours scheduling
- TA performance analytics
- Training module assignments

**Metrics:**
- 3.2 hours/week saved per professor on TA coordination
- 94% of TAs report clearer expectations
- NPS: 58

### 3. Course Analytics
Gives professors visibility into course health.

**Key features:**
- Grade distribution dashboards
- At-risk student identification
- Engagement metrics
- Grading consistency reports
- Time-to-feedback tracking

**Metrics:**
- 78% of professors check analytics weekly
- At-risk alerts have 71% accuracy
- NPS: 45 (area for improvement)

## Architecture Overview

```
┌─────────────────────────────────────────────────────────┐
│                    GradeFlow Platform                    │
├─────────────────────────────────────────────────────────┤
│  Web App (React)  │  Mobile (React Native)  │  API      │
├─────────────────────────────────────────────────────────┤
│              Core Services (Node.js/TypeScript)          │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐   │
│  │ Grading  │ │    TA    │ │Analytics │ │   Auth   │   │
│  │ Service  │ │ Service  │ │ Service  │ │ Service  │   │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘   │
├─────────────────────────────────────────────────────────┤
│              AI Layer (Python/FastAPI)                   │
│  ┌──────────────────┐ ┌──────────────────────────┐      │
│  │ Grading AI       │ │ Risk Prediction Model    │      │
│  │ (GPT-4 + fine-   │ │ (Internal ML)            │      │
│  │  tuned models)   │ │                          │      │
│  └──────────────────┘ └──────────────────────────┘      │
├─────────────────────────────────────────────────────────┤
│  PostgreSQL  │  Redis  │  S3 (assignments)  │  Pinecone │
└─────────────────────────────────────────────────────────┘
           │                    │
           ▼                    ▼
    ┌─────────────┐     ┌─────────────────┐
    │ Canvas API  │     │ Blackboard API  │
    └─────────────┘     └─────────────────┘
```

## User Types

| Role | Count | Primary Jobs-to-be-Done |
|------|-------|------------------------|
| Professor | 8,200 MAU | Set up courses, configure grading, review analytics |
| TA | 24,500 MAU | Grade assignments, hold office hours, respond to students |
| Department Admin | 450 MAU | Manage licenses, view aggregate analytics |
| Student | 185,000 MAU | Submit assignments, view feedback (lightweight) |

## Pricing Model

**Per-seat pricing based on department size:**
- Small (<50 courses): $15/course/semester
- Medium (50-200): $12/course/semester
- Large (200+): $10/course/semester + enterprise features

**AI grading add-on:** +$3/course/semester

## Key Integrations

| Integration | Status | Usage |
|------------|--------|-------|
| Canvas | Production | 78% of customers |
| Blackboard | Production | 15% of customers |
| Moodle | Beta | 5% of customers |
| Turnitin | Production | 62% of courses |
| Google Calendar | Production | Office hours sync |
| Slack | Beta | TA notifications |

## Technical Debt & Known Issues

1. **Grading service performance** - Batch operations slow above 500 submissions
2. **Mobile app feature parity** - Only 40% of web features available
3. **Analytics data freshness** - 6-hour lag on some dashboards
4. **LTI 1.3 migration** - Still supporting deprecated LTI 1.1

## Product Team Ownership

| Area | PM | Engineering Team |
|------|-----|-----------------|
| Grading Workflow | Alex Chen (me) | Platform Team (Marcus) |
| TA Coordination | Alex Chen (me) | Platform Team (Marcus) |
| Analytics | Sarah Kim | Data Team (Emily) |
| Integrations | Sarah Kim | Integrations Team (Carlos) |
| Mobile | Shared | Mobile contractors |

## Roadmap Themes (2026)

1. **AI-native grading** - Move from AI-assisted to AI-first for appropriate use cases
2. **Department-level features** - Help department heads manage across courses
3. **Student experience** - Currently minimal; opportunity to differentiate
4. **Real-time collaboration** - Co-grading, live rubric editing
