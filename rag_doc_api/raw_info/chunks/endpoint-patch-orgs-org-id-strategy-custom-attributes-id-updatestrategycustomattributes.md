---
id: endpoint-patch-orgs-org-id-strategy-custom-attributes-id-updatestrategycustomattributes
title: "Strategy: Update a custom attribute"
tags: [endpoint, strategy]
source: openapi.json (HighBond API v1.1.0)
---

## Strategy

You can use the Strategy app to identify, assess, and monitor strategic risks.

Learn more.

### `PATCH /orgs/{org_id}/strategy_custom_attributes/{id}` — Update a custom attribute

- **operationId:** `updateStrategyCustomAttributes`
- **Domínio(s):** Strategy

Make changes to the definition of a custom attribute, including updating its term or options in
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
<summary><strong>Parâmetros</strong> (2)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `id` | path | ✅ | string | The ID of the requested resource. Ex.: `9999` |

</details>

<details>
<summary><strong>Request body (payload)</strong></summary>

The custom attributes to update.

**Body obrigatório.**

**Content-Type:** `application/vnd.api+json`

**Schema:** `UpdateStrategyCustomAttributeRequest`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | object | ✅ | The data associated with the resource. |
| `data.type` | string | ✅ | The classification of the object (`"strategy_custom_attributes"`). Ex.: `"strategy_custom_attributes"` |
| `data.attributes` | object |  | The attributes associated with the resource. |
| `data.attributes.term` | string |  | The name of the custom attribute. Ex.: `"Custom Risk Attribute"` |
| `data.attributes.options` | array[string] |  | Selectable options of the values (when the `field_type` is `select` or `multiselect`). Default: `[]` Ex.: `["First Custom Select Option Text", "Second Custom Select Option Text", "Third Custom Select Option Text", "Fourth Custom Select Option Text"]` |

</details>

<details>
<summary><strong>Respostas</strong> (5)</summary>

<details>
<summary>`200` — OK.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `UpdateStrategyCustomAttributeResponse`

_Apenas campos que diferem do request body. 4 campo(s) idênticos omitidos._

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data.id` | string | ✅ | The ID of the requested resource. Ex.: `"42"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.field_type` | string |  | The data type of the custom attribute. Valores: `text`, `rich_text`, `select`, `multiselect` Default: `text` Ex.: `"select"` |
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

- `403` — Forbidden.

- `404` — Not found.

</details>
