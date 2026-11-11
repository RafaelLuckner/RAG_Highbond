---
id: endpoint-get-orgs-org-id-robots-folders-folder-id-getfolder
title: "Robots Folders: Get Robots Folder"
tags: [endpoint, robots-folders]
source: openapi.json (HighBond API v1.1.0)
---

## Robots Folders

Folders to organize Robots.

### `GET /orgs/{org_id}/robots_folders/{folder_id}` — Get Robots Folder

- **operationId:** `getFolder`
- **Domínio(s):** Robots Folders

Get a Robots Folder.

<details>
<summary><strong>Parâmetros</strong> (3)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `folder_id` | path | ✅ | number | The ID of the folder. Ex.: `2` |
| `category` | query |  | string | The Robots category for the Folder. Valores: `acl`, `highbond`, `workflow` |

</details>

<details>
<summary><strong>Respostas</strong> (4)</summary>

<details>
<summary>`200` — Success.</summary>

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

- `401` — Bad credentials.

- `403` — Forbidden.

- `404` — Not found.

</details>
