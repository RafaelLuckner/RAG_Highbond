---
id: endpoint-get-orgs-org-id-groups-getgroups
title: "Groups: List groups in an instance
"
tags: [endpoint, groups]
source: openapi.json (HighBond API v1.1.0)
---

## Groups

Groups are a security feature in Launchpad that allow you to assign the same level of access to multiple users simultaneously.

Learn more about adding and managing groups.

### `GET /orgs/{org_id}/groups` — List groups in an instance


- **operationId:** `getGroups`
- **Domínio(s):** Groups

Get a list of groups for a particular HighBond instance.

<details>
<summary><strong>Parâmetros</strong> (1)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |

</details>

<details>
<summary><strong>Respostas</strong> (4)</summary>

<details>
<summary>`200` — OK.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `MultipleGroupsResponse`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | array[object] | ✅ | An array of the groups within this HighBond instance. |
| `data.id` | string | ✅ | The group ID for the group. Ex.: `"10"` |
| `data.type` | string | ✅ | The classification of the object (`"groups"`) for API schema serialization purposes. Ex.: `"groups"` |
| `data.attributes` | object | ✅ |  |
| `data.attributes.name` | string |  | The name of the group. The character limit is 255. Ex.: `"My Group"` |
| `data.attributes.purpose` | string |  | The purpose of the group. The character limit is 500. Ex.: `"To group users with the same access level together"` |
| `data.attributes.enabled` | boolean |  | This identifies whether the group is enabled for use. Ex.: `true` |
| `data.attributes.owners` | array[object] |  | The users that are to be assigned as owners of the group. Ex.: `[{"user_uid": "P2tuGWyTWxCAQgTd1XKx"}]` |
| `data.attributes.owners.user_uid` | string |  | The user_uid |
| `data.attributes.members` | array[object] |  | The users that are to be assigned as members of the group. Ex.: `[{"user_uid": "YhxzalsjfhauYna"}]` |
| `data.attributes.members.user_uid` | string |  | The user_uid |
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

</details>
