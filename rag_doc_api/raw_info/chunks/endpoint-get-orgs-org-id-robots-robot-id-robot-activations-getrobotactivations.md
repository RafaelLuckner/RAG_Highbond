---
id: endpoint-get-orgs-org-id-robots-robot-id-robot-activations-getrobotactivations
title: "Script version activations: Get a robot's script activation history"
tags: [endpoint, robot-activations]
source: openapi.json (HighBond API v1.1.0)
---

## Script version activations

The Robots app provides two environments for managing and running analytic scripts that you author in Analytics: **development mode** and **production**.

In development mode, you can test newly committed versions of scripts against data that you have segregated for testing purposes. Once you are satisfied that the
scripts are working properly, you can activate them and make them your production version.

Learn more about development mode and production.

### `GET /orgs/{org_id}/robots/{robot_id}/robot_activations` — Get a robot's script activation history

- **operationId:** `getRobotActivations`
- **Domínio(s):** Robot Activations

Get information about a robot's script activation history.

<details>
<summary><strong>Parâmetros</strong> (2)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `robot_id` | path | ✅ | string | The ID of the robot. Ex.: `2` |

</details>

<details>
<summary><strong>Respostas</strong> (6)</summary>

<details>
<summary>`200` — OK.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `GetRobotActivationsResponse`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | array[RobotActivation] | ✅ | The data associated with the resource. |
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
| `included` | array[object] |  | All users related to the resource |
| `included.id` | string |  | The ID of the user. |
| `included.type` | string |  | The classification of the object (`"user"`). |
| `included.attributes` | object |  | The attributes associated with the flow. |
| `included.attributes.name` | string |  | Name of the user |
| `included.attributes.email` | string |  | Email of the user. |
| `included.attributes.user_type` | string |  | User type. |

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
