---
id: endpoint-post-orgs-org-id-strategy-risks-createstrategyrisk
title: "Strategy: Create a risk"
tags: [endpoint, strategy]
source: openapi.json (HighBond API v1.1.0)
---

## Strategy

You can use the Strategy app to identify, assess, and monitor strategic risks.

Learn more.

### `POST /orgs/{org_id}/strategy_risks` — Create a risk

- **operationId:** `createStrategyRisk`
- **Domínio(s):** Strategy

Create a new risk in Strategy.

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

<details>
<summary><strong>Parâmetros</strong> (1)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |

</details>

<details>
<summary><strong>Request body (payload)</strong></summary>

The data required to create a risk.

**Body obrigatório.**

**Content-Type:** `application/vnd.api+json`

**Schema:** `CreateStrategyRiskRequest`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | object | ✅ | The data associated with the resource. |
| `data.type` | string | ✅ | The classification of the object (`"strategy_risks"`). Ex.: `"strategy_risks"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.title` | string | ✅ | The title of the risk. Ex.: `"Strategic Risk"` |
| `data.attributes.description` | string |  | A detailed description of the risk. Ex.: `"Risk Description"` |
| `data.attributes.status` | string |  | Current status of the risk (current column on the dashboard) Valores: `assess`, `accepted`, `audit`, `continuously_audit`, `mitigated` Default: `assess` Ex.: `"audit"` |
| `data.attributes.strategy_custom_attributes` | array[object] |  | An array of custom attributes defined by the user that are available on this object. |
| `data.attributes.strategy_custom_attributes.id` | string |  | The ID of the custom attribute that this custom attribute value is for. Ex.: `"42"` |
| `data.attributes.strategy_custom_attributes.value` | array[string] |  | The value or values (for multiselect) to set this custom attribute to. Ex.: `["First Custom Select Option Text", "Second Custom Select Option Text"]` |

</details>

<details>
<summary><strong>Respostas</strong> (3)</summary>

<details>
<summary>`201` — Created.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `CreateStrategyRiskResponse`

_Apenas campos que diferem do request body. 9 campo(s) idênticos omitidos._

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data.id` | string | ✅ | The ID of the requested resource. Ex.: `"1"` |
| `data.attributes.strategy_custom_attributes.term` | string |  | The user defined term used to identify the custom attribute. Ex.: `"Custom Risk Attribute"` |
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

</details>
