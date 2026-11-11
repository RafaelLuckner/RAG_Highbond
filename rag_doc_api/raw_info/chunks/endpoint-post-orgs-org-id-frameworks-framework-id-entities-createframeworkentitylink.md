---
id: endpoint-post-orgs-org-id-frameworks-framework-id-entities-createframeworkentitylink
title: "Frameworks: Create framework entity link"
tags: [endpoint, frameworks]
source: openapi.json (HighBond API v1.1.0)
---

## Frameworks

A framework is a management system that allows you to define objectives, risks, and controls, perform tests, and compile information for reporting purposes. Frameworks may also
be known as audits, compliance assessments, risk assessments, or another customized term.

Learn more about frameworks.

### `POST /orgs/{org_id}/frameworks/{framework_id}/entities` — Create framework entity link

- **operationId:** `createFrameworkEntityLink`
- **Domínio(s):** Frameworks

Link entity to a framework.

> **Note**
> * Tagging a framework to an entity automatically tags a framework with all ancestor entities and descendant entities.
> * Request Get a framework with `entities` query param to get the whole list of entities linked to a framework.

Limitations:
  * Only 1 entity can be sent in the request payload.

Learn more about tagging items with entities.

<details>
<summary><strong>Parâmetros</strong> (2)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `framework_id` | path | ✅ | integer | The ID of the framework. Ex.: `1` |

</details>

<details>
<summary><strong>Request body (payload)</strong></summary>

The data required to create a framework entity link.

**Body obrigatório.**

**Content-Type:** `application/vnd.api+json`

**Schema:** `CreateFrameworkEntityRequest`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | object | ✅ | The data associated with the resource. |
| `data.id` | string | ✅ | The ID of the framework. Ex.: `"1"` |
| `data.type` | string | ✅ | The classification of the object (`"entities"`). Ex.: `"entities"` |

</details>

<details>
<summary><strong>Respostas</strong> (7)</summary>

<details>
<summary>`201` — Created.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `CreateFrameworkEntityResponse`

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
