---
id: endpoint-get-orgs-org-id-projects-project-id-results-files-getresultsfiles
title: "Results files: Get results files"
tags: [endpoint, results-files]
source: openapi.json (HighBond API v1.1.0)
---

## Results files

A results file is a supporting document or concluding memo that relates to a project. Results files typically contain information associated
with the reporting phase of a project.

> **Note —**
Only results files in projects that have an `"active"` state can be accessed using the API.

Learn more about results files.

### `GET /orgs/{org_id}/projects/{project_id}/results_files` — Get results files

- **operationId:** `getResultsFiles`
- **Domínio(s):** Results files

Get results files that belong to a project.

<details>
<summary><strong>Parâmetros</strong> (5)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `project_id` | path | ✅ | integer | The ID of the project. Ex.: `1` |
| `fields[results_files]` | query |  | string | Requesting the API to return only the specified fields. For more information, see Making requests Ex.: `name,reference_id,description,position,created_at,updated_at,custom_attributes,project,planned_start_date,actual_start_date,planned_end_date,actual_end_date,planned_milestone_date,actual_milestone_date` |
| `page[size]` | query |  | string | The number of items returned per page. Default is 50. Maximum is 100. Ex.: `25` |
| `page[number]` | query |  | string | The Base64-encoded page number of records to return. Ex.: `Mg==` |

</details>

<details>
<summary><strong>Respostas</strong> (6)</summary>

<details>
<summary>`200` — OK.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `GetResultsFilesResponse`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | array[object] | ✅ |  |
| `data.id` | string | ✅ | The ID of the requested resource. Ex.: `1` |
| `data.type` | string | ✅ | The classification of the object (`"results_files"`). Ex.: `"results_files"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.name` | string |  | The name of the results file. Ex.: `"Results File Name"` |
| `data.attributes.reference_id` | string |  | The results id, reference number, or code for the results file. Ex.: `"BPWS1"` |
| `data.attributes.description` | string |  | A detailed description of the results file. Ex.: `"<h1>Results file heading</h1><p>Results file description.</p>"` |
| `data.attributes.position` | integer |  | The value that determines the order in which it is displayed in the index action. `position` must be a value between `1` and `2147483647`. Ex.: `1` |
| `data.attributes.custom_attributes` | array[object] |  | An array of custom attributes defined on the project type used by the project this results file is from. Learn more about project types. Make a PATCH request to modify the value of a custom attribute. |
| `data.attributes.custom_attributes.id` | string |  | The ID of this custom attribute. Optional if term is included. Ex.: `"42"` |
| `data.attributes.custom_attributes.term` | string |  | The user defined term used to identify this custom attribute. Optional if id is included. Ex.: `"Custom Results Attribute"` |
| `data.attributes.custom_attributes.value` | array[string] |  | The value or values (for multiselect) for this custom attribute. Ex.: `["Custom Select Option Text"]` |
| `data.attributes.created_at` | string |  | The timestamp identifying when the results file was created. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.attributes.updated_at` | string |  | The timestamp identifying when the results file was updated. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.attributes.planned_start_date` | string |  | Planned start date Ex.: `"2019-02-09"` |
| `data.attributes.planned_end_date` | string |  | Planned end date. Ex.: `"2019-02-10"` |
| `data.attributes.actual_start_date` | string |  | Actual start date. Ex.: `"2019-02-09"` |
| `data.attributes.actual_end_date` | string |  | Actual end date. Ex.: `"2019-02-10"` |
| `data.attributes.actual_milestone_date` | string |  | Actual milestone date. Ex.: `"2019-02-10"` |
| `data.attributes.planned_milestone_date` | string |  | Planned milestone date. Ex.: `"2019-02-09"` |
| `data.relationships` | object |  | The relationships associated with the resource. |
| `data.relationships.project` | object | ✅ | Each results file has an associated project. A project is a management system that allows you to define and compile information for reporting purposes. |
| `data.relationships.project.data` | object | ✅ | The data associated with the object. |
| `data.relationships.project.data.id` | string | ✅ | The ID of the project. Ex.: `"1"` |
| `data.relationships.project.data.type` | string | ✅ | The classification of the object (`"projects"`). Ex.: `"projects"` |
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
