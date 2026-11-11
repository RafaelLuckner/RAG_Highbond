---
id: endpoint-get-orgs-org-id-controls-getorganizationcontrols
title: "Controls: Get all controls in an organization"
tags: [endpoint, controls]
source: openapi.json (HighBond API v1.1.0)
---

## Controls

A control is a program, policy, routine, or activity that is intended to mitigate a risk. Controls are organized by objectives, and can be associated with one or more risks.
The combination of identified risks and corresponding controls defines the Risk Control Matrix. Controls are also known as procedures.

> **Note:**
Controls located in such resources can be accessed using the API:
> * In projects that have an "active" state
> * In frameworks

Learn more about controls.

### `GET /orgs/{org_id}/controls` — Get all controls in an organization

- **operationId:** `getOrganizationControls`
- **Domínio(s):** Controls

Get a list of all of the controls in an organization.

> **Note:**
By default, this endpoint only returns controls from active projects. To fetch objects from archived projects or frameworks, do one of the following:
> * Specify the project or framework ID using `filter[project.id]`
> * Specify that you want results from archived projects using `filter[project.state]=archive`
> * Specify that you want results from frameworks using `filter[project.state]=framework`

<details>
<summary><strong>Parâmetros</strong> (33)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `fields[controls]` | query |  | string | Requesting the API to return only the specified fields. For more information, see Making requests Ex.: `title,description,control_id,owner,frequency,control_type,prevent_detect,method,status,position,created_at,updated_at,custom_attributes,objective,walkthrough,control_test_plan,control_tests,mitigations,owner_user,entities,framework_origin` |
| `fields[objectives]` | query |  | string | Requesting the API to return only the specified fields. For more information, see Making requests Ex.: `title,description,reference,division_department,owner,executive_owner,created_at,updated_at,project,assigned_user,custom_attributes,position,risk_control_matrix_id,walkthrough_summary_id,testing_round_1_id,testing_round_2_id,testing_round_3_id,testing_round_4_id,entities,framework,framework_origin,risk_assurance_data,planned_start_date,actual_start_date,planned_end_date,actual_end_date,planned_milestone_date,actual_milestone_date` |
| `fields[walkthroughs]` | query |  | string | Requesting the API to return only the specified fields. For more information, see Making requests Ex.: `walkthrough,control_verified,original_updated_at,preparer_signoff,detail_reviewer_signoff,general_reviewer_signoff,supplemental_reviewer,specialty_reviewer,control_performance_enabled,control_performance_readonly,signed_off,readonly,locked,enabled,planned_milestone_date,actual_milestone_date` |
| `fields[control_tests]` | query |  | string | Requesting the API to return only the specified fields. For more information, see Making requests Ex.: `assignee_name,testing_round_number,not_applicable,sample_size,testing_results,testing_conclusion,testing_conclusion_status,created_at,updated_at,control,assigned_user,actual_milestone_date,planned_milestone_date,preparer_signoff,detail_reviewer_signoff,general_reviewer_signoff,supplemental_reviewer,specialty_reviewer` |
| `sort` | query |  | string | Requesting the API to sort controls by the values in a given field. The controls are sorted ascending by default, but you can prefix the field name with `-` to sort descending (e.g., `-id`). You can sort controls by only one field at a time. Valores: `id`, `title`, `description`, `control_id`, `owner`, `control_tests.1.assigned_user.name`, `control_tests.2.assigned_user.name`, `control_tests.3.assigned_user.name`, `control_tests.4.assigned_user.name`, `control_tests.not_applicable`, `control_tests.testing_conclusion`, `control_tests.testing_conclusion_status`, `walkthrough.control_design`, `frequency`, `control_type`, `prevent_detect`, `method`, `status`, `position`, `created_at`, `updated_at`, `objective.title` Default: `id` |
| `filter[frequency]` | query |  | string | Requesting the API to filter results by frequency. For more information, see Making requests Ex.: `Multiple Times Daily` |
| `filter[owner]` | query |  | string | Requesting the API to filter results by owner. For more information, see Making requests Ex.: `some@example.com` |
| `filter[control_tests.1.assigned_user.id]` | query |  | string | Requesting the API to filter results by the user assigned to the first testing round. For more information, see Making requests Ex.: `uid1` |
| `filter[control_tests.2.assigned_user.id]` | query |  | string | Requesting the API to filter results by the user assigned to the second testing round. For more information, see Making requests Ex.: `uid1` |
| `filter[control_tests.3.assigned_user.id]` | query |  | string | Requesting the API to filter results by the user assigned to the third testing round. For more information, see Making requests Ex.: `uid1` |
| `filter[control_tests.4.assigned_user.id]` | query |  | string | Requesting the API to filter results by the user assigned to the fourth testing round. For more information, see Making requests Ex.: `uid1` |
| `filter[control_tests.not_applicable]` | query |  | string | Requesting the API to filter results to only include controls that are not being tested as part of any given testing round. For more information, see Making requests Valores: `true`, `false`, `` |
| `filter[control_tests.testing_conclusion]` | query |  | string | Requesting the API to filter results to only include controls that were marked as operating effectively. For more information, see Making requests Valores: `true`, `false`, `` |
| `filter[control_tests.testing_conclusion_status]` | query |  | string | Requesting the API to filter results to only include controls that were marked as operating effectively. For more information, see Making requests Ex.: `["Operating Effectively", "Exception(s) Noted"]` |
| `filter[walkthrough.control_design]` | query |  | string | Requesting the API to filter results to only include controls that were marked as designed appropriately. For more information, see Making requests Valores: `true`, `false`, `` |
| `filter[control_type]` | query |  | string | Requesting the API to filter results by control type. For more information, see Making requests Ex.: `Application/System Control` |
| `filter[status]` | query |  | string | Requesting the API to filter results by status. For more information, see Making requests Ex.: `Key Control` |
| `filter[objective.title]` | query |  | string | Requesting the API to filter results by objective title. For more information, see Making requests Ex.: `some objective title` |
| `filter[objective.name]` | query |  | string | Requesting the API to filter results by objective name. For more information, see Making requests Ex.: `some objective name` |
| `filter[objective.reference]` | query |  | string | Requesting the API to filter results by objective reference. For more information, see Making requests Ex.: `NM-INV` |
| `filter[project.id]` | query |  | string | Requesting the API to filter results by project ID. For more information, see Making requests Ex.: `1` |
| `filter[project.name]` | query |  | string | Requesting the API to filter results by project name. For more information, see Making requests Ex.: `some project name` |
| `filter[project.state]` | query |  | string | Requesting the API to filter results by project state. For more information, see Making requests Ex.: `active` |
| `filter[project.status]` | query |  | string | Requesting the API to filter results by project status. For more information, see Making requests Ex.: `active` |
| `filter[description]` | query |  | string | Requesting the API to filter results by control description. For more information, see Making requests Ex.: `Control description.` |
| `filter[title]` | query |  | string | Requesting the API to filter results by control title. For more information, see Making requests Ex.: `Control title.` |
| `filter[query]` | query |  | string | Requesting the API to filter results by control description, title, control_id or owner. For more information, see Making requests Ex.: `Control description or title.` |
| `filter[control_id]` | query |  | string | Requesting the API to filter results by control numbers. For more information, see Making requests Ex.: `001,002,003` |
| `filter[id]` | query |  | string | Requesting the API to filter results by control IDs. For more information, see Making requests Ex.: `1,2,3` |
| `include` | query |  | string | Requesting the API to return related resources. Valores: `objective`, `walkthough`, `control_tests`, `control_tests.assigned_user` Ex.: `objective,walkthough,control_tests,control_tests.assigned_user` |
| `page[size]` | query |  | string | The number of items returned per page. Default is 50. Maximum is 100. Ex.: `25` |
| `page[number]` | query |  | string | The Base64-encoded page number of records to return. Ex.: `Mg==` |

