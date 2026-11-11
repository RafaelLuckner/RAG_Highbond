---
id: endpoint-delete-orgs-org-id-planning-files-id-deleteplanningfile
title: "Planning files: Delete a planning file"
tags: [endpoint, planning-files]
source: openapi.json (HighBond API v1.1.0)
---

## Planning files

A planning file (also known as a reference file) is a supporting document that relates to a project or framework. Planning files typically
contain information associated with the planning phase of a project or framework.

> **Note:**
Planning files located in such resources can be accessed using the API:
> * In projects that have an "active" state
> * In frameworks

Learn more about planning files.

### `DELETE /orgs/{org_id}/planning_files/{id}` — Delete a planning file

- **operationId:** `deletePlanningFile`
- **Domínio(s):** Planning files

Delete a planning file from a project or framework.

> **Caution —**
Deleting a planning file is permanent. Once deleted, you cannot access or restore the planning file.

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
