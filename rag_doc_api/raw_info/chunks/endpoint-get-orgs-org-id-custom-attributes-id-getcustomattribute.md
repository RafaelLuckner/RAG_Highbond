---
id: endpoint-get-orgs-org-id-custom-attributes-id-getcustomattribute
title: "Custom attributes: Get a custom attribute"
tags: [endpoint, custom-attributes]
source: openapi.json (HighBond API v1.1.0)
---

## Custom attributes

Custom attributes are the customizable fields that are associated with supported objects.
Custom attributes are defined on the project type and used by the project and its children (i.e. objectives).

> **Note —**
No more than 5 custom attributes of one customizable_type can be created (no more than 8 if the customizable type is 'CustomRiskFactor').

Learn more about custom attributes.

### `GET /orgs/{org_id}/custom_attributes/{id}` — Get a custom attribute

- **operationId:** `getCustomAttribute`
- **Domínio(s):** Custom attributes

Get information about a custom attribute.

<details>
<summary><strong>Parâmetros</strong> (3)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `id` | path | ✅ | string | The ID of the requested resource. Ex.: `9999` |
| `fields[custom_attributes]` | query |  | string | Requesting the API to return only the specified fields. For more information, see Making requests Ex.: `term,options,customizable_type,field_type,weight,required,default_values` |

</details>

<details>
<summary><strong>Respostas</strong> (6)</summary>

<details>
<summary>`200` — OK.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `GetCustomAttributeResponse`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | object | ✅ | The data associated with the resource. |
| `data.id` | string | ✅ | The ID of the requested resource. Ex.: `"1"` |
| `data.type` | string | ✅ | The type of the custom attribute (`"custom_attributes"`). Ex.: `"custom_attributes"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.customizable_type` | string | ✅ | The type of the custom attribute. Valid types are: - CustomControlAttribute - CustomControlTestAttribute - CustomControlTestPlanAttribute - CustomFindingActionAttribute - CustomFindingAttribute - CustomObjectiveAttribute - CustomPlanningAttribute - CustomProjectPlanningAttribute - CustomResultsAttribute - CustomRiskAttribute - CustomRiskFactor - CustomWalkthroughAttribute  >**Note**: There can be up to 5 of each custom attribute per project type, except for CustomRiskFactor, which can have up to 8 per project type. If the customizable_type is CustomRiskFactor, the weight field becomes a required field, and the field type can only be `select`. Ex.: `"CustomRiskFactor"` |
| `data.attributes.term` | string | ✅ | The displayed name of the custom attribute. Ex.: `"Custom Risk Factor Attribute"` |
| `data.attributes.field_type` | string | ✅ | The field type of the custom attribute. Valid field types are: - select - multiselect - date - text - paragraph  >**Note**: If field_type is select or multiselect, the options field becomes a required field. Ex.: `"select"` |
| `data.attributes.options` | array[string] |  | The value or values (for multiselect) for this custom attribute.  >**Note**: This is a required field if the custom attribute is of field_type select or multiselect. Ex.: `["Option1", "Option2", "Option3"]` |
| `data.attributes.weight` | integer |  | The weight value, only for custom attributes of type CustomRiskFactor. The weight value must be an integer between 1 and 1000.  >**Note**: This is a required field if the custom attribute is of type CustomRiskFactor. Ex.: `100` |
| `data.attributes.created_at` | string |  | The timestamp identifying when the narrative was created. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.attributes.updated_at` | string |  | The timestamp identifying when the narrative was last updated. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.attributes.required` | boolean |  | A boolean value indicating whether the custom attribute is required. Ex.: `true` |
| `data.attributes.default_values` | array[string] |  | The default value or values for this custom attribute. Ex.: `["Option1", "Option2", "Option3"]` |
| `data.relationships` | object | ✅ | The relationships associated with the resource. |
| `data.relationships.project_type` | object | ✅ | Each custom attribute has an associated project type. Project types define the structure of a project or framework, including the terminology used in the project or framework. |
| `data.relationships.project_type.data` | object | ✅ | The data associated with the resource. |
| `data.relationships.project_type.data.id` | string | ✅ | The ID of the project type that this custom attribute belongs to. Ex.: `"1"` |
| `data.relationships.project_type.data.type` | string | ✅ | The classification of the object (`"project_types"`). Ex.: `"project_types"` |

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
