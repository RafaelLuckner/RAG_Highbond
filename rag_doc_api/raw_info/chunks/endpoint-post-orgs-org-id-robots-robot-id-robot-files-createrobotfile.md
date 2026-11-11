---
id: endpoint-post-orgs-org-id-robots-robot-id-robot-files-createrobotfile
title: "ACL robot related files: Upload an ACL robot related file"
tags: [endpoint, robot-files]
source: openapi.json (HighBond API v1.1.0)
---

## ACL robot related files

Related files in an ACL robot are non-Analytics files such as Excel or delimited that can be used as input for scripts in the robot.

Learn more about related files in ACL robots.

### `POST /orgs/{org_id}/robots/{robot_id}/robot_files` — Upload an ACL robot related file

- **operationId:** `createRobotFile`
- **Domínio(s):** Robot Files

Upload a related file to an ACL robot.

<details>
<summary><strong>Parâmetros</strong> (3)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `robot_id` | path | ✅ | string | The ID of the robot. Ex.: `2` |
| `env` | query |  | string | The environment of an analytic script. Valores: `development`, `production` Default: `development` Ex.: `production` |

</details>

<details>
<summary><strong>Request body (payload)</strong></summary>

The data required to create a related file.

**Body obrigatório.**

**Content-Type:** `multipart/form-data`

**Schema:** `CreateRobotFileRequest`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `file` | string | ✅ | A related file that you want to upload. |

</details>

<details>
<summary><strong>Respostas</strong> (7)</summary>

<details>
<summary>`200` — Created.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `GetRobotFileResponse`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | RobotFile | ✅ |  |
| `data.id` | string | ✅ | The ID of the robot. Ex.: `1` |
| `data.type` | string | ✅ | The classification of the object (`"robot_files"`). Ex.: `"robot_files"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.created_at` | string |  | The date the robot was created. Ex.: `"2019-03-21T20:22:48.282Z"` |
| `data.attributes.filename` | string |  | The name of the related file. Ex.: `"Data_source.xls"` |

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
