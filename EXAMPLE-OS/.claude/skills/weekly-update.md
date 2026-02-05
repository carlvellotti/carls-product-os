# Weekly Update Drafter

Draft a stakeholder update email using the weekly-update template.

## Trigger

User says: "weekly update", "draft stakeholder update", "write my weekly update for {{project}}"

## Instructions

1. **Identify the Project**
   - Ask which project if not specified
   - Find the project folder and related files

2. **Gather Information**
   - Read the project's PRD for context and milestones
   - Check recent meeting notes related to the project
   - Look at git history for changes this week
   - Review any metrics files or data
   - Check previous weekly updates for continuity

3. **Assess Status**
   - Compare progress against milestones in PRD
   - Identify any slippage or blockers
   - Determine overall status: On Track | At Risk | Blocked

4. **Draft Using Template**
   - Use `Templates/weekly-update.md` as the structure
   - Fill in all sections with gathered information
   - Keep TL;DR to 2-3 bullets max
   - Be specific about blockers and asks

5. **Review Checklist**
   Before presenting draft, verify:
   - [ ] Status accurately reflects reality
   - [ ] Metrics are current (not stale)
   - [ ] Blockers have clear asks attached
   - [ ] Next week priorities are realistic
   - [ ] No surprises - anything major was flagged earlier

## Key Principles

- **Lead with the headline** - What's the ONE thing they need to know?
- **Be honest about status** - At Risk is better than surprising people later
- **Make asks specific** - "Need decision on X by Friday" not "need support"
- **Keep it scannable** - Executives skim, make key info pop

## Example Interaction

**User:** "weekly update for gradebook redesign"

**Claude:**
1. Reads PRD at `Projects/Gradebook-Redesign/prd.md`
2. Finds recent meeting notes in `Projects/Gradebook-Redesign/`
3. Checks metrics if available
4. Drafts update using template

**Output:** Complete draft ready for review and send

## Notes

- Save drafts to `Projects/{{project}}/updates/` folder
- Reference previous updates to maintain consistency
- Flag if any section lacks information - better to note "TBD" than guess
