---
id: endpoint-post-orgs-org-id-tables-table-id-columns-bulk-bulkcreatecolumns
title: "Table columns: Create columns in a table"
tags: [endpoint, table-columns]
source: openapi.json (HighBond API v1.1.0)
---

## Table columns

A group of columns defines a table's schema.

A column's `field_name` must be unique within a table, follow the column naming requirements, and
have a supported data type (`character`, `numeric`, `logical`, `date`, `time`, `datetime`, `file`, or `digital_signature`).

### `POST /orgs/{org_id}/tables/{table_id}/columns/bulk` — Create columns in a table

- **operationId:** `bulkCreateColumns`
- **Domínio(s):** Table columns

Add new columns to a table.

Limitations:
* Once a table exists, you cannot change a column's data type.
* You cannot set a primary key when adding columns to a table.
* Each table can contain a maximum of 500 columns.

<details>
<summary><strong>Parâmetros</strong> (2)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `table_id` | path | ✅ | integer | The ID of the table. Ex.: `300` |

</details>

<details>
<summary><strong>Request body (payload)</strong></summary>

The data required to create a column.

**Body obrigatório.**

**Content-Type:** `application/json`

**Schema:** `CreateColumnPayload`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | array[object] | ✅ | The data associated with the resource. |
| `data.field_name` | string | ✅ | The underlying name of a column in a table. `field_name` must be unique within a table and follow the column naming requirements. Ex.: `"account_number"` |
| `data.display_name` | string |  | The name of the column that is displayed in the table. Ex.: `"Account number"` |
| `data.data_type` | string | ✅ | The data type of the column. Supported data types include `character`, `numeric`, `logical`, `date`, `time`, `datetime`, `file`, or `digital_signature`. Ex.: `"character"` |

</details>

<details>
<summary><strong>Respostas</strong> (7)</summary>

<details>
<summary>`201` — Created.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `MultiColumnsResponse`

_Apenas campos que diferem do request body. 1 campo(s) idênticos omitidos._

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data.id` | string | ✅ | The `field_name` of a column. Ex.: `"account_number"` |
| `data.type` | string | ✅ | The classification of the object (`"columns"`). Ex.: `"columns"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.display_name` | string |  | The name of the column that is displayed in the table. Ex.: `"Account number"` |
| `data.attributes.data_type` | string |  | The data type of the column. Supported data types include `character`, `numeric`, `logical`, `date`, `time`, `datetime`, `file`, or `digital_signature`. Ex.: `"character"` |
| `data.attributes.is_primary_key` | boolean |  | Specifies if the column is a primary key field. For more information, see Specifying a primary key. |
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

<details>
<summary>`422` — Unprocessable entity.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `Errors`

Erro no formato padrão JSON:API: objeto `errors` (array) com `status` (código HTTP), `source.pointer` (JSON Pointer RFC6901 do campo com erro), `code`, `title` e `detail`.

</details>

</details>
