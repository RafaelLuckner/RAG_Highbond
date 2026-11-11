---
id: endpoint-patch-orgs-org-id-objectives-id-updateobjective
title: "Objectives: Update an objective"
tags: [endpoint, objectives]
source: openapi.json (HighBond API v1.1.0)
---

## Objectives

Objectives are the basis of a project or framework. They are also the organizing containers for the work done in a project or framework.
Each objective states the subject matter under examination and how performance will be assessed.

Objectives may also be known as sections, processes, cycles, functional areas, application systems, risk categories, or another custom term.

> **Note:**
Objectives located in such resources can be accessed using the API:
> * In projects that have an "active" state
> * In frameworks

Learn more about objectives.

### `PATCH /orgs/{org_id}/objectives/{id}` — Update an objective

- **operationId:** `updateObjective`
- **Domínio(s):** Objectives

Make changes to an objective in a project or framework, like renaming the objective or specifying an owner.

Limitations:
* You cannot update the objective if it has been checked out using
Offline Projects or the
HighBond iPad app.
* Specifying a person's name or email in the following fields does not automatically notify them via email: `owner`, `executive_owner`.

<details>
<summary><strong>Parâmetros</strong> (3)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `id` | path | ✅ | string | The ID of the requested resource. Ex.: `9999` |
| `fields[objectives]` | query |  | string | Requesting the API to return only the specified fields. For more information, see Making requests Ex.: `title,description,reference,division_department,owner,executive_owner,created_at,updated_at,project,assigned_user,custom_attributes,position,risk_control_matrix_id,walkthrough_summary_id,testing_round_1_id,testing_round_2_id,testing_round_3_id,testing_round_4_id,entities,framework,framework_origin,risk_assurance_data,planned_start_date,actual_start_date,planned_end_date,actual_end_date,planned_milestone_date,actual_milestone_date` |

</details>

<details>
<summary><strong>Request body (payload)</strong></summary>

The data required to update an objective.

**Body obrigatório.**

**Content-Type:** `application/vnd.api+json`

**Schema:** `UpdateObjectiveRequest`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | object | ✅ | The data associated with the resource. |
| `data.id` | string | ✅ | The ID of the requested resource. Ex.: `"1"` |
| `data.type` | string | ✅ | The classification of the object (`"objectives"`). Ex.: `"objectives"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.title` | string | ✅ | The title of the objective. Ex.: `"Objective Title"` |
| `data.attributes.reference` | string | ✅ | The reference number or code for the objective. Ex.: `"ITC"` |
| `data.attributes.description` | string |  | A detailed description of the objective. Ex.: `"Objective description"` |
| `data.attributes.division_department` | string |  | The division or department responsible for the objective. Ex.: `"Finance"` |
| `data.attributes.owner` | string |  | The person responsible for the objective. Specifying a person's name or email does not automatically send them an email notification about the objective. Ex.: `"thomas@sodor.ca"` |
| `data.attributes.executive_owner` | string |  | The executive owner of the objective. Specifying a person's name or email does not automatically send them an email notification about the objective. Ex.: `"henry@sodor.com"` |
| `data.attributes.position` | integer |  | The value that determines the order in which it is displayed in the index action. `position` must be a value between `1` and `2147483647`. Ex.: `1` |
| `data.attributes.custom_attributes` | array[object] |  | An array of custom attributes defined on the project type used by the project this objective is from. Learn more about project types. Make a PATCH request to modify the value of a custom attribute. |
| `data.attributes.custom_attributes.id` | string |  | The ID of this custom attribute. Optional if term is included. Ex.: `"42"` |
| `data.attributes.custom_attributes.term` | string |  | The user defined term used to identify this custom attribute. Optional if id is included. Ex.: `"Custom Objective Attribute"` |
| `data.attributes.custom_attributes.value` | array[string] |  | The value or values (for multiselect) for this custom attribute. Ex.: `["Custom Select Option Text"]` |
| `data.attributes.planned_start_date` | string |  | Planned start date Ex.: `"2019-02-09"` |
| `data.attributes.planned_end_date` | string |  | Planned end date. Ex.: `"2019-02-10"` |
| `data.attributes.actual_start_date` | string |  | Actual start date. Ex.: `"2019-02-09"` |
| `data.attributes.actual_end_date` | string |  | Actual end date. Ex.: `"2019-02-10"` |
| `data.attributes.actual_milestone_date` | string |  | Actual milestone date. Ex.: `"2019-02-10"` |
| `data.attributes.planned_milestone_date` | string |  | Planned milestone date. Ex.: `"2019-02-09"` |
| `data.relationships` | object |  | The relationships associated with the resource. |
| `data.relationships.assigned_user` | object |  | The person assigned to the objective. Only users assigned the Professional Manager or Professional User role in the project can be specified. The user specified receives an email notification with a link to the objective, is able to view the objective on the project dashboard, and has full read and write access to the objective. |
| `data.relationships.assigned_user.data` | object | ✅ | The data associated with the resource. |
| `data.relationships.assigned_user.data.id` | string | ✅ | The unique identifier (UID) of the assigned user. For more information on obtaining this value, see Making requests. Ex.: `"3NQ6XzAUxqJMnAQ7n4KF"` |
| `data.relationships.assigned_user.data.type` | string | ✅ | The classification of the object (`"users"`). Ex.: `"users"` |
| `data.relationships.entities` | object |  | The passed entities list should match the following conditions: 1. It should be the full exact list of entities you would like to be linked to the resource.  2. The passed entities should consist of valid sub-trees with all ancestor entities as well as descendent entities.  3. Inherited entities should be included too.  Otherwise, the whole request will be rejected with the corresponding error. |
| `data.relationships.entities.data` | array[object] |  |  |
| `data.relationships.entities.data.id` | string |  | The ID of the entity. Ex.: `"1"` |
| `data.relationships.entities.data.type` | string |  | The classification of the object (`"entities"`). Ex.: `"entities"` |
| `data.relationships.framework_origin` | object |  | In the Projects app, a project `objective` can have a related counterpart in an associated framework. The `framework_origin` attribute allows you to associate an `objective` in a project with its related counterpart in a framework. Can be set only when `parent_resource_type` is `projects`. |
| `data.relationships.framework_origin.data` | object | ✅ | The data associated with the resource. |
| `data.relationships.framework_origin.data.id` | string | ✅ | The ID of the parent objective. Ex.: `"1"` |
| `data.relationships.framework_origin.data.type` | string | ✅ | The classification of the object (`"objectives"`). Ex.: `"objectives"` |

