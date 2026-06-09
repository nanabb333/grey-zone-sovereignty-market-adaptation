# Batch Processing Strategy

> Academic Research Notice:
> This document is provided for educational and research reference purposes only.
> It may contain preliminary analysis, working assumptions, draft frameworks, or evolving interpretations.
> It should not be treated as a peer-reviewed publication.

## 1. Purpose

V2 moves Repo 2 from single-event processing to multi-event processing.

Implementation status: core V2 batch processing is implemented. The engine reads all events, continues after event-level failures, writes per-event window files, writes per-event reports and figures, and writes `results/run_summary.md`.

Current V1 behavior:

```text
read first event only
process one event
generate one result row
generate one event-window file
generate one figure
generate one report
```

Target V2 behavior:

```text
read all events
process each event
generate combined event-level results
generate per-event outputs
record validation status
continue through the full batch
```

The goal is to make the engine useful for analytics comparison across events, not just one-off event analysis.

## 2. Event Iteration Strategy

V2 should read all rows from:

```text
events/events.csv
```

The conductor should then iterate through events one row at a time.

Recommended workflow:

```text
load event table
load market data once
initialize empty results list
for each event:
    extract event metadata
    validate required fields
    select asset and benchmark
    calculate returns
    calculate abnormal returns
    calculate abnormal CAR
    save event-window data
    generate event figure
    generate event report
    append event-level result row
save combined event_results.csv
print batch summary
```

The conductor should manage the sequence. Analytical modules should remain focused on their own tasks.

## 3. Per-Event Outputs

Each event should produce its own supporting files.

Recommended per-event outputs:

```text
results/event_windows/{event_id}_event_window_data.csv
figures/{event_id}_abnormal_returns.png
reports/{event_id}_report.md
```

Per-event files prevent overwriting and make it easy to inspect one event at a time.

Each event report should include:

- event metadata
- asset and benchmark
- event window
- CAR value
- validation notes
- links or paths to the event-window data and figure

Current implementation note: `car_value` is benchmark-adjusted abnormal CAR. Raw CAR is planned for a future metric enhancement.

## 4. Shared Outputs

The main shared output should be:

```text
results/event_results.csv
```

This file should contain one row per event.

It should support:

- comparison across events
- dashboard loading
- validation review
- future agent workflows

Recommended shared-output fields:

```text
event_id
event_name
event_date
mechanism
event_type
asset
benchmark
event_window_start
event_window_end
trading_days_in_window
car_value
status
error_message
```

Future output fields may add `raw_car`, `abnormal_car`, output paths, matched trading date, and richer validation labels.

The shared output is the portfolio-facing analytics table. The per-event files are the audit trail.

## 5. Error Handling Strategy

V2 should expect partial failures.

Examples:

- missing asset column
- missing benchmark column
- event date outside available market data
- event window has too few trading days
- non-trading-day event date needs matching
- figure generation fails
- report generation fails

Recommendation:

If one event fails, the entire engine should not stop.

The engine should continue processing remaining events and record the failed event in `results/event_results.csv`.

Recommended failed-event row fields:

```text
status = failed
validation_flag = fail
validation_notes = clear reason for failure
raw_car = blank
abnormal_car = blank
event_window_data_path = blank if not created
figure_path = blank if not created
report_path = blank if not created
```

This is important because multi-event processing is a batch analytics workflow. One bad event should not prevent the analyst from receiving outputs for all valid events.

## 6. Logging Strategy

V2 should use clear run-level and event-level logging.

Console output should show:

```text
Batch started
Events loaded: N
Market data loaded successfully
Processing E001 - Pelosi Visit
E001 success
Processing E002 - Joint Sword 2023
E002 success with validation warning
Processing E003 - Example Failed Event
E003 failed: missing benchmark column
Batch complete
Events processed successfully: X
Events needing review: Y
Events failed: Z
Combined results saved to results/event_results.csv
```

Future versions may also save a log file:

```text
logs/batch_run_log.txt
```

For V2, console logging plus status fields in `event_results.csv` may be enough.

## 7. Validation Strategy

Validation should happen at two levels:

1. Input validation
2. Output validation

Input validation should check:

- required event fields are present
- event date is valid
- asset column exists
- benchmark column exists
- event window values are numeric
- market data contains enough dates

Output validation should check:

- event-window data was created
- figure was created
- report was created
- car_value is not missing for successful events
- trading-day count matches expected window logic
- matched trading date is recorded

Recommended validation labels:

```text
pass
review
fail
```

Use `review` when the engine can still process the event but the analyst should inspect it.

Examples:

- event date was a weekend and matched to next trading day
- event window overlaps with another event
- event window has fewer trading rows than expected

Use `fail` when the event could not be processed.

Current implementation note: V2 currently uses `status` and `error_message`. Richer `validation_flag` values are planned for a future phase.

## 8. Stop or Continue Recommendation

The engine should continue processing remaining events if one event fails.

Recommended behavior:

```text
event fails
↓
record failure row
↓
print failure message
↓
continue to next event
↓
finish batch
↓
save combined results
```

Reason:

Repo 2 is an analytics engine, not a single script for one manual calculation. In a batch analytics workflow, partial output is valuable. The analyst can review successful events immediately and then fix failed events separately.

The only failures that should stop the entire engine are run-level failures.

Examples of run-level failures:

- `events/events.csv` is missing
- `data/market_data.csv` is missing
- market data cannot be loaded at all
- required global schema is invalid

Event-level failures should not stop the batch.

## 9. Design Principle

V2 should be resilient, auditable, and analyst-friendly.

The engine should:

- process all possible events
- clearly flag failed or review-needed events
- avoid silent failures
- avoid overwriting event-specific outputs
- produce a complete batch summary

This design supports analytics comparison, validation, future dashboards, and future AI-assisted workflows.
