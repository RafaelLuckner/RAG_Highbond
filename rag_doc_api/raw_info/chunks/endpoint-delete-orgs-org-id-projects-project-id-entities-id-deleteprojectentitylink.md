---
id: endpoint-delete-orgs-org-id-projects-project-id-entities-id-deleteprojectentitylink
title: "Projects: Delete project entity link"
tags: [endpoint, projects]
source: openapi.json (HighBond API v1.1.0)
---

## Projects

A project is a management system that allows you to define objectives, risks, and controls, perform tests, and compile information for reporting purposes. Projects may also
be known as audits, compliance assessments, risk assessments, or another customized term.

Each project has a default system classification, called a "state". A project can have one of the following states:
* `"active"`— projects that are currently in progress
* `"archive"`— projects that are inactive and have been moved to the Project Library
* `"delete"`— previously deleted projects that are stored in the Project Library for 30 days, and then permanently deleted automatically after 30 days

Projects in a `"framework"` state cannot be accessed using the API.

Learn more about projects.

### `DELETE /orgs/{org_id}/projects/{project_id}/entities/{id}` — Delete project entity link

- **operationId:** `deleteProjectEntityLink`
- **Domínio(s):** Projects

Permanently delete project entity link.

> **Note -**
Untagging a project from an entity automatically untags a project from all descendant entities.

<details>
<summary><strong>Parâmetros</strong> (3)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `project_id` | path | ✅ | integer | The ID of the project. Ex.: `1` |
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
