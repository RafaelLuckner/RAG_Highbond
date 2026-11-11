---
id: endpoint-delete-orgs-org-id-objectives-objective-id-entities-id-deleteobjectiveentitylink
title: "Objectives: Delete objective entity link"
tags: [endpoint, objectives]
source: openapi.json (HighBond API v1.1.0)
---

## Objectives

Objectives are the basis of a project or framework. They are also the organizing containers for the work done in a project or framework.
Each objective states the subject matter under examination and how performance will be assessed.

Objectives may also be known as sections, processes, cycles, functional areas, application systems, risk categories, or another custom term.

> **Note:**
Objectives located in such resources can be accessed using the API:
> * In projects that have an "active" state
> * In frameworks

Learn more about objectives.

### `DELETE /orgs/{org_id}/objectives/{objective_id}/entities/{id}` — Delete objective entity link

- **operationId:** `deleteObjectiveEntityLink`
- **Domínio(s):** Objectives

Permanently delete objective entity link.

> **Note -**
Untagging an objective from an entity automatically untags an objective from all descendant entities.

Limitations:
  * You cannot untag an objective from an entity if it has been checked out using
  Offline Projects or the
  HighBond iPad app.
  * Inherited entity tags cannot be removed.

<details>
<summary><strong>Parâmetros</strong> (3)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `objective_id` | path | ✅ | integer | The ID of the objective. Ex.: `1` |
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
