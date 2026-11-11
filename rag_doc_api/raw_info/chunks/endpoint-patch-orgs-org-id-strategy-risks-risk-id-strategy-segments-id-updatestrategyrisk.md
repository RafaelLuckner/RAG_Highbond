---
id: endpoint-patch-orgs-org-id-strategy-risks-risk-id-strategy-segments-id-updatestrategyrisk
title: "Strategy: Update a risk segment"
tags: [endpoint, strategy]
source: openapi.json (HighBond API v1.1.0)
---

## Strategy

You can use the Strategy app to identify, assess, and monitor strategic risks.

Learn more.

### `PATCH /orgs/{org_id}/strategy_risks/{risk_id}/strategy_segments/{id}` — Update a risk segment

- **operationId:** `updateStrategyRiskSegment`
- **Domínio(s):** Strategy

Make changes to a risk segment, including updating the segment's severity values and treatment weights.

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

The data required to update a risk segment.

The field `strategy_factors` lists the values of the assessed severity levels for the current segment of the risk.
To get information about this factor, use the Factor
resource.

The field `treatment_factors` lists the values of the assessed treatment weights for the current segment of the risk.

**Body obrigatório.**

**Content-Type:** `application/vnd.api+json`

**Schema:** `UpdateStrategyRiskSegmentRequest`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | object | ✅ | The data associated with the resource. |
| `data.type` | string | ✅ | The classification of the object (`"strategy_segments"`). Ex.: `"strategy_segments"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.strategy_factors` | array[object] | ✅ | The assessed severity level for each factor of this segment. |
| `data.attributes.strategy_factors.id` | string | ✅ | The ID of the scoring factor. Ex.: `"106"` |
| `data.attributes.strategy_factors.severity_value` | string |  | Decimal value of the current severity level. Ex.: `"2.0"` |
| `data.attributes.strategy_factors.treatment_factors` | array[object] |  | The treatments associated with the factor. |
| `data.attributes.strategy_factors.treatment_factors.projects_objective_id` | string | ✅ | The ID of the project objective. Ex.: `"1"` |
| `data.attributes.strategy_factors.treatment_factors.weight` | string |  | The weight of the project objective. Ex.: `"0.5"` |

</details>

<details>
<summary><strong>Respostas</strong> (4)</summary>

<details>
<summary>`200` — OK.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `UpdateStrategyRiskSegmentResponse`

_Apenas campos que diferem do request body. 9 campo(s) idênticos omitidos._

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data.id` | string | ✅ | The ID of the requested resource. Ex.: `"101"` |
| `data.attributes.strategy_factors.treatment_value` | string |  | The treatment value for the factor. Ex.: `"1"` |
| `data.attributes.strategy_factors.treatment_weight` | string |  | The treatment weight for the factor. Ex.: `"0.5"` |
| `data.attributes.strategy_factors.treatment_factors.projects_objective_uri` | string |  | The URI of the project objective. Ex.: `"/v1/orgs/1/projects/1/objectives/1"` |
| `data.attributes.strategy_factors.created_at` | string |  | The timestamp identifying when the segment was created. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.attributes.strategy_factors.updated_at` | string |  | The timestamp identifying when the segment was last updated. Ex.: `"2019-02-09T13:17:26Z"` |

</details>

<details>
<summary>`400` — Bad request.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `Errors`

Erro no formato padrão JSON:API: objeto `errors` (array) com `status` (código HTTP), `source.pointer` (JSON Pointer RFC6901 do campo com erro), `code`, `title` e `detail`.

</details>

- `401` — Bad credentials.

- `403` — Forbidden.

</details>
