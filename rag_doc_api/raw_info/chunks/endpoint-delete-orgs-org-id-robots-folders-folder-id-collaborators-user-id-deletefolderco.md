---
id: endpoint-delete-orgs-org-id-robots-folders-folder-id-collaborators-user-id-deletefolderco
title: "Robots Folders Collaborators: Delete folder collaborator"
tags: [endpoint, robots-folders-collaborators]
source: openapi.json (HighBond API v1.1.0)
---

## Robots Folders Collaborators

Folder's collaborators are users who have access to all the robots in that folder.

### `DELETE /orgs/{org_id}/robots_folders/{folder_id}/collaborators/{user_id}` — Delete folder collaborator

- **operationId:** `deleteFolderCollaborator`
- **Domínio(s):** Robots Folders Collaborators

Deletes a folder collaborator.

<details>
<summary><strong>Parâmetros</strong> (3)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `folder_id` | path | ✅ | number | The ID of the folder. Ex.: `2` |
| `user_id` | path | ✅ | number | The ID of the user. Ex.: `2` |

</details>

<details>
<summary><strong>Respostas</strong> (4)</summary>

<details>
<summary>`200` — Collaborator resource deleted.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `FolderCollaboratorResponse`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | object |  |  |
| `data.id` | number |  | The user ID. Ex.: `1` |
| `data.type` | string |  | The classification of the object (`"collaborators"`). Ex.: `"collaborators"` |
| `data.attributes` | object |  | The attributes associated with the resource. |
| `data.attributes.username` | string |  | The username Ex.: `"user"` |
| `data.attributes.email` | string |  | The email of the user. Ex.: `"user@diligent.com"` |
| `data.attributes.role` | string |  | The role a collaborator can have Valores: `reviewer`, `editor`, `owner` |
| `data.attributes.admin` | boolean |  | Whether is admin or not |

</details>

<details>
<summary>`400` — Bad Request</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `Errors`

Erro no formato padrão JSON:API: objeto `errors` (array) com `status` (código HTTP), `source.pointer` (JSON Pointer RFC6901 do campo com erro), `code`, `title` e `detail`.

</details>

- `401` — Bad credentials.

- `403` — Forbidden.

</details>
