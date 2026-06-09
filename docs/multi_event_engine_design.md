# Multi-Event Engine Design

> Academic Research Notice:
> This document is provided for educational and research reference purposes only.
> It may contain preliminary analysis, working assumptions, draft frameworks, or evolving interpretations.
> It should not be treated as a peer-reviewed publication.

## 1. Current V1 Architecture

Repo 2 V1 is a single-event analytics engine.

The current workflow is:

```text
events/events.csv
↓
scripts/run_event_study.py
↓
read first event
↓
load market data
↓
calculate returns
↓
calculate abnormal returns
↓
calculate CAR
↓
save event-level result
↓
save event-window data
↓
generate one figure
↓
generate one report
```

V1 proves that the full event-study workflow can run automatically for one event.

Current V1 outputs:

```text
results/event_results.csv
results/event_window_data.csv
figures/E001_abnormal_returns.png
reports/E001_report.md
```

The V1 conductor, `scripts/run_event_study.py`, coordinates the workflow. The analytical logic lives in separate modules:

- `data_loader.py`
- `returns_calculator.py`
- `abnormal_returns.py`
- `car_calculator.py`
- `results_writer.py`
- `figure_generator.py`
- `report_generator.py`

This separation should remain in V2.

## 2. Desired V2 Architecture

Repo 2 V2 should become a multi-event analytics engine.

The target workflow is:

```text
events/events.csv
↓
scripts/run_event_study.py
↓
read all events
↓
load market data once
↓
loop through each event
↓
calculate event-specific CAR
↓
save combined event-level results
↓
save one event-window data file per event
↓
generate one figure per event
↓
generate one report per event
```

The key V2 design change is:

```text
V1 = process first event
V2 = process every event row
```

The conductor should manage the loop. The existing modules should continue to perform focused tasks.

## 3. Required Workflow Changes

V2 requires these workflow changes:

1. Read all events

The engine should read every row in `events/events.csv`, not only the first row.

2. Load market data once

Market data should be loaded once at the beginning of the run when possible. This avoids repeatedly reading the same file for each event.

3. Process each event independently

For each event, the engine should:

- extract event metadata
- identify asset and benchmark
- calculate or select returns for that asset-benchmark pair
- calculate abnormal returns
- calculate CAR
- extract event-window data
- save event-window output
- generate figure
- generate report

4. Accumulate event-level results

Instead of overwriting `results/event_results.csv` for each event, V2 should collect all event-level results and write one combined results file.

5. Use event-specific file names

Event-window data, figures, and reports should include the event ID in the file name.

Example:

```text
results/event_windows/E001_event_window_data.csv
figures/E001_abnormal_returns.png
reports/E001_report.md
```

6. Print a run summary

The terminal output should summarize:

- number of events loaded
- number of events processed successfully
- number of events skipped or failed
- output paths

## 4. Required Output Changes

V2 should generate both combined and event-specific outputs.

Combined output:

```text
results/event_results.csv
```

This file should contain one row per event.

Recommended columns:

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
event_window_data_path
figure_path
report_path
status
notes
```

Event-specific outputs:

```text
results/event_windows/{event_id}_event_window_data.csv
figures/{event_id}_abnormal_returns.png
reports/{event_id}_report.md
```

The event-window data files should include:

```text
date
asset_return
benchmark_return
abnormal_return
```

Future V2.1 or V3 outputs may include:

```text
raw_car
abnormal_car
cumulative_asset_return
cumulative_abnormal_return
```

## 5. Validation Considerations

V2 validation should compare each event against known Repo 1 outputs where available.

Important validation questions:

1. Does the engine use the same event date as Repo 1?
2. Does the engine use the same asset and benchmark?
3. Does the engine use the same event-window rule?
4. Does the engine use raw returns or benchmark-adjusted abnormal returns?
5. Are outputs stored in decimals or percentage points?
6. Does each event window contain the expected trading days?
7. Are events on non-trading days matched correctly?

The Pelosi Visit validation showed that metric definitions matter. Repo 2 should clearly distinguish:

- raw CAR
- benchmark-adjusted abnormal CAR

For V2, the default event-study metric can remain abnormal CAR. However, the output design should prepare for adding raw CAR as a separate metric.

Validation should also include a per-event status field.

Example status values:

```text
success
missing_asset_column
missing_benchmark_column
event_date_out_of_range
empty_event_window
insufficient_data
```

## 6. Risks and Edge Cases

1. Missing asset or benchmark columns

An event may request an asset or benchmark that does not exist in `data/market_data.csv`.

2. Non-trading-day event dates

Some events may occur on weekends or holidays. V2 needs a clear rule for matching those dates to market data.

Possible rules:

- use the next available trading day
- use the previous available trading day
- skip the event and flag it for review

Repo 1 often used the next available trading day.

3. Event windows with too few trading days

An event near the beginning or end of the market dataset may not have enough observations before or after the event date.

4. Overlapping events

Multiple geopolitical events may occur close together. Their event windows may overlap, making interpretation harder.

The engine can still calculate outputs, but reports should eventually flag overlapping windows.

5. Output overwriting

If each event writes to the same event-window file, later events will overwrite earlier outputs. V2 should use event-specific file names.

6. Inconsistent units

Repo 1 includes some outputs in percentage points and Repo 2 currently uses decimal returns. V2 should label units clearly.

7. Mixed metric definitions

Raw CAR and abnormal CAR should not be mixed under a single ambiguous `car_value` label in future versions.

8. Partial failures

One failed event should not stop the entire multi-event run. V2 should continue processing remaining events and record the failed event status.

## 7. Design Principle

The V2 conductor should coordinate the batch workflow, not absorb analytical logic.

The preferred architecture is:

```text
modules do the calculations
conductor manages the sequence
results writer records the outputs
reports summarize the event
```

This keeps Repo 2 aligned with its purpose: transforming a manual research workflow into a reusable analytics engine.
