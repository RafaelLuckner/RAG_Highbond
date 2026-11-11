---
id: endpoint-get-orgs-org-id-walkthroughs-id-getwalkthrough
title: "Walkthroughs: Get a walkthrough"
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

### `GET /orgs/{org_id}/walkthroughs/{id}` — Get a walkthrough

- **operationId:** `getWalkthrough`
- **Domínio(s):** Walkthroughs

Get information about a walkthrough.

Limitation:
Existing Citation Mode highlights and links are not displayed in the `walkthrough_results` field.

<details>
<summary><strong>Parâmetros</strong> (4)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `id` | path | ✅ | string | The ID of the requested resource. Ex.: `9999` |
| `fields[walkthroughs]` | query |  | string | Requesting the API to return only the specified fields. For more information, see Making requests Ex.: `walkthrough_results,control_design,created_at,updated_at,custom_attributes,control,planned_milestone_date,actual_milestone_date` |
| `include` | query |  | string | Requesting the API to return related resources. For more information, see Making requests Ex.: `control,control.objective` |

</details>

<details>
<summary><strong>Respostas</strong> (6)</summary>

<details>
<summary>`200` — OK.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `GetWalkthroughResponse`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | object | ✅ | The data associated with the resource. |
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
