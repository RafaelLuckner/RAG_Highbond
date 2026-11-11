---
id: endpoint-delete-orgs-org-id-mitigations-id-deletemitigation
title: "Mitigations: Delete a mitigation"
tags: [endpoint, mitigations]
source: openapi.json (HighBond API v1.1.0)
---

## Mitigations

> **Note —**
Only controls in projects that have an `"active"` state can be accessed using the API.

### `DELETE /orgs/{org_id}/mitigations/{id}` — Delete a mitigation

- **operationId:** `deleteMitigation`
- **Domínio(s):** Mitigations

Permanently delete a mitigation.

Limitations:
* You cannot delete the mitigation if the objective it belongs to has been checked out using
Offline Projects or the
HighBond iPad app.

> **Caution —**
Deleting a mitigation is permanent. Once deleted, you cannot access or restore the mitigation.

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
