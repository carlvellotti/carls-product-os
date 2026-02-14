---
name: standup
description: Morning briefing from tasks, calendar, Linear, and goals
user-invocable: true
---

# Daily Standup Generator

Generate a daily standup summary based on recent work activity.

## Instructions

1. **Gather Recent Activity**
   - Read files modified in the last 24-48 hours using `git status` and `git log --since="yesterday"`
   - Look for recently edited PRDs, meeting notes, research docs
   - Check `_temp/` for quick notes or screenshots that might indicate work done

2. **Check Tasks**
   - Read `Tasks/active.md` for current sprint items, blockers, and deadlines
   - Read `GOALS.md` for quarterly targets and key metrics

3. **Check Calendar (if available)**
   - If Google Calendar MCP is connected, fetch today's events
   - Cross-reference attendees with `Knowledge/People/` files
   - If no calendar MCP: skip schedule, note "Calendar not connected"

4. **Check Linear (if available)**
   - If Linear MCP is connected, fetch issues In Progress, recently Done, and blocked
   - If no Linear MCP: fall back to `Tasks/active.md`

5. **Synthesize & Output**
   - Connect meetings to tickets to blockers
   - Output: Today's Schedule → In Progress → Completed → Blockers → Suggested Focus

## Output Format

```
## Standup — {{today's date}}

### Today's Schedule
- {{time}} — {{meeting}} ({{context from People/ files}})

### In Progress
- {{ticket/task}}: {{status and next step}}

### Recently Completed
- {{completed items}}

### Blockers & Risks
- {{blocker}}: {{impact and proposed resolution}}

### Suggested Focus
{{1-2 sentences on what matters most today and why}}
```

## Notes

- Keep items concise - this is a summary, not a log
- Prioritize items by impact, not just recency
- Flag anything overdue or stalled
