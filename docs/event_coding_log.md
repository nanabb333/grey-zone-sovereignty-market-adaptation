# Event Coding Log

> Academic Research Notice:
> This document is provided for educational and research reference purposes only.
> It records transparent qualitative coding decisions for dissertation revision.

## Purpose

This log documents the coding decisions used to create `data/events_v2.csv`. The upgrade adds four fields to the existing master event sample:

- `surprise_score`
- `surprise_rationale`
- `event_family`
- `event_repetition_level`

The coding is interpretive and transparent. It does not add new events, new event-study calculations, forecasting, or causal claims.

## Master Dataset

The current master event dataset for this upgrade is:

```text
data/events/event_sample.csv
```

The upgraded dataset is:

```text
data/events_v2.csv
```

## Coding Scale

### Surprise Score

| Score | Meaning |
| --- | --- |
| High | Event timing, occurrence, scale, or market relevance was not clearly expected before Day 0. |
| Medium | Event was plausible or partially discussed, but important uncertainty remained. |
| Low | Event was widely anticipated, scheduled, or part of an established repeated pattern. |

### Event Repetition Level

| Level | Meaning |
| --- | --- |
| 1 | First or novel event in the sample. |
| 2 | Similar prior event exists, but the pattern is not yet routinized. |
| 3 | Repeated event family with a recognizable market or policy pattern. |
| 4 | Highly repeated or expected grey-zone signaling pattern. |

## Event-Level Coding Log

| Event | Surprise Assignment | Event Family Assignment | Repetition Assignment |
| --- | --- | --- | --- |
| China Warns Against Pelosi Taiwan Visit | Medium: the visit was already publicly discussed, but the warning clarified PRC escalation risk. | `Diplomatic_Shock`: the event is a diplomatic warning tied to a high-level Taiwan visit. | 1: early diplomatic escalation case in the sample. |
| Pelosi Visit | High: the visit was discussed, but occurrence and PRC response remained uncertain. | `Diplomatic_Shock`: the event centers on a high-level U.S. political visit to Taiwan. | 1: first major diplomatic shock in the sample period. |
| China Trade Restrictions After Pelosi Visit | Medium: retaliation was plausible, but the specific trade restrictions were not fully known. | `Economic_Coercion`: the event uses trade restrictions as political pressure. | 1: first economic-coercion case in the event sample. |
| PLA Military Exercises After Pelosi Visit | Medium: military retaliation was expected, but scale and operational intensity still mattered. | `Military_Exercise`: the event is a PLA exercise and military demonstration around Taiwan. | 1: first major military-exercise case in the sample period. |
| BIS Advanced Semiconductor Export Controls | Medium: technology controls were foreseeable, but the scope of the rules added new information. | `Export_Control`: the event is a U.S. technology-control policy shock. | 1: first export-control case in the sample. |
| TSMC Arizona US$40B Expansion | Medium: Arizona investment was known, but the expanded scale changed strategic interpretation. | `Strategic_Investment`: the event reinforces Taiwan's semiconductor importance through investment. | 1: first major strategic-investment case in the sample. |
| Joint Sword 2023 | Medium: a response to the Tsai-McCarthy meeting was plausible, but timing and scale were uncertain. | `Military_Exercise`: the event is part of PLA military signaling around Taiwan. | 2: similar military exercises occurred after the Pelosi Visit, but the Joint Sword pattern was still emerging. |
| Lai U.S. Transit | Low: the transit was scheduled and publicly visible before the event. | `Diplomatic_Shock`: the event is a Taiwan-U.S. diplomatic transit. | 2: similar diplomatic-transit and visit-related tensions had occurred earlier in the sample. |
| PLA Drills After Lai U.S. Transit | Medium: a military response was foreseeable, but the timing and operational form still mattered. | `Military_Exercise`: the event is a PLA drill after a Taiwan-related diplomatic event. | 2: repeated military response pattern, but not yet fully routinized. |
| China Sends Aircraft and Vessels After U.S. Arms Sale | Low: PRC military signaling after arms-related developments fits a recurring pattern. | `Military_Exercise`: the event involves PLA aircraft and vessels around Taiwan. | 3: by this point, similar military signaling had become a recognizable pattern. |
| TSMC CHIPS Act Preliminary Terms | Medium: CHIPS Act support was expected, but terms with TSMC contained new detail. | `Strategic_Investment`: the event reinforces TSMC's role in allied semiconductor policy. | 2: follows earlier TSMC investment announcements but still contains new policy detail. |
| Lai Ching-te Inauguration | Low: the inauguration date was scheduled and highly visible. | `Political_Signaling`: the event is a political transition with cross-strait signaling implications. | 1: first presidential inauguration case in the event sample. |
| Joint Sword-2024A | Medium: a PRC response after Lai's inauguration was plausible, but operational timing and form mattered. | `Military_Exercise`: the event is a Joint Sword military exercise. | 3: repeated Joint Sword-style military signaling with a recognizable pattern. |
| PRC Judicial Guidelines on Taiwan Independence | Medium: legal pressure was consistent with PRC signaling, but formal guidelines added specific legal content. | `Legal_Judicial_Signaling`: the event uses legal language to signal political pressure. | 1: first legal-judicial signaling case in the sample. |
| Joint Sword-2024B | Low: the event fit an increasingly recognizable Joint Sword pattern. | `Military_Exercise`: the event is a repeated PLA military demonstration around Taiwan. | 4: highly repeated event family by this point in the sample. |
| PLA Joint Combat Readiness Patrols Around Taiwan | Low: patrols around Taiwan had become part of a recurring grey-zone pattern. | `Military_Exercise`: the event involves repeated PLA presence and patrol activity. | 4: highly repeated grey-zone military signaling. |
| TSMC US$165B U.S. Expansion | Medium: further investment was plausible, but the scale and framing added new information. | `Strategic_Investment`: the event reinforces Taiwan's strategic semiconductor role. | 3: later-stage strategic-investment event after earlier TSMC-U.S. investment cases. |
| Strait Thunder-2025A | Medium: military drills were repeated, but the name, scale, and simulated blockade content carried new information. | `Military_Exercise`: the event is a PLA military drill around Taiwan. | 4: highly repeated military-signaling family, though still event-specific in scale and content. |

## Interpretation Note

The coding intentionally separates event repetition from surprise. A repeated event can still be coded Medium surprise if its scale, timing, or operational details introduce new information. Conversely, a first-of-kind event may not always be High surprise if it was scheduled or heavily signaled before Day 0.

