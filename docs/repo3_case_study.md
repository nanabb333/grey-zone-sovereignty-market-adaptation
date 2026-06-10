# Repo 3 Case Study

> Academic Research Notice:
> This document is provided for educational and research reference purposes only.
> It may contain preliminary analysis, working assumptions, draft frameworks, or evolving interpretations.
> It should not be treated as a peer-reviewed publication.

## Project Overview

Repo 3 is an AI-ready geopolitical risk dashboard that converts Repo 2 event-study outputs into a decision-support interface for a geopolitical risk analyst.

The product focuses on explaining Taiwan-related geopolitical event-study results through KPI cards, executive summaries, rule-based insights, historical comparisons, executive briefs, and LLM-ready context.

No LLM APIs are used in the current version. The intelligence layer is deterministic and rule-based.

## Business Problem

Political risk and financial research teams often need to move quickly from event data to decision-support insight.

CSV outputs, figures, and event reports are useful, but they can be slow to review when analysts need to identify:

- the strongest positive or negative market reactions
- whether an event was stronger than its mechanism average
- which outputs support an analyst explanation
- what summary can be shared with non-technical stakeholders

Repo 3 addresses this gap by turning structured event-study outputs into a dashboard-ready analyst workflow.

## Product Goal

The product goal is to help a geopolitical risk analyst move from Repo 2 analytics outputs to an analyst-ready interpretation layer.

The dashboard should answer:

- What happened in the latest event-study run?
- Which event had the strongest abnormal return?
- How does each event compare with its mechanism average?
- What deterministic insights can be surfaced for analyst review?
- What structured context is ready for future LLM-assisted interpretation?

## Analytics Pipeline

Repo 3 consumes Repo 2 outputs:

```text
results/dashboard_data.csv
results/mechanism_summary.csv
results/executive_summary.md
results/event_insights.json
```

It generates additional dashboard intelligence outputs:

```text
results/historical_comparison.json
results/executive_brief.json
results/llm_context.json
```

The pipeline follows:

```text
Repo 2 event-study outputs
↓
Dashboard data layer
↓
Rule-based insight generator
↓
Historical comparison engine
↓
Executive brief generator
↓
LLM-ready context builder
↓
Dashboard V1
```

## Dashboard Architecture

Dashboard V1 includes:

- KPI cards
- Latest Event View
- Executive Summary display
- Executive Brief section
- Historical Comparison section
- Intelligence Overview section
- Rule-Based Insight Panel

The dashboard is designed as a single-page analyst workspace. It emphasizes clarity, traceability, and communication value rather than complex filtering or prediction.

## Intelligence Layer

The Repo 3 intelligence layer is deterministic.

It includes:

- rule-based event insights
- event-versus-mechanism comparison metadata
- deterministic executive brief templates
- structured LLM-ready context for future use

The current intelligence layer does not use:

- OpenAI
- Claude
- Gemini
- external APIs
- forecasting
- trading recommendations

## Business Value

Repo 3 creates value by reducing the gap between analytical outputs and stakeholder communication.

For a geopolitical risk analyst, the dashboard helps:

- scan event-study results quickly
- identify important abnormal-return outcomes
- compare events against mechanism averages
- review deterministic insights and supporting evidence
- prepare non-technical summaries for discussion

For a Business Analytics portfolio, Repo 3 demonstrates product thinking, dashboard design, rule-based automation, and AI-ready architecture.

## Limitations

Current limitations:

- small event sample
- no live data refresh
- no interactive filtering
- no database layer
- no LLM-generated interpretation
- no statistical significance testing inside the dashboard
- no forecasting or scenario prediction

These limitations are intentional for the V1 portfolio version. The goal is to demonstrate a clear analytics product workflow before expanding complexity.

## Future AI Roadmap

Future versions may add analyst-reviewed LLM support using the structured `llm_context.json` file.

Possible future AI features:

- event explanation drafts
- mechanism interpretation drafts
- caveat checklists
- executive brief drafting
- analyst-editable summary text
- source-grounded narrative generation

AI outputs should remain:

- grounded in Repo 2 and Repo 3 structured outputs
- clearly labeled as draft interpretation
- auditable by the analyst
- free of forecasting, trading recommendations, and unsupported claims
