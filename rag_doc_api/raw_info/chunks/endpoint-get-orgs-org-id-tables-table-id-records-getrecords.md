---
id: endpoint-get-orgs-org-id-tables-table-id-records-getrecords
title: "Table records: Get records"
tags: [endpoint, records]
source: openapi.json (HighBond API v1.1.0)
---

## Table records

Records are rows in a table. Each record can have multiple attributes with values.

### `GET /orgs/{org_id}/tables/{table_id}/records` — Get records

- **operationId:** `getRecords`
- **Domínio(s):** Records

Get all the records in a table.

> **Note:**
> * By default, this endpoint returns a maximum of 100,000 records. Records above this limit are truncated.
> * Use query parameters to filter and get the records you need.
>   * Parameters can be applied to any field in the table with the following data type: Character, Numeric, Date, and Datetime.
>   * You can have a maximum of 2 unique fields in a single query.
>   * You can filter records by a single value or multiple values. For multiple values, add the filter string
> multiple times with an addition of array indication `[]` to each of filter keys.
>   * The maximum limit of the query string is 6000 characters.
>
> Examples:
> * If you need to get records that are in "New" status:
> `{protocol}://{server}/v1/orgs/{org_id}/tables/{table_id}/records?filter[metadata.status]=New`
> * If you need to get records that are in either "New" or "Open" status:
> `{protocol}://{server}/v1/orgs/{org_id}/tables/{table_id}/records?filter[metadata.status][]=New&filter[metadata.status][]=Open`
> * If you need to get records that are in either "New" or "Open" status with a publish date of "2022-05-10T00:03:46Z".
> `{protocol}://{server}/v1/orgs/{org_id}/tables/{table_id}/records?filter[metadata.status][]=New&filter[metadata.status][]=Open&filter[metadata.publish_date]=2022-05-10T00:03:46Z`

<details>
<summary><strong>Parâmetros</strong> (4)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `table_id` | path | ✅ | integer | The ID of the table. Ex.: `300` |
| `filter[metadata.status][]` | query |  | string | Requesting the API to return records with the specified statuses only. To filter the records for multiple values, add the filter string multiple times. For example, if you need to get records that have either "New" or "Open" status, pass the filters as follows `?filter[metadata.status][]=New&filter[metadata.status][]=Open`. For more information, see Making requests Ex.: `New` |
| `filter[metadata.assignee]` | query |  | string | Requesting the API to return records with the specified assignees only. For more information, see Making requests Ex.: `Bob%20Marley` |

</details>

<details>
<summary><strong>Respostas</strong> (6)</summary>

<details>
<summary>`200` — OK.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `MultiRecordsResponse`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `columns` | array[object] | ✅ | A key value pair. The key represents the column name and the value represents the column data type. See the request sample for details. Ex.: `[{"field_name": "field_one", "display_name": "Field one", "data_type": "character"}, {"field_name": "field_two", "display_name": "Field two", "data...` |
| `data` | array[object] | ✅ | A key value pair. The key represents the column name and the value represents the column data. See the request sample for details. Ex.: `[{"field_one": "X", "field_two": "2"}, {"field_one": "XYZ", "field_two": "676"}]` |

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
