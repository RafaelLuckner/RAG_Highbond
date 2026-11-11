---
id: endpoint-get-orgs-org-id-robots-robot-id-jobs-getrobotjobs
title: "Robot task runs: List robot task runs"
tags: [endpoint, robot-jobs]
source: openapi.json (HighBond API v1.1.0)
---

## Robot task runs

Robot task runs, also known as robot jobs, are individual executions of a robot task. For example, for any given robot task, you can schedule a task run once every 24 hours, or you can initiate a task run manually at any time.

### `GET /orgs/{org_id}/robots/{robot_id}/jobs` — List robot task runs

- **operationId:** `getRobotJobs`
- **Domínio(s):** Robot Jobs

Get a list of task runs for a robot.

<details>
<summary><strong>Parâmetros</strong> (6)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `robot_id` | path | ✅ | string | The ID of the robot. Ex.: `2` |
| `env` | query |  | string | The environment of an analytic script. Valores: `development`, `production` Default: `development` Ex.: `production` |
| `include` | query |  | string | If specified, the associated objects will be included in the `included` list Valores: `robot`, `task`, `triggered_by` Ex.: `robot,task,triggered_by` |
| `page[size]` | query |  | string | The number of items returned per page. Default is 100. Ex.: `100` |
| `page[number]` | query |  | string | The page number of records to return. Default is 1. Ex.: `1` |

</details>

<details>
<summary><strong>Respostas</strong> (6)</summary>

<details>
<summary>`200` — OK.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `GetRobotJobsResponse`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | array[RobotJob] |  | The data associated with the resource. |
| `data.id` | string | ✅ | The ID of the task run. Ex.: `1` |
| `data.type` | string | ✅ | The classification of the object (`"robot_jobs"`). Ex.: `"robot_jobs"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.app_version` | integer |  | The version of the script. Ex.: `1` |
| `data.attributes.completed_at` | string |  | The date the task run was completed. Ex.: `"2019-03-21T20:22:48.282Z"` |
| `data.attributes.count` | integer |  | The folder name that is automatically created in the Robots Agent. The folder corresponds to an individual task run. Ex.: `1` |
| `data.attributes.delete_failed` | boolean |  | If a user made a request to delete a task run, this indicates whether the deletion failed. Ex.: `false` |
| `data.attributes.discarded_at` | string |  | If a user made a request to delete a task run, this is the time the user made the request. Ex.: `null` |
| `data.attributes.environment` | string |  | The environment of the script. Valores: `production`, `development` |
| `data.attributes.error_code` | string |  | If the task run failed due to a known reason, this error code indicates that reason. Not all failed task runs have associated error codes. Ex.: `null` |
| `data.attributes.queued_at` | string |  | The date the task run was queued to execute. Ex.: `"2019-03-21T20:22:48.282Z"` |
| `data.attributes.result_analytics` | array[object] |  | Includes analytics information about the task run. |
| `data.attributes.result_analytics.name` | string |  | The name of the script. |
| `data.attributes.result_analytics.logs` | array[object] |  | Information about the system trace logs. |
| `data.attributes.result_analytics.logs.key` | string |  | The key HighBond uses to download the system trace log file. |
| `data.attributes.result_analytics.logs.file_name` | string |  | The file name for the system trace log. |
| `data.attributes.result_analytics.success` | boolean |  | Indicates whether this particular script executed successfully. Ex.: `true` |
| `data.attributes.result_downloadable` | boolean |  | Indicates whether you can download the result files in the UI. Ex.: `true` |
| `data.attributes.status` | string |  | The status of the task run. Valores: `success`, `failed`, `cancelled`, `queued`, `running`, `skipped` |
| `data.attributes.trigger_type` | string |  | The trigger type of the task run. Valores: `schedule`, `manual`, `event` |
| `data.attributes.agent_count` | string |  | For ACL Robot task runs that run with an on-premise agent, this is the ID of the agent that ran it. For all other robot types, this value is `null`. Ex.: `null` |
| `data.relationships` | object |  | List of associated objects with the robot task run. |
| `data.relationships.robot` | object |  | Information about the robot associated with the task run. |
| `data.relationships.robot.data` | object |  | Data about the robot. |
| `data.relationships.robot.data.id` | string |  | The ID of the robot. |
| `data.relationships.robot.data.type` | string |  | The classification of the object (`"robot"`). |
| `data.relationships.task` | object |  | Information about the task associated with the task run. |
| `data.relationships.task.data` | object |  | Data about the task. |
| `data.relationships.task.data.id` | string |  | The ID of the task. |
| `data.relationships.task.data.type` | string |  | The classification of the object (`"task"`). |
| `data.relationships.triggered_by` | object |  | Information about the user who triggered the task run. |
| `data.relationships.triggered_by.data` | object |  | Data about the user. |
| `data.relationships.triggered_by.data.id` | string |  | The ID of the user. In addition to the user IDs used elsewhere in the HighBond API, each user also has an ID specific to Robots. To see a list of users  and their Robots IDs in the response, use the `include=triggered_by` parameter. |
| `data.relationships.triggered_by.data.type` | string |  | The classification of the object (`"user"`). |
| `links` | object |  |  |
| `links.prev` | string |  | Previous page url |
| `links.next` | string |  | Next page url |

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
