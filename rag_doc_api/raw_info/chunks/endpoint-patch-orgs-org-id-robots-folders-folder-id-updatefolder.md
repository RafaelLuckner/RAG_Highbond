---
id: endpoint-patch-orgs-org-id-robots-folders-folder-id-updatefolder
title: "Robots Folders: Update Folder"
tags: [endpoint, robots-folders]
source: openapi.json (HighBond API v1.1.0)
---

## Robots Folders

Folders to organize Robots.

### `PATCH /orgs/{org_id}/robots_folders/{folder_id}` — Update Folder

- **operationId:** `updateFolder`
- **Domínio(s):** Robots Folders

Updates a Robots Folder.

<details>
<summary><strong>Parâmetros</strong> (2)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `folder_id` | path | ✅ | number | The ID of the folder. Ex.: `2` |

</details>

<details>
<summary><strong>Request body (payload)</strong></summary>

The data required to update a Folder.

**Body obrigatório.**

**Content-Type:** `application/vnd.api+json`

**Schema:** `UpdateRobotsFolderRequest`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | object | ✅ | The data associated with the resource. |
| `data.type` | string | ✅ | The classification of the object (`"robots_folders"`). Ex.: `"robots_folders"` |
| `data.attributes` | object | ✅ |  |
| `data.attributes.name` | string |  | The name of the Robots Folder. Ex.: `"updated test folder"` |

</details>

<details>
<summary><strong>Respostas</strong> (5)</summary>

<details>
<summary>`200` — Updated.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `RobotsFolderResponse`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `id` | number |  | The Folder ID. Ex.: `1` |
| `type` | string |  | The classification of the object (`"robots_folders"`). Ex.: `"robots_folders"` |
| `attributes` | object |  | The attributes associated with the resource. |
| `attributes.name` | string |  | The name of the Robots Folder. Ex.: `"test folder"` |
| `attributes.category` | string |  | Category of the Robots Folder. Ex.: `"highbond"` |
| `attributes.created_at` | string |  | The date the Robots Folder was created. Ex.: `"2019-02-09T13:17:26Z"` |
| `attributes.created_by` | string |  | User who created the Folder. Ex.: `"xyz"` |
| `attributes.discarded_at` | string |  | Date when the Robots Folder was discarded. Ex.: `"2019-02-09T13:17:26Z"` |
| `attributes.delete_failed` | string |  | Specifies if the Robots Folder deletion failed. Ex.: `false` |

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
