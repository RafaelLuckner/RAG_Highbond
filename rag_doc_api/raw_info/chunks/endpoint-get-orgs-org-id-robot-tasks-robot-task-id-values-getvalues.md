---
id: endpoint-get-orgs-org-id-robot-tasks-robot-task-id-values-getvalues
title: "Robot tasks: List values in a robot task"
tags: [endpoint, robot-tasks]
source: openapi.json (HighBond API v1.1.0)
---

## Robot tasks

When you create a task, a robot runs the task according to the settings that you configure. A task can be scheduled or run ad hoc (manually).
Each task has its own unique settings.

Learn more about tasks.

### `GET /orgs/{org_id}/robot_tasks/{robot_task_id}/values` — List values in a robot task

- **operationId:** `getValues`
- **Domínio(s):** Robot Tasks

Get information about a robot's task, like its analytic name and data type.

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

**Schema:** `GetRobotTaskValuesResponse`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | array[RobotTaskValue] | ✅ | The data associated with the resource. |
| `data.id` | string | ✅ | The ID of the task. Ex.: `1` |
| `data.type` | string | ✅ | The classification of the object (`"values"`). Ex.: `"values"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.analytic_name` | string | ✅ | The name of the script, which is used as a parameter value. Ex.: `"Extended foreground project"` |
| `data.attributes.parameter_id` | string | ✅ | The identifier of the parameter. Ex.: `"v_time"` |
| `data.attributes.encrypted` | boolean | ✅ | If `true`, the script contains a `PASSWORD` analytic tag, which prompts the user for a password before running the analytic, and encrypts the entered value. The `PASSWORD` parameter is required in any command that imports from or exports to HighBond. |
| `data.attributes.data` | object | ✅ | The data associated with the resource. |
| `data.attributes.data.value` | RobotTaskRequestValue | ✅ |  |
| `data.attributes.data.value` | RobotTaskRequestValue |  | ↩ *referência recursiva — ver schema* `RobotTaskRequestValue` |
| `data.attributes.data.type` | string | ✅ | The data type of the value. Valores: `character`, `date`, `datetime`, `file`, `logical`, `number`, `table`, `time` |

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
