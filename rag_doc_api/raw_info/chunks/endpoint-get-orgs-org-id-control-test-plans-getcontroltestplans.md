---
id: endpoint-get-orgs-org-id-control-test-plans-getcontroltestplans
title: "Test plans: Get organization test plans"
tags: [endpoint, control-test-plans]
source: openapi.json (HighBond API v1.1.0)
---

## Test plans

A test plan is a document that details how controls are assessed. Test plans identify the testing method or type of evidence obtained, specify the total sample size
(split amongst testing rounds), and illustrate test steps or attributes.

If your project includes at least one testing round, each control you create has one corresponding test plan.

> **Note:**
> * To access test plans using the API, the test plans tab must be enabled in the project type associated with the project or framework.
>
> Test plans located in such resources can be accessed using the API:
> * In Internal Control workflow projects that have an "active" state
> * In frameworks

Learn more about test plans.

### `GET /orgs/{org_id}/control_test_plans` — Get organization test plans

- **operationId:** `getControlTestPlans`
- **Domínio(s):** Control test plans

Get a list of all of the test plans in an organization.

> **Note:**
By default, this endpoint only returns test plans from active projects. To fetch objects from archived projects or frameworks, do one of the following:
> * Specify the project or framework ID using `filter[project.id]`
> * Specify that you want results from archived projects using `filter[project.state]=archive`
> * Specify that you want results from frameworks using `filter[project.state]=framework`

<details>
<summary><strong>Parâmetros</strong> (13)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `fields[control_test_plans]` | query |  | string | Requesting the API to return only the specified fields. For more information, see Making requests Ex.: `testing_method,total_sample_size,test_steps,created_at,updated_at,custom_attributes,control,framework_origin,preparer_signoff,detail_reviewer_signoff,general_reviewer_signoff,supplemental_reviewer,specialty_reviewer` |
| `page[size]` | query |  | string | The number of items returned per page. Default is 50. Maximum is 100. Ex.: `25` |
| `page[number]` | query |  | string | The Base64-encoded page number of records to return. Ex.: `Mg==` |
| `sort` | query |  | string | Requesting the API to sort test plans by the values in a given field. The test plans are sorted ascending by default, but you can prefix the field name with `-` to sort descending (e.g., `-id`). You can sort test plans by only one field at a time. Valores: `id`, `testing_method`, `total_sample_size`, `test_steps`, `created_at`, `updated_at` Default: `id` |
| `filter[project.id]` | query |  | string | Requesting the API to filter results by project ID. For more information, see Making requests Ex.: `1` |
| `filter[project.name]` | query |  | string | Requesting the API to filter results by project name. For more information, see Making requests Ex.: `some project name` |
| `filter[project.state]` | query |  | string | Requesting the API to filter results by project state. For more information, see Making requests Ex.: `active` |
| `filter[project.status]` | query |  | string | Requesting the API to filter results by project status. For more information, see Making requests Ex.: `active` |
| `filter[control.id]` | query |  | string | Requesting the API to filter results by control IDs. For more information, see Making requests Ex.: `1,2,3` |
| `include` | query |  | string | Requesting the API to return related resources. For more information, see Making requests Ex.: `control,control.objective` |
| `fields[objectives]` | query |  | string | Requesting the API to return only the specified fields. For more information, see Making requests Ex.: `title,description,reference,division_department,owner,executive_owner,created_at,updated_at,project,assigned_user,custom_attributes,position,risk_control_matrix_id,walkthrough_summary_id,testing_round_1_id,testing_round_2_id,testing_round_3_id,testing_round_4_id,entities,framework,framework_origin,risk_assurance_data,planned_start_date,actual_start_date,planned_end_date,actual_end_date,planned_milestone_date,actual_milestone_date` |
| `fields[controls]` | query |  | string | Requesting the API to return only the specified fields. For more information, see Making requests Ex.: `title,description,control_id,owner,frequency,control_type,prevent_detect,method,status,position,created_at,updated_at,custom_attributes,objective,walkthrough,control_test_plan,control_tests,mitigations,owner_user,entities,framework_origin` |

</details>

<details>
<summary><strong>Respostas</strong> (6)</summary>

<details>
<summary>`200` — OK.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `GetControlTestPlansResponse`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | array[object] | ✅ |  |
| `data.id` | string |  | The ID of the requested resource. Ex.: `1` |
| `data.type` | string |  | The classification of the object (`"control_test_plans"`). Ex.: `"control_test_plans"` |
| `data.attributes` | object |  | The attributes associated with the resource. |
| `data.attributes.testing_method` | string |  | The method specifying how evidence will be obtained. The exact values for this field depend on the configuration of the project type.  >**Note**: If the `testing_method` field has been disabled in the project type, the field is hidden from the API response. Ex.: `"Inspection"` |
| `data.attributes.total_sample_size` | integer |  | The total sample size, split among testing rounds. `total_sample_size` must be a value between `0` and `2147483647`.  Sample size is set when a test plan is created the first time, which occurs when you create a control. The logic used to automatically set the sample size field is based on two control attribute fields: `frequency` and `type`. For more information, see Executing procedures and testing controls.  >**Note**: If the `total_sample_size` field has been disabled in the project type, the field is hidden from the API response. Ex.: `1` |
| `data.attributes.test_steps` | string |  | The steps or attributes associated with the test plan. Ex.: `"<h1>Heading</h1><p>Test Steps description.</p>"` |
| `data.attributes.created_at` | string |  | The timestamp identifying when the test plan was created. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.attributes.updated_at` | string |  | The timestamp identifying when the test plan was updated. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.attributes.custom_attributes` | array[object] |  | An array of custom attributes defined on the project type used by the project this control test is from. Learn more about project types. Make a PATCH request to modify the value of a custom attribute. |
| `data.attributes.custom_attributes.id` | string |  | The ID of this custom attribute. Optional if term is included. Ex.: `"42"` |
| `data.attributes.custom_attributes.term` | string |  | The user defined term used to identify this custom attribute. Optional if id is included. Ex.: `"Custom Control Test Plan Attribute"` |
| `data.attributes.custom_attributes.value` | array[string] |  | The value or values (for multiselect) for this custom attribute. Ex.: `["Custom Select Option Text"]` |
| `data.relationships` | object |  | The relationships associated with the resource. |
| `data.relationships.control` | object |  | Each test plan has an associated control. A control is a program, policy, routine, or activity that is intended to mitigate a risk. |
| `data.relationships.control.data` | object | ✅ | The data associated with the resource. |
| `data.relationships.control.data.id` | string | ✅ | The ID of the control. Ex.: `"1"` |
| `data.relationships.control.data.type` | string | ✅ | The classification of the object (`"controls"`). Ex.: `"controls"` |
| `data.relationships.framework_origin` | object |  | In the Projects app, a project `control_test_plan` can have a related counterpart in an associated framework. The `framework_origin` attribute shows related counterpart of `control_test_plan` from a framework. |
| `data.relationships.framework_origin.data` | object | ✅ | The data associated with the resource. |
| `data.relationships.framework_origin.data.id` | string | ✅ | The ID of the parent control. Ex.: `"1"` |
| `data.relationships.framework_origin.data.type` | string | ✅ | The classification of the object (`"control_test_plans"`). Ex.: `"control_test_plans"` |
| `included` | array[object] |  | Included resources. Ex.: `[{"id": 1, "type": "controls", "attributes": {"title": "Control Title", "description": "Control description", "control_id": "001", "owner": "thomas...` |
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
