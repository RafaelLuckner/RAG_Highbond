---
id: endpoint-delete-orgs-org-id-narratives-id-deletenarratrive
title: "Narratives: Delete a narrative"
tags: [endpoint, narratives]
source: openapi.json (HighBond API v1.1.0)
---

## Narratives

A narrative is a description of a business process or area under review. Narratives are also known as policies, IT policies, process narratives, process descriptions, or control guides.

> **Note:**
> * To access narratives using the API, the narratives tab must be enabled in the project type associated with the project or framework.
>
> Narratives located in such resources can be accessed using the API:
> * In Internal Control workflow projects that have an "active" state
> * In frameworks

Learn more about narratives.

### `DELETE /orgs/{org_id}/narratives/{id}` — Delete a narrative

- **operationId:** `deleteNarratrive`
- **Domínio(s):** Narratives

Permanently delete a narrative from an objective.

Limitations:
* You cannot delete the narrative if it is included in an existing certification program.
* You cannot delete the narrative if the objective it belongs to has been checked out using
Offline Projects or the
HighBond iPad app.

> **Caution —**
Deleting a narrative is permanent. Once deleted, you cannot access or restore the narrative.

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
