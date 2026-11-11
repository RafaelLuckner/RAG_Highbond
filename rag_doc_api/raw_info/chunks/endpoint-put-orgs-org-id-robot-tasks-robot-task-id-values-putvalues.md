---
id: endpoint-put-orgs-org-id-robot-tasks-robot-task-id-values-putvalues
title: "Robot tasks: Update values in a robot task"
tags: [endpoint, robot-tasks]
source: openapi.json (HighBond API v1.1.0)
---

## Robot tasks

When you create a task, a robot runs the task according to the settings that you configure. A task can be scheduled or run ad hoc (manually).
Each task has its own unique settings.

Learn more about tasks.

### `PUT /orgs/{org_id}/robot_tasks/{robot_task_id}/values` — Update values in a robot task

- **operationId:** `putValues`
- **Domínio(s):** Robot Tasks

Change values for a robot task, like its analytic name.

<details>
<summary><strong>Parâmetros</strong> (2)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `robot_task_id` | path | ✅ | string | The ID of the robot task. Ex.: `2` |

</details>

<details>
<summary><strong>Request body (payload)</strong></summary>

The data required to create values.

**Body obrigatório.**

**Content-Type:** `application/vnd.api+json`

**Schema:** `UpdateRobotTaskValuesRequest`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | array[object] | ✅ | The data associated with the resource. |
| `data.type` | string |  | The classification of the object (`"values"`). Ex.: `"values"` |
| `data.attributes` | object |  | The attributes associated with the resource. |
| `data.attributes.analytic_name` | string | ✅ | The name of the script, which is used as a parameter value. Ex.: `"Extended foreground project"` |
| `data.attributes.parameter_id` | string | ✅ | The identifier of the parameter. Ex.: `"v_time"` |
| `data.attributes.encrypted` | boolean | ✅ | If `true`, the script contains a `PASSWORD` analytic tag, which prompts the user for a password before running the analytic, and encrypts the entered value. The `PASSWORD` parameter is required in any command that imports from or exports to HighBond. |
| `data.attributes.data` | object | ✅ | The data associated with the resource. |
| `data.attributes.data.value` | RobotTaskRequestValue | ✅ |  |
| `data.attributes.data.value` | StringValue |  | ↩ *referência recursiva — ver schema* `StringValue` |
| `data.attributes.data.value` | StringValues |  | ↩ *referência recursiva — ver schema* `StringValues` |
| `data.attributes.data.type` | string | ✅ | The data type of the value. Valores: `character`, `date`, `datetime`, `file`, `logical`, `number`, `table`, `time` |

</details>

<details>
<summary><strong>Respostas</strong> (7)</summary>

<details>
<summary>`200` — Updated.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `GetRobotTaskValuesResponse`

_Apenas campos que diferem do request body. 6 campo(s) idênticos omitidos._

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | array[RobotTaskValue] | ✅ | The data associated with the resource. |
| `data.id` | string | ✅ | The ID of the task. Ex.: `1` |
| `data.type` | string | ✅ | The classification of the object (`"values"`). Ex.: `"values"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.data.value` | RobotTaskRequestValue |  | ↩ *referência recursiva — ver schema* `RobotTaskRequestValue` |

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

<details>
<summary>`422` — Unprocessable entity.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `RobotsError`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `errors` | array[object] | ✅ |  |
| `errors.status` | string |  | A HTTP response status code indicating an unprocessable entity. Valores: `422` Ex.: `"422"` |
| `errors.source` | object |  |  |
| `errors.source.pointer` | string |  | Indicates the specific source of the error. Ex.: `"/data/attributes/name"` |
| `errors.title` | string |  | A title of the error. Ex.: `"can't be blank"` |
| `errors.detail` | string |  | A descriptive statement of the error. Ex.: `"Name can't be blank"` |

</details>

</details>
