# Meeting Prep Tool

Gathers context for an upcoming meeting by searching relevant files and extracting action items.

## Quick Start

```bash
# Prep for meeting with a person
python run.py "Sarah Kim"

# Prep for a specific meeting type
python run.py "Gradebook Design Review" --type review

# Prep for customer call
python run.py "Riverside School District" --type customer
```

## What It Does

### For Person-Based Meetings (1:1s)
1. Finds previous meeting notes with that person
2. Extracts open action items from most recent meeting
3. Lists related documents mentioning them
4. Shows active projects for context
5. Generates suggested topics

### For Meeting Types
Provides type-specific checklists:

**Review meetings** (`--type review`)
- PRD/spec readiness
- Decision documentation
- Open questions

**Planning meetings** (`--type planning`)
- Retro completion
- Backlog prioritization
- Dependencies and capacity

**Customer calls** (`--type customer`)
- Customer context
- Research questions
- "Do not promise" reminders

## Output Example

```markdown
# Meeting Prep: Sarah Kim
**Generated:** 2025-01-15 09:30

## Previous Meetings
- [[1on1-sarah-2025-01-08.md]] - 2025-01-08
- [[1on1-sarah-2025-01-01.md]] - 2025-01-01

## Open Action Items (from last meeting)
- [ ] Follow up on API timeline with Platform team
- [ ] Share gradebook research findings

## Related Documents
- [[prd-gradebook-redesign.md]]
- [[research-summary-grading-workflow.md]]

## Active Projects (for context)
- Gradebook-Redesign
- Parent-Portal-V2

## Suggested Topics
- [ ] Follow up on action items above
- [ ] Share relevant project updates
- [ ]
```

## Integration with Calendar MCP

When calendar MCP is configured, you can use:
```bash
python run.py --calendar
```

This will:
1. Fetch your next meeting from the calendar
2. Identify attendees
3. Auto-detect meeting type from title
4. Run appropriate prep

## File Search

The tool searches these locations:
- All `.md` files in the workspace
- Excludes `Templates/` and `_Registry/`
- Scores results by filename match + content mentions
- Sorts by relevance, then recency

## Integration with Claude

Claude can run this tool before meetings to gather context. Example prompts:
- "Prep me for my 1:1 with Marcus"
- "What should I know before the design review?"
- "Gather context for my customer call with Riverside"

The output can be used directly or as input to the `meeting-prep` skill for more detailed preparation.
