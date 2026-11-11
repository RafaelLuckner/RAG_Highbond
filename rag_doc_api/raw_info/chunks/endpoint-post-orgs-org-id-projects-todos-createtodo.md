---
id: endpoint-post-orgs-org-id-projects-todos-createtodo
title: "To-dos: Create a to-do"
tags: [endpoint, to-dos]
source: openapi.json (HighBond API v1.1.0)
---

## To-dos

To-dos are a collaboration tool between teammates and reviewers.

Learn more about to-dos.

### `POST /orgs/{org_id}/projects_todos` — Create a to-do

- **operationId:** `createTodo`
- **Domínio(s):** To-dos

Create a new todo in an existing project.

<details>
<summary><strong>Parâmetros</strong> (3)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `fields[projects_todos]` | query |  | string | Requesting the API to return only the specified fields. For more information, see Making requests Ex.: `description,due_date,status,created_at,updated_at,assigned_to,creator,target` |
| `include` | query |  | string | Requesting the API to return related resources. For more information, see Making requests Ex.: `assigned_to,target,creator` |

</details>

<details>
<summary><strong>Request body (payload)</strong></summary>

The data required to create a todo.

**Body obrigatório.**

**Content-Type:** `application/vnd.api+json`

**Schema:** `CreateTodoRequest`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | object | ✅ | The data associated with the resource. |
| `data.type` | string | ✅ | The classification of the object (`"projects_todos"`). Ex.: `"projects_todos"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.description` | string | ✅ | A detailed description of the todo. Ex.: `"Todo details"` |
| `data.attributes.due_date` | string |  | Specifies when the todo should be fulfilled by. Ex.: `"2021-01-18"` |
| `data.attributes.status` | string |  | Status of the todo. Can have one of the following values - "open", "cleared", "closed". Ex.: `"open"` |
| `data.relationships` | object | ✅ | The relationships associated with the resource. |
| `data.relationships.assigned_to` | object | ✅ | Specifies the user to whom the todo is assigned to. |
| `data.relationships.assigned_to.data` | object | ✅ | The data associated with a project. |
| `data.relationships.assigned_to.data.id` | string | ✅ | The unique identifier (UID) of the user. For more information on obtaining this value, see Making requests. Ex.: `"YhxzalsjfhauYna"` |
| `data.relationships.assigned_to.data.type` | string | ✅ | The classification of the object (`"users"`). Ex.: `"users"` |
| `data.relationships.target` | object | ✅ | Specifies the resource that the todo is associated with. |
| `data.relationships.target.data` | object | ✅ | The data associated with a project. |
| `data.relationships.target.data.id` | string | ✅ | The ID of the resource. Ex.: `"1"` |
| `data.relationships.target.data.type` | string | ✅ | The classification of the object.  A target can have one of the following types: `"projects"`, `"controls"`, `"control_tests"`, `"control_test_plans"`, `"issues"`, `"narratives"`, `"objectives"`, `"walkthrough_summaries"`, `"project_files"`, `"project_plannings"`, `"project_results"`, `"risks"`, `"risk_control_matrices"`, `"testing_rounds"`, `"walkthroughs"`. Ex.: `"objectives"` |

</details>

<details>
<summary><strong>Respostas</strong> (7)</summary>

<details>
<summary>`201` — Created.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `CreateTodoResponse`

_Apenas campos que diferem do request body. 13 campo(s) idênticos omitidos._

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data.id` | string | ✅ | The ID of the requested resource. Ex.: `"1"` |
| `data.attributes.created_at` | string | ✅ | The timestamp identifying when the todo was created. Ex.: `"2021-01-18T13:17:26Z"` |
| `data.attributes.updated_at` | string | ✅ | The timestamp identifying when the todo was last updated. Ex.: `"2021-01-18T13:17:26Z"` |
| `data.attributes.due_date` | string | ✅ | Specifies when the todo should be fulfilled by. Ex.: `"2021-01-18"` |
| `data.attributes.status` | string | ✅ | Status of the todo. Can have one of the following values - "open", "cleared", "closed". Ex.: `"open"` |
| `data.relationships.creator` | object | ✅ | Specifies the user to who is the todo's creator. |
| `data.relationships.creator.data` | object | ✅ | The data associated with a project. |
| `data.relationships.creator.data.id` | string | ✅ | The unique identifier (UID) of the user. For more information on obtaining this value, see Making requests. Ex.: `"YhxzalsjfhauYna"` |
| `data.relationships.creator.data.type` | string | ✅ | The classification of the object (`"users"`). Ex.: `"users"` |

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
