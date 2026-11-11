---
id: endpoint-get-orgs-org-id-strategy-risks-risk-id-strategy-metrics-getstrategyriskmetrics
title: "Strategy: Get risk metrics"
tags: [endpoint, strategy]
source: openapi.json (HighBond API v1.1.0)
---

## Strategy

You can use the Strategy app to identify, assess, and monitor strategic risks.

Learn more.

### `GET /orgs/{org_id}/strategy_risks/{risk_id}/strategy_metrics` — Get risk metrics

- **operationId:** `getStrategyRiskMetrics`
- **Domínio(s):** Strategy

Retrieves the list of metrics linked to the current risk from
Strategy.

A metric is a calculation that can be labeled as a specific type of key indicator.

This list contains the metric's URI as `metric_uri` pointing to the specific Metric inside the
Results
application, where its full data can be accessed. This is the
same as using the `metric_id` directly as the `id` for the endpoint
/orgs/{org_id}/metrics/{id}.

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

**Schema:** `GetStrategyRiskMetricsResponse`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `links` | object | ✅ |  |
| `links.next` | string | ✅ | Next page url Ex.: `"/v1/orgs/1/strategy_risks/1/strategy_metrics?page[number]=Mg=="` |
| `links.prev` | string | ✅ | Previous page url Ex.: `null` |
| `data` | array[object] | ✅ | Array of metrics |
| `data.id` | string | ✅ | The ID of the requested resource. Ex.: `"3013"` |
| `data.type` | string | ✅ | The classification of the object (`"strategy_metrics"`). Ex.: `"strategy_metrics"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.name` | string |  | The name of the metric. Ex.: `"KPIs for Q2"` |
| `data.attributes.description` | string |  | The name of the metric. Ex.: `"Key Performance Indicators for the second quarter"` |
| `data.attributes.metric_id` | string |  | The metric's ID inside the Results application. Ex.: `"41792"` |
| `data.attributes.metric_uri` | string |  | The metric's URI inside the Results application. Ex.: `"/v1/orgs/1/metrics/41792"` |
| `data.attributes.created_at` | string |  | The timestamp identifying when the metric was created. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.attributes.updated_at` | string |  | The timestamp identifying when the metric was last updated. Ex.: `"2019-02-09T13:17:26Z"` |

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
