# V2 Refactor Plan

> Academic Research Notice:
> This document is provided for educational and research reference purposes only.
> It may contain preliminary analysis, working assumptions, draft frameworks, or evolving interpretations.
> It should not be treated as a peer-reviewed publication.

## 1. Purpose

This document translates the V2 architecture into a safe implementation plan before changing code.

Implementation status: the core V2 refactor described in this plan has been completed. The engine now processes all rows in `events/events.csv`, writes event-specific window data, records event-level status, continues after event-level failures, and writes `results/run_summary.md`.

The current architectural decision is:

```text
separate batch coordination from single-event analysis
```

The goal is to move from V1 single-event processing to V2 multi-event processing without rewriting the engine all at once.

## 2. Current V1 Implementation Structure

The current main engine file is:

```text
scripts/run_event_study.py
```

It currently acts as both:

- the workflow conductor
- the single-event processor

Its current responsibilities appear to be:

- read the first event from `events/events.csv`
- extract event metadata
- load market data for the selected asset and benchmark
- calculate returns
- calculate abnormal returns
- calculate CAR
- save event-level results
- save event-window data
- generate one figure
- generate one report
- print progress messages

The current V1 flow is:

```text
read_first_event()
↓
load_market_data()
↓
calculate_returns()
↓
calculate_abnormal_returns()
↓
calculate_car()
↓
save_event_results()
↓
generate_event_figure()
↓
generate_event_report()
```

The project already has useful single-purpose modules:

```text
scripts/data_loader.py
scripts/returns_calculator.py
scripts/abnormal_returns.py
scripts/car_calculator.py
scripts/results_writer.py
scripts/figure_generator.py
scripts/report_generator.py
```

These modules should be preserved and reused where possible.

## 3. Current Input and Output State

Current V2 input:

```text
events/events.csv
```

This file now contains four events:

- E001 Pelosi Visit
- E002 Joint Sword 2023
- E003 Joint Sword 2024A
- E004 NVIDIA Taiwan AI Factory

Current output folders:

```text
results/
reports/
figures/
```

Current V2 generated outputs:

```text
results/event_results.csv
results/event_windows/{event_id}_event_window_data.csv
results/run_summary.md
figures/E001_abnormal_returns.png
reports/E001_report.md
```

Important observation:

- `figure_generator.py` already uses event-specific figure paths.
- `report_generator.py` already uses event-specific report paths.
- `results_writer.py` writes one master `results/event_results.csv`.
- `results_writer.py` writes event-specific window files in `results/event_windows/`.
- `results_writer.py` writes a batch-level `results/run_summary.md`.

The old V1 file `results/event_window_data.csv` is deprecated and should not be treated as the active V2 event-window output.

## 4. Single-Event Processor Logic to Preserve

The following current logic should remain part of the Single-Event Processor.

It represents the repeatable unit of work for one event:

- loading one event
- extracting event metadata
- selecting asset and benchmark
- loading market data
- calculating returns
- calculating abnormal returns
- calculating CAR
- generating one event result
- generating one figure
- generating one report

Conceptually, the current V1 engine already proves this path.

The first implementation pass should preserve this behavior while making it callable for each event.

## 5. New Run-Level Controller Logic Needed

V2 needs a Run-Level Controller that manages the full batch.

New responsibilities:

- load all events from `events/events.csv`
- iterate through events
- call the Single-Event Processor for each event
- collect success records
- collect failure records
- continue after event-level failures
- write final master results
- print final run summary

The Run-Level Controller should answer:

```text
How many events were loaded?
Which event is currently processing?
Did the event succeed, fail, or get skipped?
How many events completed?
Where is the final master results file?
```

The Run-Level Controller should not contain CAR formula logic.

## 6. New Output Manager Responsibilities Needed

V2 needs clearer Output Manager responsibilities.

Required output responsibilities:

- write `results/event_results.csv`
- write event-specific window data
- write `figures/{event_id}_abnormal_returns.png`
- write `reports/{event_id}_report.md`
- possibly create `results/event_windows/`

