---
id: endpoint-delete-orgs-org-id-risks-id-deleterisk
title: "Risks: Delete a risk"
tags: [endpoint, risks]
source: openapi.json (HighBond API v1.1.0)
---

## Risks

A risk is an effect of uncertainty on an objective, with the effect having a positive or negative deviation from what is expected.
Risks are organized by objectives, and can be associated with one or more controls. A risk may also be known as a requirement.

> **Note:**
Risks located in such resources can be accessed using the API:
> * In projects that have an "active" state
> * In frameworks

Learn more about risks.

### `DELETE /orgs/{org_id}/risks/{id}` — Delete a risk

- **operationId:** `deleteRisk`
- **Domínio(s):** Risks

Permanently delete a risk from an objective.

Limitations:
You cannot delete the risk in the following scenarios:
* if the risk is included in an existing certification program
* if the objective it belongs to has been checked out using
Offline Projects or the
HighBond iPad app

> **Caution —**
Deleting a risk also removes associated data (including assessment drivers, to-dos, requests, issues, actions, time entries, etc.). Once deleted, you cannot access or restore the risk.

<details>
<summary><strong>Parâmetros</strong> (2)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `id` | path | ✅ | string | The ID of the requested resource. Ex.: `9999` |

</details>

<details>
<summary><strong>Respostas</strong> (5)</summary>

- `204` — No content.

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
