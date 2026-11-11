---
id: endpoint-get-orgs-org-id-robots-robot-id-versions-version-id-getrobotscriptversion
title: "Robot script versions: Get script version of a robot"
tags: [endpoint, robot-script-versions]
source: openapi.json (HighBond API v1.1.0)
---

## Robot script versions

A version of a robot that includes the hcl script in json.  You can upload new version of your hcl script to your highbond robot or workflow robot.

Flow json includes python script, variables and system token user uid.  See example of flow json in request body schema.

### `GET /orgs/{org_id}/robots/{robot_id}/versions/{version_id}` — Get script version of a robot

- **operationId:** `getRobotScriptVersion`
- **Domínio(s):** Robot Script Versions

Get version of a robot.

<details>
<summary><strong>Parâmetros</strong> (4)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `robot_id` | path | ✅ | string | The ID of the robot. Ex.: `2` |
| `version_id` | path | ✅ | string | The ID of the version. Ex.: `2` |
| `include` | query |  | string | If specified, the associated analytic scripts will be included in the `included` object Valores: `analytics` Ex.: `analytics` |

</details>

<details>
<summary><strong>Respostas</strong> (6)</summary>

<details>
<summary>`200` — OK.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `GetRobotScriptVersionResponse`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | RobotScriptVersion | ✅ |  |
| `data.id` | string | ✅ | The ID of the script version. Ex.: `1` |
| `data.type` | string | ✅ | The classification of the object (`"robot_apps"`). Ex.: `"analytics"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.comment` | string |  | An informative statement in the version history. Ex.: `"Example commit comment"` |
| `data.attributes.version` | integer |  | The version of the analytic Ex.: `10` |
| `data.relationships` | object |  | The resouces associated with this script version. |
| `data.relationships.analytics` | object |  | List of flows associated with the script version. |
| `data.relationships.analytics.data` | array[object] |  | An array of analytic IDs associated with the script version. |
| `data.relationships.analytics.data.id` | string |  | The ID of the analytic. |
| `data.relationships.analytics.data.type` | string |  | The classification of the object (`"analytic"`). |
| `included` | array[object] |  | All analytics related to the resource |
| `included.id` | string |  | The ID of the flow. |
| `included.type` | string |  | The classification of the object (`"analytics"`). |
| `included.attributes` | object |  | The attributes associated with the flow. |
| `included.attributes.name` | string |  | The name of the flow Ex.: `"Example Flow"` |
| `included.attributes.raw` | object |  | Configuration object of the flow of a highbond robots or workflow robots. |

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
