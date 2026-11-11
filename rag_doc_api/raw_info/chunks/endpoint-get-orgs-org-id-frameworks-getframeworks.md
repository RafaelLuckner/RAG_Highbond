---
id: endpoint-get-orgs-org-id-frameworks-getframeworks
title: "Frameworks: Get frameworks"
tags: [endpoint, frameworks]
source: openapi.json (HighBond API v1.1.0)
---

## Frameworks

A framework is a management system that allows you to define objectives, risks, and controls, perform tests, and compile information for reporting purposes. Frameworks may also
be known as audits, compliance assessments, risk assessments, or another customized term.

Learn more about frameworks.

### `GET /orgs/{org_id}/frameworks` — Get frameworks

- **operationId:** `getFrameworks`
- **Domínio(s):** Frameworks

Get a list of all frameworks in an account.

<details>
<summary><strong>Parâmetros</strong> (5)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `fields[frameworks]` | query |  | string | Requesting the API to return only the specified fields. For more information, see Making requests Ex.: `name,created_at,updated_at,folder_name,description,background,position,purpose,scope,risk_assurance,entities,project_type,collaborators,risk_assurance_data,collaborator_groups` |
| `page[size]` | query |  | string | The number of items returned per page. Default is 50. Maximum is 100. Ex.: `25` |
| `page[number]` | query |  | string | The Base64-encoded page number of records to return. Ex.: `Mg==` |
| `filter[name]` | query |  | string | Filter by name.  Response will include partial matches and ignore case. Ex.: `LoremIpsum` |

</details>

<details>
<summary><strong>Respostas</strong> (6)</summary>

<details>
<summary>`200` — OK.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `GetFrameworksResponse`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | array[object] | ✅ | Array of frameworks |
| `data.id` | string | ✅ | The ID of the requested resource. Ex.: `"1"` |
| `data.type` | string | ✅ | The classification of the object (`"frameworks"`). Ex.: `"frameworks"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.name` | string |  | The name of the framework. Ex.: `"Example Application"` |
| `data.attributes.created_at` | string |  | The timestamp specifying when the framework was created. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.attributes.updated_at` | string |  | The timestamp specifying when the framework's settings were updated. Ex.: `"2019-03-18T22:02:05Z"` |
| `data.attributes.folder_name` | string |  |  |
| `data.attributes.description` | string |  | A detailed description of the framework. Ex.: `"Framework description."` |
| `data.attributes.background` | string |  | The contextual circumstances of the framework. Ex.: `"<h1>Heading</h1><p>Framework background description.</p>"` |
| `data.attributes.purpose` | string |  | The intended results, aims, or goals of the framework. Ex.: `"<h1>Heading</h1><p>Framework purpose description.</p>"` |
| `data.attributes.scope` | string |  | What is, and is not, covered by this framework. Ex.: `"<h1>Heading</h1><p>Framework scope description.</p>"` |
| `data.attributes.position` | integer |  | Legacy field that was used to determine the order in which it is displayed in the index action. This field is no longer supported and will always return 0. Ex.: `0` |
| `data.attributes.risk_assurance` | boolean |  | Specifies if the Risk Assurance feature has been enabled (`true`) or disabled (`false`) for the project. The default is `false`. You must be a System Admin with a Professional subscription to configure this field. For more information, see Getting started with assurance for risk. Ex.: `false` |
| `data.attributes.custom_attributes` | array[object] |  | An array of custom attributes defined on the project type used by this framework. Learn more about project types. Make a PATCH request to modify the value of a custom attribute. |
| `data.attributes.custom_attributes.id` | string |  | The ID of this custom attribute. Optional if term is included. Ex.: `"42"` |
| `data.attributes.custom_attributes.term` | string |  | The user defined term used to identify this custom attribute. Optional if id is included. Ex.: `"Custom Framework Planning Attribute"` |
| `data.attributes.custom_attributes.value` | array[string] |  | The value or values (for multiselect) for this custom attribute. Ex.: `["Custom Select Option Text"]` |
| `data.attributes.risk_assurance_data` | object |  | Fields that determines assurance values. Assurance is an expression of confidence that risk is effectively mitigated. Returns `null` if Risk Assurance feature is disabled. |
| `data.attributes.risk_assurance_data.inherent_risk` | number |  | The risk that an activity would pose if no controls or other mitigating factors were in place. Can also be referred to as the gross risk, or risks before controls, and can act as the baseline for your organization's risk tolerance or appetite. Ex.: `1.1` |
| `data.attributes.risk_assurance_data.residual_risk` | number |  | The risk that remains after controls are taken into account. Can also be referred to as the net risk or risk after controls. Ex.: `1.1` |
| `data.attributes.risk_assurance_data.assurance` | number |  | The level of assurance that the controls in place effectively mitigate risk to the business. Ex.: `0` |
| `data.relationships` | object | ✅ | The relationships associated with the resource. |
| `data.relationships.project_type` | object | ✅ | Each framework has an associated project type. Project types define the structure of a framework, including the terminology used in the framework. The project type defines which workflow the framework uses and which custom attributes are available on the framework. Because of this dependency the project type can't be updated at the same time as the custom attributes. |
| `data.relationships.project_type.data` | object | ✅ | The data associated with the resource. |
| `data.relationships.project_type.data.id` | string | ✅ | The ID of the project type. Ex.: `"1"` |
| `data.relationships.project_type.data.type` | string | ✅ | The classification of the object (`"project_types"`). Ex.: `"project_types"` |
| `data.relationships.entities` | object |  | Each framework has an associated framework entities. |
| `data.relationships.entities.data` | array[object] | ✅ | The data associated with the resource. |
| `data.relationships.entities.data.id` | string | ✅ | The ID of the entity. Ex.: `"1"` |
| `data.relationships.entities.data.type` | string | ✅ | The classification of the object (`"entities"`). Ex.: `"entities"` |
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
