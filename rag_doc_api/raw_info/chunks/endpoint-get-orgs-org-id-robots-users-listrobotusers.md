---
id: endpoint-get-orgs-org-id-robots-users-listrobotusers
title: "Robot Users: List Robot Users"
tags: [endpoint, robot-users]
source: openapi.json (HighBond API v1.1.0)
---

## Robot Users

Users of the Robots module including some Robots-specific fields. Only Robots Admins can access this endpoint.

### `GET /orgs/{org_id}/robots/users` — List Robot Users

- **operationId:** `listRobotUsers`
- **Domínio(s):** Robot Users

Get a list of users of the Robots module.

<details>
<summary><strong>Parâmetros</strong> (2)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `cursor` | query |  | string | Pagination cursor. Ex.: `MTU=` |

</details>

<details>
<summary><strong>Respostas</strong> (3)</summary>

<details>
<summary>`200` — Success</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `ListRobotUsersResponse`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | object |  | The data associated with the resource |
| `data.users` | array[object] |  | The list of users |
| `data.users.id` | number |  | The user ID. Ex.: `1` |
| `data.users.type` | string |  | The classification of the object (`"users"`). Ex.: `"users"` |
| `data.users.attributes` | object |  | The attributes associated with the resource. |
| `data.users.attributes.uid` | string |  | The user UID Ex.: `"mkggNBvDK2Thnqp12J5H"` |
| `data.users.attributes.name` | string |  | The user's name Ex.: `"Remy Miller"` |
| `data.users.attributes.email` | string |  | The email of the user. Ex.: `"rpaquin@diligent.com"` |
| `data.users.attributes.robots_role` | string |  | The role of the user in the Robots module Valores: `admin`, `user` |
| `data.users.attributes.agent_manager` | boolean |  | Whether the user can access the agent manager page |
| `data.next` | string |  | The full request url to fetch the next set of users Ex.: `"https://apis.highbond.com/v1/orgs/15/robots/users?cursor=MTU="` |

</details>

- `401` — Bad credentials.

- `403` — Forbidden.

</details>