</details>

<details>
<summary><strong>Respostas</strong> (7)</summary>

<details>
<summary>`200` — OK.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `GetObjectiveResponseWithIncludes`

_Apenas campos que diferem do request body. 28 campo(s) idênticos omitidos._

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data.attributes.risk_control_matrix_id` | string |  | The id of the risk control matrix. Ex.: `"100"` |
| `data.attributes.walkthrough_summary_id` | string |  | The id of the walkthrough summary. Ex.: `"200"` |
| `data.attributes.testing_round_1_id` | string |  | The id of testing round 1 (if applicable). Ex.: `"301"` |
| `data.attributes.testing_round_2_id` | string |  | The id of testing round 2 (if applicable). Ex.: `"302"` |
| `data.attributes.testing_round_3_id` | string |  | The id of testing round 3 (if applicable). Ex.: `"303"` |
| `data.attributes.testing_round_4_id` | string |  | The id of testing round 4 (if applicable). Ex.: `"304"` |
| `data.attributes.created_at` | string |  | The timestamp identifying when the objective was created. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.attributes.updated_at` | string |  | The timestamp identifying when the objective was last updated. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.attributes.risk_assurance_data` | object |  | Fields that determines assurance values. Assurance is an expression of confidence that risk is effectively mitigated. Returns `null` if Risk Assurance feature is disabled. |
| `data.attributes.risk_assurance_data.inherent_risk` | number |  | The risk that an activity would pose if no controls or other mitigating factors were in place. Can also be referred to as the gross risk, or risks before controls, and can act as the baseline for your organization's risk tolerance or appetite. Ex.: `1.1` |
| `data.attributes.risk_assurance_data.residual_risk` | number |  | The risk that remains after controls are taken into account. Can also be referred to as the net risk or risk after controls. Ex.: `1.1` |
| `data.attributes.risk_assurance_data.assurance` | number |  | The level of assurance that the controls in place effectively mitigate risk to the business. Ex.: `0` |
| `data.relationships` | object | ✅ | The relationships associated with the resource. |
| `data.relationships.project` | object |  | Each objective has an associated project or framework. Project/framework is a management system that allows you to define and compile information for reporting purposes. |
| `data.relationships.project.data` | object | ✅ | The data associated with the resource. |
| `data.relationships.project.data.id` | string | ✅ | The ID of the project. Ex.: `"1"` |
| `data.relationships.project.data.type` | string | ✅ | The classification of the object (`"projects"`). Ex.: `"projects"` |
| `data.relationships.framework` | object |  | Each objective has an associated project or framework. Project/framework is a management system that allows you to define and compile information for reporting purposes. |
| `data.relationships.framework.data` | object | ✅ | The data associated with the resource. |
| `data.relationships.framework.data.id` | string | ✅ | The ID of the framework. Ex.: `"1"` |
| `data.relationships.framework.data.type` | string | ✅ | The classification of the object (`"frameworks"`). Ex.: `"frameworks"` |
| `data.relationships.assigned_user` | object | ✅ | The person assigned to the objective. Only users assigned the Professional Manager or Professional User role in the project can be specified. The user specified receives an email notification with a link to the objective, is able to view the objective on the project dashboard, and has full read and write access to the objective. |
| `data.relationships.entities` | object |  | Each objective has an associated objective entities. |
| `data.relationships.entities.data` | array[object] | ✅ | The data associated with the resource. |
| `data.relationships.entities.data.id` | string | ✅ | The ID of the entity. Ex.: `"1"` |
| `data.relationships.entities.data.type` | string | ✅ | The classification of the object (`"entities"`). Ex.: `"entities"` |

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
