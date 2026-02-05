# Tags

Tag taxonomy for organizing files in this PM workspace.

---

## Project Tags

Used in project files to categorize work.

### By Product Area
| Tag | Description |
|-----|-------------|
| `#gradebook` | Gradebook and grading features |
| `#reports` | Reporting and analytics features |
| `#parent-portal` | Parent-facing features |
| `#admin` | School admin features |
| `#integrations` | Third-party integrations |
| `#platform` | Platform/infrastructure work |

### By Type
| Tag | Description |
|-----|-------------|
| `#feature` | New feature development |
| `#enhancement` | Improvement to existing feature |
| `#bug` | Bug fix |
| `#tech-debt` | Technical debt reduction |
| `#research` | Research initiative |
| `#experiment` | A/B test or experiment |

---

## Status Tags

Track project and document status.

### Project Status
| Tag | Description |
|-----|-------------|
| `#status/proposed` | Idea stage, not yet approved |
| `#status/planning` | Approved, in planning |
| `#status/in-progress` | Actively being worked on |
| `#status/blocked` | Blocked on dependency |
| `#status/shipped` | Launched to production |
| `#status/on-hold` | Paused, may resume |
| `#status/canceled` | Will not proceed |

### Document Status
| Tag | Description |
|-----|-------------|
| `#draft` | Work in progress |
| `#review` | Ready for review |
| `#approved` | Approved/finalized |
| `#archived` | No longer current |

---

## Priority Tags

| Tag | Description |
|-----|-------------|
| `#p0` | Critical - must do |
| `#p1` | High priority - should do |
| `#p2` | Medium priority - nice to have |
| `#p3` | Low priority - backlog |

---

## People Tags

| Tag | Description |
|-----|-------------|
| `#team/product` | Product team |
| `#team/engineering` | Engineering team |
| `#team/design` | Design team |
| `#team/leadership` | Leadership/execs |
| `#stakeholder/marcus` | Marcus (manager) |
| `#stakeholder/sarah` | Sarah (eng lead) |
| `#stakeholder/jennifer` | Jennifer (design lead) |

---

## Time Tags

| Tag | Description |
|-----|-------------|
| `#q1-2025` | Q1 2025 work |
| `#q2-2025` | Q2 2025 work |
| `#h1-2025` | First half 2025 |
| `#2025` | 2025 fiscal year |

---

## Research Tags

| Tag | Description |
|-----|-------------|
| `#research/interview` | User interview |
| `#research/survey` | Survey research |
| `#research/usability` | Usability testing |
| `#research/competitive` | Competitive analysis |
| `#research/data` | Data analysis |

---

## Usage Examples

**PRD frontmatter:**
```yaml
tags:
  - gradebook
  - feature
  - status/planning
  - p0
  - q1-2025
```

**Research file:**
```yaml
tags:
  - research/interview
  - gradebook
  - status/approved
```

**Meeting notes:**
```yaml
tags:
  - stakeholder/sarah
  - team/engineering
```
