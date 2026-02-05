# PRD Section Drafter

Help write or improve a specific section of a PRD.

## Trigger

User says: "help me write the {{section}} section", "draft PRD section", "improve my user stories"

## Instructions

1. **Identify Context**
   - Which PRD? (ask or infer from recent work)
   - Which section? Map to template sections:
     - Problem Statement
     - Solution Overview
     - User Stories
     - Success Metrics
     - Technical Approach
     - Launch Plan
     - Timeline

2. **Gather Inputs**
   - Read existing PRD draft if available
   - Pull relevant research summaries
   - Check related project briefs
   - Look for competitive analysis

3. **Section-Specific Guidance**

   **Problem Statement:**
   - Lead with user pain, not solution
   - Include evidence (data, quotes, tickets)
   - Quantify impact where possible
   - Questions to answer: Who? What pain? Why now? What if we don't?

   **User Stories:**
   - Format: "As a [persona], I want to [action] so that [outcome]"
   - Include acceptance criteria for P0 stories
   - Prioritize ruthlessly (P0 = must have, P1 = should have, P2 = nice to have)
   - Cover both happy path and edge cases

   **Success Metrics:**
   - Primary metrics: What MUST improve for this to be successful?
   - Secondary metrics: What else should we monitor?
   - Guardrails: What should NOT get worse?
   - Include current baseline and target

   **Solution Overview:**
   - Start with the "what" before the "how"
   - Be explicit about scope boundaries
   - Reference user stories being addressed

   **Technical Approach:**
   - Partner with engineering on this section
   - Focus on approach, not implementation details
   - Call out dependencies and risks

4. **Draft the Section**
   - Use the PRD template structure
   - Fill with specific, concrete content
   - Flag assumptions or gaps needing input
   - Suggest alternatives where appropriate

5. **Review Checklist**
   Verify the section:
   - [ ] Uses clear, jargon-free language
   - [ ] Includes specific examples, not just abstract statements
   - [ ] Cites evidence where making claims
   - [ ] Is appropriately detailed for current stage (don't over-specify early)

## Example Interaction

**User:** "help me write user stories for the gradebook redesign"

**Claude:**
1. Reads existing Gradebook Redesign PRD
2. Pulls research on teacher grading workflows
3. Identifies key user personas (Teacher, Admin)
4. Drafts user stories based on documented pain points

**Output:**
```
### Primary User: High School Teacher

| As a... | I want to... | So that... | Priority |
|---------|--------------|------------|----------|
| Teacher | Enter grades for an entire assignment in one view | I can grade faster without clicking between students | P0 |
| Teacher | See a student's recent grades while grading | I can identify if a student is struggling | P1 |
| Teacher | Import grades from external tools (Google Forms) | I don't have to re-enter data manually | P1 |
| Teacher | Set up automatic late penalties | I don't have to calculate and adjust each grade | P2 |
```

## Notes

- Always ground in user research when available
- Challenge assumptions - ask "how do we know this?"
- Suggest what research is needed if gaps exist
- Keep iterating - PRDs are living documents
