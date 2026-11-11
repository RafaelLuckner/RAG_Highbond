---
id: endpoint-get-orgs-org-id-robots-folders-listfolders
title: "Robots Folders: List Folders"
tags: [endpoint, robots-folders]
source: openapi.json (HighBond API v1.1.0)
---

## Robots Folders

Folders to organize Robots.

### `GET /orgs/{org_id}/robots_folders` — List Folders

- **operationId:** `listFolders`
- **Domínio(s):** Robots Folders

Get a list of Robots Folders.

<details>
<summary><strong>Parâmetros</strong> (1)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |

</details>

<details>
<summary><strong>Respostas</strong> (3)</summary>

<details>
<summary>`200` — Success.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `ListRobotsFoldersResponse`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | array[object] |  | The data associated with the resource. |
| `data.id` | number |  | The Folder ID. Ex.: `1` |
| `data.type` | string |  | The classification of the object (`"robots_folders"`). Ex.: `"robots_folders"` |
| `data.attributes` | object |  | The attributes associated with the resource. |
| `data.attributes.name` | string |  | The name of the Robots Folder. Ex.: `"test folder"` |
| `data.attributes.category` | string |  | Category of the Robots Folder. Ex.: `"highbond"` |
| `data.attributes.created_at` | string |  | The date the Robots Folder was created. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.attributes.created_by` | string |  | User who created the Folder. Ex.: `"xyz"` |
| `data.attributes.discarded_at` | string |  | Date when the Robots Folder was discarded. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.attributes.delete_failed` | string |  | Specifies if the Robots Folder deletion failed. Ex.: `false` |

</details>

- `401` — Bad credentials.

- `403` — Forbidden.

</details>
