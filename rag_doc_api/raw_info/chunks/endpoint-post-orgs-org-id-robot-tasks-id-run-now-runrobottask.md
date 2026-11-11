---
id: endpoint-post-orgs-org-id-robot-tasks-id-run-now-runrobottask
title: "Robot tasks: Run a robot task"
tags: [endpoint, robot-tasks]
source: openapi.json (HighBond API v1.1.0)
---

## Robot tasks

When you create a task, a robot runs the task according to the settings that you configure. A task can be scheduled or run ad hoc (manually).
Each task has its own unique settings.

Learn more about tasks.

### `POST /orgs/{org_id}/robot_tasks/{id}/run_now` — Run a robot task

- **operationId:** `runRobotTask`
- **Domínio(s):** Robot Tasks

Run a robot task. This creates a robot job

<details>
<summary><strong>Parâmetros</strong> (3)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `id` | path | ✅ | string | The ID of the requested resource. Ex.: `9999` |
| `include` | query |  | string | To return child objects of the job. Example ?include=job_values,result_tables |

</details>

<details>
<summary><strong>Respostas</strong> (6)</summary>

<details>
<summary>`200` — OK.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `GetRunRobotTaskResponse`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | object |  | The data associated with the resource. |
| `data.id` | string | ✅ | The ID of the job. Ex.: `1` |
| `data.type` | string | ✅ | The classification of the object (`"robot_jobs"`). Ex.: `"robot_jobs"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.app_version` | integer |  | The version of the script. Ex.: `1` |
| `data.attributes.completed_at` | string |  | The date the job was completed. Ex.: `"2019-03-21T20:22:48.282Z"` |
| `data.attributes.count` | integer |  | The folder name that is automatically created in the Robots Agent. The folder corresponds to an individual job. Ex.: `1` |
| `data.attributes.delete_failed` | boolean |  | Indicate if the job failed to be deleted. Ex.: `"2019-03-21T20:22:48.282Z"` |
| `data.attributes.environment` | string |  | The environment of the script. Valores: `production`, `development` |
| `data.attributes.queued_at` | string |  | The date the job was queued to execute. Ex.: `"2019-03-21T20:22:48.282Z"` |
| `data.attributes.result_analytics` | array[string] |  | Includes information of the analytic results. |
| `data.attributes.status` | string |  | The status of the job. Valores: `success`, `failed`, `cancelled`, `queued`, `running`, `skipped` |
| `data.attributes.trigger_type` | string |  | The trigger type of the job. Valores: `schedule`, `manual`, `event` |
| `data.relationships` | object |  | List of associated objects with the robot job. |
| `data.relationships.robot` | object |  | Associated robot with the job. |
| `data.relationships.robot.data` | object | ✅ |  |
| `data.relationships.robot.data.id` | string | ✅ | The ID of the robot. |
| `data.relationships.robot.data.type` | string | ✅ | The classification of the object (`"robot"`). |
| `data.relationships.task` | object |  | Associated task with the job. |
| `data.relationships.task.data` | object | ✅ |  |
| `data.relationships.task.data.id` | string | ✅ | The ID of the task. |
| `data.relationships.task.data.type` | string | ✅ | The classification of the object (`"task"`). |
| `data.relationships.triggered_by` | object |  | User who triggered the job. |
| `data.relationships.triggered_by.data` | object | ✅ |  |
| `data.relationships.triggered_by.data.id` | string | ✅ | The ID of the user. |
| `data.relationships.triggered_by.data.type` | string | ✅ | The classification of the object (`"user"`). |

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
