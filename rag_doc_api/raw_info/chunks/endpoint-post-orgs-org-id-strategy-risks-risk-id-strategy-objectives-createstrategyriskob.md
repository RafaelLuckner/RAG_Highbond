---
id: endpoint-post-orgs-org-id-strategy-risks-risk-id-strategy-objectives-createstrategyriskob
title: "Strategy: Create a risk objective link"
tags: [endpoint, strategy]
source: openapi.json (HighBond API v1.1.0)
---

## Strategy

You can use the Strategy app to identify, assess, and monitor strategic risks.

Learn more.

### `POST /orgs/{org_id}/strategy_risks/{risk_id}/strategy_objectives` — Create a risk objective link

- **operationId:** `createStrategyRiskObjective`
- **Domínio(s):** Strategy

Create a new link between a risk and an objective.

<details>
<summary><strong>Parâmetros</strong> (2)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `risk_id` | path | ✅ | integer | The ID of the risk. Ex.: `1` |

</details>

<details>
<summary><strong>Request body (payload)</strong></summary>

The data required to create a risk objective link.

**Body obrigatório.**

**Content-Type:** `application/vnd.api+json`

**Schema:** `CreateStrategyRiskObjectiveLinkRequest`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | object | ✅ | The data associated with the resource. |
| `data.type` | string | ✅ | The classification of the object (`"strategy_risk_objectives"`). Ex.: `"strategy_risk_objectives"` |
| `data.id` | string | ✅ | The ID of the risk objective link. Ex.: `"1"` |

</details>

<details>
<summary><strong>Respostas</strong> (5)</summary>

<details>
<summary>`201` — Created.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `CreateStrategyRiskObjectiveLinkResponse`

_Apenas campos que diferem do request body. 1 campo(s) idênticos omitidos._

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
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
