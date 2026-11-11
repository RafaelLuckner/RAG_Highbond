---
id: endpoint-post-orgs-org-id-objectives-objective-id-entities-createobjectiveentitylink
title: "Objectives: Create objective entity link"
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

### `POST /orgs/{org_id}/objectives/{objective_id}/entities` — Create objective entity link

- **operationId:** `createObjectiveEntityLink`
- **Domínio(s):** Objectives

Link entity to an objective.

> **Note**
> * Tagging an objective to an entity automatically tags an objective with all ancestor entities and descendant entities.
> * Request Get an objective with `entities` query param to get the whole list of entities linked to an objective.

Limitations:
  * You cannot tag the objective with entity if it has been checked out using
  Offline Projects or the
  HighBond iPad app.
  * Only 1 entity can be sent in the request payload.

Learn more about tagging items with entities.

<details>
<summary><strong>Parâmetros</strong> (2)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `objective_id` | path | ✅ | integer | The ID of the objective. Ex.: `1` |

</details>

<details>
<summary><strong>Request body (payload)</strong></summary>

The data required to create a objective entity link.

**Body obrigatório.**

**Content-Type:** `application/vnd.api+json`

**Schema:** `CreateObjectiveEntityRequest`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | object | ✅ | The data associated with the resource. |
| `data.id` | string | ✅ | The ID of the objective. Ex.: `"1"` |
| `data.type` | string | ✅ | The classification of the object (`"entities"`). Ex.: `"entities"` |

</details>

<details>
<summary><strong>Respostas</strong> (7)</summary>

<details>
<summary>`201` — Created.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `CreateObjectiveEntityResponse`

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
