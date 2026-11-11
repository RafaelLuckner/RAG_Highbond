---
id: endpoint-get-orgs-org-id-robot-files-id-getrobotfile
title: "ACL robot related files: Get an ACL robot related file metadata"
tags: [endpoint, robot-files]
source: openapi.json (HighBond API v1.1.0)
---

## ACL robot related files

Related files in an ACL robot are non-Analytics files such as Excel or delimited that can be used as input for scripts in the robot.

Learn more about related files in ACL robots.

### `GET /orgs/{org_id}/robot_files/{id}` — Get an ACL robot related file metadata

- **operationId:** `getRobotFile`
- **Domínio(s):** Robot Files

Get the metadata for a related file by ACL robot ID.

<details>
<summary><strong>Parâmetros</strong> (2)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `id` | path | ✅ | string | The ID of the requested resource. Ex.: `9999` |

</details>

<details>
<summary><strong>Respostas</strong> (6)</summary>

<details>
<summary>`200` — OK.</summary>

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

</details>
