# Portfolio Positioning

> Academic Research Notice:
> This document is provided for educational and research reference purposes only.
> It may contain preliminary analysis, working assumptions, draft frameworks, or evolving interpretations.
> It should not be treated as a peer-reviewed publication.

## Project Name

Taiwan Geopolitical Risk Event Study Engine

## One-Sentence Description

An automated analytics engine that measures how Taiwan-related geopolitical events affect financial markets using event-study methodology.

## Business Problem

Geopolitical shocks can affect markets quickly, but manual analysis is slow, inconsistent, and difficult to repeat across events.

Analysts need a repeatable workflow that can turn an event date, asset, benchmark, and event window into structured outputs for decision support.

## Analytics Problem

The project converts a manual event-study process into a standardized pipeline:

- define an event
- load market data
- calculate returns
- calculate abnormal returns
- calculate CAR
- save results
- generate figures
- generate reports

The analytics challenge is not only calculating CAR. The challenge is designing a reliable workflow that moves from input data to reusable outputs with minimal manual intervention.

## Inputs

Current V1 inputs:

- `events/events.csv`
- `data/market_data.csv`

The event input defines:

- event ID
- event name
- event date
- theoretical mechanism
- event type
- asset
- benchmark
- event window

The market data input provides standardized asset and benchmark price columns.

## Processing Workflow

```text
Input event
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
```

## Outputs

Current V1 outputs:

- `results/event_results.csv`
- `results/event_window_data.csv`
- `figures/E001_abnormal_returns.png`
- `reports/E001_report.md`

These outputs support both validation and analyst review.

## Skills Demonstrated

- Data Analytics
- Workflow Automation
- Event Study Methodology
- Financial Data Processing
- Python
- Research Automation
- Report Generation
- Data Validation
- Analytics Product Design
- Reproducible Analysis

## Why This Project Is Different

Traditional academic paper:

- focuses on argument, literature, and interpretation
- often contains static tables and figures
- may rely on manual calculations

Manual event study:

- can answer one research question
- is useful but hard to repeat
- often mixes data cleaning, calculations, charting, and interpretation

Automated event-study engine:

- separates inputs, processing modules, and outputs
- allows the same workflow to be rerun
- produces structured CSVs, figures, and reports
- turns research methodology into an analytics product

Repo 1 proved the research method.

Repo 2 packages the method into a repeatable analytics workflow.

## Target Audience

- Business Analytics recruiters
- Political Risk firms
- Financial research teams
- Graduate admissions committees
- Policy analytics teams
- Investment research teams
- Research automation teams

## Resume Bullet Example

Built an automated Python event-study engine that processes Taiwan-related geopolitical events, loads standardized market data, calculates benchmark-adjusted abnormal returns and CAR, and generates CSV outputs, figures, and Markdown reports for analyst review.

## LinkedIn Project Example

I built the Taiwan Geopolitical Risk Event Study Engine, an analytics workflow that transforms a manual research process into an automated event-study pipeline.

The engine reads standardized event inputs, loads market data, calculates returns and abnormal returns, computes CAR, saves event-level and event-window outputs, generates an abnormal return figure, and produces a Markdown report.

This project demonstrates how research methodology can be turned into a reusable analytics product for political risk, financial research, and business analytics workflows.

## GitHub README Positioning

The Taiwan Geopolitical Risk Event Study Engine is a Python-based analytics engine for studying financial market responses to Taiwan-related geopolitical shocks.

Version 1 processes one event from start to finish:

```text
events/events.csv
→ data/market_data.csv
→ returns
→ abnormal returns
→ CAR
→ results
→ figure
→ report
```

The project is designed as an analytics product rather than a research paper. It emphasizes workflow automation, reproducibility, and structured outputs for analyst review.
