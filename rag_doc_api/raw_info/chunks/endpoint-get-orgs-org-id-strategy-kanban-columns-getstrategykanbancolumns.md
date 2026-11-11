---
id: endpoint-get-orgs-org-id-strategy-kanban-columns-getstrategykanbancolumns
title: "Strategy: Get risk status columns"
tags: [endpoint, strategy]
source: openapi.json (HighBond API v1.1.0)
---

## Strategy

You can use the Strategy app to identify, assess, and monitor strategic risks.

Learn more.

### `GET /orgs/{org_id}/strategy_kanban_columns` — Get risk status columns

- **operationId:** `getStrategyKanbanColumns`
- **Domínio(s):** Strategy

Retrieves the risk status board from
Strategy.

Each column lists the risks contained inside that column.

The `id` can be one of the following:
  - `assess`
  - `accepted`
  - `audit`
  - `continuously_audit`
  - `mitigated`

This information is also provided inside the Risk
resource as the field `status`.

<details>
<summary><strong>Parâmetros</strong> (1)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |

</details>

<details>
<summary><strong>Respostas</strong> (5)</summary>

<details>
<summary>`200` — OK.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `GetStrategyKanbanColumnsResponse`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | array[object] | ✅ | Array of segments |
| `data.id` | string | ✅ | The ID of the requested resource. Ex.: `"assess"` |
| `data.type` | string | ✅ | The classification of the object (`"strategy_kanban_columns"`). Ex.: `"strategy_kanban_columns"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.name` | string |  | The name of the column. Ex.: `"Assessment"` |
| `data.attributes.risk_ids` | array[string] |  | IDs of the risks inside the column. Ex.: `["1", "2", "13", "41"]` |

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