Recommended V2 output structure:

```text
results/event_results.csv
results/event_windows/{event_id}_event_window_data.csv
figures/{event_id}_abnormal_returns.png
reports/{event_id}_report.md
```

The Output Manager should also return paths so the master results table can store them.

Recommended master result path fields:

```text
event_window_data_path
figure_path
report_path
```

The Output Manager should avoid overwriting event-specific files.

## 7. Minimal-Risk Refactor Sequence

The safest path is to refactor in small stages.

### A. Preserve Current Single-Event Behavior

Before changing batch behavior, preserve the current V1 workflow as a known-good path.

Goal:

```text
one event can still be processed end to end
```

This prevents the V2 refactor from breaking the working engine immediately.

### B. Extract or Clearly Separate Single-Event Processing

Create a clear single-event processing boundary.

The logic currently inside `main()` should become conceptually separable:

```text
process_one_event(event)
```

This unit should return:

- event result row
- event-window data path
- figure path
- report path
- status
- validation notes

The exact implementation can be decided later, but the boundary should be explicit.

### C. Add Loop Over Events

After the single-event boundary is clear, add run-level iteration:

```text
read all events
for each event:
    process one event
```

At this stage, the engine should print progress for each event.

### D. Add Per-Event Output Paths

Update output writing so event-window data does not overwrite itself.

Recommended change:

```text
results/event_window_data.csv
↓
results/event_windows/{event_id}_event_window_data.csv
```

Figures and reports already use event-specific paths, so this stage should mainly focus on event-window data and master results.

### E. Add Failure Handling

Add event-level failure handling after the loop exists.

Failure behavior:

```text
event fails
↓
record failure row
↓
continue to next event
```

Do not let one bad event stop the whole batch unless the failure is run-level.

### F. Validate Outputs Against the V2 Design Documents

Compare the implemented outputs against:

- `docs/multi_event_engine_design.md`
- `docs/v2_output_schema.md`
- `docs/batch_processing_strategy.md`
- `docs/multi_event_workflow_map.md`
- `docs/multi_event_loop_design.md`

Validation questions:

- Does the engine process every event row?
- Does the master results table contain one row per event?
- Are event-specific outputs created?
- Are failure statuses recorded?
- Are metric definitions unchanged?
- Are output paths captured clearly?

## 8. Do Not Change Yet

The first implementation pass should not change analytical meaning.

Do not change yet:

- metric definitions
- CAR formula
- benchmark logic
- event schema
- return calculation method
- abnormal return calculation method
- market data contract
- existing working output types unless necessary
- report interpretation text
- figure design except for event-specific generation needs

Specifically, do not mix in the Raw CAR plus Abnormal CAR enhancement during the first V2 loop refactor.

That should remain a separate metric enhancement after the multi-event workflow is stable.

## 9. Acceptance Criteria

After the V2 refactor is implemented, the following must be true:

- engine processes all rows in `events/events.csv`
- `results/event_results.csv` has one row per event
- each successful event has a report
- each successful event has a figure
- each successful event has event-window data
- failures are recorded without stopping the whole run
- existing single-event behavior remains understandable
- output paths are included in the master results table
- event-level status is visible
- no event-specific output is accidentally overwritten by another event

The engine should be able to process the current four-event test file:

```text
E001 Pelosi Visit
E002 Joint Sword 2023
E003 Joint Sword 2024A
E004 NVIDIA Taiwan AI Factory
```

and produce a coherent batch output.

Current status: this acceptance criterion is met for the valid four-event input.

## 10. Safest First Implementation Step

The safest first implementation step is to preserve the V1 behavior while extracting the existing event-processing sequence into a clearly named single-event processing boundary.

This should happen before adding the event loop.

Reason:

```text
if one-event processing remains stable,
then multi-event processing can safely repeat it
```

This reduces risk because the engine's analytical behavior stays unchanged while the workflow architecture becomes more modular.
