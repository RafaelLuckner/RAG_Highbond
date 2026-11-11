---
id: endpoint-patch-orgs-org-id-strategy-factors-id-updatestrategyfactor
title: "Strategy: Update a scoring factor"
tags: [endpoint, strategy]
source: openapi.json (HighBond API v1.1.0)
---

## Strategy

You can use the Strategy app to identify, assess, and monitor strategic risks.

Learn more.

### `PATCH /orgs/{org_id}/strategy_factors/{id}` — Update a scoring factor

- **operationId:** `updateStrategyFactor`
- **Domínio(s):** Strategy

Make changes to a scoring factor, including updating the factor's name, description, weight and severities.

<details>
<summary><strong>Parâmetros</strong> (2)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `id` | path | ✅ | string | The ID of the requested resource. Ex.: `9999` |

</details>

<details>
<summary><strong>Request body (payload)</strong></summary>

The data required to update a scoring factor.

**Body obrigatório.**

**Content-Type:** `application/vnd.api+json`

**Schema:** `UpdateStrategyFactorRequest`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | object | ✅ | The data associated with the resource. |
| `data.type` | string | ✅ | The classification of the object (`"strategy_factors"`). Ex.: `"strategy_factors"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.name` | string |  | The name of the risk factor. Ex.: `"Likelihood"` |
| `data.attributes.description` | string |  | The description of the risk factor. Ex.: `"Likelihood of the risk"` |
| `data.attributes.weight` | string |  | Numeric weight of the factor Ex.: `"1.0"` |
| `data.attributes.severities` | array[object] |  | The factor's severity levels |
| `data.attributes.severities.id` | string |  | The ID of the severity level Ex.: `"21979"` |
| `data.attributes.severities.name` | string | ✅ | The name of the severity level (also shown in the assessment table on the UI) Ex.: `"Low"` |
| `data.attributes.severities.description` | string |  | Description of the severity level Ex.: `"The lowest possible severity level"` |
| `data.attributes.severities.value` | string | ✅ | Decimal value of the severity level Ex.: `"1"` |

</details>

<details>
<summary><strong>Respostas</strong> (7)</summary>

<details>
<summary>`200` — OK.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `UpdateStrategyFactorResponse`

_Apenas campos que diferem do request body. 9 campo(s) idênticos omitidos._

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data.id` | string | ✅ | The ID of the requested resource. Ex.: `"106"` |
| `data.attributes.name` | string | ✅ | The name of the risk factor. Ex.: `"Likelihood"` |
| `data.attributes.severities` | array[object] | ✅ | The factor's severity levels |
| `data.attributes.is_default` | boolean |  | True for the scoring factors which are automatically created Ex.: `false` |
| `data.attributes.created_at` | string |  | The timestamp identifying when the factor was created. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.attributes.updated_at` | string |  | The timestamp identifying when the factor was last updated. Ex.: `"2019-02-09T13:17:26Z"` |

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
