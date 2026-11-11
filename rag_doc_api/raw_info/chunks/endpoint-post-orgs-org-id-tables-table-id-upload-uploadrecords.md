---
id: endpoint-post-orgs-org-id-tables-table-id-upload-uploadrecords
title: "Table records: Upload records data"
tags: [endpoint, records]
source: openapi.json (HighBond API v1.1.0)
---

## Table records

Records are rows in a table. Each record can have multiple attributes with values.

### `POST /orgs/{org_id}/tables/{table_id}/upload` — Upload records data

- **operationId:** `uploadRecords`
- **Domínio(s):** Records

When uploading records, you need to specify column names, data types, and records data.

Valid data types are `character`, `numeric`, `logical`, `date`, `time`, and `datetime`. For more information, see
Supported data types.

> **Caution —**
Changing a column's data type can break workflows in HighBond that depend on the affected column, such as visualizations, metrics, triggers, and Results table published to Activity Center.

Limitations:

- You cannot upload records to Projects tables.

- Each table can contain a maximum of 100,000 records, 500 columns, and 256 characters per field, including blank characters.

- You can upload up to 100 columns at once. For instance, if you need to upload 300 columns, you can do so in batches of 100 columns three times. However, please note that the total number of columns in a table cannot exceed 500.

- You cannot upload more than 100kbs of records nor make multiple requests simultaneously (429 error). To upload more than 100kb of data, split your records into multiple, smaller requests that can be made in sequence.

- If the table contains a primary key field, the values in the field must be unique. This field is used to uniquely identify each record in the table.

<details>
<summary><strong>Parâmetros</strong> (2)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `table_id` | path | ✅ | integer | The ID of the table. Ex.: `300` |

</details>

<details>
<summary><strong>Request body (payload)</strong></summary>

The data required to upload records.

**Body obrigatório.**

**Content-Type:** `application/json`

**Schema:** `CreateRecordsPayload`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | object | ✅ | The data associated with the resource. |
| `data.columns` | object | ✅ | A key value pair. The key represents the column name and the value represents the column data type. See the request sample for details. Ex.: `{"field_one": "character", "field_two": "character"}` |
| `data.records` | array[object] | ✅ | A key value pair. The key represents the column name and the value represents the column data. See the request sample for details. Ex.: `[{"field_one": "X", "field_two": "2"}, {"field_one": "XYZ", "field_two": "676"}]` |
| `options` | object |  | The options associated with the resource. |
| `options.purge` | boolean |  | Setting to `true` deletes existing records in the table and uploads the new records. Setting to `false` uploads new records and appends them to existing records in the table. Ex.: `true` |

</details>

<details>
<summary><strong>Respostas</strong> (7)</summary>

- `202` — Accepted.

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
