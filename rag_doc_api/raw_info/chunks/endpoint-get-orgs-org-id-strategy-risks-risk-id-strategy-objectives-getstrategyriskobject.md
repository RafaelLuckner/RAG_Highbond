---
id: endpoint-get-orgs-org-id-strategy-risks-risk-id-strategy-objectives-getstrategyriskobject
title: "Strategy: Get risk objectives"
tags: [endpoint, strategy]
source: openapi.json (HighBond API v1.1.0)
---

## Strategy

You can use the Strategy app to identify, assess, and monitor strategic risks.

Learn more.

### `GET /orgs/{org_id}/strategy_risks/{risk_id}/strategy_objectives` — Get risk objectives

- **operationId:** `getStrategyRiskObjectives`
- **Domínio(s):** Strategy

Retrieves the full list of a risk's objectives from
Strategy.

A strategic objective is a business process, functional area, or auditable area that relates to an operating segment.
The organization's objectives can be accessed with the
Objectives resource.

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

**Schema:** `GetStrategyRiskObjectivesResponse`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `links` | object | ✅ |  |
| `links.next` | string | ✅ | Next page url Ex.: `"/v1/orgs/1/strategy_risks/1/strategy_objectives?page[number]=Mg=="` |
| `links.prev` | string | ✅ | Previous page url Ex.: `null` |
| `data` | array[object] | ✅ | Array of objectives |
| `data.id` | string | ✅ | The ID of the requested resource. Ex.: `"31"` |
| `data.type` | string | ✅ | The classification of the object (`"strategy_objectives"`). Ex.: `"strategy_objectives"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.name` | string |  | The name of the objective. Ex.: `"Increase Profit Margin"` |
| `data.attributes.segment_ids` | array[string] |  | Segments connected to this objective, see Strategy Map. Ex.: `["101", "121"]` |
| `data.attributes.created_at` | string |  | The timestamp identifying when the objective was created. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.attributes.updated_at` | string |  | The timestamp identifying when the objective was last updated. Ex.: `"2019-02-09T13:17:26Z"` |

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
