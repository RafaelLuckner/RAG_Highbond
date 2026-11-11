---
id: endpoint-patch-orgs-org-id-robots-users-user-id-updaterobotuser
title: "Robot Users: Update robot user"
tags: [endpoint, robot-users]
source: openapi.json (HighBond API v1.1.0)
---

## Robot Users

Users of the Robots module including some Robots-specific fields. Only Robots Admins can access this endpoint.

### `PATCH /orgs/{org_id}/robots/users/{user_id}` — Update robot user

- **operationId:** `updateRobotUser`
- **Domínio(s):** Robot Users

Updates a robot user.

<details>
<summary><strong>Parâmetros</strong> (2)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `user_id` | path | ✅ | number | The ID of the user. Ex.: `2` |

</details>

<details>
<summary><strong>Request body (payload)</strong></summary>

The data required to update a robot user.

**Body obrigatório.**

**Content-Type:** `application/vnd.api+json`

**Schema:** `UpdateRobotUserRequest`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | object |  |  |
| `data.attributes` | object |  |  |
| `data.attributes.robots_role` | string | ✅ | The role of the user in the Robots module Valores: `admin`, `user` |
| `data.attributes.agent_manager` | boolean | ✅ | Whether the user can access the agent manager page |

Exemplo:

```json
{
  "data": {
    "attributes": {
      "robots_role": "admin",
      "agent_manager": true
    }
  }
}
```

</details>

<details>
<summary><strong>Respostas</strong> (4)</summary>

<details>
<summary>`200` — Success</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `UpdateRobotUserResponse`

_Apenas campos que diferem do request body. 1 campo(s) idênticos omitidos._

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data.id` | number |  | The user ID. Ex.: `1` |
| `data.type` | string |  | The classification of the object (`"users"`). Ex.: `"users"` |
| `data.attributes` | object |  | The attributes associated with the resource. |
| `data.attributes.uid` | string |  | The user UID Ex.: `"mkggNBvDK2Thnqp12J5H"` |
| `data.attributes.name` | string |  | The user's name Ex.: `"Remy Miller"` |
| `data.attributes.email` | string |  | The email of the user. Ex.: `"rpaquin@diligent.com"` |
| `data.attributes.robots_role` | string |  | The role of the user in the Robots module Valores: `admin`, `user` |
| `data.attributes.agent_manager` | boolean |  | Whether the user can access the agent manager page |

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
