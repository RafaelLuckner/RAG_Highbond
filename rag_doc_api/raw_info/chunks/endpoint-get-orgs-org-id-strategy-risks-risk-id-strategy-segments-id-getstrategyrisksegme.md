---
id: endpoint-get-orgs-org-id-strategy-risks-risk-id-strategy-segments-id-getstrategyrisksegme
title: "Strategy: Get a risk segment"
tags: [endpoint, strategy]
source: openapi.json (HighBond API v1.1.0)
---

## Strategy

You can use the Strategy app to identify, assess, and monitor strategic risks.

Learn more.

### `GET /orgs/{org_id}/strategy_risks/{risk_id}/strategy_segments/{id}` — Get a risk segment

- **operationId:** `getStrategyRiskSegment`
- **Domínio(s):** Strategy

Get information about an operating segment for the risk.
The field `strategy_factors` lists the values of the assessed severity levels for the current segment of the risk.
To get information about this factor, use the Factor
resource.

To fetch the treatment data, you can specify the required fields via the `fields[strategy_segments]` or
`fields[strategy_factors]` query parameters, as described below.

<details>
<summary><strong>Parâmetros</strong> (5)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `risk_id` | path | ✅ | integer | The ID of the risk. Ex.: `1` |
| `id` | path | ✅ | string | The ID of the requested resource. Ex.: `9999` |
| `fields[strategy_segments]` | query |  | string | Requesting the API to return only the specified fields for the segment. For more information, see Making requests Ex.: `name,score,strategy_factors,created_at,updated_at` |
| `fields[strategy_factors]` | query |  | string | Requesting the API to return only the specified fields for treatments. For more information, see Making requests Ex.: `id,treatment_value,treatment_weight,treatment_factors,severity_value` |

</details>

<details>
<summary><strong>Respostas</strong> (5)</summary>

<details>
<summary>`200` — OK.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `GetStrategyRiskSegmentResponse`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | object | ✅ | The data associated with the resource. |
| `data.id` | string | ✅ | The ID of the requested resource. Ex.: `"101"` |
| `data.type` | string | ✅ | The classification of the object (`"strategy_segments"`). Ex.: `"strategy_segments"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.name` | string |  | The name of the segment. Ex.: `"EMEA"` |
| `data.attributes.score` | string |  | Decimal score of the segment for the risk. Ex.: `"2.0"` |
| `data.attributes.strategy_factors` | array[object] |  | The assessed severity level for each factor of this segment |
| `data.attributes.strategy_factors.id` | string |  | The ID of the scoring factor. Ex.: `"106"` |
| `data.attributes.strategy_factors.severity_value` | string |  | Decimal value of the current severity level. Ex.: `"2.0"` |
| `data.attributes.created_at` | string |  | The timestamp identifying when the segment was created. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.attributes.updated_at` | string |  | The timestamp identifying when the segment was last updated. Ex.: `"2019-02-09T13:17:26Z"` |

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
