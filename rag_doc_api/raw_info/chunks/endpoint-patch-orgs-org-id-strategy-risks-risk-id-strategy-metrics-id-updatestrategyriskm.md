---
id: endpoint-patch-orgs-org-id-strategy-risks-risk-id-strategy-metrics-id-updatestrategyriskm
title: "Strategy: Update a risk metric"
tags: [endpoint, strategy]
source: openapi.json (HighBond API v1.1.0)
---

## Strategy

You can use the Strategy app to identify, assess, and monitor strategic risks.

Learn more.

### `PATCH /orgs/{org_id}/strategy_risks/{risk_id}/strategy_metrics/{id}` — Update a risk metric

- **operationId:** `updateStrategyRiskMetric`
- **Domínio(s):** Strategy

Make changes to a risk metric, including updating the metric's description.

<details>
<summary><strong>Parâmetros</strong> (3)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `risk_id` | path | ✅ | integer | The ID of the risk. Ex.: `1` |
| `id` | path | ✅ | string | The ID of the requested resource. Ex.: `9999` |

</details>

<details>
<summary><strong>Request body (payload)</strong></summary>

The data required to update a risk metric.

**Body obrigatório.**

**Content-Type:** `application/vnd.api+json`

**Schema:** `UpdateStrategyRiskMetricRequest`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | object | ✅ | The data associated with the resource. |
| `data.type` | string | ✅ | The classification of the object (`"strategy_metrics"`). Ex.: `"strategy_metrics"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.metric_id` | string | ✅ | The metric's ID inside the Results application. Ex.: `"41792"` |
| `data.attributes.description` | string |  | The name of the metric. Ex.: `"Key Performance Indicators for the second quarter"` |

</details>

<details>
<summary><strong>Respostas</strong> (7)</summary>

<details>
<summary>`200` — OK.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `UpdateStrategyRiskMetricResponse`

_Apenas campos que diferem do request body. 4 campo(s) idênticos omitidos._

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data.id` | string | ✅ | The ID of the requested resource. Ex.: `"3013"` |
| `data.attributes.name` | string |  | The name of the metric. Ex.: `"KPIs for Q2"` |
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
