# Dissertation Upgrade Memo

> Academic Research Notice:
> This document is provided for educational and research reference purposes only.
> It evaluates dissertation improvement priorities without adding new empirical claims.

## Purpose

This memo assesses the current dissertation and ranks the next improvements most likely to increase credibility, clarity, and research value. The focus is on strengthening the adaptation mechanism while avoiding overstatement.

## Current Strengths

### Theory

The dissertation has a clear theoretical contribution. The grey-zone sovereignty framework links Taiwan's unresolved sovereignty status to recurring geopolitical and geoeconomic shocks. It avoids a simple risk-damage model by arguing that markets respond through investor interpretation.

The most promising theoretical move is the distinction between objective risk and interpreted risk. This allows the dissertation to explain why some Taiwan-related shocks generate negative reactions while others are muted or positive.

### Literature Review

The project bridges international relations, international political economy, geopolitical risk, and financial-market response. This interdisciplinary positioning is a strength for policy research and graduate-school applications because it shows the ability to connect political mechanisms with empirical market outcomes.

### Research Design

The event-study design is appropriate for an exploratory dissertation. It provides a transparent structure for comparing Taiwan-related shocks across event type, market outcome, and CAR window. The use of TWSE and TSMC also gives the analysis both broad-market and strategically important firm-level relevance.

### Event Study Implementation

The implementation is reproducible and interpretable. The benchmark-adjusted abnormal-return approach improves on raw returns by accounting for broader technology and semiconductor-sector movement. The project is credible as a research portfolio because the code, data organization, figures, and results are visible.

## Current Weaknesses

### Adaptation Identification

The central mechanism, investor adaptation, is currently inferred rather than directly observed. The empirical results are consistent with adaptation, but they do not fully distinguish adaptation from anticipation, prior pricing, broader market momentum, or event-specific context.

### Surprise Measurement

Surprise is theoretically important but not yet fully operationalized. Without a transparent surprise variable, it is difficult to separate repeated-event adaptation from expected-event pricing.

### Small Sample Concerns

The event sample is necessarily limited. This is acceptable for an exploratory dissertation, but it limits statistical leverage and makes individual cases influential. The dissertation should lean into careful interpretation rather than broad generalization.

## Ranked Next Improvements

### Priority 1: Add Surprise Coding

The highest-value next improvement is to add a transparent surprise variable with a rationale for each event. This directly addresses the anticipation/prior-pricing rival explanation. It would strengthen the dissertation without requiring a full redesign.

Expected quality gain:
High. This would make the adaptation argument more cautious, more testable, and more defensible.

### Priority 2: Add Adaptation vs Anticipation Discussion

The dissertation should include a dedicated discussion of adaptation versus anticipation. This section should explain why the current results are consistent with adaptation but do not prove it. It should also define what future evidence would strengthen or weaken the adaptation interpretation.

Expected quality gain:
High. This would improve theoretical credibility and demonstrate awareness of rival explanations.

### Priority 3: Add Event-Family Repetition Coding

The dataset should include `event_family` and `event_repetition_level`. These fields would make it possible to compare repeated PLA exercise events against more novel diplomatic, sanctions, or strategic-investment events.

Expected quality gain:
Medium to high. This would improve transparency and help organize the adaptation argument, though it would still require careful interpretation because repetition and anticipation may overlap.

## Improvements With Lower Immediate Priority

1. Larger event sample: useful, but may introduce coding complexity and heterogeneous events.
2. More advanced statistical modeling: potentially valuable, but risks over-engineering a small exploratory sample.
3. Forecasting or predictive modeling: not appropriate for the dissertation's current research question.
4. Strong causal claims: should be avoided unless the identification strategy becomes substantially stronger.

## Bottom Line

The dissertation is strongest when framed as a theory-building event study. Its main contribution is not proving that adaptation causes market resilience. Its contribution is showing that Taiwan-related geopolitical risk is mediated by investor interpretation, and that adaptation is a plausible mechanism alongside anticipation, strategic importance, and surprise.

