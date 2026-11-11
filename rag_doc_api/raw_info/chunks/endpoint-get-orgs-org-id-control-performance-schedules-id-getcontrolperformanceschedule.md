---
id: endpoint-get-orgs-org-id-control-performance-schedules-id-getcontrolperformanceschedule
title: "Control performance schedules: Get a control performance schedule"
tags: [endpoint, control-performance-schedules]
source: openapi.json (HighBond API v1.1.0)
---

## Control performance schedules

A control performance schedule is a schedule of control tests that are performed on a recurring basis. Control performance schedules are associated with controls.

> **Note:**
Control performance schedules located in such resources can be accessed using the API:
> * In projects that have an "active" state
> * In frameworks

Learn more about control performance schedules.

### `GET /orgs/{org_id}/control_performance_schedules/{id}` — Get a control performance schedule

- **operationId:** `getControlPerformanceSchedule`
- **Domínio(s):** Control performance schedules

Get information about a control performance schedule.

<details>
<summary><strong>Parâmetros</strong> (2)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `id` | path | ✅ | string | The ID of the requested resource. Ex.: `9999` |

</details>

<details>
<summary><strong>Respostas</strong> (4)</summary>

<details>
<summary>`200` — OK.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `GetControlPerformanceScheduleResponse`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | object |  | The data associated with the resource. |
| `data.id` | string | ✅ | The ID of the requested resource. Ex.: `"1"` |
| `data.type` | string | ✅ | The classification of the object (`"control_performance_schedules"`). Ex.: `"control_performance_schedules"` |
| `data.attributes` | object | ✅ | The attributes of the requested resource. |
| `data.attributes.title` | string |  | The title of the control performance schedule. Mandatory. Ex.: `"Control performance schedule 1"` |
| `data.attributes.sent` | boolean |  | Whether the control performance schedule has been sent. Ex.: `false` |
| `data.attributes.enabled` | boolean |  | Whether the control performance schedule is enabled. Ex.: `true` |
| `data.attributes.procedure` | string |  | The procedure of the control performance schedule. Ex.: `"<p>Control performance schedule 1 procedure</p>"` |
| `data.attributes.frequency_type` | string |  | The frequency type of the control performance schedule. Mandatory.  Values: "daily", "weekly", "monthly", "quarterly", "custom". Ex.: `"daily"` |
| `data.attributes.frequency_timezone_offset` | number |  | The frequency timezone offset of the control performance schedule. Mandatory. Ex.: `0` |
| `data.attributes.frequency_day_of_week` | integer |  | The frequency day of week of the control performance schedule.  Values: 0-6, null; 0 means first day of the week. Mandatory if frequency_type is "weekly". Ex.: `0` |
| `data.attributes.frequency_day_of_month` | integer |  | The frequency day of month of the control performance schedule. Values: 1-28,32, null. Mandatory if frequency_type is "monthly". Ex.: `null` |
| `data.attributes.frequency_starts_on` | string |  | The frequency starts on of the control performance schedule. Mandatory. Ex.: `"2019-01-01"` |
| `data.attributes.frequency_days` | integer |  | The frequency days of the control performance schedule. Mandatory if frequency_type is "custom". Ex.: `1` |
| `data.attributes.frequency_run_at` | string |  | The frequency run at of the control performance schedule in time format. Ex.: `"15:30:00"` |
| `data.attributes.frequency_local_run_at` | object |  | The frequency local run at of the control performance schedule. Mandatory. |
| `data.attributes.frequency_local_run_at.hour` | integer |  | Hour of the control performance schedule. Ex.: `0` |
| `data.attributes.frequency_local_run_at.minute` | integer |  | Minute of the control performance schedule. Ex.: `0` |
| `data.attributes.frequency_local_run_at.second` | integer |  | Second of the control performance schedule. Ex.: `0` |
| `data.attributes.frequency_local_run_at.second_of_day` | integer |  | Second of day of the control performance schedule. Ex.: `0` |
| `data.attributes.frequency_timezone` | string |  | The frequency timezone of the control performance schedule. Ex.: `"Central Time (US & Canada)"` |
| `data.attributes.results_questionnaire_id` | integer |  | The results questionnaire ID of the control performance schedule. Mandatory. Ex.: `1` |
| `data.attributes.performer_user_ids` | array[string] |  | The performer user UIDs of the control performance schedule.  Mandatory if performer_contact_emails is empty. Ex.: `["P2tuGWyTWxCAQgTd1XKx"]` |
| `data.attributes.performer_contact_emails` | array[string] |  | The performer contact emails of the control performance schedule. Mandatory if performer_user_ids is empty. Ex.: `["jhon.doe@example.com"]` |
| `data.attributes.created_at` | string |  | The date and time when the control performance schedule was created. Ex.: `"2019-01-01T00:00:00Z"` |
| `data.attributes.updated_at` | string |  | The date and time when the control performance schedule was last updated. Ex.: `"2019-01-01T00:00:00Z"` |
| `data.relationships` | object |  | The relationship between the control performance schedule and the control. |
| `data.relationships.control` | object |  |  |
| `data.relationships.control.data` | object |  |  |
| `data.relationships.control.data.id` | string |  | The ID of the control. Ex.: `"1"` |
| `data.relationships.control.data.type` | string |  | The classification of the object (`"controls"`). Ex.: `"controls"` |

</details>

- `401` — Bad credentials.

- `403` — Forbidden.

- `404` — Not found.

</details>
