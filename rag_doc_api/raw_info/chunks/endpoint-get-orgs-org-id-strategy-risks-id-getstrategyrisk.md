---
id: endpoint-get-orgs-org-id-strategy-risks-id-getstrategyrisk
title: "Strategy: Get a risk"
tags: [endpoint, strategy]
source: openapi.json (HighBond API v1.1.0)
---

## Strategy

You can use the Strategy app to identify, assess, and monitor strategic risks.

Learn more.

### `GET /orgs/{org_id}/strategy_risks/{id}` — Get a risk

- **operationId:** `getStrategyRisk`
- **Domínio(s):** Strategy

Get information about a risk.

<details>
<summary><strong>Parâmetros</strong> (3)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `id` | path | ✅ | string | The ID of the requested resource. Ex.: `9999` |
| `fields[strategy_risks]` | query |  | string | Requesting the API to return only the specified fields. For more information, see Making requests Ex.: `title,description,status,score,residual_score,heat,residual_heat,strategy_custom_attributes,risk_manager_risk_id,created_at,updated_at` |

</details>

<details>
<summary><strong>Respostas</strong> (4)</summary>

<details>
<summary>`200` — OK.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `GetStrategyRiskResponse`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | object | ✅ | The data associated with the resource. |
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

- `401` — Bad credentials.

- `403` — Forbidden.

- `404` — Not found.

</details>
