---
id: endpoint-get-orgs-org-id-strategy-factors-getstrategyfactors
title: "Strategy: Get scoring factors"
tags: [endpoint, strategy]
source: openapi.json (HighBond API v1.1.0)
---

## Strategy

You can use the Strategy app to identify, assess, and monitor strategic risks.

Learn more.

### `GET /orgs/{org_id}/strategy_factors` — Get scoring factors

- **operationId:** `getStrategyFactors`
- **Domínio(s):** Strategy

Retrieves the full list of the organization's risk scoring factors from
Strategy.

Risk scoring factors are multiplied together to calculate the risk score, with each risk scoring factor
multiplied by its assigned weight.
Learn more.

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

**Schema:** `GetStrategyFactorsResponse`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `links` | object | ✅ |  |
| `links.next` | string | ✅ | Next page url Ex.: `"/v1/orgs/1/strategy_factors?page[number]=Mg=="` |
| `links.prev` | string | ✅ | Previous page url Ex.: `null` |
| `data` | array[object] | ✅ | Array of factors |
| `data.id` | string | ✅ | The ID of the requested resource. Ex.: `"106"` |
| `data.type` | string | ✅ | The classification of the object (`"strategy_factors"`). Ex.: `"strategy_factors"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.name` | string |  | The name of the risk factor. Ex.: `"Likelihood"` |
| `data.attributes.description` | string |  | The description of the risk factor. Ex.: `"Likelihood of the risk"` |
| `data.attributes.weight` | string |  | Numeric weight of the factor Ex.: `"1.0"` |
| `data.attributes.is_default` | boolean |  | True for the scoring factors which are automatically created Ex.: `false` |
| `data.attributes.created_at` | string |  | The timestamp identifying when the tag was created. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.attributes.updated_at` | string |  | The timestamp identifying when the tag was last updated. Ex.: `"2019-02-09T13:17:26Z"` |

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
