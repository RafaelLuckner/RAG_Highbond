---
id: endpoint-post-orgs-org-id-controls-control-id-entities-createcontrolentitylink
title: "Controls: Create control entity link"
tags: [endpoint, controls]
source: openapi.json (HighBond API v1.1.0)
---

## Controls

A control is a program, policy, routine, or activity that is intended to mitigate a risk. Controls are organized by objectives, and can be associated with one or more risks.
The combination of identified risks and corresponding controls defines the Risk Control Matrix. Controls are also known as procedures.

> **Note:**
Controls located in such resources can be accessed using the API:
> * In projects that have an "active" state
> * In frameworks

Learn more about controls.

### `POST /orgs/{org_id}/controls/{control_id}/entities` — Create control entity link

- **operationId:** `createControlEntityLink`
- **Domínio(s):** Controls

Link entity to a control.

> **Note**
> * Tagging a control to an entity automatically tags a control with all ancestor entities and descendant entities.
> * Request Get a control with `entities` query param to get the whole list of entities linked to a control.

Limitations:
  * You cannot tag the control with entity if the objective it belongs to has been checked out using
  Offline Projects or the
  HighBond iPad app.
  * Only 1 entity can be sent in the request payload.

Learn more about tagging items with entities.

<details>
<summary><strong>Parâmetros</strong> (2)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `control_id` | path | ✅ | integer | The ID of the control. Ex.: `1` |

</details>

<details>
<summary><strong>Request body (payload)</strong></summary>

The data required to create a control entity link.

**Body obrigatório.**

**Content-Type:** `application/vnd.api+json`

**Schema:** `CreateControlEntityRequest`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | object | ✅ | The data associated with the resource. |
| `data.id` | string | ✅ | The ID of the control. Ex.: `"1"` |
| `data.type` | string | ✅ | The classification of the object (`"entities"`). Ex.: `"entities"` |

</details>

<details>
<summary><strong>Respostas</strong> (7)</summary>

<details>
<summary>`201` — Created.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `CreateControlEntityResponse`

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
