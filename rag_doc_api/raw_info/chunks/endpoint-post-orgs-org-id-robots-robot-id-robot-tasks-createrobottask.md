---
id: endpoint-post-orgs-org-id-robots-robot-id-robot-tasks-createrobottask
title: "Robot tasks: Create a robot task"
tags: [endpoint, robot-tasks]
source: openapi.json (HighBond API v1.1.0)
---

## Robot tasks

When you create a task, a robot runs the task according to the settings that you configure. A task can be scheduled or run ad hoc (manually).
Each task has its own unique settings.

Learn more about tasks.

### `POST /orgs/{org_id}/robots/{robot_id}/robot_tasks` — Create a robot task

- **operationId:** `createRobotTask`
- **Domínio(s):** Robot Tasks

Create a new task for a specified robot.

<details>
<summary><strong>Parâmetros</strong> (2)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `robot_id` | path | ✅ | string | The ID of the robot. Ex.: `2` |

</details>

<details>
<summary><strong>Request body (payload)</strong></summary>

The data required to create a robot task.

**Body obrigatório.**

**Content-Type:** `application/vnd.api+json`

**Schema:** `CreateRobotTaskRequest`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | object | ✅ | The data associated with the resource. |
| `data.type` | string |  | The classification of the object (`"robot_tasks"`). Ex.: `"robot_tasks"` |
| `data.attributes` | object |  | The attributes associated with the resource. |
| `data.attributes.app_version` | integer |  | The version of the script. Ex.: `1` |
| `data.attributes.email_notifications_enabled` | boolean |  | If `true`, an email notification is sent to one or more specific users if the task fails. |
| `data.attributes.environment` | string |  | The environment of the script. Valores: `production`, `development` |
| `data.attributes.log_enabled` | boolean |  | If `true`, a log is available every time the analytic is run. |
| `data.attributes.name` | string |  | The name of the task. Ex.: `"Intelligent Iron Clock"` |
| `data.attributes.public_key_name` | string |  | The public RSA key for encrypting password values. Ex.: `"Super_secret_public_key_name"` |
| `data.attributes.publish_to_results` | boolean |  | This is not currently supported. |
| `data.attributes.share_encrypted` | boolean |  | If `true`, any user with access to the robot can run, disable, or enable the task. If `false`, only the user who entered the password can run, disable, or enable the task. Ex.: `true` |
| `data.attributes.analytic_names` | array[string] |  | A list of the names of scripts to run. |

</details>

<details>
<summary><strong>Respostas</strong> (7)</summary>

<details>
<summary>`200` — Created.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `GetRobotTaskResponse`

_Apenas campos que diferem do request body. 3 campo(s) idênticos omitidos._

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | RobotTask | ✅ |  |
| `data.id` | string | ✅ | The ID of the task. Ex.: `1` |
| `data.type` | string | ✅ | The classification of the object (`"robot_tasks"`). Ex.: `"robot_tasks"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.analytic_names` | array[string] |  | A list of the names of scripts to run. Ex.: `["Analyze"]` |
| `data.attributes.conflicts` | object |  | Specifies the conflicts related to a script activation. Ex.: `"2019-03-21T16:25:00.478Z"` |
| `data.attributes.count` | integer |  | The folder name that is automatically created in the Robots Agent. The folder corresponds to an individual task. Ex.: `1` |
| `data.attributes.created_at` | string |  | The date the task was created. Ex.: `"2019-03-21T20:22:48.282Z"` |
| `data.attributes.email_notifications_enabled` | boolean |  | If `true`, an email notification is sent to one or more specific users if the task fails. Ex.: `true` |
| `data.attributes.enabled` | boolean |  | Specifies whether the task is enabled. You cannot run a disabled task. Ex.: `true` |
| `data.attributes.log_enabled` | boolean |  | If `true`, a log is available every time the analytic is run. Ex.: `true` |
| `data.attributes.name` | string |  | The name of the task. Ex.: `"Incredible Copper Pants"` |
| `data.attributes.publish_to_results` | boolean |  | This is not currently supported. Ex.: `true` |
| `data.attributes.share_encrypted` | boolean |  | If `true`, any user with access to the robot can run, disable, or enable the task. If `false`, only the user who entered the password can run, disable, or enable the task. Ex.: `false` |
| `data.attributes.updated_at` | string |  | The date when the task was updated. Ex.: `"2019-03-21T20:22:48.282Z"` |
| `data.attributes.next_runs` | array[string] |  | Specifies when the task will next run. |

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
