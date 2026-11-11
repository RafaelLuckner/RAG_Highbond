---
id: endpoint-get-orgs-org-id-objectives-objective-id-risks-getrisks
title: "Risks: Get risks"
tags: [endpoint, risks]
source: openapi.json (HighBond API v1.1.0)
---

## Risks

A risk is an effect of uncertainty on an objective, with the effect having a positive or negative deviation from what is expected.
Risks are organized by objectives, and can be associated with one or more controls. A risk may also be known as a requirement.

> **Note:**
Risks located in such resources can be accessed using the API:
> * In projects that have an "active" state
> * In frameworks

Learn more about risks.

### `GET /orgs/{org_id}/objectives/{objective_id}/risks` — Get risks

- **operationId:** `getRisks`
- **Domínio(s):** Risks

Get a list of all risks for an objective.

<details>
<summary><strong>Parâmetros</strong> (6)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `objective_id` | path | ✅ | integer | The ID of the objective. Ex.: `1` |
| `fields[risks]` | query |  | string | Requesting the API to return only the specified fields. For more information, see Making requests Ex.: `title,description,risk_id,owner,position,impact,likelihood,custom_attributes,custom_factors,created_at,updated_at,objective,mitigations,owner_user,entities,framework_origin,risk_assurance_data` |
| `include` | query |  | string | Requesting the API to return related resources. For more information, see Making requests Ex.: `objective` |
| `page[size]` | query |  | string | The number of items returned per page. Default is 50. Maximum is 100. Ex.: `25` |
| `page[number]` | query |  | string | The Base64-encoded page number of records to return. Ex.: `Mg==` |

</details>

<details>
<summary><strong>Respostas</strong> (6)</summary>

