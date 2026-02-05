# Daily Standup Generator

Generate a daily standup summary based on recent work activity.

## Trigger

User says: "standup", "daily standup", "what did I work on"

## Instructions

1. **Gather Recent Activity**
   - Read files modified in the last 24-48 hours using `git status` and `git log --since="yesterday"`
   - Look for recently edited PRDs, meeting notes, research docs
   - Check `_temp/` for quick notes or screenshots that might indicate work done

2. **Identify Key Work**
   - Group changes by project/initiative
   - Note any completed items (closed tasks, finished docs)
   - Identify work in progress

3. **Generate Standup Format**

   Output in this format:

   ```
   ## Standup - {{today's date}}

   ### Yesterday
   - {{completed work item}}
   - {{progress on item}}

   ### Today
   - {{planned work based on open items, upcoming meetings}}

   ### Blockers
   - {{any blockers identified from notes or stalled work}}
   ```

4. **Context Sources**
   - Recent 1:1 notes for action items due
   - PRDs in progress for status
   - Weekly update drafts for priorities
   - Calendar (if MCP available) for meetings that generated work

## Example Output

```
## Standup - January 15, 2025

### Yesterday
- Completed user interview synthesis for Gradebook Redesign (5 interviews)
- Updated PRD success metrics based on Sarah's feedback
- 1:1 with Marcus - discussed Q1 roadmap priorities

### Today
- Finish PRD draft for stakeholder review
- Prep for Thursday's design review
- Follow up on API timeline with Platform team

### Blockers
- Waiting on Platform team for API feasibility answer (asked Monday)
```

## Notes

- Keep items concise - this is a summary, not a log
- Prioritize items by impact, not just recency
- Flag anything overdue or stalled
