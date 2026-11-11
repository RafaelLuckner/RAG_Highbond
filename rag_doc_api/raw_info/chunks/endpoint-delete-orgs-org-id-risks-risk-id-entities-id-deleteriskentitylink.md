---
id: endpoint-delete-orgs-org-id-risks-risk-id-entities-id-deleteriskentitylink
title: "Risks: Delete risk entity link"
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

### `DELETE /orgs/{org_id}/risks/{risk_id}/entities/{id}` — Delete risk entity link

- **operationId:** `deleteRiskEntityLink`
- **Domínio(s):** Risks

Permanently delete risk entity link.

> **Note -**
Untagging a risk from an entity automatically untags a risk from all descendant entities.

Limitations:
  * You cannot untag a risk from an entity if the objective it belongs to has been checked out using
  Offline Projects or the
  HighBond iPad app.
  * Inherited entity tags cannot be removed.

<details>
<summary><strong>Parâmetros</strong> (3)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `risk_id` | path | ✅ | integer | The ID of the risk. Ex.: `1` |
| `id` | path | ✅ | string | The ID of the requested resource. Ex.: `9999` |

</details>

<details>
<summary><strong>Respostas</strong> (7)</summary>

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

<details>
<summary>`422` — Unprocessable entity.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `Errors`

Erro no formato padrão JSON:API: objeto `errors` (array) com `status` (código HTTP), `source.pointer` (JSON Pointer RFC6901 do campo com erro), `code`, `title` e `detail`.

</details>

</details>
