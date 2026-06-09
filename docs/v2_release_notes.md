# Repo 2 Release Notes - V2

> Academic Research Notice:
> This document is provided for educational and research reference purposes only.
> It may contain preliminary analysis, working assumptions, draft frameworks, or evolving interpretations.
> It should not be treated as a peer-reviewed publication.

## Release Date

2026-06-09

## Project

Taiwan Geopolitical Risk Event Study Engine

## V2 Status

V2 multi-event batch processing is implemented.

The engine now processes every row in `events/events.csv`, generates per-event outputs, records event-level status, continues after event-level failures, and writes a run-level summary.

## V2 Features Completed

- Multi-event batch loop in `scripts/run_event_study.py`
- Clear `process_one_event(event)` single-event processing boundary
- Run-level controller that iterates through all events
- Master event results table with one row per event
- Event-level `status` and `error_message` fields
- Basic event-level failure handling
- Per-event event-window CSV outputs
- Per-event abnormal return figures
- Per-event Markdown reports
- Batch-level `results/run_summary.md`
- Portfolio-level `results/mechanism_summary.csv`

## Files Modified

Core engine files:

- `scripts/run_event_study.py`
- `scripts/results_writer.py`

Input and generated output files:

- `events/events.csv`
- `results/event_results.csv`
- `results/event_windows/{event_id}_event_window_data.csv`
- `figures/{event_id}_abnormal_returns.png`
- `reports/{event_id}_report.md`
- `results/run_summary.md`
- `results/mechanism_summary.csv`

Documentation files:

- `README.md`
- `docs/v2_output_schema.md`
- `docs/multi_event_workflow_map.md`
- `docs/multi_event_loop_design.md`
- `docs/v2_refactor_plan.md`
- `docs/batch_processing_strategy.md`
- `docs/v2_release_notes.md`

## Output Architecture

V2 active outputs:

```text
results/event_results.csv
results/event_windows/{event_id}_event_window_data.csv
figures/{event_id}_abnormal_returns.png
reports/{event_id}_report.md
results/run_summary.md
results/mechanism_summary.csv
```

Deprecated V1 output:

```text
results/event_window_data.csv
```

The V2 active event-window output is now:

```text
results/event_windows/{event_id}_event_window_data.csv
```

## Current Result Schema

`results/event_results.csv` currently includes:

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

`car_value` is benchmark-adjusted abnormal CAR under the current engine definition.

## Validation and Smoke Test

The V2 smoke test command is:

```bash
MPLCONFIGDIR=/private/tmp/matplotlib-cache /Users/cjy/miniconda3/bin/python3 scripts/run_event_study.py
```

Expected valid-run result for the current input:

- 4 total events
- 4 successful events
- 0 failed events
- 4 event-window files
- 4 figures
- 4 reports
- 1 run summary
- 1 mechanism summary

## Known Limitations

- Raw CAR is not yet implemented as a separate output field.
- `car_value` currently means benchmark-adjusted abnormal CAR only.
- Event windows currently use the existing V1 CAR logic and have not yet been changed to trading-day indexing.
- `results/event_results.csv` does not yet include output path columns for reports, figures, or event-window files.
- Failure handling is basic and records `status` plus `error_message`.
- No complex logging framework has been added.
- No dashboard exists yet.
- No AI-assisted event classification exists yet.

## Next Possible Improvements

- Add `raw_car` and `abnormal_car` as separate output fields.
- Add output path columns to `results/event_results.csv`.
- Add matched trading date and event-window validation fields.
- Add richer validation labels such as `pass`, `review`, and `fail`.
- Add a batch report index.
- Expand dashboard-ready summary tables.
- Add AI-assisted event classification in a later phase.
