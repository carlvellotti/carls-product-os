# Step 1: Gather Metrics

## Metrics Sources

| Metric | Source | How to Access |
|--------|--------|---------------|
| Teacher Activation Rate | Amplitude | Dashboard: "Teacher Funnel" → "7-Day Activation" |
| Weekly Active Teachers | Amplitude | Dashboard: "Core Metrics" → "WAU Teachers" |
| Student Submissions | Amplitude | Dashboard: "Engagement" → "Weekly Submissions" |
| MRR | Stripe | Billing → MRR Overview |
| Trial → Paid Conversion | Stripe | Billing → Conversion Funnel |
| Support Tickets | Intercom | Reports → Volume → This Week |
| NPS (monthly) | Delighted | Dashboard → Trend |

## Which Metrics to Include

**Always include (core health):**
- Teacher Activation Rate (target: 65%)
- MRR and WoW change
- Trial conversion rate

**Include if notable movement (>10% change):**
- WAU teachers
- Student submission volume
- Support ticket volume

**Include monthly:**
- NPS score and trend
- Churn rate

## How to Present Metrics

Format: `Metric: Current (vs Last Week, vs Target)`

Example:
```
- Teacher Activation: 58% (+3% WoW, target 65%)
- MRR: $47.2K (+$1.8K WoW)
- Trial Conversion: 12% (flat, target 15%)
```

## Red/Yellow/Green Framework

- **Green**: At or above target
- **Yellow**: Within 10% of target
- **Red**: More than 10% below target

Always note color in the TL;DR if any metric is red.

## Getting the Data

### Amplitude Quick Pull
1. Open Amplitude → Dashboards → "PM Weekly Metrics"
2. Set date range to last 7 days
3. Screenshot or copy the key numbers

### Stripe Quick Pull
1. Open Stripe Dashboard → Billing
2. Note MRR from top card
3. Click into "Subscriptions" → filter by created date for trial conversions

### Intercom Quick Pull
1. Reports → Conversations → Volume
2. Filter to last 7 days
3. Note total count and compare to prior week
