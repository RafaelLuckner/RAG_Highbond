---
id: endpoint-get-orgs-org-id-robots-robot-id-robot-apps-getrobotapps
title: "Analytic scripts: List a robot's analytic scripts"
tags: [endpoint, robot-apps]
source: openapi.json (HighBond API v1.1.0)
---

## Analytic scripts

An analytic script is a regular script with an analytic header. You can upload analytic scripts to a robot.

The analytic header is a series of declarative tags that allow the script to run in the Robots app. The analytic header includes input parameters that a user populates in
advance, which allows the analytic script to run unattended, either immediately, or at a scheduled time.

Learn more about analytic scripts.

### `GET /orgs/{org_id}/robots/{robot_id}/robot_apps` — List a robot's analytic scripts

- **operationId:** `getRobotApps`
- **Domínio(s):** Robot Apps

Get a list of a robot's analytic scripts.

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

**Schema:** `GetRobotAppsResponse`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | array[RobotApp] |  | The data associated with the resource. |
| `data.id` | string | ✅ | The ID of the robot. Ex.: `1` |
| `data.type` | string | ✅ | The classification of the object (`"robot_apps"`). Ex.: `"robot_apps"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.comment` | string |  | An informative statement in the version history of the script. Ex.: `"If we synthesize the application, we can get to the SSL firewall through the mobile XSS sensor!"` |
| `data.attributes.version` | integer |  | The script version number. Ex.: `1` |
| `data.attributes.created_at` | string |  | The date the robot was created. Ex.: `"2019-03-21T16:25:00.478Z"` |

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
