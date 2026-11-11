---
id: endpoint-delete-orgs-org-id-results-files-id-deleteresultsfile
title: "Results files: Delete a results file"
tags: [endpoint, results-files]
source: openapi.json (HighBond API v1.1.0)
---

## Results files

A results file is a supporting document or concluding memo that relates to a project. Results files typically contain information associated
with the reporting phase of a project.

> **Note —**
Only results files in projects that have an `"active"` state can be accessed using the API.

Learn more about results files.

### `DELETE /orgs/{org_id}/results_files/{id}` — Delete a results file

- **operationId:** `deleteResultsFile`
- **Domínio(s):** Results files

Delete a results file from a project.

> **Caution —**
Deleting a results file is permanent. Once deleted, you cannot access or restore the results file.

<details>
<summary><strong>Parâmetros</strong> (2)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `id` | path | ✅ | string | The ID of the requested resource. Ex.: `9999` |

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
<summary>`422` — Unprocessable entity.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `Errors`

Erro no formato padrão JSON:API: objeto `errors` (array) com `status` (código HTTP), `source.pointer` (JSON Pointer RFC6901 do campo com erro), `code`, `title` e `detail`.

</details>

</details>
