---
id: endpoint-get-orgs-org-id-strategy-risks-getstrategyrisks
title: "Strategy: Get risks"
tags: [endpoint, strategy]
source: openapi.json (HighBond API v1.1.0)
---

## Strategy

You can use the Strategy app to identify, assess, and monitor strategic risks.

Learn more.

### `GET /orgs/{org_id}/strategy_risks` — Get risks

- **operationId:** `getStrategyRisks`
- **Domínio(s):** Strategy

Retrieves the full list of the organization's risks from
Strategy.

A strategic risk is an effect of uncertainty on a strategic objective, with the effect having a positive or
negative deviation from what is expected. 

The `status` field is the current state of the risk on the Kanban Board,
its values can be:
  - `assess`
  - `accepted`
  - `audit`
  - `continuously_audit`
  - `mitigated`

The field `strategy_custom_attributes` is an array containing all the currently assigned
custom attributes for the risk. To get the definition of any custom attribute, you can use the
Get a custom attribute endpoint.

To retrive the `heat`, `score` and any other hidden fields, use the `fields[strategy_risks]` query parameter as
described below.

<details>
<summary><strong>Parâmetros</strong> (4)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `fields[strategy_risks]` | query |  | string | Requesting the API to return only the specified fields. For more information, see Making requests Ex.: `title,description,status,score,residual_score,heat,residual_heat,strategy_custom_attributes,risk_manager_risk_id,created_at,updated_at` |
| `page[size]` | query |  | string | The number of items returned per page. Default is 20. Maximum is 100. Ex.: `10` |
| `page[number]` | query |  | string | The Base64-encoded page number of records to return. Ex.: `Mg==` |

</details>

<details>
<summary><strong>Respostas</strong> (5)</summary>

<details>
<summary>`200` — OK.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `GetStrategyRisksResponse`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `links` | object | ✅ |  |
| `links.next` | string | ✅ | Next page url Ex.: `"/v1/orgs/1/strategy_risks?page[number]=Mg=="` |
| `links.prev` | string | ✅ | Previous page url Ex.: `null` |
| `data` | array[object] | ✅ | Array of risks |
| `data.id` | string | ✅ | The ID of the requested resource. Ex.: `"1"` |
| `data.type` | string | ✅ | The classification of the object (`"strategy_risks"`). Ex.: `"strategy_risks"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.title` | string | ✅ | The title of the risk. Ex.: `"Strategic Risk"` |
| `data.attributes.description` | string |  | A detailed description of the risk. Ex.: `"Risk Description"` |
| `data.attributes.status` | string |  | Current status of the risk (current column on the dashboard) Valores: `assess`, `accepted`, `audit`, `continuously_audit`, `mitigated` Default: `assess` Ex.: `"audit"` |
| `data.attributes.strategy_custom_attributes` | array[object] |  | An array of custom attributes defined by the user that are available on this object. |
| `data.attributes.strategy_custom_attributes.id` | string |  | The ID of the custom attribute that this custom attribute value is for. Ex.: `"42"` |
| `data.attributes.strategy_custom_attributes.term` | string |  | The user defined term used to identify the custom attribute. Ex.: `"Custom Risk Attribute"` |
| `data.attributes.strategy_custom_attributes.value` | array[string] |  | The value or values (for multiselect) to set this custom attribute to. Ex.: `["First Custom Select Option Text", "Second Custom Select Option Text"]` |
| `data.attributes.score` | string |  | Score of the Strategy Risk. Ex.: `"0.0"` |
| `data.attributes.residual_score` | string |  | Residual Score of the Strategy Risk. Ex.: `"0.0"` |
| `data.attributes.heat` | string |  | Heat of the Strategy Risk. Ex.: `"0.0"` |
| `data.attributes.residual_heat` | string |  | Residual Heat of the Strategy Risk. Ex.: `"0.0"` |
| `data.attributes.risk_manager_risk_id` | string |  | This is the ID of the risk in Risk Manager. Ex.: `"1"` |
| `data.attributes.created_at` | string |  | The timestamp identifying when the risk was created. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.attributes.updated_at` | string |  | The timestamp identifying when the risk was last updated. Ex.: `"2019-02-09T13:17:26Z"` |

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
