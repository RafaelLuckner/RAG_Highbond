---
id: endpoint-get-orgs-org-id-metrics-id-getmetric
title: "Metrics: Get a metric"
tags: [endpoint, metrics]
source: openapi.json (HighBond API v1.1.0)
---

## Metrics

A metric is a calculation that you label as a specific type of key indicator. Key indicators are quantitative measurements of success (KPI, KCI) or risk (KRI) that are
associated with a company's objectives. Metrics monitor the data in a single column over a time period using an aggregate function such as average, count, or
percentage of total.

Your organization can have a maximum of 8,000 metrics.

Learn more about metrics.

### `GET /orgs/{org_id}/metrics/{id}` — Get a metric

- **operationId:** `getMetric`
- **Domínio(s):** Metrics

Get information about a metric.

<details>
<summary><strong>Parâmetros</strong> (2)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `id` | path | ✅ | string | The ID of the requested resource. Ex.: `9999` |

</details>

<details>
<summary><strong>Respostas</strong> (6)</summary>

<details>
<summary>`200` — OK.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `SingleMetricResponse`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | object | ✅ | The data associated with the resource. |
| `data.id` | string | ✅ | The ID of the metric. Ex.: `"5001"` |
| `data.type` | string | ✅ | The classification of the object (`"metrics"`). Ex.: `"metrics"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.name` | string |  | The name of the metric. Ex.: `"My first Metric"` |
| `data.attributes.base_color` | string |  | Sets the color of the metric when the calculation does not exceed the threshold. Ex.: `"#3F3D3C"` |
| `data.attributes.func` | string |  | Defines the aggregate function to use in the metric calculation.  Valid functions: `count`, `positives`, `negatives`, `zeros`, `total`, `average`, `lowest`, `highest`, `standard_deviation`, `uniques`, `blanks`, `percent-of` Ex.: `"percent-of"` |
| `data.attributes.interval` | string |  | Summarizes the metric into a period.  Valid periods: `day`, `month`, `quarter`, `year` Ex.: `"month"` |
| `data.attributes.metric_type` | string |  | Tags the metric as an indicator type, such as a key performance indicator or key risk indicator. Ex.: `"kpi"` |
| `data.attributes.show_sparkline` | boolean |  | Shows (`true`) or hides (`false`) the trend of key indicator performance from the earliest calculation period to the current period for users that view the metric. Ex.: `true` |
| `data.attributes.view_thresholds` | boolean |  | Shows (`true`) or hides (`false`) active trigger thresholds on the sparkline. Ex.: `false` |
| `data.attributes.field_name` | string |  | The underlying name of the column in the table used for the metric calculation. `field_name` must be unique within a table and follow the column naming requirements. Ex.: `"balance"` |
| `data.attributes.time_field_name` | string |  | A column in the table with a `date`, `datetime` or `time` data type. Ex.: `"created_at"` |
| `data.attributes.config` | string |  | A JSON string storing the metric format configuration. Ex.: `"{\n  \"field_format_map\": { },\n  \"conditional_formats_map\": { }\n}\n"` |
| `data.attributes.filter_config` | string |  | A JSON string storing the metric filter configuration. Ex.: `"{\n  \"filtersOpen\": true,\n  \"params\": { }\n}\n"` |
| `data.attributes.func_argument` | string |  | A JSON string storing the arguments of the Metric function.  Valid operators:  `>`, `=`, `<=`, `==`, `!=`, `between`, `not-between`, `begins-with`, `contains`, `does-not-contain`, `is-blank`, `is-not-blank` Ex.: `"{\n  \"operator\": \"is-blank\"\n}\n"` |
| `data.attributes.created_at` | string |  | The date the metric was created. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.attributes.updated_at` | string |  | The date the metric was updated. Ex.: `"2019-03-18T22:02:05Z"` |
| `data.relationships` | object | ✅ | The relationships associated with the resource. Ex.: `{"table": {"data": {"id": "300", "type": "tables"}}}` |
| `data.relationships.table` | RelationshipObject |  |  |
| `data.relationships.table.data` | object | ✅ | The data associated with the related object. |
| `data.relationships.table.data.id` | string | ✅ | The ID of the related object. Ex.: `1` |
| `data.relationships.table.data.type` | string | ✅ | The classification of the related object. Ex.: `"collection"` |

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

</details>
