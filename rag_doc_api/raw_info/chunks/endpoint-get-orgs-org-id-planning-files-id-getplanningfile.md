---
id: endpoint-get-orgs-org-id-planning-files-id-getplanningfile
title: "Planning files: Get a planning file"
tags: [endpoint, planning-files]
source: openapi.json (HighBond API v1.1.0)
---

## Planning files

A planning file (also known as a reference file) is a supporting document that relates to a project or framework. Planning files typically
contain information associated with the planning phase of a project or framework.

> **Note:**
Planning files located in such resources can be accessed using the API:
> * In projects that have an "active" state
> * In frameworks

Learn more about planning files.

### `GET /orgs/{org_id}/planning_files/{id}` — Get a planning file

- **operationId:** `getPlanningFile`
- **Domínio(s):** Planning files

Get information about a planning file.

Limitation:
Existing Citation Mode highlights and links are not displayed in the `description` field.

<details>
<summary><strong>Parâmetros</strong> (3)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `id` | path | ✅ | string | The ID of the requested resource. Ex.: `9999` |
| `fields[planning_files]` | query |  | string | Requesting the API to return only the specified fields. For more information, see Making requests Ex.: `name,reference_id,description,position,created_at,updated_at,custom_attributes,project,framework,planned_start_date,actual_start_date,planned_end_date,actual_end_date,planned_milestone_date,actual_milestone_date` |

</details>

<details>
<summary><strong>Respostas</strong> (5)</summary>

<details>
<summary>`200` — OK.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `GetPlanningFileResponse`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | object | ✅ | The data associated with the resource. |
| `data.id` | string | ✅ | The ID of the requested resource. Ex.: `1` |
| `data.type` | string | ✅ | The classification of the object (`"planning_files"`). Ex.: `"planning_files"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.name` | string |  | The name of the planning file. Ex.: `"Planning File Name"` |
| `data.attributes.reference_id` | string |  | The planning id, reference number, or code for the planning file. Ex.: `"BPWS1"` |
| `data.attributes.description` | string |  | A detailed description of the planning file. Ex.: `"<h1>Planning file heading</h1><p>Planning file description.</p>"` |
| `data.attributes.position` | integer |  | The value that determines the order in which it is displayed in the index action. `position` must be a value between `1` and `2147483647`. Ex.: `1` |
| `data.attributes.custom_attributes` | array[object] |  | An array of custom attributes defined on the project type used by the project this planning file is from. Learn more about project types. Make a PATCH request to modify the value of a custom attribute. |
| `data.attributes.custom_attributes.id` | string |  | The ID of this custom attribute. Optional if term is included. Ex.: `"42"` |
| `data.attributes.custom_attributes.term` | string |  | The user defined term used to identify this custom attribute. Optional if id is included. Ex.: `"Custom Planning Attribute"` |
| `data.attributes.custom_attributes.value` | array[string] |  | The value or values (for multiselect) for this custom attribute. Ex.: `["Custom Select Option Text"]` |
| `data.attributes.created_at` | string |  | The timestamp identifying when the planning file was created. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.attributes.updated_at` | string |  | The timestamp identifying when the planning file was updated. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.attributes.planned_start_date` | string |  | Planned start date Ex.: `"2019-02-09"` |
| `data.attributes.planned_end_date` | string |  | Planned end date. Ex.: `"2019-02-10"` |
| `data.attributes.actual_start_date` | string |  | Actual start date. Ex.: `"2019-02-09"` |
| `data.attributes.actual_end_date` | string |  | Actual end date. Ex.: `"2019-02-10"` |
| `data.attributes.actual_milestone_date` | string |  | Actual milestone date. Ex.: `"2019-02-10"` |
| `data.attributes.planned_milestone_date` | string |  | Planned milestone date. Ex.: `"2019-02-09"` |
| `data.relationships` | object |  | The relationships associated with the resource. |
| `data.relationships.project` | object | ✅ | Each planning file has an associated project or framework. A project/framework is a management system that allows you to define and compile information for reporting purposes. |
| `data.relationships.project.data` | object | ✅ | The data associated with the object. |
| `data.relationships.project.data.id` | string | ✅ | The ID of the project. Ex.: `"1"` |
| `data.relationships.project.data.type` | string | ✅ | The classification of the object (`"projects"`). Ex.: `"projects"` |
| `data.relationships.framework` | object |  | Each planning file has an associated project or framework. A project/framework is a management system that allows you to define and compile information for reporting purposes. |
| `data.relationships.framework.data` | object | ✅ | The data associated with the object. |
| `data.relationships.framework.data.id` | string | ✅ | The ID of the framework. Ex.: `"1"` |
| `data.relationships.framework.data.type` | string | ✅ | The classification of the object (`"frameworks"`). Ex.: `"frameworks"` |

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

</details>
