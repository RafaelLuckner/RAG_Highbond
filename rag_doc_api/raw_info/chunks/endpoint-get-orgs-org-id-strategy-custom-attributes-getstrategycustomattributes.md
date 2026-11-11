---
id: endpoint-get-orgs-org-id-strategy-custom-attributes-getstrategycustomattributes
title: "Strategy: Get custom attributes"
tags: [endpoint, strategy]
source: openapi.json (HighBond API v1.1.0)
---

## Strategy

You can use the Strategy app to identify, assess, and monitor strategic risks.

Learn more.

### `GET /orgs/{org_id}/strategy_custom_attributes` — Get custom attributes

- **operationId:** `getStrategyCustomAttributes`
- **Domínio(s):** Strategy

Retrieves the full list of the organization's custom attribute definitions from
Strategy.

Each organization can have a maximum of 10 user-defined attributes, which can be associated with each risk inside
the application.
The `field_type` specifies the data type of the attribute. Its value can be one of the following:
- `text`
- `rich_text`
- `select`
- `multiselect`

The `field_type` `multiselect` and `select` can have multiple possible options defined. These are shown inside
the field `options` as an array. For all other types this field will be empty.

To get a risk's custom attributes use the Risk resource
which lists all of its linked attributes and their values.

`is_default` is a boolean value which indicates whether the attribute is created by default or not. After changing
any data of the attribute, the `is_default` value will be set to `false`.

<details>
<summary><strong>Parâmetros</strong> (3)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `page[size]` | query |  | string | The number of items returned per page. Default is 20. Maximum is 100. Ex.: `10` |
| `page[number]` | query |  | string | The Base64-encoded page number of records to return. Ex.: `Mg==` |

</details>

<details>
<summary><strong>Respostas</strong> (5)</summary>

<details>
<summary>`200` — OK.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `GetStrategyCustomAttributesResponse`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `links` | object | ✅ |  |
| `links.next` | string | ✅ | Next page url Ex.: `"/v1/orgs/1/strategy_custom_attributes?page[number]=Mg=="` |
| `links.prev` | string | ✅ | Previous page url Ex.: `null` |
| `data` | array[object] | ✅ | Array of custom attributes |
| `data.id` | string | ✅ | The ID of the requested resource. Ex.: `"42"` |
| `data.type` | string | ✅ | The classification of the object (`"strategy_custom_attributes"`). Ex.: `"strategy_custom_attributes"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.term` | string |  | The name of the custom attribute. Ex.: `"Custom Risk Attribute"` |
| `data.attributes.field_type` | string |  | The data type of the custom attribute. Valores: `text`, `rich_text`, `select`, `multiselect` Default: `text` Ex.: `"select"` |
| `data.attributes.options` | array[string] |  | Selectable options of the values (when the `field_type` is `select` or `multiselect`). Default: `[]` Ex.: `["First Custom Select Option Text", "Second Custom Select Option Text", "Third Custom Select Option Text", "Fourth Custom Select Option Text"]` |
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
