---
id: endpoint-get-orgs-org-id-robots-folders-folder-id-collaborators-listfoldercollaborators
title: "Robots Folders Collaborators: List Folder Collaborators"
tags: [endpoint, robots-folders-collaborators]
source: openapi.json (HighBond API v1.1.0)
---

## Robots Folders Collaborators

Folder's collaborators are users who have access to all the robots in that folder.

### `GET /orgs/{org_id}/robots_folders/{folder_id}/collaborators` — List Folder Collaborators

- **operationId:** `listFolderCollaborators`
- **Domínio(s):** Robots Folders Collaborators

Get a list of collaborators from a folder.

<details>
<summary><strong>Parâmetros</strong> (4)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `folder_id` | path | ✅ | number | The ID of the folder. Ex.: `2` |
| `offset` | query |  | integer | Required data records start position, start from 0 Ex.: `1` |
| `usersPerPage` | query |  | integer | Required number of records to read, start from 1 Ex.: `2` |

</details>

<details>
<summary><strong>Respostas</strong> (3)</summary>

<details>
<summary>`200` — Success</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `ListFolderCollaboratorsResponse`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | array[object] |  | The data associated with the resource |
| `data.id` | number |  | The user ID. Ex.: `1` |
| `data.type` | string |  | The classification of the object (`"collaborators"`). Ex.: `"collaborators"` |
| `data.attributes` | object |  | The attributes associated with the resource. |
| `data.attributes.username` | string |  | The username Ex.: `"user"` |
| `data.attributes.email` | string |  | The email of the user. Ex.: `"user@diligent.com"` |
| `data.attributes.role` | string |  | The role a collaborator can have Valores: `reviewer`, `editor`, `owner` |
| `data.attributes.admin` | boolean |  | Whether is admin or not |
| `total` | number |  | The total number of collaborators in the folder. Ex.: `100` |

</details>

- `401` — Bad credentials.

- `403` — Forbidden.

</details>
