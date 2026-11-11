---
id: endpoint-get-orgs-org-id-actions-action-id-comments-getactioncomments
title: "Actions: List action comments in an action"
tags: [endpoint, actions]
source: openapi.json (HighBond API v1.1.0)
---

## Actions

An action is a specific follow-up measure that is associated with an identified issue. You can add actions and assign action owners. You can also set up reminders for
yourself to retest issues or track hours spent on retesting by self-assigning actions.

> **Note —**
Only actions in projects that have an `"active"` state can be accessed using the API.

Learn more about actions.

### `GET /orgs/{org_id}/actions/{action_id}/comments` — List action comments in an action

- **operationId:** `getActionComments`
- **Domínio(s):** Actions

Get a list of all action comments associated with an action.

<details>
<summary><strong>Parâmetros</strong> (5)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `action_id` | path | ✅ | integer | The ID of the action. Ex.: `1` |
| `page[size]` | query |  | string | The number of items returned per page. Default is 50. Maximum is 100. Ex.: `25` |
| `page[number]` | query |  | string | The Base64-encoded page number of records to return. Ex.: `Mg==` |
| `fields[action_comments]` | query |  | string | Requesting the API to return only the specified fields. For more information, see Making requests Ex.: `message_content,commenter_name,commenter_email,created_at,updated_at,action,commenter_user` |

</details>

<details>
<summary><strong>Respostas</strong> (6)</summary>

<details>
<summary>`200` — OK.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `GetActionCommentsResponse`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | array[object] | ✅ | Array of action comments |
| `data.id` | string | ✅ | The ID of the requested resource. Ex.: `"1"` |
| `data.type` | string | ✅ | The classification of the object (`"action_comments"`). Ex.: `"action_comments"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.message_content` | string |  | The content of the action comment. Ex.: `"Message content"` |
| `data.attributes.commenter_name` | string |  | The name of the user who created the action comment. Ex.: `"Tom Wachowski"` |
| `data.attributes.commenter_email` | string |  | The email of the user who created the action comment. Ex.: `"tom@example.com"` |
| `data.attributes.created_at` | string |  | The timestamp identifying when the action comment was created. Ex.: `"2021-06-09T13:17:26Z"` |
| `data.attributes.updated_at` | string |  | The timestamp identifying when the action comment was updated. Ex.: `"2021-06-09T13:17:26Z"` |
| `data.relationships` | object | ✅ | The relationships associated with the resource. |
| `data.relationships.action` | object | ✅ | The attributes associated with the resource. |
| `data.relationships.action.data` | object | ✅ | The data associated with the resource. |
| `data.relationships.action.data.id` | string | ✅ | The ID of the action. Ex.: `"1"` |
| `data.relationships.action.data.type` | string | ✅ | The classification of the object (`"actions"`). Ex.: `"actions"` |
| `data.relationships.commenter_user` | object |  | The ID for the user who created the action comment. Can be `null` if commenter is an external user. |
| `data.relationships.commenter_user.data` | object | ✅ | The data associated with the resource. |
| `data.relationships.commenter_user.data.id` | string | ✅ | The unique identifier (UID) of the commenter user. For more information on obtaining this value, see Making requests. Ex.: `"3NQ6XzAUxqJMnAQ7n4KF"` |
| `data.relationships.commenter_user.data.type` | string | ✅ | The classification of the object (`"users"`). Ex.: `"users"` |
| `links` | object | ✅ |  |
| `links.next` | string | ✅ | Next page url Ex.: `"/api/resource?page[number]=Mg=="` |
| `links.prev` | string | ✅ | Previous page url Ex.: `null` |

</details>

<details>
<summary>`400` — Bad request.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `Errors`

Erro no formato padrão JSON:API: objeto `errors` (array) com `status` (código HTTP), `source.pointer` (JSON Pointer RFC6901 do campo com erro), `code`, `title` e `detail`.

</details>

- `401` — Bad credentials.

- `403` — Forbidden.

- `404` — Not found.

<details>
<summary>`415` — Unsupported media type.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `Errors`

Erro no formato padrão JSON:API: objeto `errors` (array) com `status` (código HTTP), `source.pointer` (JSON Pointer RFC6901 do campo com erro), `code`, `title` e `detail`.

</details>

</details>
