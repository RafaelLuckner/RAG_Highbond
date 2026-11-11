---
id: endpoint-patch-orgs-org-id-control-test-plans-id-updatecontroltestplan
title: "Test plans: Update a test plan"
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

### `PATCH /orgs/{org_id}/control_test_plans/{id}` — Update a test plan

- **operationId:** `updateControlTestPlan`
- **Domínio(s):** Control test plans

Make changes to a test plan in a project or framework, like updating the testing method or test steps.

Limitations:
* You cannot update the test plan if it is signed off.
* You cannot update the test plan if the objective it belongs to has been checked out using
Offline Projects or the
HighBond iPad app.

<details>
<summary><strong>Parâmetros</strong> (3)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `id` | path | ✅ | string | The ID of the requested resource. Ex.: `9999` |
| `include` | query |  | string | Requesting the API to return related resources. For more information, see Making requests Ex.: `control,control.objective` |

</details>

<details>
<summary><strong>Request body (payload)</strong></summary>

The data required to update a control test.

**Body obrigatório.**

**Content-Type:** `application/vnd.api+json`

**Schema:** `UpdateControlTestPlanRequest`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | object | ✅ | The data associated with the resource. |
| `data.id` | string | ✅ | The ID of the requested resource. Ex.: `1` |
| `data.type` | string | ✅ | The classification of the object (`"control_test_plans"`). Ex.: `"control_test_plans"` |
| `data.attributes` | object |  | The attributes associated with the resource. |
| `data.attributes.testing_method` | string |  | The method specifying how evidence will be obtained. The exact values for this field depend on the configuration of the project type.  >**Note**: If the `testing_method` field has been disabled in the project type, the field is hidden from the API response. Ex.: `"Inspection"` |
| `data.attributes.total_sample_size` | integer |  | The total sample size, split among testing rounds. `total_sample_size` must be a value between `0` and `2147483647`.  Sample size is set when a test plan is created the first time, which occurs when you create a control. The logic used to automatically set the sample size field is based on two control attribute fields: `frequency` and `type`. For more information, see Executing procedures and testing controls.  >**Note**: If the `total_sample_size` field has been disabled in the project type, the field is hidden from the API response. Ex.: `1` |
| `data.attributes.test_steps` | string |  | The steps or attributes associated with the test plan. Ex.: `"<h1>Heading</h1><p>Test Steps description.</p>"` |
| `data.attributes.custom_attributes` | array[object] |  | An array of custom attributes defined on the project type used by the project this control test is from. Learn more about project types. Make a PATCH request to modify the value of a custom attribute. |
| `data.attributes.custom_attributes.id` | string |  | The ID of this custom attribute. Optional if term is included. Ex.: `"42"` |
| `data.attributes.custom_attributes.term` | string |  | The user defined term used to identify this custom attribute. Optional if id is included. Ex.: `"Custom Control Test Plan Attribute"` |
| `data.attributes.custom_attributes.value` | array[string] |  | The value or values (for multiselect) for this custom attribute. Ex.: `["Custom Select Option Text"]` |

</details>

<details>
<summary><strong>Respostas</strong> (7)</summary>

<details>
<summary>`200` — OK.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `GetControlTestPlanResponse`

_Apenas campos que diferem do request body. 9 campo(s) idênticos omitidos._

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data.id` | string |  | The ID of the requested resource. Ex.: `1` |
| `data.type` | string |  | The classification of the object (`"control_test_plans"`). Ex.: `"control_test_plans"` |
| `data.attributes.created_at` | string |  | The timestamp identifying when the test plan was created. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.attributes.updated_at` | string |  | The timestamp identifying when the test plan was updated. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.relationships` | object |  | The relationships associated with the resource. |
| `data.relationships.control` | object |  | Each test plan has an associated control. A control is a program, policy, routine, or activity that is intended to mitigate a risk. |
| `data.relationships.control.data` | object | ✅ | The data associated with the resource. |
| `data.relationships.control.data.id` | string | ✅ | The ID of the control. Ex.: `"1"` |
| `data.relationships.control.data.type` | string | ✅ | The classification of the object (`"controls"`). Ex.: `"controls"` |
| `data.relationships.framework_origin` | object |  | In the Projects app, a project `control_test_plan` can have a related counterpart in an associated framework. The `framework_origin` attribute shows related counterpart of `control_test_plan` from a framework. |
| `data.relationships.framework_origin.data` | object | ✅ | The data associated with the resource. |
| `data.relationships.framework_origin.data.id` | string | ✅ | The ID of the parent control. Ex.: `"1"` |
| `data.relationships.framework_origin.data.type` | string | ✅ | The classification of the object (`"control_test_plans"`). Ex.: `"control_test_plans"` |

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
