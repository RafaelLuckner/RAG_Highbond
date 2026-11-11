---
id: endpoint-post-orgs-org-id-issues-issue-id-entities-createissueentitylink
title: "Issues: Create issue entity link"
tags: [endpoint, issues]
source: openapi.json (HighBond API v1.1.0)
---

## Issues

An issue is a problem, control gap, or exception that has been identified within a project. Adding an issue involves recording basic information about the issue and assigning
the issue to an owner. Issues may also be known as deficiencies, findings, or another customized term.

> **Note —**
Only issues in projects that have an `"active"` state can be accessed using the API.

Learn more about issues.

### `POST /orgs/{org_id}/issues/{issue_id}/entities` — Create issue entity link

- **operationId:** `createIssueEntityLink`
- **Domínio(s):** Issues

Link entity to an issue.

> **Note**
> * Tagging an issue to an entity automatically tags an issue with all ancestor entities and descendant entities.
> * Request Get an issue with `entities` query param to get the whole list of entities linked to an issue.

Limitations:
  * You cannot tag the issue with entity if the objective it belongs to has been checked out using
  Offline Projects or the
  HighBond iPad app.
  * Only 1 entity can be sent in the request payload.

Learn more about tagging items with entities.

<details>
<summary><strong>Parâmetros</strong> (2)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `issue_id` | path | ✅ | integer | The ID of the issue. Ex.: `1` |

</details>

<details>
<summary><strong>Request body (payload)</strong></summary>

The data required to create a issue entity link.

**Body obrigatório.**

**Content-Type:** `application/vnd.api+json`

**Schema:** `CreateIssueEntityRequest`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | object | ✅ | The data associated with the resource. |
| `data.id` | string | ✅ | The ID of the issue. Ex.: `"1"` |
| `data.type` | string | ✅ | The classification of the object (`"entities"`). Ex.: `"entities"` |

</details>

<details>
<summary><strong>Respostas</strong> (7)</summary>

<details>
<summary>`201` — Created.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `CreateIssueEntityResponse`

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
