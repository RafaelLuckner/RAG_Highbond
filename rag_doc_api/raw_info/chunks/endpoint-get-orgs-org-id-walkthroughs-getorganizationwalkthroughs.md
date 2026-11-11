---
id: endpoint-get-orgs-org-id-walkthroughs-getorganizationwalkthroughs
title: "Walkthroughs: Get organization walkthroughs"
tags: [endpoint, walkthroughs]
source: openapi.json (HighBond API v1.1.0)
---

## Walkthroughs

A walkthrough is a series of steps you perform to establish the reliability of controls and test the design of controls. Each control you define has a corresponding
walkthrough that is used to verify that the control is designed appropriately. In a Workplan workflow project, a walkthrough is called an execute procedure.

> **Note**
> * Only walkthroughs in projects that have an `"active"` state can be accessed using the API.
> * To access walkthroughs using the API, the walkthroughs tab must be enabled in the project type associated with the project.

Learn more about walkthroughs.

### `GET /orgs/{org_id}/walkthroughs` — Get organization walkthroughs

- **operationId:** `getOrganizationWalkthroughs`
- **Domínio(s):** Walkthroughs

Get a list of all of the walkthroughs in an organization.

> **Note:**
By default, this endpoint only returns walkthroughs from active projects. To fetch objects from archived projects or frameworks, do one of the following:
> * Specify the project or framework ID using `filter[project.id]`
> * Specify that you want results from archived projects using `filter[project.state]=archive`
> * Specify that you want results from frameworks using `filter[project.state]=framework`

<details>
<summary><strong>Parâmetros</strong> (27)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `fields[walkthroughs]` | query |  | string | Requesting the API to return only the specified fields. For more information, see Making requests Ex.: `walkthrough_results,control_design,created_at,updated_at,custom_attributes,control,planned_milestone_date,actual_milestone_date` |
| `page[size]` | query |  | string | The number of items returned per page. Default is 50. Maximum is 100. Ex.: `25` |
| `page[number]` | query |  | string | The Base64-encoded page number of records to return. Ex.: `Mg==` |
| `sort` | query |  | string | Requesting the API to sort walkthroughs by the values in a given field. The walkthroughs are sorted ascending by default, but you can prefix the field name with `-` to sort descending (e.g., `-id`). You can sort walkthroughs by only one field at a time. Valores: `id`, `walkthrough_results`, `control_design`, `created_at`, `updated_at` Default: `id` |
| `filter[project.id]` | query |  | string | Requesting the API to filter results by project ID. For more information, see Making requests Ex.: `1` |
| `filter[project.name]` | query |  | string | Requesting the API to filter results by project name. For more information, see Making requests Ex.: `some project name` |
| `filter[project.state]` | query |  | string | Requesting the API to filter results by project state. For more information, see Making requests Ex.: `active` |
| `filter[project.status]` | query |  | string | Requesting the API to filter results by project status. For more information, see Making requests Ex.: `active` |
| `filter[control.id]` | query |  | string | Requesting the API to filter results by control IDs. For more information, see Making requests Ex.: `1,2,3` |
| `filter[control_design]` | query |  | string | Requesting the API to filter results to only include walkthroughs that were marked as designed appropriately. For more information, see Making requests Valores: `true`, `false`, `` |
| `filter[objective.title]` | query |  | string | Requesting the API to filter results by objective title. For more information, see Making requests Ex.: `some objective title` |
| `filter[objective.reference]` | query |  | string | Requesting the API to filter results by objective reference. For more information, see Making requests Ex.: `ITC` |
| `filter[control.control_id]` | query |  | string | Requesting the API to filter results by numbers of the control. For more information, see Making requests Ex.: `001,002,003` |
| `filter[control.title]` | query |  | string | Requesting the API to filter results by control title. For more information, see Making requests Ex.: `some control title` |
| `filter[control.query]` | query |  | string | Requesting the API to filter results by control title or description. For more information, see Making requests Ex.: `some control title or description` |
| `filter[control.status]` | query |  | string | Requesting the API to filter results by control status. For more information, see Making requests Ex.: `Key Control` |
| `filter[control.owner]` | query |  | string | Requesting the API to filter results by control owner. For more information, see Making requests Ex.: `some@example.com` |
| `filter[control.frequency]` | query |  | string | Requesting the API to filter results by control frequency. For more information, see Making requests Ex.: `Multiple Times Daily` |
| `filter[control.control_type]` | query |  | string | Requesting the API to filter results by control type. For more information, see Making requests Ex.: `Application/System Control` |
| `filter[control.control_tests.1.assigned_user.id]` | query |  | string | Requesting the API to filter results by the user assigned to the first testing round in the related control. For more information, see Making requests Ex.: `uid1` |
| `filter[control.control_tests.2.assigned_user.id]` | query |  | string | Requesting the API to filter results by the user assigned to the second testing round in the related control. For more information, see Making requests Ex.: `uid1` |
| `filter[control.control_tests.3.assigned_user.id]` | query |  | string | Requesting the API to filter results by the user assigned to the third testing round in the related control. For more information, see Making requests Ex.: `uid1` |
| `filter[control.control_tests.4.assigned_user.id]` | query |  | string | Requesting the API to filter results by the user assigned to the fourth testing round in the related control. For more information, see Making requests Ex.: `uid1` |
| `include` | query |  | string | Requesting the API to return related resources. For more information, see Making requests Ex.: `control,control.objective` |
| `fields[controls]` | query |  | string | Requesting the API to return only the specified fields. For more information, see Making requests Ex.: `title,description,control_id,owner,frequency,control_type,prevent_detect,method,status,position,created_at,updated_at,custom_attributes,objective,walkthrough,control_test_plan,control_tests,mitigations,owner_user,entities,framework_origin` |
| `fields[objectives]` | query |  | string | Requesting the API to return only the specified fields. For more information, see Making requests Ex.: `title,description,reference,division_department,owner,executive_owner,created_at,updated_at,project,assigned_user,custom_attributes,position,risk_control_matrix_id,walkthrough_summary_id,testing_round_1_id,testing_round_2_id,testing_round_3_id,testing_round_4_id,entities,framework,framework_origin,risk_assurance_data,planned_start_date,actual_start_date,planned_end_date,actual_end_date,planned_milestone_date,actual_milestone_date` |

