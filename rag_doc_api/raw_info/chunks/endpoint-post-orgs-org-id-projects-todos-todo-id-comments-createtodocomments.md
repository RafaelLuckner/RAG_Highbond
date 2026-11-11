---
id: endpoint-post-orgs-org-id-projects-todos-todo-id-comments-createtodocomments
title: "To-dos: Create a to-do comment"
tags: [endpoint, to-dos]
source: openapi.json (HighBond API v1.1.0)
---

## To-dos

To-dos are a collaboration tool between teammates and reviewers.

Learn more about to-dos.

### `POST /orgs/{org_id}/projects_todos/{todo_id}/comments` — Create a to-do comment

- **operationId:** `createTodoComments`
- **Domínio(s):** To-dos

Create a new to-do comment

<details>
<summary><strong>Parâmetros</strong> (3)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `project_id` | path | ✅ | integer | The ID of the project. Ex.: `1` |
| `todo_id` | path | ✅ | integer | The ID of the to-do. Ex.: `1` |

</details>

<details>
<summary><strong>Request body (payload)</strong></summary>

The data required to create a to-do comment.

**Body obrigatório.**

**Content-Type:** `application/vnd.api+json`

**Schema:** `CreateTodoCommentRequest`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | object | ✅ | The data associated with the resource. |
| `data.type` | string | ✅ | The classification of the object (`"comments"`). Ex.: `"comments"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.text` | string |  | Body of commment. Ex.: `"Sample body"` |

</details>

<details>
<summary><strong>Respostas</strong> (7)</summary>

<details>
<summary>`201` — Created.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `GetTodoCommentResponse`

_Apenas campos que diferem do request body. 4 campo(s) idênticos omitidos._

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data.id` | string | ✅ | The ID of the requested resource. Ex.: `"1"` |
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

<details>
<summary>`422` — Unprocessable entity.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `Errors`

Erro no formato padrão JSON:API: objeto `errors` (array) com `status` (código HTTP), `source.pointer` (JSON Pointer RFC6901 do campo com erro), `code`, `title` e `detail`.

</details>

</details>
