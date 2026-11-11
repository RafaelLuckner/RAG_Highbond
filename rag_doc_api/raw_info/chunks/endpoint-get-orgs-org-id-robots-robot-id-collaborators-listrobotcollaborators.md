---
id: endpoint-get-orgs-org-id-robots-robot-id-collaborators-listrobotcollaborators
title: "Robot Collaborators: List Robot Collaborators"
tags: [endpoint, robot-collaborators]
source: openapi.json (HighBond API v1.1.0)
---

## Robot Collaborators

Robot collaborators are users who have access to that particular robot.

### `GET /orgs/{org_id}/robots/{robot_id}/collaborators` — List Robot Collaborators

- **operationId:** `listRobotCollaborators`
- **Domínio(s):** Robot Collaborators

Get a list of collaborators for a robot.

<details>
<summary><strong>Parâmetros</strong> (4)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `robot_id` | path | ✅ | string | The ID of the robot. Ex.: `2` |
| `offset` | query |  | integer | Required data records start position, start from 0 Ex.: `1` |
| `usersPerPage` | query |  | integer | Required number of records to read, start from 1 Ex.: `2` |

</details>

<details>
<summary><strong>Respostas</strong> (3)</summary>

<details>
<summary>`200` — Success</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `ListRobotCollaboratorsResponse`

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
| `total` | number |  | The total number of collaborators in the robot. Ex.: `100` |

</details>

- `401` — Bad credentials.

- `403` — Forbidden.

</details>
