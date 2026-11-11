---
id: endpoint-delete-orgs-org-id-tables-table-id-columns-bulk-bulkdeletecolumns
title: "Table columns: Delete table columns"
tags: [endpoint, table-columns]
source: openapi.json (HighBond API v1.1.0)
---

## Table columns

A group of columns defines a table's schema.

A column's `field_name` must be unique within a table, follow the column naming requirements, and
have a supported data type (`character`, `numeric`, `logical`, `date`, `time`, `datetime`, `file`, or `digital_signature`).

### `DELETE /orgs/{org_id}/tables/{table_id}/columns/bulk` — Delete table columns

- **operationId:** `bulkDeleteColumns`
- **Domínio(s):** Table columns

Delete all the columns in a table.

> **Caution —**
Once you delete columns, the data is permanently removed. You cannot access or restore deleted columns.
Once a table is created and populated with records, deleting a column can break workflows in HighBond that depend on the affected column,
like metrics, visualizations, and triggers.

Limitations: You cannot delete metadata columns (Priority, Status, Published, Publisher Name, Updated, Closed, Assignee, and Workflow Group) or primary key fields.

<details>
<summary><strong>Parâmetros</strong> (2)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `table_id` | path | ✅ | integer | The ID of the table. Ex.: `300` |

</details>

<details>
<summary><strong>Request body (payload)</strong></summary>

An array of column objects.

**Body obrigatório.**

**Content-Type:** `application/json`

**Schema:** `DeleteColumnPayload`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | array[object] | ✅ | The data associated with the resource. |
| `data.field_name` | string | ✅ | The underlying name of a column in a table. `field_name` must be unique within a table and follow the column naming requirements. Ex.: `"account_number"` |

</details>

<details>
<summary><strong>Respostas</strong> (6)</summary>

- `204` — No content.

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
