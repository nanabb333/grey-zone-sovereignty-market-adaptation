# Input Schema

> Academic Research Notice:
> This document is provided for educational and research reference purposes only.
> It may contain preliminary analysis, working assumptions, draft frameworks, or evolving interpretations.
> It should not be treated as a peer-reviewed publication.

## 1. Purpose

events/events.csv defines the event-level inputs for the Taiwan Geopolitical Risk Event Study Engine.

Each row represents one geopolitical event to be analyzed by the engine.

## 2. Schema

| Column | Meaning | Example | Required |
|---|---|---|---|
| event_id | Unique event identifier | E001 | Yes |
| event_name | Name of the geopolitical event | Pelosi Visit | Yes |
| event_date | Main event date in YYYY-MM-DD format | 2022-08-02 | Yes |
| mechanism | Theoretical mechanism from Repo 1 | Risk | Yes |
| event_type | More specific event category | Diplomatic Shock | Yes |
| asset | Asset being analyzed | TSMC | Yes |
| benchmark | Benchmark used for abnormal returns | SOX | Yes |
| event_window_start | Start of CAR window relative to event date | -7 | Yes |
| event_window_end | End of CAR window relative to event date | 7 | Yes |

## 3. Example Row

```csv
E001,Pelosi Visit,2022-08-02,Risk,Diplomatic Shock,TSMC,SOX,-7,7
```
