# Taiwan Geopolitical Risk Event Study Engine - Run Summary

## Run-Level Counts

| Metric | Count |
|---|---:|
| Total events | 4 |
| Successful events | 4 |
| Failed events | 0 |

## Event Status

| event_id | event_name | mechanism | status | car_value | error_message |
|---|---|---|---|---:|---|
| E001 | Pelosi Visit | Risk | success | 0.0044332006595363 |  |
| E002 | Joint Sword 2023 | Risk | success | -0.0065243053328469 |  |
| E003 | Joint Sword 2024A | Risk | success | -0.0054448613183898 |  |
| E004 | NVIDIA Taiwan AI Factory | Strategic_Importance | success | -0.0176057315529649 |  |

## Output Locations

- results/event_results.csv
- results/mechanism_summary.csv
- results/dashboard_data.csv
- results/executive_summary.md
- results/event_windows/
- reports/
- figures/

## Notes

- `status=success` means the event was processed successfully.
- `status=failed` means the event failed but the batch continued.
- `car_value` is benchmark-adjusted abnormal CAR based on the current engine definition.
