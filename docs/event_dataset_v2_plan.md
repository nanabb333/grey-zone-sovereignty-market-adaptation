# Event Dataset V2 Plan

> Academic Research Notice:
> This document is provided for educational and research reference purposes only.
> It proposes dataset upgrades for dissertation revision and future replication.

## Purpose

The current event dataset supports an exploratory event study of Taiwan-related geopolitical and geoeconomic shocks. The next dataset version should make investor expectations more explicit by adding variables for surprise, event-family repetition, and coding rationale.

The purpose of this upgrade is to strengthen transparency. It does not require new event-study calculations and does not by itself establish causal identification.

## Proposed New Fields

| Field | Type | Description |
| --- | --- | --- |
| `surprise_score` | Categorical | High, Medium, or Low assessment of how unexpected the event was before Day 0. |
| `surprise_rationale` | Text | Brief explanation of the evidence used to code surprise. |
| `event_family` | Categorical | Groups related events, such as PLA exercise, diplomatic visit, export control, investment announcement, recognition switch, or judicial/legal signaling. |
| `event_repetition_level` | Ordinal or categorical | Captures whether the event is first-of-kind, repeated, or highly routinized within the sample period. |

## Suggested Coding Rules

### `surprise_score`

| Value | Meaning |
| --- | --- |
| High | Event timing, occurrence, scale, or market relevance was not clearly expected before Day 0. |
| Medium | Event was plausible or partially discussed, but important uncertainty remained. |
| Low | Event was widely anticipated, followed scheduled triggers, or fit an established repeated pattern. |

### `event_family`

Possible values:

- `Military_Exercise`
- `Diplomatic_Shock`
- `Economic_Coercion`
- `Export_Control`
- `Strategic_Investment`
- `Political_Signaling`
- `Legal_Judicial_Signaling`
- `Recognition_Diplomacy`

### `event_repetition_level`

Possible values:

| Value | Meaning |
| --- | --- |
| 1 | First or novel event in the sample. |
| 2 | Similar prior event exists, but pattern is not yet routinized. |
| 3 | Repeated event family with recognizable market and policy pattern. |
| 4 | Highly repeated or expected grey-zone signaling pattern. |

## Example Coding

| Event Name | Proposed `surprise_score` | Proposed `event_family` | Proposed `event_repetition_level` | Rationale |
| --- | --- | --- | ---: | --- |
| Pelosi Visit | High | Diplomatic_Shock | 1 | The visit was publicly discussed, but uncertainty remained over whether it would occur and how Beijing would respond. It introduced meaningful new information about escalation risk and diplomatic resolve. |
| Joint Sword 2023 | Medium | Military_Exercise | 2 | PLA military exercises after high-profile Taiwan-related diplomatic events were plausible, but the scale and market interpretation were still uncertain. |
| Joint Sword-2024A | Medium-Low | Military_Exercise | 3 | The event followed Lai's inauguration and occurred within a known pattern of PRC military signaling, but the specific timing and operational form still mattered. |
| Joint Sword-2024B | Low | Military_Exercise | 4 | The event fit a repeated Joint Sword pattern and may have been more easily interpreted as coercive signaling rather than immediate escalation. |
| TSMC CHIPS Act Preliminary Terms | Medium | Strategic_Investment | 2 | The policy direction was expected, but the details and market interpretation of the preliminary terms still contained relevant information. |

## Dataset Template

| event_date | event_name | mechanism | event_family | event_repetition_level | surprise_score | surprise_rationale | source_notes |
| --- | --- | --- | --- | ---: | --- | --- | --- |
| YYYY-MM-DD | Event name | Risk / Strategic_Importance | Category | 1-4 | High / Medium / Low | Coding explanation | Source references |

## Dissertation Value

Adding these fields would improve the dissertation in three ways:

1. It would make the adaptation claim more transparent.
2. It would directly address the anticipation/prior-pricing rival explanation.
3. It would allow the results chapter to distinguish event severity from event expectedness.

The upgraded dataset should be described as a qualitative coding enhancement to the exploratory event study, not as a fully causal identification strategy.