</details>

<details>
<summary><strong>Respostas</strong> (6)</summary>

<details>
<summary>`200` — OK.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `GetOrganizationControlsResponse`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | array[object] | ✅ | Array of controls |
| `data.id` | string | ✅ | The ID of the requested resource. Ex.: `"1"` |
| `data.type` | string | ✅ | The classification of the object (`"controls"`). Ex.: `"controls"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.title` | string |  | The title of the control. Ex.: `"Control Title"` |
| `data.attributes.description` | string |  | A detailed description of the control. Ex.: `"Control description"` |
| `data.attributes.control_id` | string |  | The reference number or code of the control. This field is known as the procedure reference number in Workplan workflow projects. Ex.: `"001"` |
| `data.attributes.owner` | string |  | The person responsible for the control. Specifying a person's name or email does not automatically send them an email notification about the control. Ex.: `"thomas@sodor.ca"` |
| `data.attributes.frequency` | string |  | A user configurable field that determines the default testing method and sample size in the test plan. The options available depends on the configuration of the project type.  >**Note**: This is a **required field** if the control belongs to an  Internal Control workflow project. If the control (procedure) belongs to a  Workplan workflow project, or if the `frequency` field has been disabled in the project type, the field is hidden from the API response.  For more information about the `frequency` field, see Executing procedures and testing controls. Ex.: `"Daily"` |
| `data.attributes.control_type` | string |  | A user configurable field that determines the default testing method and sample size in the test plan. The options available depends on the configuration of the project type.  >**Note**: This is a **required field** if the control belongs to an  Internal Control workflow project. If the control (procedure) belongs to a  Workplan workflow project, or if the `control_type` field has been disabled in the project type, the field is hidden from the API response.  For more information about the `control_type` field, see Executing procedures and testing controls. Ex.: `"Application/System Control"` |
| `data.attributes.prevent_detect` | string |  | A user configurable field that specifies whether the control is intended to prevent or detect risk, or if it is not applicable. The options available depends on the configuration of the project type.  >**Note**: This is a **required field** if the control belongs to an  Internal Control workflow project. If the control (procedure) belongs to a  Workplan workflow project, or if the `prevent_detect` field has been disabled in the project type, the field is hidden from the API response. Ex.: `"Prevent"` |
| `data.attributes.method` | string |  | A user configurable field that specifies how the control will be tested or implemented. The options available depends on the configuration of the project type.  >**Note**: If the control (procedure) belongs to a  Workplan workflow project, or if the `method` field has been disabled in the project type, the field is hidden from the API response. Ex.: `"Management Review"` |
| `data.attributes.status` | string |  | A user configurable field that specifies the current state of the control. The options available depends on the configuration of the project type.  >**Note**: If the control (procedure) belongs to a  Workplan workflow project, or if the `status` field has been disabled in the project type, the field is hidden from the API response. Ex.: `"Key Control"` |
| `data.attributes.position` | integer |  | The value that determines the order in which it is displayed in the index action. `position` must be a value between `1` and `2147483647`. Ex.: `1` |
| `data.attributes.created_at` | string |  | The timestamp identifying when the control was created. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.attributes.updated_at` | string |  | The timestamp identifying when the control was last updated. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.attributes.custom_attributes` | array[object] |  | An array of custom attributes defined by the user that are available on this object. |
| `data.attributes.custom_attributes.id` | string |  | The ID of the custom attribute that this custom attribute value is for. Optional if term is included. Ex.: `"42"` |
| `data.attributes.custom_attributes.term` | string |  | The user defined term used to identify the custom attribute. Optional if id is included. Ex.: `"Custom Control Attribute"` |
| `data.attributes.custom_attributes.value` | array[string] |  | The value or values (for multiselect) to set this custom attribute to. Ex.: `["Custom Select Option Text"]` |
| `data.relationships` | object |  | The relationships associated with the resource. |
| `data.relationships.objective` | object | ✅ | Each control has an associated objective. Objectives are the organizing containers for the work done in a project or framework. |
| `data.relationships.objective.data` | object | ✅ | The data associated with the resource. |
| `data.relationships.objective.data.id` | string | ✅ | The ID of the objective. Ex.: `"1"` |
| `data.relationships.objective.data.type` | string | ✅ | The classification of the object (`"objectives"`). Ex.: `"objectives"` |
| `data.relationships.walkthrough` | object |  | Each control has an associated walkthrough. A walkthrough is a series of steps you perform to establish the reliability of controls and test the design of controls.  To return this field, you must specify the `fields[controls]=walkthrough` parameter in your request. For more information, see Making requests. |
| `data.relationships.walkthrough.data` | object | ✅ | The data associated with the resource. |
| `data.relationships.walkthrough.data.id` | string | ✅ | The ID of the walkthrough. Ex.: `"1"` |
| `data.relationships.walkthrough.data.type` | string | ✅ | The classification of the object (`"walkthroughs"`). Ex.: `"walkthroughs"` |
| `data.relationships.control_test_plan` | object |  | Each control has an associated control test plan. A test plan is a document that details how controls are assessed.  To return this field, you must specify the `fields[controls]=control_test_plans` parameter in your request. For more information, see Making requests. |
| `data.relationships.control_test_plan.data` | object | ✅ | The data associated with the resource. |
| `data.relationships.control_test_plan.data.id` | string | ✅ | The ID of the test plan. Ex.: `"1"` |
| `data.relationships.control_test_plan.data.type` | string | ✅ | The classification of the object (`"control_test_plans"`). Ex.: `"control_test_plans"` |
| `data.relationships.control_tests` | object |  | Control tests evaluate the operating effectiveness of a control.  If your project includes one testing round, each control you create has one corresponding control test. If your project includes multiple testing rounds, each control you create has a corresponding series of control tests.  To return this field, you must specify the `fields[controls]=control_tests` parameter in your request. For more information, see Making requests. |
| `data.relationships.control_tests.data` | array[object] | ✅ |  |
| `data.relationships.control_tests.data.id` | string | ✅ | The ID of the control test. Ex.: `"1"` |
| `data.relationships.control_tests.data.type` | string | ✅ | The classification of the object (`"control_tests"`). Ex.: `"control_tests"` |
| `data.relationships.mitigations` | object |  | To return this field, you must specify the `fields[controls]=mitigations` parameter in your request. For more information, see Making requests. |
| `data.relationships.mitigations.data` | array[object] | ✅ |  |
| `data.relationships.mitigations.data.id` | string | ✅ | The ID of the mitigation. Ex.: `"1"` |
| `data.relationships.mitigations.data.type` | string | ✅ | The classification of the object (`"mitigations"`). Ex.: `"mitigations"` |
| `data.relationships.framework_origin` | object |  | In the Projects app, a project `control` can have a related counterpart in an associated framework. The `framework_origin` attribute allows you to associate an `control` and related `control_test_plan` in a project with its related counterpart in a framework. |
| `data.relationships.framework_origin.data` | object | ✅ | The data associated with the resource. |
| `data.relationships.framework_origin.data.id` | string | ✅ | The ID of the parent control. Ex.: `"1"` |
| `data.relationships.framework_origin.data.type` | string | ✅ | The classification of the object (`"controls"`). Ex.: `"controls"` |
| `data.relationships.owner_user` | object |  | Specifies the user responsible for the control. A value in this field will override any value provided in the `owner` attribute. Specifiying a user will automatically send them an email notification about the control.  To return this field, you must specify the `fields[controls]=owner_user` parameter in your request. For more information, see Making requests. |
| `data.relationships.owner_user.data` | object | ✅ | The data associated with the resource. |
| `data.relationships.owner_user.data.id` | string | ✅ | The unique identifier (UID) of the user. For more information on obtaining this value, see Making requests. Ex.: `"3NQ6XzAUxqJMnAQ7n4KF"` |
| `data.relationships.owner_user.data.type` | string | ✅ | The classification of the object (`"users"`). Ex.: `"users"` |
| `data.relationships.entities` | object |  | Each control has an associated control entities. |
| `data.relationships.entities.data` | array[object] | ✅ | The data associated with the resource. |
| `data.relationships.entities.data.id` | string | ✅ | The ID of the entity. Ex.: `"1"` |
| `data.relationships.entities.data.type` | string | ✅ | The classification of the object (`"entities"`). Ex.: `"entities"` |
| `included` | array[object] |  | Included resources. Ex.: `[{"id": 1, "type": "objectives", "attributes": {"title": "The title of the objective"}}, {"id": 2, "type": "walkthoughs", "attributes": {"walkthrou...` |
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
