# V3 Dashboard Analytics

> Academic Research Notice:
> This document is provided for educational and research reference purposes only.
> It may contain preliminary analysis, working assumptions, draft frameworks, or evolving interpretations.
> It should not be treated as a peer-reviewed publication.

## 1. Purpose

V3 adds dashboard-ready analytics outputs to the Taiwan Geopolitical Risk Event Study Engine.

The goal is to make the existing V2 batch outputs easier to use in business-facing summaries, future dashboards, and analyst review workflows.

V3 does not change:

- metric definitions
- CAR formula
- benchmark logic
- event schema
- existing V2 outputs

## 2. Why Dashboard-Ready Outputs Matter

V2 produces strong analytics artifacts, including event-level results, mechanism summaries, event-window files, figures, reports, and a run summary.

Dashboard tools need a flatter and more presentation-ready dataset.

The V3 dashboard layer converts the master event results into a single table that is easier to filter, visualize, and connect to generated artifacts.

## 3. Dashboard Data Output

V3 creates:

```text
results/dashboard_data.csv
```

This file contains one row per event and includes:

- event metadata
- asset and benchmark
- `car_value`
- `car_percent`
- `car_direction`
- event processing status
- report path
- figure path
- event-window data path

This structure supports future Repo 3 dashboard work by giving the dashboard a single event-level data source.

## 4. Executive Summary Output

V3 also creates:

```text
results/executive_summary.md
```

This file summarizes the batch run for a non-technical reader.

It includes:

- total events analyzed
- successful and failed event counts
- strongest positive event
- strongest negative event
- mechanism-level summary
- short interpretation
- non-investment-advice note

## 5. Product Role

The V3 layer turns engine outputs into communication-ready analytics.

It helps bridge:

```text
event-study engine
↓
dashboard data
↓
business-facing summary
↓
future analytics interface
```

This makes Repo 2 more useful as a portfolio analytics product and prepares the project for a possible Repo 3 dashboard.
