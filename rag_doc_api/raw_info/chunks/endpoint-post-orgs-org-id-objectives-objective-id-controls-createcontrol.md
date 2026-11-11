---
id: endpoint-post-orgs-org-id-objectives-objective-id-controls-createcontrol
title: "Controls: Create a control"
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

### `POST /orgs/{org_id}/objectives/{objective_id}/controls` — Create a control

- **operationId:** `createControl`
- **Domínio(s):** Controls

Create a new control in an existing objective.

Limitations:
* Each objective in a project or framework can contain a maximum of 1000 controls.
* You cannot create a control if the existing objective has been checked out using
Offline Projects or the
HighBond iPad app.

<details>
<summary><strong>Parâmetros</strong> (4)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `objective_id` | path | ✅ | integer | The ID of the objective. Ex.: `1` |
| `fields[controls]` | query |  | string | Requesting the API to return only the specified fields. For more information, see Making requests Ex.: `title,description,control_id,owner,frequency,control_type,prevent_detect,method,status,position,created_at,updated_at,custom_attributes,objective,walkthrough,control_test_plan,control_tests,mitigations,owner_user,entities,framework_origin` |
| `include` | query |  | string | Requesting the API to return related resources. For more information, see Making requests Ex.: `objective` |

</details>

<details>
<summary><strong>Request body (payload)</strong></summary>

The data required to create a control.

**Body obrigatório.**

**Content-Type:** `application/vnd.api+json`

**Schema:** `CreateControlRequest`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | object | ✅ | The data associated with the resource. |
| `data.type` | string | ✅ | The classification of the object (`"controls"`). Ex.: `"controls"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.title` | string |  | The title of the control. Ex.: `"Control Title"` |
| `data.attributes.description` | string | ✅ | A detailed description of the control. Ex.: `"Control description"` |
| `data.attributes.control_id` | string | ✅ | The reference number or code of the control. This field is known as the procedure reference number in Workplan workflow projects. Ex.: `"001"` |
| `data.attributes.owner` | string |  | The person responsible for the control. Specifying a person's name or email does not automatically send them an email notification about the control. Ex.: `"thomas@sodor.ca"` |
| `data.attributes.frequency` | string |  | A user configurable field that determines the default testing method and sample size in the test plan. The options available depends on the configuration of the project type.  >**Note**: This is a **required field** if the control belongs to an  Internal Control workflow project. If the control (procedure) belongs to a  Workplan workflow project, or if the `frequency` field has been disabled in the project type, the field is hidden from the API response.  For more information about the `frequency` field, see Executing procedures and testing controls. Ex.: `"Daily"` |
| `data.attributes.method` | string |  | A user configurable field that specifies how the control will be tested or implemented. The options available depends on the configuration of the project type.  >**Note**: If the control (procedure) belongs to a  Workplan workflow project, or if the `method` field has been disabled in the project type, the field is hidden from the API response. Ex.: `"Management Review"` |
| `data.attributes.control_type` | string |  | A user configurable field that determines the default testing method and sample size in the test plan. The options available depends on the configuration of the project type.  >**Note**: This is a **required field** if the control belongs to an  Internal Control workflow project. If the control (procedure) belongs to a  Workplan workflow project, or if the `control_type` field has been disabled in the project type, the field is hidden from the API response.  For more information about the `control_type` field, see Executing procedures and testing controls. Ex.: `"Application/System Control"` |
| `data.attributes.prevent_detect` | string |  | A user configurable field that specifies whether the control is intended to prevent or detect risk, or if it is not applicable. The options available depends on the configuration of the project type.  >**Note**: This is a **required field** if the control belongs to an  Internal Control workflow project. If the control (procedure) belongs to a  Workplan workflow project, or if the `prevent_detect` field has been disabled in the project type, the field is hidden from the API response. Ex.: `"Prevent"` |
| `data.attributes.status` | string |  | A user configurable field that specifies the current state of the control. The options available depends on the configuration of the project type.  >**Note**: If the control (procedure) belongs to a  Workplan workflow project, or if the `status` field has been disabled in the project type, the field is hidden from the API response. Ex.: `"Key Control"` |
| `data.attributes.position` | integer |  | The value that determines the order in which it is displayed in the index action. `position` must be a value between `1` and `2147483647`. Ex.: `1` |
| `data.attributes.custom_attributes` | array[object] |  | An array of custom attributes defined by the user that are available on this object. |
| `data.attributes.custom_attributes.id` | string |  | The ID of the custom attribute that this custom attribute value is for. Optional if term is included. Ex.: `"42"` |
| `data.attributes.custom_attributes.term` | string |  | The user defined term used to identify the custom attribute. Optional if id is included. Ex.: `"Custom Control Attribute"` |
| `data.attributes.custom_attributes.value` | array[string] |  | The value or values (for multiselect) to set this custom attribute to. Ex.: `["Custom Select Option Text"]` |
| `data.relationships` | object |  | The relationships associated with the resource. |
| `data.relationships.owner_user` | object |  | Specifies the user responsible for the control. A value in this field will override any value provided in the `owner` attribute. Specifiying a user will automatically send them an email notification about the control.  To return this field, you must specify the `fields[controls]=owner_user` parameter in your request. For more information, see Making requests. |
| `data.relationships.owner_user.data` | object | ✅ | The data associated with the resource. |
| `data.relationships.owner_user.data.id` | string | ✅ | The unique identifier (UID) of the user. For more information on obtaining this value, see Making requests. Ex.: `"3NQ6XzAUxqJMnAQ7n4KF"` |
| `data.relationships.owner_user.data.type` | string | ✅ | The classification of the object (`"users"`). Ex.: `"users"` |
| `data.relationships.framework_origin` | object |  | In the Projects app, a project `control` can have a related counterpart in an associated framework. The `framework_origin` attribute allows you to associate an `control` and related `control_test_plan` in a project with its related counterpart in a framework. |
| `data.relationships.framework_origin.data` | object | ✅ | The data associated with the resource. |
| `data.relationships.framework_origin.data.id` | string | ✅ | The ID of the parent control. Ex.: `"1"` |
| `data.relationships.framework_origin.data.type` | string | ✅ | The classification of the object (`"controls"`). Ex.: `"controls"` |

</details>

<details>
<summary><strong>Respostas</strong> (7)</summary>

<details>
<summary>`201` — Created.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `GetControlResponse`

_Apenas campos que diferem do request body. 24 campo(s) idênticos omitidos._

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data.id` | string | ✅ | The ID of the requested resource. Ex.: `"1"` |
| `data.attributes.description` | string |  | A detailed description of the control. Ex.: `"Control description"` |
| `data.attributes.control_id` | string |  | The reference number or code of the control. This field is known as the procedure reference number in Workplan workflow projects. Ex.: `"001"` |
| `data.attributes.created_at` | string |  | The timestamp identifying when the control was created. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.attributes.updated_at` | string |  | The timestamp identifying when the control was last updated. Ex.: `"2019-02-09T13:17:26Z"` |
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
| `data.relationships.entities` | object |  | Each control has an associated control entities. |
| `data.relationships.entities.data` | array[object] | ✅ | The data associated with the resource. Ex.: `[]` |
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