<details>
<summary>`200` — OK.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `GetRisksResponse`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | array[object] | ✅ | Array of risks |
| `data.id` | string | ✅ | The ID of the requested resource. Ex.: `"1"` |
| `data.type` | string | ✅ | The classification of the object (`"risks"`). Ex.: `"risks"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.title` | string |  | The title of the risk. Ex.: `"Risk Title"` |
| `data.attributes.description` | string | ✅ | A detailed description of the risk. Ex.: `"Risk Description"` |
| `data.attributes.risk_id` | string |  | The reference number or code for the risk. Ex.: `"1"` |
| `data.attributes.owner` | string |  | The person responsible for the risk. Specifying a person's name or email does not automatically send them an email notification about the risk. Ex.: `"thomas@sodor.ca"` |
| `data.attributes.impact` | string |  | A user configurable rating of the consequences of the risk occurring. The options available depend on the configuration of the project type. Ex.: `"High"` |
| `data.attributes.likelihood` | string |  | A user configurable rating of the probability of the risk occurring. The options available depend on the configuration of the project type. Ex.: `"High"` |
| `data.attributes.position` | integer |  | The value that determines the order in which it is displayed in the index action. `position` must be a value between `1` and `2147483647`. Ex.: `1` |
| `data.attributes.created_at` | string |  | The timestamp identifying when the risk was created. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.attributes.updated_at` | string |  | The timestamp identifying when the risk was last updated. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.attributes.custom_attributes` | array[object] |  | An array of custom attributes defined by the user that are available on this object. |
| `data.attributes.custom_attributes.id` | string |  | The ID of the custom attribute that this custom attribute value is for. Optional if term is included. Ex.: `"42"` |
| `data.attributes.custom_attributes.term` | string |  | The user defined term used to identify the custom attribute. Optional if id is included. Ex.: `"Custom Risk Attribute"` |
| `data.attributes.custom_attributes.value` | array[string] |  | The value or values (for multiselect) to set this custom attribute to. Ex.: `["Custom Select Option Text"]` |
| `data.attributes.custom_factors` | array[object] |  | An array of custom risk factors defined by the user that are available on this object. |
| `data.attributes.custom_factors.id` | string |  | The ID of the custom risk factor that this custom risk factor value is for. Optional if term is included. Ex.: `"42"` |
| `data.attributes.custom_factors.term` | string |  | The user defined term used to identify the custom risk factor. Optional if id is included. Ex.: `"Custom Risk Factor"` |
| `data.attributes.custom_factors.value` | array[string] |  | The value to set this custom risk factor to. Ex.: `["Custom Risk Factor Option Text"]` |
| `data.attributes.risk_assurance_data` | object |  | Fields that determines assurance values. Assurance is an expression of confidence that risk is effectively mitigated. Returns `null` if Risk Assurance feature is disabled. |
| `data.attributes.risk_assurance_data.inherent_risk` | number |  | The risk that an activity would pose if no controls or other mitigating factors were in place. Can also be referred to as the gross risk, or risks before controls, and can act as the baseline for your organization's risk tolerance or appetite. Ex.: `1.1` |
| `data.attributes.risk_assurance_data.residual_risk` | number |  | The risk that remains after controls are taken into account. Can also be referred to as the net risk or risk after controls. Ex.: `1.1` |
| `data.attributes.risk_assurance_data.assurance` | number |  | The level of assurance that the controls in place effectively mitigate risk to the business. Ex.: `0` |
| `data.relationships` | object | ✅ | The relationships associated with the resource. |
| `data.relationships.objective` | object | ✅ | Each risk has an associated objective. Objectives are the organizing containers for the work done in a project or framework. |
| `data.relationships.objective.data` | object | ✅ | The data associated with the resource. |
| `data.relationships.objective.data.id` | string | ✅ | The ID of the objective. Ex.: `"1"` |
| `data.relationships.objective.data.type` | string | ✅ | The classification of the object (`"objectives"`). Ex.: `"objectives"` |
| `data.relationships.mitigations` | object |  | To return this field, you must specify the `fields[risks]=mitigations` parameter in your request. For more information, see Making requests. |
| `data.relationships.mitigations.data` | array[object] | ✅ |  |
| `data.relationships.mitigations.data.id` | string | ✅ | The ID of the mitigation. Ex.: `"1"` |
| `data.relationships.mitigations.data.type` | string | ✅ | The classification of the object (`"mitigations"`). Ex.: `"mitigations"` |
| `data.relationships.entities` | object |  | Each risk has an associated risk entities. |
| `data.relationships.entities.data` | array[object] | ✅ | The data associated with the resource. |
| `data.relationships.entities.data.id` | string | ✅ | The ID of the entity. Ex.: `"1"` |
| `data.relationships.entities.data.type` | string | ✅ | The classification of the object (`"entities"`). Ex.: `"entities"` |
| `data.relationships.framework_origin` | object |  | In the Projects app, a project `risk` can have a related counterpart in an associated framework. The `framework_origin` attribute allows you to associate an `risk` in a project with its related counterpart in a framework. |
| `data.relationships.framework_origin.data` | object | ✅ | The data associated with the resource. |
| `data.relationships.framework_origin.data.id` | string | ✅ | The ID of the parent control. Ex.: `"1"` |
| `data.relationships.framework_origin.data.type` | string | ✅ | The classification of the object (`"risks"`). Ex.: `"risks"` |
| `data.relationships.owner_user` | object |  | Specifies the user responsible for the risk. A value in this field will override any value provided in the `owner` attribute. Specifiying a user will automatically send them an email notification about the risk.  To return this field, you must specify the `fields[risks]=owner_user` parameter in your request. For more information, see Making requests. |
| `data.relationships.owner_user.data` | object | ✅ | The data associated with the resource. |
| `data.relationships.owner_user.data.id` | string | ✅ | The unique identifier (UID) of the user. For more information on obtaining this value, see Making requests. Ex.: `"3NQ6XzAUxqJMnAQ7n4KF"` |
| `data.relationships.owner_user.data.type` | string | ✅ | The classification of the object (`"users"`). Ex.: `"users"` |
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
