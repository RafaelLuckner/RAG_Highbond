---
id: endpoint-post-orgs-org-id-robots-robot-id-working-files-createrobotworkingfile
title: "HighBond/Workflow robot working files: Upload a HighBond/Workflow robot working file"
tags: [endpoint, robot-working-files]
source: openapi.json (HighBond API v1.1.0)
---

## HighBond/Workflow robot working files

Working files in a HighBond robot or a Workflow robot are files such as Excel or CSV that can be used as input for scripts in the robot.

### `POST /orgs/{org_id}/robots/{robot_id}/working_files` — Upload a HighBond/Workflow robot working file

- **operationId:** `createRobotWorkingFile`
- **Domínio(s):** Robot Working Files

Upload a working file to a HighBond or Workflow robot.

<details>
<summary><strong>Parâmetros</strong> (4)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `robot_id` | path | ✅ | string | The ID of the robot. Ex.: `2` |
| `env` | query |  | string | The environment of an analytic script. Valores: `development`, `production` Default: `development` Ex.: `production` |
| `overwrite` | query |  | boolean | Overwrite an existing working file with the same name. Default: `False` |

</details>

<details>
<summary><strong>Request body (payload)</strong></summary>

The data required to upload a working file.

**Body obrigatório.**

**Content-Type:** `application/json`

**Schema:** `CreateRobotWorkingFileRequest`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | object | ✅ | The data associated with the resource. |
| `data.type` | string |  | The classification of the object (`"robot_files"`). Ex.: `"robot_files"` |
| `data.attributes` | object |  | The attributes associated with the resource. |
| `data.attributes.filename` | string |  | The name of the file. Ex.: `"Data_source.xls"` |

</details>

<details>
<summary><strong>Respostas</strong> (5)</summary>

<details>
<summary>`200` — Created.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `CreateRobotWorkingFileResponse`

_Apenas campos que diferem do request body. 1 campo(s) idênticos omitidos._

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data.id` | string | ✅ | The ID of the robot. Ex.: `"Data_source.xls"` |
| `data.type` | string | ✅ | The classification of the object (`"robot_files"`). Ex.: `"robot_files"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.uploadUrl` | string |  | The url to upload the file to. Ex.: `"https://acl-highbond-drive-us2-main-s1.s3.us-west-2.amazonaws.com/1000223/robots/dev/48586/working_files/Data_source.xls"` |
| `data.attributes.expirationDate` | string |  | The date the url expires. Ex.: `"2019-03-21T20:22:48.282Z"` |

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

</details>
