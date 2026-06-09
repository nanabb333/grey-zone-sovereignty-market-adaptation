# Single Event Engine Specification

> Academic Research Notice:
> This document is provided for educational and research reference purposes only.
> It may contain preliminary analysis, working assumptions, draft frameworks, or evolving interpretations.
> It should not be treated as a peer-reviewed publication.

## Purpose

The first version of the Taiwan Geopolitical Risk Event Study Engine should process one event from start to finish.

The goal is not scalability.

The goal is to prove that the workflow can be executed automatically.

---

## Input

Source:

events/events.csv

Example:

E001,Pelosi Visit,2022-08-02,Risk,Diplomatic Shock,TSMC,SOX,-7,7

---

## Workflow

Step 1

Read event metadata.

Outputs:

* event_name
* event_date
* asset
* benchmark
* event window

---

Step 2

Load required market data.

Example:

* TSMC
* SOX

Outputs:

aligned price dataset

---

Step 3

Calculate daily returns.

Outputs:

daily return series

---

Step 4

Calculate abnormal returns.

Outputs:

abnormal return series

---

Step 5

Calculate CAR.

Outputs:

event-level CAR metric

---

Step 6

Save results.

Outputs:

results/event_results.csv

---

Step 7

Generate figure.

Outputs:

figures/pelosi_visit_event_chart.png

---

Step 8

Generate report.

Outputs:

reports/pelosi_visit_report.md

---

## Success Criteria

The engine should be able to process one event and automatically produce:

1. Event-level CAR
2. Results table
3. Figure
4. Report

without manual calculation.

---

## Non-Goals

Version 1 does not need:

* multiple events
* AI classification
* agent behavior
* automated event discovery

These features belong to future phases.
