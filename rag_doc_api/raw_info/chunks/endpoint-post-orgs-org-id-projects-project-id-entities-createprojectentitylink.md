---
id: endpoint-post-orgs-org-id-projects-project-id-entities-createprojectentitylink
title: "Projects: Create project entity link"
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

### `POST /orgs/{org_id}/projects/{project_id}/entities` — Create project entity link

- **operationId:** `createProjectEntityLink`
- **Domínio(s):** Projects

Link entity to a project.

> **Note**
> * Tagging a project to an entity automatically tags a project with all ancestor entities and descendant entities.
> * Request Get a project with `entities` query param to get the whole list of entities linked to a project.

Limitations:
  * Only 1 entity can be sent in the request payload.

Learn more about tagging items with entities.

<details>
<summary><strong>Parâmetros</strong> (2)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `project_id` | path | ✅ | integer | The ID of the project. Ex.: `1` |

</details>

<details>
<summary><strong>Request body (payload)</strong></summary>

The data required to create a project entity link.

**Body obrigatório.**

**Content-Type:** `application/vnd.api+json`

**Schema:** `CreateProjectEntityRequest`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | object | ✅ | The data associated with the resource. |
| `data.id` | string | ✅ | The ID of the project. Ex.: `"1"` |
| `data.type` | string | ✅ | The classification of the object (`"entities"`). Ex.: `"entities"` |

</details>

<details>
<summary><strong>Respostas</strong> (7)</summary>

<details>
<summary>`201` — Created.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `CreateProjectEntityResponse`

_Mesma estrutura de campos do request body (tabela acima)._

</details>

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
