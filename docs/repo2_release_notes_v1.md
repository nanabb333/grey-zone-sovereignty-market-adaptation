# Repo 2 Release Notes - V1

> Academic Research Notice:
> This document is provided for educational and research reference purposes only.
> It may contain preliminary analysis, working assumptions, draft frameworks, or evolving interpretations.
> It should not be treated as a peer-reviewed publication.

## Release Date

2026-06-08

## Project

Taiwan Geopolitical Risk Event Study Engine

## Major Features

* Standardized event input layer
* Market data loader
* Return calculation
* Abnormal return calculation
* CAR calculation
* Event-level CSV output
* Event-window CSV output
* Figure generation
* Markdown report generation

## Validation Findings

Repo 1 and Repo 2 initially produced different Pelosi Visit results.

Investigation showed that:

* Repo 1 reported raw cumulative returns.
* Repo 2 reported benchmark-adjusted abnormal CAR.

This was a metric-definition difference rather than a calculation error.

## Outputs Generated

* results/event_results.csv
* results/event_window_data.csv
* figures/E001_abnormal_returns.png
* reports/E001_report.md

## Lessons Learned

* Workflow design
* Automation architecture
* Validation methodology
* Research-to-product transformation

## Next Release

V2 Multi-Event Engine
