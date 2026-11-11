---
id: endpoint-put-orgs-org-id-tables-id-updatetable
title: "Tables: Update a table"
tags: [endpoint, tables]
source: openapi.json (HighBond API v1.1.0)
---

## Tables

Tables store records of data in rows and columns. They are a third level of organization in Results. Each table lives in an analysis, which lives in a collection.

Your organization can have a maximum of 5,000 tables and each table can hold a maximum of 100,000 rows, 500 columns, and 256 characters per field, including blank characters.

There are different types of tables in HighBond: **data analytics**, **surveys**, **event reports**, **Projects**, **assessment**, and **system**. The tables API currently only supports **data analytic** tables, **assessment** tables, and **system** tables that are in the Reference Collection.

Learn more about tables.

### `PUT /orgs/{org_id}/tables/{id}` — Update a table

- **operationId:** `updateTable`
- **Domínio(s):** Tables

Make changes to a table, like renaming it. You do not need to update tables for them to reflect changes in data.

<details>
<summary><strong>Parâmetros</strong> (2)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `id` | path | ✅ | string | The ID of the requested resource. Ex.: `9999` |

</details>

<details>
<summary><strong>Request body (payload)</strong></summary>

The data required to update a table.

**Body obrigatório.**

**Content-Type:** `application/vnd.api+json`

**Schema:** `UpdateTablePayload`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | object | ✅ | The data associated with the resource. |
| `data.id` | string | ✅ | The ID of the table. Ex.: `"300"` |
| `data.type` | string | ✅ | The classification of the object (`"tables"`). Ex.: `"tables"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.name` | string |  | The name of the table. Ex.: `"My first Table"` |
| `data.attributes.description` | string |  | The description of the table. Ex.: `"Description of My first Table"` |
| `data.attributes.script_name` | string |  | The name of the script, or process, used to generate the result set. Ex.: `"Sec01_Wknd_Unauth_Access_Point"` |
| `data.attributes.publish_platform_reporting_sync` | boolean |  | The flag that indicates whether the table is synchronizing with activity center. Ex.: `true` |
| `data.attributes.primary_key` | string |  | Field that uniquely identifies a record. Specifying a primary key field allows uploads of records sharing the same primary key to be merged rather than duplicated. Default: `None` Ex.: `"primary_key"` |
| `data.attributes.record_identifiers` | array[string] |  | Select a few non-sensitive fields that identify a record. You can select any imported data, Results metadata fields, and questionnaire fields. These fields will be displayed in emails sent to recipients and when they fill out questionnaires. In sequential certifications, recipients always see previous answers. * You can select values from `user_fields` (user-created columns in the table) * You can select values from `metadata_fields`, which can be one or more of the following: `record_id`, `position`, `priority`, `status`, `publish_date`, `publisher`, `assignee`, `group`, `updated_at`, `closed_at` Default: `[':record_id']` Ex.: `[":record_id"]` |

</details>

<details>
<summary><strong>Respostas</strong> (7)</summary>

<details>
<summary>`200` — OK.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `SingleTableResponse`

_Apenas campos que diferem do request body. 10 campo(s) idênticos omitidos._

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data.attributes.table_type` | string |  | Table type; this cannot be updated once table is created. Valores: `data_analytic`, `assessment_table` Default: `data_analytic` Ex.: `"data_analytic"` |
| `data.attributes.questionnaire_id` | string |  | The id of the single questionnaire associated with this table (assessment tables only). Ex.: `"1"` |
| `data.attributes.data_table_id` | integer |  | The data table ID of the table. Ex.: `123` |
| `data.attributes.created_at` | string |  | The date the table was created. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.attributes.updated_at` | string |  | The date the table was updated. Ex.: `"2019-03-18T22:02:05Z"` |
| `data.relationships` | object | ✅ | The relationships associated with the resource. Ex.: `{"analysis": {"data": {"id": "20", "type": "analyses"}}}` |
| `data.relationships.analysis` | RelationshipObject |  |  |
| `data.relationships.analysis.data` | object | ✅ | The data associated with the related object. |
| `data.relationships.analysis.data.id` | string | ✅ | The ID of the related object. Ex.: `1` |
| `data.relationships.analysis.data.type` | string | ✅ | The classification of the related object. Ex.: `"collection"` |

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
