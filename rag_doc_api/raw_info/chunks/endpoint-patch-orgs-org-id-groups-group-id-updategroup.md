---
id: endpoint-patch-orgs-org-id-groups-group-id-updategroup
title: "Groups: Update group information"
tags: [endpoint, groups]
source: openapi.json (HighBond API v1.1.0)
---

## Groups

Groups are a security feature in Launchpad that allow you to assign the same level of access to multiple users simultaneously.

Learn more about adding and managing groups.

### `PATCH /orgs/{org_id}/groups/{group_id}` — Update group information

- **operationId:** `updateGroup`
- **Domínio(s):** Groups

Updates information for a single group.

<details>
<summary><strong>Parâmetros</strong> (2)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `group_id` | path | ✅ | string | The ID of the group. Ex.: `10` |

</details>

<details>
<summary><strong>Request body (payload)</strong></summary>

The data required to update a group.

**Body obrigatório.**

**Content-Type:** `application/vnd.api+json`

**Schema:** `UpdateGroupRequest`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | object | ✅ | The data to update. |
| `data.type` | string | ✅ | The classification of the object (`"groups"`) for API schema serialization purposes. Ex.: `"groups"` |
| `data.attributes` | object | ✅ | The attributes associated with the group. |
| `data.attributes.name` | string |  | The name of the group. The character limit is 255. Ex.: `"My Group"` |
| `data.attributes.purpose` | string |  | The purpose of the group. The character limit is 500. Ex.: `"To group users with the same access level together"` |
| `data.attributes.enabled` | boolean |  | This identifies whether the group is enabled for use. Ex.: `true` |
| `data.attributes.owners` | array[object] |  | The users that are to be assigned as owners of the group. If omitted, defaults to the user who initiates the request. Ex.: `[{"user_uid": "P2tuGWyTWxCAQgTd1XKx"}]` |
| `data.attributes.owners.user_uid` | string |  | The user_uid |
| `data.attributes.members` | array[object] |  | The users that are to be assigned as members of the group. If a member is contained in the owners list, it will be ignored. Ex.: `[{"user_uid": "YhxzalsjfhauYna"}]` |
| `data.attributes.members.user_uid` | string |  | The user_uid |

</details>

<details>
<summary><strong>Respostas</strong> (6)</summary>

<details>
<summary>`200` — Group updated.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `GetGroupResponse`

_Apenas campos que diferem do request body. 6 campo(s) idênticos omitidos._

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | object | ✅ |  |
| `data.id` | string | ✅ | The group ID for the group. Ex.: `"10"` |
| `data.attributes` | object | ✅ |  |
| `data.attributes.owners` | array[object] |  | The users that are to be assigned as owners of the group. Ex.: `[{"user_uid": "P2tuGWyTWxCAQgTd1XKx"}]` |
| `data.attributes.members` | array[object] |  | The users that are to be assigned as members of the group. Ex.: `[{"user_uid": "YhxzalsjfhauYna"}]` |
| `data.attributes.member_count` | number |  | The number of owners and members that the group has. Ex.: `2` |

</details>

<details>
<summary>`400` — Bad request.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `Errors`

Erro no formato padrão JSON:API: objeto `errors` (array) com `status` (código HTTP), `source.pointer` (JSON Pointer RFC6901 do campo com erro), `code`, `title` e `detail`.

</details>

- `401` — Bad credentials.

- `404` — Not found.

- `422` — Unprocessable entity.

- `429` — Too many requests.

</details>
