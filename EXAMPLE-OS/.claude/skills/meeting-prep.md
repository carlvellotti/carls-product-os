# Meeting Prep

Prepare context and talking points for an upcoming meeting.

## Trigger

User says: "prep for meeting with {{person}}", "meeting prep", "prepare for {{meeting_name}}"

## Instructions

1. **Identify the Meeting**
   - Get meeting name/attendees from user or calendar MCP
   - Determine meeting type: 1:1, stakeholder review, design review, customer call, etc.

2. **Gather Context by Meeting Type**

   **For 1:1s:**
   - Read previous 1:1 notes with this person
   - Check for outstanding action items (yours and theirs)
   - Look for recent work that affects them
   - Review any feedback you've been meaning to share

   **For Stakeholder Reviews:**
   - Pull latest project status (PRD, weekly updates)
   - Gather current metrics
   - Identify decisions needed
   - Prepare for likely questions

   **For Design Reviews:**
   - Read relevant PRD sections
   - Review user research findings
   - Note open design questions
   - Prep technical constraints to raise

   **For Customer Calls:**
   - Check customer history/context if available
   - Review relevant feature requests or support tickets
   - Prepare research questions
   - Note what NOT to promise

3. **Generate Prep Doc**

   Output format:

   ```
   ## Meeting Prep: {{meeting_name}}
   **Date/Time:** {{datetime}}
   **Attendees:** {{list}}
   **Type:** {{meeting_type}}

   ### Context
   {{Brief background on what this meeting is about}}

   ### My Goals for This Meeting
   1.
   2.

   ### Key Points to Cover
   - {{topic}}: {{what to say}}

   ### Questions to Ask
   1.
   2.

   ### Decisions Needed
   - {{decision}}: My recommendation is {{X}} because {{Y}}

   ### Potential Questions I'll Get (and Answers)
   - Q: {{likely question}}
     A: {{prepared answer}}

   ### Action Items to Follow Up On
   - [ ] {{from last meeting}}

   ### Don't Forget
   - {{important thing to remember}}
   ```

4. **Use Tools if Available**
   - Calendar MCP: Get meeting details, attendees
   - Granola MCP: Check for past meeting transcripts with this person
   - Search files for any mentions of attendee names

## Example

**User:** "prep for my 1:1 with Sarah"

**Claude:**
1. Finds recent `1on1-notes-sarah-*.md` files
2. Extracts open action items
3. Checks for any project updates that affect Sarah's team
4. Notes that Sarah asked about API timeline last time
5. Outputs prep doc with context and suggested talking points

## Notes

- For recurring meetings, establish patterns (what does Sarah always ask about?)
- Flag if no previous notes exist - suggest what to learn in this meeting
- Keep prep concise - it's a reference, not a script
