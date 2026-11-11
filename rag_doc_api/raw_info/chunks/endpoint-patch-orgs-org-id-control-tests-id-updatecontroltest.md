---
id: endpoint-patch-orgs-org-id-control-tests-id-updatecontroltest
title: "Control tests: Update a control test"
tags: [endpoint, control-tests]
source: openapi.json (HighBond API v1.1.0)
---

## Control tests

Control tests evaluate the operating effectiveness of a control.
* If your project includes one testing round, each control you create has one corresponding control test.
* If your project includes multiple testing rounds, each control you create has a corresponding series of control tests.

> **Note —**
Only control tests in Internal Control workflow projects that have an `"active"` state can be accessed using the API.

Learn more about control tests.

### `PATCH /orgs/{org_id}/control_tests/{id}` — Update a control test

- **operationId:** `updateControlTest`
- **Domínio(s):** Control tests

> **Deprecation notice —**
Please note that `testing_conclusion` field will be deprecated. Consider using new `testing_conclusion_status` field instead.

Make changes to a control test in a project, like updating the testing results or conclusion.

Limitations:
* You cannot update the control test if it is signed off or if the objective it belongs to has been checked out using
Offline Projects or the
HighBond iPad app.
* You cannot update the `testing_conclusion_status` and `testing_conclusion` field if the field is automated using an
assessment driver.

<details>
<summary><strong>Parâmetros</strong> (4)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `id` | path | ✅ | string | The ID of the requested resource. Ex.: `9999` |
| `fields[control_tests]` | query |  | string | Requesting the API to return only the specified fields. For more information, see Making requests Ex.: `assignee_name,testing_round_number,not_applicable,sample_size,testing_results,testing_conclusion,testing_conclusion_status,created_at,updated_at,control,assigned_user,actual_milestone_date,planned_milestone_date,preparer_signoff,detail_reviewer_signoff,general_reviewer_signoff,supplemental_reviewer,specialty_reviewer` |
| `include` | query |  | string | Requesting the API to return related resources. For more information, see Making requests Ex.: `control,control.objective` |

</details>

<details>
<summary><strong>Request body (payload)</strong></summary>

The data required to update a control test.

**Body obrigatório.**

**Content-Type:** `application/vnd.api+json`

**Schema:** `UpdateControlTestRequest`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | object | ✅ | The data associated with the resource. |
| `data.id` | string | ✅ | The ID of the requested resource. Ex.: `1` |
| `data.type` | string | ✅ | The classification of the object (`"control_tests"`). Ex.: `"control_tests"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.not_applicable` | boolean | ✅ | `false` specifies that the control test is applicable to the testing round. `true` specifies that the control test is not applicable to the testing round. Only applicable control tests are included in assurance calculations. Ex.: `false` |
| `data.attributes.sample_size` | integer |  | The total sample size, split among testing rounds. `sample_size` must be a value between `0` and `2147483647`.  Sample size is set when a test plan is created the first time, which occurs when you create a control. The logic used to automatically set the sample size field is based on two control attribute fields: `frequency` and `type`. For more information, see Executing procedures and testing controls. Ex.: `24` |
| `data.attributes.testing_results` | string |  | A detailed evaluation that describes whether or not the control is operating effectively. Ex.: `"<h1>Heading</h1><p>Testing results description.</p>"` |
| `data.attributes.testing_conclusion` | boolean |  | A rating that specifies whether the control passes (`true`) or fails (`false`).  The exact values for this field (E.g. "Operating Effectively" and "Exception(s) Noted") depend on the configuration of the project type. `true` maps to the first customizable value (E.g. "Operating Effectively") and `false` maps to the second customizable value (E.g. "Exception(s) Noted") in the project type. Ex.: `true` |
| `data.attributes.testing_conclusion_status` | string |  | The control rating choice. Ex.: `"Operating Effectively"` |
| `data.attributes.actual_milestone_date` | string |  | Actual milestone date. Ex.: `"2019-02-10"` |
| `data.attributes.planned_milestone_date` | string |  | Planned milestone date. Ex.: `"2019-02-09"` |
| `data.attributes.custom_attributes` | array[object] |  | An array of custom attributes defined on the project type used by the project this control test is from. Learn more about project types. Make a PATCH request to modify the value of a custom attribute. |
| `data.attributes.custom_attributes.id` | string |  | The ID of this custom attribute.  Optional if term is included. Ex.: `"42"` |
| `data.attributes.custom_attributes.term` | string |  | The user defined term used to identify this custom attribute. Optional if id is included. Ex.: `"Custom Control Test Attribute"` |
| `data.attributes.custom_attributes.value` | array[string] |  | The value or values (for multiselect) for this custom attribute. Ex.: `["Custom Select Option Text"]` |
| `data.relationships` | object | ✅ | The relationships associated with the resource. |
| `data.relationships.control` | object | ✅ | The attributes associated with the resource. |
| `data.relationships.control.data` | object | ✅ | The data associated with the resource. |
| `data.relationships.control.data.id` | string | ✅ | The ID of the control. Ex.: `"1"` |
| `data.relationships.control.data.type` | string | ✅ | The classification of the object (`"controls"`). Ex.: `"controls"` |
| `data.relationships.assigned_user` | object |  | The person assigned to the control test. Only users assigned the Professional Manager, Professional User, or Contributor Tester role in the project can be specified. The user specified receives an email notification with a link to the control test, and has full read and write access to the control test.  To return this field, you must specify the `fields[control_tests]=assigned_user` parameter in your request. For more information, see Making requests. |
| `data.relationships.assigned_user.data` | object | ✅ | The data associated with the resource. |
| `data.relationships.assigned_user.data.id` | string | ✅ | The unique identifier (UID) of the assigned user. For more information on obtaining this value, see Making requests. Ex.: `"3NQ6XzAUxqJMnAQ7n4KF"` |
| `data.relationships.assigned_user.data.type` | string | ✅ | The classification of the object (`"users"`). Ex.: `"users"` |

</details>

<details>
<summary><strong>Respostas</strong> (7)</summary>

<details>
<summary>`200` — OK.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `GetControlTestResponse`

_Apenas campos que diferem do request body. 22 campo(s) idênticos omitidos._

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data.attributes` | object |  | The attributes associated with the resource. |
| `data.attributes.assignee_name` | string |  | The name of the person to whom the issue was assigned. Ex.: `"Payam Moghaddam"` |
| `data.attributes.testing_round_number` | integer |  | The specific testing round `(1-4)` that the control test belongs to. A control may have 0, 1, 2, or 4 testing rounds, depending upon the `number_of_testing_rounds`  defined in the project settings.  The names for testing rounds are customizable and depend on the configuration of the project type.  **Examples**  1 testing round = **"Testing"** (`1`)  2 testing rounds = **"Interim"** (`1`), **"Final"** (`2`)  4 testing rounds = **"Q1"** (`1`), **"Q2"** (`2`), **"Q3"** (`3`), **"Q4"** (`4`) Ex.: `1` |
| `data.attributes.created_at` | string |  | The timestamp identifying when the control test was created. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.attributes.updated_at` | string |  | The timestamp identifying when the control test was updated. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.attributes.not_applicable` | boolean |  | `false` specifies that the control test is applicable to the testing round. `true` specifies that the control test is not applicable to the testing round. Only applicable control tests are included in assurance calculations. Ex.: `false` |

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
