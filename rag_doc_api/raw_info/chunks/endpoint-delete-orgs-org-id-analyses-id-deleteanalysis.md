---
id: endpoint-delete-orgs-org-id-analyses-id-deleteanalysis
title: "Analyses: Delete an analysis"
tags: [endpoint, analyses]
source: openapi.json (HighBond API v1.1.0)
---

## Analyses

An analysis is a second-level container. Analyses live in collections, and they are used to organize tables. Once you have created a collection, you can add one or
more analyses to that collection.

Your organization can have a maximum of 2,000 analyses.

Learn more about analyses.

### `DELETE /orgs/{org_id}/analyses/{id}` — Delete an analysis

- **operationId:** `deleteAnalysis`
- **Domínio(s):** Analyses

Permanently delete an analysis.

> **Caution —**
Deleting an analysis also permanently removes tables associated with the analysis.

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
