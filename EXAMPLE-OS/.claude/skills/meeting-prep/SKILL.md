---
name: meeting-prep
description: Context-loaded prep for any meeting
argument-hint: "[person-name]"
user-invocable: true
---

# Meeting Prep

Prepare context and talking points for an upcoming meeting.

## Instructions

1. **Find the Person's Profile**
   - Look in `Knowledge/People/` for their file — load communication preferences
   - Note their preferred format, what they care about, how to work with them

2. **Gather Past Meeting History**
   - Find past meeting notes in `Meetings/1on1s/` or `Meetings/` — extract open action items
   - Look for recent decisions, escalations, or commitments involving them

3. **Pull Current Context**
   - Check `Tasks/active.md` for anything relevant to discuss
   - Check `GOALS.md` for metrics they care about
   - Search `Meetings/` for recent decisions or commitments

4. **Generate Prep Doc**
   - Output talking points in their preferred format (e.g., BLUF for David)
   - Include open items, relevant metrics, prep questions

## Output Format

```
## Meeting Prep: {{person/meeting}}
**Date/Time:** {{datetime}}
**Type:** {{meeting_type}}

### Context
{{Brief background}}

### Key Points to Cover
- {{topic}}: {{what to say}}

### Open Action Items
- [ ] {{from last meeting}}

### Questions to Ask
1. {{question}}

### Decisions Needed
- {{decision}}: My recommendation is {{X}} because {{Y}}
```

## Notes

- Format output according to the person's communication preferences
- Flag if no previous notes exist - suggest what to learn in this meeting
- Keep prep concise - it's a reference, not a script
