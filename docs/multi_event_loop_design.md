# Multi-Event Loop Design

> Academic Research Notice:
> This document is provided for educational and research reference purposes only.
> It may contain preliminary analysis, working assumptions, draft frameworks, or evolving interpretations.
> It should not be treated as a peer-reviewed publication.

## 1. Purpose

V2 needs a loop architecture because the engine is moving from one-event processing to batch event processing.

Implementation status: this loop architecture is now implemented in `scripts/run_event_study.py`.

Current V1:

```text
Load First Event
↓
Process Event
↓
Output Results
```

Target V2:

```text
Load All Events
↓
FOR EACH EVENT
    Process Event
↓
Aggregate Outputs
```

The goal is not simply to repeat V1 code multiple times.

The goal is to create a workflow structure that can process multiple events, record per-event outcomes, and produce a final multi-event results table.

## 2. Logical Layers

V2 should be designed around three logical layers:

1. Run-Level Controller
2. Single-Event Processor
3. Output Manager

These layers separate coordination, event analysis, and output writing.

## 3. Run-Level Controller

The Run-Level Controller manages the full batch run.

Responsibilities:

- load `events/events.csv`
- iterate through all events
- track progress
- handle event failures
- continue processing after event-level failures
- generate final run summary

The Run-Level Controller answers:

```text
Which events need to be processed?
What is the current event?
Did the event succeed or fail?
Should the engine continue?
What happened during the full run?
```

The Run-Level Controller should not contain the analytical logic for returns, abnormal returns, or CAR.

Its job is orchestration.

## 4. Single-Event Processor

The Single-Event Processor handles one event at a time.

Responsibilities:

- receive one event
- validate event
- load market data
- calculate returns
- calculate abnormal returns
- calculate CAR
- generate outputs

This component should remain similar to the current V1 engine.

In V1, the whole engine behaves like a single-event processor.

In V2, that single-event workflow should become the repeatable unit inside the batch loop.

The Single-Event Processor answers:

```text
Can this event be analyzed?
What are its returns?
What is its abnormal return?
What is its CAR?
What event-window data should be saved?
What figure and report should be generated?
```

## 5. Output Manager

The Output Manager controls how outputs are written and organized.

Responsibilities:

- append rows to `event_results.csv`
- save event-specific window data
- save event-specific figures
- save event-specific reports

The Output Manager should prevent overwriting event-specific outputs.

Recommended output structure:

```text
results/event_results.csv
results/event_windows/{event_id}_event_window_data.csv
figures/{event_id}_abnormal_returns.png
reports/{event_id}_report.md
```

The Output Manager answers:

```text
Where should this event's outputs go?
How does this event get represented in the master results table?
Did the figure and report get created?
What output paths should be recorded?
```

## 6. Failure Recording Design

V2 should record the processing status of every event.

Recommended status values:

```text
success
failed
skipped
```

Current implementation uses `success` and `failed`. `skipped` is reserved for a future input-filtering phase.

### success

Use `success` when the event completes the full workflow.

Expected outputs:

- event-level result row
- event-window data file
- figure
- report

### failed

Use `failed` when the engine attempts to process the event but cannot complete it.

Examples:

- missing asset column
- missing benchmark column
- event date outside market data
- empty event window
- calculation error
- output generation error

Failed events should still appear in the master results table.

### skipped

Use `skipped` when the event is intentionally not processed.

Examples:

- event marked inactive in a future input schema
- event excluded from current run
- event belongs to an unsupported asset or benchmark group

Skipped events should appear in the master results table if they were present in the input file and intentionally bypassed.

## 7. Where Status Should Be Stored

Status should be stored in:

```text
results/event_results.csv
```

Recommended status-related fields:

```text
status
error_message
```

This makes `event_results.csv` both an analytics output and a run audit table.

Current implementation note: generated output paths are visible in the per-event reports and run summary, while richer path columns in `event_results.csv` are reserved for a future dashboard-readiness enhancement.

For failed or skipped events, unavailable output paths should be blank and the reason should be recorded in `validation_notes` or `error_message`.

## 8. Execution Sequence

Recommended V2 execution sequence:

```text
Load Events

FOR EACH EVENT

    Run Single Event Processor

    IF Success
        Save Outputs

    IF Failure
        Record Failure

Continue

Generate Run Summary
```

Expanded sequence:

```text
start run
↓
load events.csv
↓
load or verify market data
↓
initialize master results list
↓
for each event:
    print progress message
    validate event
    process event
    save event outputs if successful
    record status row
    continue to next event
↓
write final event_results.csv
↓
write final run_summary.md
↓
print final run summary path
```

The loop should continue after event-level failures.

Only run-level failures should stop the run.

## 9. Future Scaling

This architecture supports future scaling because it separates responsibilities.

### 100+ Events

For 100+ events, the Run-Level Controller can track progress, count successes and failures, and avoid stopping the batch because of one problematic event.

The Single-Event Processor remains reusable because it only needs to understand one event at a time.

The Output Manager keeps event files organized and prevents overwriting.

### Dashboard Integration

Dashboards need structured, predictable outputs.

The master results table can become the dashboard data source.

Per-event files can support drill-down views.

Example dashboard flow:

```text
event_results.csv
↓
dashboard summary table
↓
select event
↓
open event-window data, figure, and report
```

### Agent Orchestration

Future agents can use the same layers:

- Run-Level Controller: decides which events to process
- Single-Event Processor: analyzes one event
- Output Manager: records outputs for later review

An agent could inspect failed events, summarize reports, or recommend which event windows need analyst review.

### Automated Research Workflows

This design supports automated research workflows because each event becomes a repeatable unit of analysis.

The engine can eventually support:

- batch event-study runs
- recurring event updates
- comparison across mechanisms
- automated report generation
- analyst review queues
- research portfolio summaries

## 10. Design Principle

The most important V2 principle is:

```text
batch coordination should be separate from single-event analysis
```

The engine should not become one large script that mixes iteration, calculations, file writing, and reporting.

V2 should preserve clean boundaries:

```text
Run-Level Controller = orchestration
Single-Event Processor = analysis
Output Manager = persistence and artifacts
```

This keeps the engine easier to validate, easier to scale, and easier to connect to future dashboards or agent workflows.
