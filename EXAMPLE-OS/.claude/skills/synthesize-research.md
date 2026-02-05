# Research Synthesizer

Synthesize findings across multiple research files into actionable insights.

## Trigger

User says: "synthesize research", "summarize research for {{topic}}", "what did we learn about {{topic}}"

## Instructions

1. **Locate Research Files**
   - Search for interview notes, research summaries related to the topic
   - Include: `interview-notes-*.md`, `research-summary-*.md`
   - Check `_temp/` for quick notes that might be relevant

2. **Extract Key Data**
   From each file, pull:
   - Key findings and confidence levels
   - Pain points with severity ratings
   - Verbatim quotes (especially emotional or insightful ones)
   - Recommendations made

3. **Identify Patterns**
   - Group similar findings across sources
   - Count frequency of themes
   - Note contradictions or outliers
   - Assess overall confidence based on consistency

4. **Generate Synthesis**

   Output format:

   ```
   ## Research Synthesis: {{topic}}

   **Sources:** {{N}} interviews, {{N}} surveys, etc.
   **Date Range:** {{earliest}} to {{latest}}

   ### Top Findings

   #### 1. {{Finding}}
   - **Frequency:** Mentioned by X/Y participants
   - **Confidence:** High/Medium/Low
   - **Evidence:** {{summary}}
   - **Key Quote:** "{{quote}}" — P{{X}}

   #### 2. {{Finding}}
   ...

   ### Patterns & Themes

   | Theme | Frequency | Segments Most Affected |
   |-------|-----------|------------------------|
   | | | |

   ### Contradictions / Nuances
   - {{where findings differed and why}}

   ### Recommendations
   1. **Do Now:** {{high confidence, high impact}}
   2. **Explore:** {{needs more research}}
   3. **Avoid:** {{anti-patterns identified}}

   ### Gaps / Open Questions
   - {{what we still don't know}}
   ```

5. **Link to Sources**
   - Include wikilinks to all source documents
   - Make findings traceable

## Example

**User:** "synthesize research on grading workflow"

**Claude:**
1. Finds: `interview-notes-teacher-01.md`, `interview-notes-teacher-02.md`, `research-summary-grading-pain-points.md`
2. Extracts findings about grading workflow from each
3. Identifies that 4/5 teachers mentioned "batch grading" as a pain point
4. Outputs synthesis with recommendations

## Notes

- Preserve participant anonymity (use IDs, not names)
- Weight findings by recency if research spans long periods
- Call out when sample size is too small for confidence
- Suggest follow-up research for low-confidence areas
