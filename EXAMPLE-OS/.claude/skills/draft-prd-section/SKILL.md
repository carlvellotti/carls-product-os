---
name: draft-prd-section
description: Write a specific PRD section grounded in project research and goals
argument-hint: "[section-name] [project-path]"
user-invocable: true
---

# PRD Section Drafter

Help write or improve a specific section of a PRD.

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
   - Reference `GOALS.md` for OKR alignment

3. **Section-Specific Guidance**

   **Problem Statement:**
   - Lead with user pain, not solution
   - Include evidence (data, quotes, tickets)
   - Quantify impact where possible

   **User Stories:**
   - Format: "As a [persona], I want to [action] so that [outcome]"
   - Include acceptance criteria for P0 stories
   - Prioritize: P0 = must have, P1 = should have, P2 = nice to have

   **Success Metrics:**
   - Primary metrics: What MUST improve?
   - Secondary metrics: What else should we monitor?
   - Guardrails: What should NOT get worse?
   - Include current baseline and target

4. **Draft the Section**
   - Use the PRD template structure from `Templates/prd.md`
   - Ground every claim in evidence from the project's research
   - Flag assumptions or gaps needing input

## Notes

- Always ground in user research when available
- Challenge assumptions - ask "how do we know this?"
- Keep iterating - PRDs are living documents
