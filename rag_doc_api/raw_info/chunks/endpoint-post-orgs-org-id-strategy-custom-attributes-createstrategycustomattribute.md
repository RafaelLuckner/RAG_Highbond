---
id: endpoint-post-orgs-org-id-strategy-custom-attributes-createstrategycustomattribute
title: "Strategy: Create a custom attribute"
tags: [endpoint, strategy]
source: openapi.json (HighBond API v1.1.0)
---

## Strategy

You can use the Strategy app to identify, assess, and monitor strategic risks.

Learn more.

### `POST /orgs/{org_id}/strategy_custom_attributes` — Create a custom attribute

- **operationId:** `createStrategyCustomAttribute`
- **Domínio(s):** Strategy

Create a new custom attribute.
Updates the organization's custom attribute definitions in
Strategy.

Each organization can have a maximum of 10 user-defined attributes, which can be associated with each risk inside
the application.
The `field_type` specifies the data type of the attribute. Its value can be one of the following:
- `text`
- `rich_text`
- `select`
- `multiselect`

`options` is a required array which lists all the selectable options for `select` or `multiselect` field types. For all other types, this attribute can be omitted.

<details>
<summary><strong>Parâmetros</strong> (1)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |

</details>

<details>
<summary><strong>Request body (payload)</strong></summary>

The data required to Create a custom attribute.

**Body obrigatório.**

**Content-Type:** `application/vnd.api+json`

**Schema:** `CreateStrategyCustomAttributeRequest`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | object | ✅ | The data associated with the resource. |
| `data.type` | string | ✅ | The classification of the object (`"strategy_custom_attributes"`). Ex.: `"strategy_custom_attributes"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.term` | string | ✅ | The name of the custom attribute. Ex.: `"Custom Risk Attribute"` |
| `data.attributes.field_type` | string |  | The data type of the custom attribute. Valores: `text`, `rich_text`, `select`, `multiselect` Default: `text` Ex.: `"select"` |
| `data.attributes.options` | array[string] |  | Selectable options of the values (when the `field_type` is `select` or `multiselect`). Default: `[]` Ex.: `["First Custom Select Option Text", "Second Custom Select Option Text", "Third Custom Select Option Text", "Fourth Custom Select Option Text"]` |

</details>

<details>
<summary><strong>Respostas</strong> (5)</summary>

<details>
<summary>`201` — Created.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `CreateStrategyCustomAttributeResponse`

_Apenas campos que diferem do request body. 5 campo(s) idênticos omitidos._

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data.id` | string | ✅ | The ID of the requested resource. Ex.: `"42"` |
| `data.attributes.term` | string |  | The name of the custom attribute. Ex.: `"Custom Risk Attribute"` |
| `data.attributes.is_default` | boolean |  | True for custom attributes created automatically by the system, false after the attribute is modified. Default: `True` Ex.: `false` |
| `data.attributes.created_at` | string |  | The timestamp identifying when the custom attribute was created. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.attributes.updated_at` | string |  | The timestamp identifying when the custom attribute was last updated. Ex.: `"2019-02-09T13:17:26Z"` |

</details>

<details>
<summary>`400` — Bad request.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `Errors`

Erro no formato padrão JSON:API: objeto `errors` (array) com `status` (código HTTP), `source.pointer` (JSON Pointer RFC6901 do campo com erro), `code`, `title` e `detail`.

</details>

- `401` — Bad credentials.

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
