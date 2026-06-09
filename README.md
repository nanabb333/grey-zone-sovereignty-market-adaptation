# Taiwan Geopolitical Risk Event Study Engine

## Academic Research Notice

This repository contains research-oriented analytics tools, datasets, workflow documentation, and supporting materials developed for academic and educational purposes.

Any research notes, coding schemas, event classifications, findings summaries, or supporting documents should be treated as preliminary academic materials unless explicitly identified as peer-reviewed or formally published.

Nothing in this repository should be interpreted as investment advice, policy advice, or an official publication.

## One-Sentence Description

An automated analytics engine that measures financial market responses to Taiwan-related geopolitical events using event-study methodology.

## Business Problem

Geopolitical events can affect financial markets quickly, but manual event-study analysis is slow, difficult to repeat, and vulnerable to inconsistent workflow decisions.

Political risk analysts, financial research teams, and business analytics stakeholders need a repeatable workflow that can convert event metadata, market data, and event-window assumptions into structured outputs for review.

## Analytics Solution

This project transforms a manual Taiwan geopolitical-risk event study into an automated analytics engine.

The engine reads standardized event inputs, loads market data, calculates returns, calculates benchmark-adjusted abnormal returns, calculates cumulative abnormal return (CAR), and generates reusable CSV, figure, and Markdown report outputs.

Repo 2 is designed as an analytics product, not a research paper.

## Current Status

V2 multi-event batch processing is implemented.

The engine currently:

- reads multiple events from `events/events.csv`
- processes each event in a batch loop
- preserves a clear `process_one_event(event)` boundary
- records success or failure for each event
- continues processing after event-level failures
- writes a run summary after each batch execution

## Workflow

```text
events/events.csv
↓
Load all events
↓
FOR EACH EVENT
    Load market data
    Calculate returns
    Calculate abnormal returns
    Calculate CAR
    Save event-window data
    Generate figure
    Generate report
    Record event status
↓
Write master results table
↓
Write mechanism summary
↓
Write run summary
```

## Current Input Files

| Input | Path | Purpose |
|---|---|---|
| Event input | `events/events.csv` | Defines events, assets, benchmarks, and event windows |
| Market data | `data/market_data.csv` | Standardized market price data used by the engine |

Current event schema:

```csv
event_id,event_name,event_date,mechanism,event_type,asset,benchmark,event_window_start,event_window_end
```

## Current Outputs

| Output | Path | Purpose |
|---|---|---|
| Master event results | `results/event_results.csv` | One row per processed event |
| Mechanism summary | `results/mechanism_summary.csv` | Portfolio-level CAR summary by mechanism |
| Event-window data | `results/event_windows/{event_id}_event_window_data.csv` | Daily event-window returns and abnormal returns |
| Event figures | `figures/{event_id}_abnormal_returns.png` | Per-event abnormal return figure |
| Event reports | `reports/{event_id}_report.md` | Per-event analyst-facing Markdown report |
| Run summary | `results/run_summary.md` | Batch-level status summary |

The old V1 file `results/event_window_data.csv` is deprecated. V2 active event-window outputs are stored in `results/event_windows/`.

## Example Output Figure

![Pelosi Visit Abnormal Returns](figures/E001_abnormal_returns.png)

## Example Report

The engine automatically generates one Markdown report per successful event.

Example:

[reports/E001_report.md](reports/E001_report.md)

## How to Run V2

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the batch engine:

```bash
MPLCONFIGDIR=/private/tmp/matplotlib-cache /Users/cjy/miniconda3/bin/python3 scripts/run_event_study.py
```

The `MPLCONFIGDIR` setting gives Matplotlib a writable cache location on this machine.

## Current Metric Definition

`car_value` is benchmark-adjusted abnormal CAR under the current engine definition.

The engine calculates:

```text
asset_return = asset daily percentage change
benchmark_return = benchmark daily percentage change
abnormal_return = asset_return - benchmark_return
car_value = sum of abnormal_return inside the event window
```

For the current TSMC examples, the benchmark is SOX.

Raw CAR is not yet implemented as a separate output field. It is planned as a future enhancement.

## Event-Level Failure Handling

The engine records a status for each event in `results/event_results.csv`.

Current status behavior:

- `success`: the event processed successfully
- `failed`: the event failed, but the batch continued

Failed events are recorded with an `error_message` so the analyst can diagnose the problem without losing outputs for other events.

## Portfolio Analytics Layer

The engine also generates:

```text
results/mechanism_summary.csv
```

This file summarizes `car_value` by mechanism using successful events for CAR statistics and counting failed events separately.

Current mechanism summary fields:

```text
mechanism
event_count
mean_car_value
min_car_value
max_car_value
successful_event_count
failed_event_count
```

## Skills Demonstrated

- Business Analytics Workflow Design
- Financial Data Analytics
- Event Study Methodology
- Research Automation
- Python Analytics Pipeline
- Batch Processing
- Portfolio-Level Analytics
- Report Generation
- Validation and Metric Definition
- Research-to-Product Transformation

## Connection to Repo 1

Repo 1 was the manual research project:

**Grey-Zone Sovereignty and Market Adaptation: Financial Responses to Taiwan-Related Geopolitical Shocks**

Repo 1 developed the event classifications, market data workflow, abnormal-return calculations, CAR outputs, figures, and research interpretation.

Repo 2 turns that manual event-study workflow into an automated analytics engine.

```text
Repo 1 = research method and evidence trail
Repo 2 = repeatable analytics engine
```

## Roadmap

- Raw CAR + abnormal CAR outputs
- Richer validation fields
- Batch report index
- Dashboard development
- AI-assisted event classification
- Agent-assisted analyst review
