---
id: endpoint-get-orgs-org-id-projects-todos-getorgprojectstodos
title: "To-dos: Get organization's to-dos"
tags: [endpoint, to-dos]
source: openapi.json (HighBond API v1.1.0)
---

## To-dos

To-dos are a collaboration tool between teammates and reviewers.

Learn more about to-dos.

### `GET /orgs/{org_id}/projects_todos` — Get organization's to-dos

- **operationId:** `getOrgProjectsTodos`
- **Domínio(s):** To-dos

Get a list of all projects to-dos in an organization.

> **Note:**
By default, this endpoint only returns to-dos from active projects. To fetch objects from frameworks, do one of the following:
> * Specify the project or framework ID using `filter[project.id]`
> * Specify that you want results from frameworks using `filter[project.state]=framework`

<details>
<summary><strong>Parâmetros</strong> (9)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `fields[projects_todos]` | query |  | string | Requesting the API to return only specific fields. For more information, see Making requests Ex.: `description,created_at,updated_at,due_date,status,project,target` |
| `filter[project.id]` | query |  | string | Requesting the API to filter results by project ID. For more information, see Making requests Ex.: `1` |
| `filter[project.state]` | query |  | string | Requesting the API to filter results by project state. For more information, see Making requests Ex.: `active` |
| `filter[target.id]` | query |  | string | Requesting the API to filter results by target ID. For more information, see Making requests Ex.: `1` |
| `filter[target.type]` | query |  | string | Requesting the API to filter results by target type. For more information, see Making requests Ex.: `test_plans` |
| `sort` | query |  | string | Orders the resulting resources by the given field. Sorts ascending by default, prefix with `-` to sort descending. You can provide multiple sort fields separated by comma. Valores: `status`, `created_at` Default: `id` |
| `page[size]` | query |  | string | The number of items returned per page. Default is 50. Maximum is 100. Ex.: `25` |
| `page[number]` | query |  | string | The Base64-encoded page number of records to return. Ex.: `Mg==` |

</details>

<details>
<summary><strong>Respostas</strong> (6)</summary>

<details>
<summary>`200` — OK.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `GetOrgProjectsTodosResponse`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | array[object] | ✅ |  |
| `data.id` | string | ✅ | The ID of the requested resource. Ex.: `"1"` |
| `data.type` | string | ✅ | The classification of the object (`"projects_todos"`). Ex.: `"projects_todos"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.description` | string |  | A detailed description of the todo. Ex.: `"Todo details"` |
| `data.attributes.created_at` | string |  | The timestamp identifying when the todo was created. Ex.: `"2021-01-18T13:17:26Z"` |
| `data.attributes.updated_at` | string |  | The timestamp identifying when the todo was last updated. Ex.: `"2021-01-18T13:17:26Z"` |
| `data.attributes.due_date` | string |  | Specifies when the todo should be fulfilled by. Ex.: `"2021-01-18"` |
| `data.attributes.status` | string |  | Status of the todo. Can have one of the following values - "open", "cleared", "closed". Ex.: `"open"` |
| `data.relationships` | object | ✅ | The relationships associated with the resource. |
| `data.relationships.project` | object |  | Specifies the project that the todo is associated with. |
| `data.relationships.project.data` | object |  | The data associated with a project. |
| `data.relationships.project.data.id` | string |  | The ID of the project. Ex.: `"1"` |
| `data.relationships.project.data.type` | string |  | The classification of the object (`"projects"`). Ex.: `"projects"` |
| `data.relationships.target` | object |  | Specifies the resource that the todo is associated with. |
| `data.relationships.target.data` | object | ✅ | The data associated with a project. |
| `data.relationships.target.data.id` | string | ✅ | The ID of the resource. Ex.: `"1"` |
| `data.relationships.target.data.type` | string | ✅ | The classification of the object.  A target can have one of the following types: `"projects"`, `"controls"`, `"control_tests"`, `"control_test_plans"`, `"issues"`, `"narratives"`, `"objectives"`, `"walkthrough_summaries"`, `"project_files"`, `"project_plannings"`, `"project_results"`, `"risks"`, `"risk_control_matrices"`, `"testing_rounds"`, `"walkthroughs"`. Ex.: `"objectives"` |
| `links` | object |  |  |
| `links.next` | string | ✅ | Next page url Ex.: `"/api/resource?page[number]=Mw=="` |
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
