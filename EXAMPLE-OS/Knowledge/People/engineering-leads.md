# Engineering Leads - Working Styles

*How to work effectively with each engineering lead*

---

## Marcus Lee - Platform Team Lead

*My primary engineering partner*

### Quick Facts
- **Role:** Staff Engineer, Platform Team Lead
- **Tenure:** 3 years
- **Background:** Senior Eng at Stripe, before that a startup
- **Team:** 8 engineers (Platform Team)
- **Location:** SF, in office Mon/Wed/Fri
- **Focus areas:** Grading service, TA features, core infrastructure

### Communication Style

**Prefers:**
- Written specs with clear requirements
- Context on the "why" behind requests
- Early involvement in problem framing
- Async communication (Slack, Notion)
- Technical discussions over diagrams

**Dislikes:**
- Vague requirements ("make it better")
- Last-minute scope changes
- Skipping technical review
- Meetings without agendas
- Being told how to implement (vs. what to solve)

### Working Together

**How to write specs for Marcus:**
1. Start with user problem and outcome
2. Include success metrics
3. Define what's out of scope explicitly
4. List questions/uncertainties
5. Let him propose technical approach

**In planning meetings:**
- He's quiet until he has something substantive
- When he raises concerns, take them seriously
- He won't pad estimates; if he says 2 weeks, it's 2 weeks
- Ask for his input on phasing and tradeoffs

**Getting quick answers:**
- Slack him with context, not just "can we chat?"
- He'll respond thoughtfully (give him time)
- For urgent issues, say "urgent" explicitly

### What Marcus Cares About

- **Code quality:** Won't ship hacky solutions
- **System reliability:** Thinks about scale and edge cases
- **Team growth:** Mentors junior engineers
- **Technical debt:** Advocates for paying it down
- **Understanding context:** Wants to know the user story

### How to Build Trust With Marcus

1. Write thorough specs (he notices the effort)
2. Don't change requirements mid-sprint without good reason
3. Defend engineering time against scope creep
4. Credit the team publicly for wins
5. Be honest when PM screwed up

### Personal Notes
- Homebrew beer hobbyist
- Dry humor; appreciates sarcasm
- Introverted but warms up over time
- Goes deep on problems (don't rush him)

---

## Emily Zhang - Data Team Lead

*Partner for analytics and AI features*

### Quick Facts
- **Role:** Staff Engineer, Data Team Lead
- **Tenure:** 2 years
- **Background:** ML Engineer at Netflix, PhD in CS (ML focus)
- **Team:** 5 engineers (Data Team)
- **Location:** Remote (Seattle), visits SF monthly
- **Focus areas:** Analytics, AI/ML features, data pipeline

### Communication Style

**Prefers:**
- Structured problem statements
- Data to support hypotheses
- Async deep-dives (she writes long docs)
- Technical specificity
- Loom videos for complex explanations

**Dislikes:**
- Hand-wavy ML requests ("just use AI for this")
- Underestimating ML complexity
- Scope creep on ML features
- Meetings without clear outcomes
- Being asked for "quick" ML solutions

### Working Together

**How to request AI/ML work:**
1. Define the user problem precisely
2. Specify what "good enough" looks like (accuracy threshold)
3. Identify training data availability
4. Discuss evaluation approach
5. Plan for ongoing maintenance

**Getting AI estimates:**
- She'll want to spike before committing
- Respect uncertainty - ML timelines are variable
- Plan for iteration (v1 rarely nails it)

**In cross-functional meetings:**
- She speaks up when there are ML implications
- Don't oversimplify ML in front of stakeholders without her input
- Let her explain technical constraints directly

### What Emily Cares About

- **ML best practices:** Won't deploy half-baked models
- **Bias and fairness:** Takes ethics seriously
- **Research rigor:** Appreciates when PM reads papers
- **Long-term maintenance:** Thinks about model drift
- **Clear success criteria:** "Improved" isn't specific enough

### How to Build Trust With Emily

1. Do your homework on ML fundamentals
2. Don't promise AI features without her input
3. Give her team credit for AI wins
4. Be patient with experimentation
5. Bring her customer feedback on AI performance

### Personal Notes
- Runs a ML reading group internally
- Board game enthusiast
- Direct communication style (not rude, just efficient)
- Appreciates intellectual curiosity

---

## Carlos Rivera - Integrations Team Lead

*Partner for LMS integrations and third-party APIs*

### Quick Facts
- **Role:** Senior Engineer, Integrations Team Lead
- **Tenure:** 18 months
- **Background:** Integration architect at Salesforce
- **Team:** 4 engineers (Integrations Team)
- **Location:** SF, in office Tue/Wed
- **Focus areas:** LMS integrations (Canvas, Blackboard), third-party APIs

### Communication Style

**Prefers:**
- Clear priority stack-ranking
- Customer-specific context (which university needs what)
- Heads-up on incoming sales asks
- Documented external requirements
- Direct communication

**Dislikes:**
- Constantly shifting priorities
- Vague integration requirements from sales
- Being surprised by customer escalations
- Assuming integrations are "simple"
- Undocumented third-party APIs

### Working Together

**Requesting integration work:**
1. Specify customer and timeline driver
2. Share third-party API documentation
3. Define minimum viable scope
4. Identify testing requirements
5. Plan for ongoing maintenance

**Managing customer escalations:**
- Loop Carlos in early, not after it's urgent
- He's good with customers directly (can join calls)
- Get him accurate reproduction steps
- Don't promise integration fixes without consulting him

**Cross-LMS features:**
- Always ask "does this work for Canvas AND Blackboard?"
- Different LMS = different edge cases
- Integration testing is time-consuming (factor into timeline)

### What Carlos Cares About

- **Reliability:** Integrations failing = customer pain
- **Documentation:** External API changes break things
- **Predictability:** Stable priorities help his team plan
- **Customer impact:** Motivated by helping universities
- **Technical debt:** Integration code accumulates cruft

### How to Build Trust With Carlos

1. Be a buffer against sales priority churn
2. Provide complete requirements upfront
3. Give realistic timelines to customers
4. Appreciate integration complexity
5. Share customer feedback (especially wins)

### Personal Notes
- Mexican heritage; occasionally brings team to his favorite taqueria
- Very reliable; if he commits, it happens
- Calm under pressure
- Appreciates recognition (doesn't seek it)

---

## Cross-Team Dynamics

### Marcus + Emily (Platform + Data)
- Good relationship; collaborate on AI features
- Marcus handles services; Emily handles models
- Coordinate through shared planning docs
- Occasional tension on AI performance requirements

### Marcus + Carlos (Platform + Integrations)
- Clear boundaries; less overlap
- Integration issues sometimes surface Platform bugs
- Carlos escalates infrastructure issues to Marcus
- Respect each other's domains

### Emily + Carlos (Data + Integrations)
- Lighter interaction
- Coordinate on data from external systems
- Analytics for integration health

### When All Three Need to Align
- Rare but important (big features touching everything)
- Use shared planning docs, not meetings
- I facilitate alignment; they execute in parallel
- Flag dependencies early
