# Research Design

## Public Summary

The project uses an event-study design to examine market reactions around Taiwan-related geopolitical events.

The workflow is:

```text
Identify event
→ code event characteristics
→ align market data
→ calculate returns
→ calculate abnormal returns
→ calculate cumulative abnormal returns
→ interpret results cautiously
```

## Method Overview

The event study compares asset returns with benchmark returns around event windows.

The project uses abnormal returns and cumulative abnormal returns to estimate whether selected assets moved differently from benchmarks during the event window.

The evidence is descriptive and interpretive. It should not be read as a causal proof that one mechanism alone caused the observed market movement.

## Key Variables

| Variable | Purpose |
|---|---|
| `surprise_score` | Codes whether an event appears high, medium, or low surprise based on pre-event information. |
| `surprise_rationale` | Explains the evidence behind the surprise coding decision. |
| `event_family` | Groups comparable event types, such as military exercises, diplomatic shocks, or strategic investments. |
| `event_repetition_level` | Codes whether an event is novel or part of a repeated pattern. |

These variables help separate adaptation from anticipation.

They do not prove investor beliefs. They make the interpretation more transparent and reduce the risk of overstating the adaptation argument.

## Data Inputs

Important public-facing inputs include:

- [events/events.csv](../../events/events.csv)
- [data/events_v2.csv](../../data/events_v2.csv)
- [data/market_data.csv](../../data/market_data.csv)

## Deeper Documents

- [Research Design Revision V2](../research_design_revision_v2.md)
- [Surprise Variable Framework](../surprise_variable_framework.md)
- [Market Data Contract](../market_data_contract.md)
- [Input Schema](../input_schema.md)
