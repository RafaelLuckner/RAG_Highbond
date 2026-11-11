---
id: endpoint-delete-orgs-org-id-objectives-id-deleteobjective
title: "Objectives: Delete an objective"
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

### `DELETE /orgs/{org_id}/objectives/{id}` — Delete an objective

- **operationId:** `deleteObjective`
- **Domínio(s):** Objectives

Permanently delete an objective from a project or framework.

Limitations:
You cannot delete the objective in the following scenarios:
* if the objective is included in an existing certification program
* if the objective has been checked out using
Offline Projects or the
HighBond iPad app

> **Caution —**
Deleting an objective also removes associated data (including risks, controls, walkthroughs, test plans, control tests, to-dos, requests, issues, actions, time entries, etc.). Once deleted, you cannot access or restore the objective.

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
