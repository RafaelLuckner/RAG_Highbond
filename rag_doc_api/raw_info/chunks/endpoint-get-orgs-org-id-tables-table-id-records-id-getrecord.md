---
id: endpoint-get-orgs-org-id-tables-table-id-records-id-getrecord
title: "Table records: Get a table record"
tags: [endpoint, records]
source: openapi.json (HighBond API v1.1.0)
---

## Table records

Records are rows in a table. Each record can have multiple attributes with values.

### `GET /orgs/{org_id}/tables/{table_id}/records/{id}` — Get a table record

- **operationId:** `getRecord`
- **Domínio(s):** Records

Get information about a table record.

<details>
<summary><strong>Parâmetros</strong> (3)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `table_id` | path | ✅ | integer | The ID of the table. Ex.: `300` |
| `id` | path | ✅ | string | The ID of the requested resource. Ex.: `9999` |

</details>

<details>
<summary><strong>Respostas</strong> (5)</summary>

<details>
<summary>`200` — OK.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `SingleRecordResponse`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `columns` | array[object] | ✅ | A key value pair. The key represents the column name and the value represents the column data type. See the request sample for details. Ex.: `[{"field_name": "field_one", "display_name": "Field one", "data_type": "character"}, {"field_name": "field_two", "display_name": "Field two", "data...` |
| `data` | object | ✅ | A key value pair. The key represents the column name and the value represents the column data. See the request sample for details. Ex.: `{"field_one": "X", "field_two": "2"}` |

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
