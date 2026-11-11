---
id: endpoint-get-orgs-org-id-robot-tasks-robot-task-id-schedule-getschedule
title: "Robot tasks: Get a robot task's schedule"
tags: [endpoint, robot-tasks]
source: openapi.json (HighBond API v1.1.0)
---

## Robot tasks

When you create a task, a robot runs the task according to the settings that you configure. A task can be scheduled or run ad hoc (manually).
Each task has its own unique settings.

Learn more about tasks.

### `GET /orgs/{org_id}/robot_tasks/{robot_task_id}/schedule` — Get a robot task's schedule

- **operationId:** `getSchedule`
- **Domínio(s):** Robot Tasks

See when a task is scheduled to run and additional information, like time zone and its last run date.

<details>
<summary><strong>Parâmetros</strong> (2)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `robot_task_id` | path | ✅ | string | The ID of the robot task. Ex.: `2` |

</details>

<details>
<summary><strong>Respostas</strong> (6)</summary>

<details>
<summary>`200` — OK.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `GetRobotTaskScheduleResponse`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | RobotTaskSchedule | ✅ |  |
| `data.id` | string | ✅ | The ID of the task. Ex.: `1` |
| `data.type` | string | ✅ | The classification of the object (`"schedule"`). Ex.: `"schedule"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.frequency` | string |  | The interval at which the task is repeatedly run. Valores: `once`, `hourly`, `daily`, `weekly`, `monthly` Ex.: `"weekly"` |
| `data.attributes.interval` | integer |  | The interval in minutes between runs. To safeguard the HighBond API against bursts of usage, there is a minimum interval of 10 minutes between runs. |
| `data.attributes.starts_at` | string |  | The time of day to start running the task. Ex.: `"2019-03-21T16:25:00.478Z"` |
| `data.attributes.starts_at_timezone` | string |  | The timezone used to start running the task. Ex.: `"America/Los_Angeles"` |
| `data.attributes.last_run_at` | string |  | The time when robot task was last run at. |
| `data.attributes.next_run_at` | string |  | The time when robot task will next run at. |
| `data.attributes.settings` | object | ✅ | The settings associated with the resource. |
| `data.attributes.settings.days` | array[integer] |  | The days that the task is scheduled to run. If the task is scheduled to run on a weekly frequency, `days` are represented from `0` to `6`, where `0` represents Sunday and `6` represents Saturday. If the task is scheduled to run on a monthly frequency, `days` is represented as a number between `1` and `28` or specified as `last_day`. `days` does not return anything for once, hourly, and daily frequencies. Ex.: `[0, 1, 2]` |

</details>

<details>
<summary>`400` — Bad request.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `Errors`

Erro no formato padrão JSON:API: objeto `errors` (array) com `status` (código HTTP), `source.pointer` (JSON Pointer RFC6901 do campo com erro), `code`, `title` e `detail`.

</details>

- `401` — Bad credentials.

- `403` — Forbidden.

- `404` — Not found.

<details>
<summary>`415` — Unsupported media type.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `Errors`

Erro no formato padrão JSON:API: objeto `errors` (array) com `status` (código HTTP), `source.pointer` (JSON Pointer RFC6901 do campo com erro), `code`, `title` e `detail`.

</details>

</details>
