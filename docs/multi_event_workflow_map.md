# Multi-Event Workflow Map

> Academic Research Notice:
> This document is provided for educational and research reference purposes only.
> It may contain preliminary analysis, working assumptions, draft frameworks, or evolving interpretations.
> It should not be treated as a peer-reviewed publication.

## 1. Purpose

This document maps the transition from the V1 single-event workflow to the V2 multi-event workflow for the Taiwan Geopolitical Risk Event Study Engine.

Implementation status: V2 multi-event batch processing is implemented.

The goal of V2 is not to change the event-study logic.

The goal is to change the workflow shape:

```text
Single Event Workflow
↓
Multi-Event Workflow
```

V1 proves that one event can move through the full analytics pipeline.

V2 should allow many events to move through the same pipeline in one batch run.

## 2. Current V1 Workflow

V1 reads one event and produces one set of outputs.

```text
events.csv
↓
Load Event
↓
Calculate Returns
↓
Calculate Abnormal Returns
↓
Calculate CAR
↓
Generate Results
↓
Generate Figure
↓
Generate Report
```

Current V1 behavior:

- reads the first event from `events/events.csv`
- loads market data
- calculates asset and benchmark returns
- calculates abnormal returns
- calculates CAR for one event window
- writes one event-level result
- writes one event-window data file
- generates one figure
- generates one Markdown report

V1 is useful as a proof of workflow automation.

Its limitation is that it does not yet process a portfolio of events.

## 3. Target V2 Workflow

V2 should read all events and process each event through the same analytical sequence.

```text
events.csv
↓
Load Events
↓
FOR EACH EVENT
    Validate Event
    Calculate Returns
    Calculate Abnormal Returns
    Calculate CAR
    Generate Result Row
    Generate Figure
    Generate Report
↓
Append Result to Master Results Table
↓
Continue Processing Remaining Events
↓
Final event_results.csv
↓
Run Summary
```

The main workflow shift is:

```text
V1 = one event, one output set
V2 = many events, repeated output sets, one master results table
```

The conductor should manage iteration. The analytical modules should continue to perform focused workflow steps.

## 4. Failure Handling

V2 should distinguish between event-level failures and run-level failures.

Event-level failures should not stop processing.

Examples of event-level failures:

- missing asset column for one event
- missing benchmark column for one event
- event date outside the available market range
- empty event window
- figure generation failure for one event
- report generation failure for one event

Recommended event-level behavior:

```text
event fails
↓
record failed event
↓
save failure reason
↓
continue processing remaining events
```

Failed events should be recorded in the master results table with a status field and validation note.

Remaining events should continue running.

Run-level failures may stop the run.

Examples of run-level failures:

- missing `events/events.csv`
- invalid event input schema
- missing `data/market_data.csv`
- market data cannot be loaded
- global output folders cannot be created

This distinction is important because V2 is a batch analytics workflow. A single problematic event should not prevent the engine from producing useful outputs for other events.

## 5. Output Architecture

V2 should produce shared outputs and per-event outputs.

### Master Results Table

```text
results/event_results.csv
```

This should become the main multi-event output.

In V1, it contains one event.

In V2, it should contain one row per processed event.

Each row should include:

- event metadata
- asset and benchmark
- event window
- CAR metrics
- processing status
- error message, if the event failed

The master table supports comparison across events and future dashboard development.

### Event-Window Data

Current V1 output:

```text
results/event_window_data.csv
```

For V2, a single shared file may become too ambiguous because each event has its own window.

Preferred V2 pattern:

```text
results/event_windows/{event_id}_event_window_data.csv
```

This is the active V2 event-window output.

The old V1 output is deprecated:

```text
results/event_window_data.csv
```

It should not be used as the active V2 event-window source.

Each event-window file should include the daily data used to calculate CAR:

- date
- asset return
- benchmark return
- abnormal return

This creates an audit trail for each event.

### Reports

```text
reports/
```

V2 should generate one report per event.

Recommended pattern:

```text
reports/{event_id}_report.md
```

Each report should summarize:

- event metadata
- asset and benchmark
- event window
- CAR value
- validation notes
- paths to the event-window data and figure

Reports are analyst-facing outputs.

### Figures

```text
figures/
```

V2 should generate one figure per event.

Recommended pattern:

```text
figures/{event_id}_abnormal_returns.png
```

Each figure should visualize event-window abnormal returns.

Figures support quick visual inspection and portfolio presentation.

### Run Summary

```text
results/run_summary.md
```

V2 writes a run-level Markdown summary after each batch execution.

The run summary includes:

- total event count
- successful event count
- failed event count
- event-level status table
- output locations
- notes on `status` and `car_value`

## 6. Future Compatibility

The V2 workflow should support future product directions.

### Dashboard Development

The master results table can become the data source for a future dashboard.

A dashboard could filter by:

- mechanism
- event type
- event year
- asset
- benchmark
- CAR value
- validation status

### Agent Workflows

Future agent workflows can use the master results table and per-event reports as structured context.

An agent could:

- identify events needing review
- summarize event results
- compare Risk and Strategic_Importance events
- draft analyst notes
- flag inconsistent metrics

### Batch Analytics

The multi-event workflow allows the engine to support batch analytics rather than one-off analysis.

Examples:

- process all events in a research sample
- compare CAR across mechanisms
- identify outlier events
- generate repeated reports automatically

### Portfolio-Level Analysis

V2 creates the foundation for portfolio-level event analysis.

Instead of asking:

```text
What happened during one event?
```

the engine can begin answering:

```text
How do different types of Taiwan-related geopolitical events compare across the full sample?
```

This is the product shift from event calculator to analytics engine.

## 7. Design Principle

V2 should preserve the clean separation established in V1:

```text
inputs define the event
modules perform calculations
the conductor manages workflow
outputs support analyst review
```

The multi-event engine should not become a single large script.

It should remain a workflow system that coordinates reusable modules.
