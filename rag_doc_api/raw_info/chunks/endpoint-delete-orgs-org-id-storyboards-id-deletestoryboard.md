---
id: endpoint-delete-orgs-org-id-storyboards-id-deletestoryboard
title: "Storyboards: Delete a storyboard"
tags: [endpoint, storyboards]
source: openapi.json (HighBond API v1.1.0)
---

## Storyboards

A storyboard is a communication platform that displays multiple visualizations and rich text content in rows and columns. You can use this API to create, configure,
update, and delete storyboards. However, to see your storyboards, you need to log in to HighBond or have someone send you a link to that storyboard.

Learn more about storyboards.

### `DELETE /orgs/{org_id}/storyboards/{id}` — Delete a storyboard

- **operationId:** `deleteStoryboard`
- **Domínio(s):** Storyboards

Permanently delete a storyboard.

> **Caution —**
Once you delete a storyboard, it cannot be recovered.

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