</details>

<details>
<summary><strong>Respostas</strong> (6)</summary>

<details>
<summary>`200` — OK.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `GetWalkthroughsResponse`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | array[object] | ✅ |  |
| `data.id` | string | ✅ | The ID of the requested resource. Ex.: `1` |
| `data.type` | string | ✅ | The classification of the object (`"walkthroughs"`). Ex.: `"walkthroughs"` |
| `data.attributes` | object |  | The attributes associated with the resource. |
| `data.attributes.walkthrough_results` | string |  | A description that captures the results of performing the walkthrough. Ex.: `"<h1>Heading</h1><p>Walkthrough results description.</p>"` |
| `data.attributes.created_at` | string |  | The timestamp identifying when the walkthrough was created. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.attributes.updated_at` | string |  | The timestamp identifying when the walkthrough was updated. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.attributes.actual_milestone_date` | string |  | Actual milestone date. Ex.: `"2019-02-10"` |
| `data.attributes.planned_milestone_date` | string |  | Planned milestone date. Ex.: `"2019-02-09"` |
| `data.attributes.control_design` | boolean |  | A rating that specifies whether the control design passes (`true`) or fails (`false`).  The exact values for this field (E.g. "Designed Appropriately" / "No Issues" and "Design Failure" / "Issue(s) Noted") depend on the configuration of the project type.  `true` maps to the first customizable value (E.g. "Designed Appropriately" / "No Issues") and `false` maps to the second customizable value (E.g. "Design Failure" / "Issue(s) Noted") in the project type. Ex.: `true` |
| `data.attributes.custom_attributes` | array[object] |  | An array of custom attributes defined on the project type used by the project this walkthrough is from. Learn more about project types. Make a PATCH request to modify the value of a custom attribute. |
| `data.attributes.custom_attributes.id` | string |  | The ID of this custom attribute. Optional if term is included. Ex.: `"42"` |
| `data.attributes.custom_attributes.term` | string |  | The user defined term used to identify this custom attribute. Optional if id is included. Ex.: `"Custom Walkthrough Attribute"` |
| `data.attributes.custom_attributes.value` | array[string] |  | The value or values (for multiselect) for this custom attribute. Ex.: `["Custom Select Option Text"]` |
| `data.relationships` | object | ✅ | The relationships associated with the resource. |
| `data.relationships.control` | object | ✅ | The attributes associated with the resource. |
| `data.relationships.control.data` | object | ✅ | The data associated with the resource. |
| `data.relationships.control.data.id` | string | ✅ | The ID of the control. Ex.: `"1"` |
| `data.relationships.control.data.type` | string | ✅ | The classification of the object (`"controls"`). Ex.: `"controls"` |
| `included` | array[object] |  | Included resources. Ex.: `[{"id": 1, "type": "control", "attributes": {"title": "Control Title", "description": "Control description", "control_id": "001", "owner": "thomas@...` |
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
