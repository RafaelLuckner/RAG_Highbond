---
id: endpoint-delete-orgs-org-id-project-types-id-deleteprojecttype
title: "Project types: Delete a project type"
tags: [endpoint, project-types]
source: openapi.json (HighBond API v1.1.0)
---

## Project types

Project types define the structure of a project or framework, including the terminology used in the project or framework. Updates to project types apply to
all active projects, archived projects, temporarily deleted projects, and frameworks associated with the project type.

Each project type has an associated workflow: Workplan (`procedure`) or Internal Control (`control`). Workflows define the components available in a project
or framework.  The attributes `narrative_terms`, `control_test_terms`, and `test_plan_terms` are not available for a Workplan (`procedure`) workflow.

When creating a new project type, only the basic defining attributes are available. After creating the project type default customizable terms and toggles
are returned and available on PATCH requests for update.

### `DELETE /orgs/{org_id}/project_types/{id}` — Delete a project type

- **operationId:** `deleteProjectType`
- **Domínio(s):** Project types

Delete a project type from a HighBond instance.

Limitation:
You cannot delete project types that are associated with active projects, archived projects, temporarily deleted projects, or frameworks.

> **Caution —**
Deleting a project type is permanent. Once deleted, you cannot access or restore the project type.

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
<summary>`422` — Unprocessable entity.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `Errors`

Erro no formato padrão JSON:API: objeto `errors` (array) com `status` (código HTTP), `source.pointer` (JSON Pointer RFC6901 do campo com erro), `code`, `title` e `detail`.

</details>

</details>
