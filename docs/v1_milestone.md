# Single Event Engine V1 Milestone

> Academic Research Notice:
> This document is provided for educational and research reference purposes only.
> It may contain preliminary analysis, working assumptions, draft frameworks, or evolving interpretations.
> It should not be treated as a peer-reviewed publication.

## 1. Status

Single Event Engine V1 is complete.

The engine can process one event from standardized event input through CAR calculation, CSV outputs, figure generation, and Markdown report generation.

## 2. Current Workflow

events/events.csv

↓

scripts/run_event_study.py

↓

Load market data

↓

Calculate returns

↓

Calculate abnormal returns

↓

Calculate CAR

↓

Save event-level results

↓

Save event-window data

↓

Generate abnormal return figure

↓

Generate Markdown report

## 3. Current Outputs

| Output | Path | Purpose |
|---|---|---|
| Event results | results/event_results.csv | Stores event-level CAR result |
| Event window data | results/event_window_data.csv | Stores daily event-window abnormal returns |
| Figure | figures/E001_abnormal_returns.png | Visualizes abnormal returns |
| Report | reports/E001_report.md | Analyst-facing event summary |

## 4. Current Example

The current V1 example uses:

- Event: Pelosi Visit
- Date: 2022-08-02
- Asset: TSMC
- Benchmark: SOX
- Event window: [-7, +7]
- CAR value: 0.0044332006595363405

## 5. What V1 Does Not Do Yet

V1 does not yet support:

- multiple events
- AI event classification
- automatic raw data downloading
- natural language interpretation
- dashboard interface
- agent behavior

## 6. Next Phase

The next phase is to move from one-event processing to multi-event processing.
