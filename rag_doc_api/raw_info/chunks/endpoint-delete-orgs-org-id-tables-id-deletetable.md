---
id: endpoint-delete-orgs-org-id-tables-id-deletetable
title: "Tables: Delete a table"
tags: [endpoint, tables]
source: openapi.json (HighBond API v1.1.0)
---

## Tables

Tables store records of data in rows and columns. They are a third level of organization in Results. Each table lives in an analysis, which lives in a collection.

Your organization can have a maximum of 5,000 tables and each table can hold a maximum of 100,000 rows, 500 columns, and 256 characters per field, including blank characters.

There are different types of tables in HighBond: **data analytics**, **surveys**, **event reports**, **Projects**, **assessment**, and **system**. The tables API currently only supports **data analytic** tables, **assessment** tables, and **system** tables that are in the Reference Collection.

Learn more about tables.

### `DELETE /orgs/{org_id}/tables/{id}` — Delete a table

- **operationId:** `deleteTable`
- **Domínio(s):** Tables

Permanently delete a table.

> **Caution —**
Deleting a table also permanently removes associated records, interpretations, metrics, and triggers.

Limitations: Generally, you cannot delete tables that were created in HighBond to support the operation of another feature (for example, Certifications and Control Performance generates their own data structures). You can delete these tables by deleting the project that generated them in the Projects app.

<details>
<summary><strong>Parâmetros</strong> (2)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `id` | path | ✅ | string | The ID of the requested resource. Ex.: `9999` |

</details>

<details>
<summary><strong>Respostas</strong> (6)</summary>

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

</details>
