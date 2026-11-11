---
id: endpoint-post-orgs-org-id-robots-robot-id-robot-apps-robot-app-id-activate-createrobotact
title: "Script version activations: Activate a script version"
tags: [endpoint, robot-activations]
source: openapi.json (HighBond API v1.1.0)
---

## Script version activations

The Robots app provides two environments for managing and running analytic scripts that you author in Analytics: **development mode** and **production**.

In development mode, you can test newly committed versions of scripts against data that you have segregated for testing purposes. Once you are satisfied that the
scripts are working properly, you can activate them and make them your production version.

Learn more about development mode and production.

### `POST /orgs/{org_id}/robots/{robot_id}/robot_apps/{robot_app_id}/activate` — Activate a script version

- **operationId:** `createRobotActivation`
- **Domínio(s):** Robot Activations

You can activate a script version in a robot's development history that has an environment with runtime `Python 3.11` and includes `HCL 3.0.*` in its requirements. When you activate a version, the scripts in that version become the scripts that run in production tasks.

<details>
<summary><strong>Parâmetros</strong> (5)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `robot_id` | path | ✅ | string | The ID of the robot. Ex.: `2` |
| `robot_app_id` | path | ✅ | string | The ID of the robot app. Ex.: `2` |
| `force` | query |  | boolean | Overwrites the production scripts with the selected development mode version and ignores conflicts. Forcing the activation sets any existing tasks that are affected by the conflict to an idle status. When a task is set to idle, you must provide the missing parameter input or select the new script names before you can restart the task. Ex.: `true` |
| `comment` | query |  | string | An informative statement in the version history that explains what you are activating. Ex.: `activate this` |

</details>

<details>
<summary><strong>Request body (payload)</strong></summary>

Empty body

**Content-Type:** `application/json`

**Schema:** `CreateRobotActivationRequest`

_Schema sem propriedades documentadas._

</details>

<details>
<summary><strong>Respostas</strong> (7)</summary>

<details>
<summary>`200` — Created.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `CreateRobotActivationResponse`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | RobotActivation | ✅ |  |
| `data.id` | string | ✅ | The ID of the robot. Ex.: `1` |
| `data.type` | string | ✅ | The classification of the object (`"robot_activations"`). Ex.: `"robot_activations"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.activated_at` | string |  | The date when the script was activated. Ex.: `"2019-03-21T20:22:48.282Z"` |
| `data.attributes.comment` | string |  | An informative statement in the version history of the script. Ex.: `"The orthogonal features, when combined, can explode into complexity"` |
| `data.attributes.version` | integer |  | The script version number. Ex.: `1` |
| `data.relationships` | object |  | The relationships associated with the resource. Ex.: `{"activator": {"data": {"id": 2, "type": "user"}}}` |
| `data.relationships.activator` | object |  | User that activated the script activation. |
| `data.relationships.activator.data` | object |  |  |
| `data.relationships.activator.data.id` | string |  | The ID of the user. |
| `data.relationships.activator.data.type` | string |  | The classification of the object (`"user"`). |

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

**Schema:** `RobotActivationError`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `errors` | array[object] | ✅ |  |
| `errors.status` | string | ✅ | A HTTP response status code indicating an unprocessable entity. Valores: `422` |
| `errors.source` | object | ✅ |  |
| `errors.source.parameter` | string |  | Indicates the parameter in conflict. Parameters are compared between the current production version of the script and the version you are activating. Ex.: `"version"` |
| `errors.meta` | object | ✅ |  |
| `errors.meta.task_id` | integer |  | The ID of the robot task. Ex.: `1` |
| `errors.meta.conflicts` | object |  |  |
| `errors.meta.conflicts.missing_analytics` | array[string] |  | Specifies a script name conflict. This occurs when when a script that is selected to run in an existing production task or tasks has been renamed in the development script version or removed from the development script version. Ex.: `["Monitored zero administration superstructure"]` |
| `errors.meta.conflicts.missing_values` | array[string] |  | Specifies a parameter conflict. This occurs when a new input parameter has been added in the development script version. Ex.: `["Adaptive attitude-oriented customer loyalty"]` |
| `errors.meta.conflicts.changed_attributes` | array[string] |  | Specifies a parameter conflict. This occurs when the attributes of an existing input parameter have been changed in the development script version. Ex.: `["Streamlined background algorithm"]` |

</details>

</details>
