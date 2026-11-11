---
id: endpoint-delete-orgs-org-id-robots-robot-id-working-files-deleterobotworkingfile
title: "HighBond/Workflow robot working files: Delete a HighBond/Workflow robot working file"
tags: [endpoint, robot-working-files]
source: openapi.json (HighBond API v1.1.0)
---

## HighBond/Workflow robot working files

Working files in a HighBond robot or a Workflow robot are files such as Excel or CSV that can be used as input for scripts in the robot.

### `DELETE /orgs/{org_id}/robots/{robot_id}/working_files` — Delete a HighBond/Workflow robot working file

- **operationId:** `deleteRobotWorkingFile`
- **Domínio(s):** Robot Working Files

Delete a working file to a HighBond or Workflow robot.

<details>
<summary><strong>Parâmetros</strong> (4)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `robot_id` | path | ✅ | string | The ID of the robot. Ex.: `2` |
| `env` | query |  | string | The environment of an analytic script. Valores: `development`, `production` Default: `development` Ex.: `production` |
| `filename` | query | ✅ | string | Filename id. Ex.: `filename.txt` |

</details>

<details>
<summary><strong>Respostas</strong> (5)</summary>

<details>
<summary>`200` — The name of the deleted file.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `DeleteRobotWorkingFileResponse`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | object | ✅ | The data associated with the resource |
| `data.id` | string |  | The ID of the file. Ex.: `"Data_source.xls"` |
| `data.type` | string |  | The classification of the object (`"robot_files"`). Ex.: `"robot_files"` |

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
