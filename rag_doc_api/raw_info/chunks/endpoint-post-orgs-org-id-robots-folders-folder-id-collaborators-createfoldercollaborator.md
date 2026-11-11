---
id: endpoint-post-orgs-org-id-robots-folders-folder-id-collaborators-createfoldercollaborator
title: "Robots Folders Collaborators: Create Folder Collaborator"
tags: [endpoint, robots-folders-collaborators]
source: openapi.json (HighBond API v1.1.0)
---

## Robots Folders Collaborators

Folder's collaborators are users who have access to all the robots in that folder.

### `POST /orgs/{org_id}/robots_folders/{folder_id}/collaborators` — Create Folder Collaborator

- **operationId:** `createFolderCollaborator`
- **Domínio(s):** Robots Folders Collaborators

Create a single collaborator for a folder.

<details>
<summary><strong>Parâmetros</strong> (2)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `folder_id` | path | ✅ | number | The ID of the folder. Ex.: `2` |

</details>

<details>
<summary><strong>Request body (payload)</strong></summary>

The data required to create a robot.

**Body obrigatório.**

**Content-Type:** `application/json`

**Schema:** `CreateFolderCollaboratorRequest`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | object | ✅ |  |
| `data.attributes` | object |  |  |
| `data.attributes.user_id` | number |  | The user ID. Ex.: `1` |
| `data.attributes.role` | string |  | The role a collaborator can have Valores: `reviewer`, `editor`, `owner` |

</details>

<details>
<summary><strong>Respostas</strong> (4)</summary>

<details>
<summary>`200` — Success</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `FolderCollaboratorResponse`

_Apenas campos que diferem do request body. 1 campo(s) idênticos omitidos._

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | object |  |  |
| `data.id` | number |  | The user ID. Ex.: `1` |
| `data.type` | string |  | The classification of the object (`"collaborators"`). Ex.: `"collaborators"` |
| `data.attributes` | object |  | The attributes associated with the resource. |
| `data.attributes.username` | string |  | The username Ex.: `"user"` |
| `data.attributes.email` | string |  | The email of the user. Ex.: `"user@diligent.com"` |
| `data.attributes.admin` | boolean |  | Whether is admin or not |

</details>

- `401` — Bad credentials.

- `403` — Forbidden.

<details>
<summary>`422` — Unprocessable entity.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `Errors`

Erro no formato padrão JSON:API: objeto `errors` (array) com `status` (código HTTP), `source.pointer` (JSON Pointer RFC6901 do campo com erro), `code`, `title` e `detail`.

</details>

</details>
