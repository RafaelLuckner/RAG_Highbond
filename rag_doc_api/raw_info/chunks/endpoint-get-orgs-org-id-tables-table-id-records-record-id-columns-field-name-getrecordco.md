---
id: endpoint-get-orgs-org-id-tables-table-id-records-record-id-columns-field-name-getrecordco
title: "Record columns: Get record attachments"
tags: [endpoint, record-columns]
source: openapi.json (HighBond API v1.1.0)
---

## Record columns

### `GET /orgs/{org_id}/tables/{table_id}/records/{record_id}/columns/{field_name}` — Get record attachments

- **operationId:** `getRecordColumn`
- **Domínio(s):** Record columns

Get file attachments from a record attachment field

> **Note —**
  You must be a system admin with a Professional subscription to access this API endpoint.

**Make a note of the following:**
* If there are multiple attachments in a single record field, all the attachments are retrieved in the response and each attachment will have a separate signed URL.
* Multiple signed URLs are separated by commas.
* The signed URL to an attachment is valid for only 2 minutes.

<details>
<summary><strong>Parâmetros</strong> (4)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `table_id` | path | ✅ | integer | The ID of the table. Ex.: `300` |
| `record_id` | path | ✅ | string | The ID of the "metadata.record_id". Ex.: `2171909125478738` |
| `field_name` | path | ✅ | string | Field name. Ex.: `q1234567` |

</details>

<details>
<summary><strong>Respostas</strong> (6)</summary>

<details>
<summary>`200` — OK.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `SingleRecordColumnResponse`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `columns` | array[object] | ✅ | description |
| `columns.field_name` | string |  | The underlying name of a column in a table. Ex.: `"q4123324"` |
| `columns.display_name` | string |  | The name of the column that is displayed in the table. Ex.: `"Supporting_evidence"` |
| `columns.data_type` | string |  | The data type of the column. Ex.: `"file"` |
| `data` | object | ✅ | A key value pair. The key represents the column name and the value represents the column data. See the request sample for details. Ex.: `{"q4123324": ["https://drive-api-us2-main-s3.s3.us-west-2.amazonaws.com/fiels/1/700b6b7c-7b6a-4f2d-a1e1-f9ca62727492", "https://drive-api-us2-main-...` |

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

</details>
