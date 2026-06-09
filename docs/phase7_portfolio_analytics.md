# Phase 7 Portfolio Analytics Layer

> Academic Research Notice:
> This document is provided for educational and research reference purposes only.
> It may contain preliminary analysis, working assumptions, draft frameworks, or evolving interpretations.
> It should not be treated as a peer-reviewed publication.

## Purpose

Phase 7 adds a portfolio-level analytics output to Repo 2.

V2 produced event-level outputs. Phase 7 adds a mechanism-level summary so analysts can compare groups of events.

## New Output

```text
results/mechanism_summary.csv
```

## Input Source

The mechanism summary is generated only from:

```text
results/event_results.csv
```

No metric logic is recalculated from raw market data.

## Output Columns

```text
mechanism
event_count
mean_car_value
min_car_value
max_car_value
successful_event_count
failed_event_count
```

## Calculation Rules

- Group rows by `mechanism`.
- Count all rows for `event_count`.
- Use only `status=success` rows for mean, min, and max CAR statistics.
- Count `status=success` rows in `successful_event_count`.
- Count `status=failed` rows in `failed_event_count`.
- Failed rows do not contribute to CAR statistics.

## Current Metric Definition

`car_value` is benchmark-adjusted abnormal CAR under the current engine definition.

Phase 7 does not change:

- CAR formula
- benchmark logic
- event schema
- abnormal return calculation

## Product Value

The mechanism summary turns event-level outputs into portfolio-level analytics.

It supports:

- comparison across mechanisms
- dashboard development
- batch analytics
- political risk portfolio review
- future agent workflows

## Known Limitations

- The current sample has only four events.
- Raw CAR is not yet implemented as a separate portfolio metric.
- Mechanism-level statistics are descriptive and should not be interpreted as causal estimates.
