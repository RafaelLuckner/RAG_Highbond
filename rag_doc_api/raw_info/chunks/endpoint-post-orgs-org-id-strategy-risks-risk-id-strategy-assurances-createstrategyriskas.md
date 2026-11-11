---
id: endpoint-post-orgs-org-id-strategy-risks-risk-id-strategy-assurances-createstrategyriskas
title: "Strategy: Create a risk assurance link"
tags: [endpoint, strategy]
source: openapi.json (HighBond API v1.1.0)
---

## Strategy

You can use the Strategy app to identify, assess, and monitor strategic risks.

Learn more.

### `POST /orgs/{org_id}/strategy_risks/{risk_id}/strategy_assurances` — Create a risk assurance link

- **operationId:** `createStrategyRiskAssurance`
- **Domínio(s):** Strategy

Create a new link between a risk and an assurance.

<details>
<summary><strong>Parâmetros</strong> (2)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `risk_id` | path | ✅ | integer | The ID of the risk. Ex.: `1` |

</details>

<details>
<summary><strong>Request body (payload)</strong></summary>

The data required to create a risk assurance link.

**Body obrigatório.**

**Content-Type:** `application/vnd.api+json`

**Schema:** `CreateStrategyRiskAssuranceLinkRequest`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | object | ✅ | The data associated with the resource. |
| `data.type` | string | ✅ | The classification of the object (`"strategy_assurances"`). Ex.: `"strategy_assurances"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.projects_project_id` | string | ✅ | The identifier of the audit/project inside Projects Ex.: `"13921"` |
| `data.attributes.projects_objective_id` | string | ✅ | The identifier of the objective inside Projects Ex.: `"73022"` |

</details>

<details>
<summary><strong>Respostas</strong> (5)</summary>

<details>
<summary>`201` — Created.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `GetStrategyRiskAssuranceResponse`

_Apenas campos que diferem do request body. 3 campo(s) idênticos omitidos._

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data.id` | string | ✅ | The ID of the requested resource. Ex.: `"49191"` |
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
