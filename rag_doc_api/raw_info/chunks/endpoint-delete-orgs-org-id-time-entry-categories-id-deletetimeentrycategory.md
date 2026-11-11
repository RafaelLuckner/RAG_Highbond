---
id: endpoint-delete-orgs-org-id-time-entry-categories-id-deletetimeentrycategory
title: "Non-project time categories: Delete a non-project time category"
tags: [endpoint, non-project-time-categories]
source: openapi.json (HighBond API v1.1.0)
---

## Non-project time categories

Use non-project time categories to divide non-project time entries by categories.

Learn more about non-project time categories.

### `DELETE /orgs/{org_id}/time_entry_categories/{id}` — Delete a non-project time category

- **operationId:** `deleteTimeEntryCategory`
- **Domínio(s):** Non-project time categories

Permanently delete a non-project time category.

> **Caution —**
Deleting a non-project time category also permanently deletes any associated time entries.

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
<summary>`415` — Unsupported media type.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `Errors`

Erro no formato padrão JSON:API: objeto `errors` (array) com `status` (código HTTP), `source.pointer` (JSON Pointer RFC6901 do campo com erro), `code`, `title` e `detail`.

</details>

</details>
