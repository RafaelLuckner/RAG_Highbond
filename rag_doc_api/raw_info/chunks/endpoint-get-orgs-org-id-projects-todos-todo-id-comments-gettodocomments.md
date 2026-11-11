---
id: endpoint-get-orgs-org-id-projects-todos-todo-id-comments-gettodocomments
title: "To-dos: Get to-do comments"
tags: [endpoint, to-dos]
source: openapi.json (HighBond API v1.1.0)
---

## To-dos

To-dos are a collaboration tool between teammates and reviewers.

Learn more about to-dos.

### `GET /orgs/{org_id}/projects_todos/{todo_id}/comments` — Get to-do comments

- **operationId:** `getTodoComments`
- **Domínio(s):** To-dos

Get a list of to-do comments

<details>
<summary><strong>Parâmetros</strong> (5)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `project_id` | path | ✅ | integer | The ID of the project. Ex.: `1` |
| `todo_id` | path | ✅ | integer | The ID of the to-do. Ex.: `1` |
| `fields[comments]` | query |  | string | Requesting the API to return only the specified fields. For more information, see Making requests Ex.: `text,user` |
| `include` | query |  | string | Requesting the API to return related resources. Valores: `user` Ex.: `user` |

</details>

<details>
<summary><strong>Respostas</strong> (6)</summary>

<details>
<summary>`200` — OK.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `GetTodoCommentsResponse`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | array[object] | ✅ |  |
| `data.id` | string | ✅ | The ID of the requested resource. Ex.: `"1"` |
| `data.type` | string | ✅ | The classification of the object (`"comments"`). Ex.: `"comments"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.text` | string |  | Body of commment. Ex.: `"Sample body"` |
| `data.attributes.created_at` | string |  | The timestamp identifying when the comment was created. Ex.: `"2021-01-18T13:17:26Z"` |
| `data.relationships` | object | ✅ | The relationships associated with the resource. |
| `data.relationships.user` | object |  | Specifies the user responsible for fulfilling the request. A value in this field will override any values provided in the `owner` and `owner_email` attributes or contact reference fields. This field becomes required if the `owner` attribute is not provided. |
| `data.relationships.user.data` | object | ✅ | The data associated with the resource. |
| `data.relationships.user.data.id` | string | ✅ | The unique identifier (UID) of the user. For more information on obtaining this value, see Making requests. Ex.: `"3NQ6XzAUxqJMnAQ7n4KF"` |
| `data.relationships.user.data.type` | string | ✅ | The classification of the object (`"users"`). Ex.: `"users"` |

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
