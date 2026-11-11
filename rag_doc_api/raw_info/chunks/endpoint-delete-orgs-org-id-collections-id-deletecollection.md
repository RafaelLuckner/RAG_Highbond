---
id: endpoint-delete-orgs-org-id-collections-id-deletecollection
title: "Collections: Delete a collection"
tags: [endpoint, collections]
source: openapi.json (HighBond API v1.1.0)
---

## Collections

A collection is a container used to organize analyses that relate to different departments, business processes, or data sets. Collections are the highest level of
organization in the Results app.

Your organization can have a maximum of 2,000 collections.

Learn more about collections.

### `DELETE /orgs/{org_id}/collections/{id}` — Delete a collection

- **operationId:** `deleteCollection`
- **Domínio(s):** Collections

Permanently delete a collection.

> **Caution —**
Deleting a collection also permanently removes all of the analyses and tables associated with the collection.

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
