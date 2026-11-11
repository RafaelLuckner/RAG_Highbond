---
id: endpoint-get-orgs-org-id-strategy-risks-risk-id-strategy-assurances-getstrategyriskassura
title: "Strategy: Get risk assurances"
tags: [endpoint, strategy]
source: openapi.json (HighBond API v1.1.0)
---

## Strategy

You can use the Strategy app to identify, assess, and monitor strategic risks.

Learn more.

### `GET /orgs/{org_id}/strategy_risks/{risk_id}/strategy_assurances` — Get risk assurances

- **operationId:** `getStrategyRiskAssurances`
- **Domínio(s):** Strategy

Retrieves the list of assurances for the current risk from
Strategy.

Assurances link risks in Strategy to testing results, issues and controls inside the
Projects
application.
See the Projects Objective resource to learn more.

<details>
<summary><strong>Parâmetros</strong> (4)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `risk_id` | path | ✅ | integer | The ID of the risk. Ex.: `1` |
| `page[size]` | query |  | string | The number of items returned per page. Default is 20. Maximum is 100. Ex.: `10` |
| `page[number]` | query |  | string | The Base64-encoded page number of records to return. Ex.: `Mg==` |

</details>

<details>
<summary><strong>Respostas</strong> (5)</summary>

<details>
<summary>`200` — OK.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `GetStrategyRiskAssurancesResponse`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `links` | object | ✅ |  |
| `links.next` | string | ✅ | Next page url Ex.: `"/v1/orgs/1/strategy_risks/1/strategy_assurances?page[number]=Mg=="` |
| `links.prev` | string | ✅ | Previous page url Ex.: `null` |
| `data` | array[object] | ✅ | Array of assurances |
| `data.id` | string | ✅ | The ID of the requested resource. Ex.: `"49191"` |
| `data.type` | string | ✅ | The classification of the object (`"strategy_assurances"`). Ex.: `"strategy_assurances"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.projects_project_id` | string |  | The identifier of the audit/project inside Projects Ex.: `"13921"` |
| `data.attributes.projects_objective_id` | string |  | The identifier of the objective inside Projects Ex.: `"73022"` |
| `data.attributes.projects_objective_uri` | string |  | The URI of the objective inside Projects Ex.: `"/v1/orgs/1/objectives/73022"` |
| `data.attributes.created_at` | string |  | The timestamp identifying when the assurance was created. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.attributes.updated_at` | string |  | The timestamp identifying when the assurance was last updated. Ex.: `"2019-02-09T13:17:26Z"` |

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
