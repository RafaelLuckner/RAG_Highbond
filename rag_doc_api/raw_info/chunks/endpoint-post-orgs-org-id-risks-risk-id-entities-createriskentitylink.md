---
id: endpoint-post-orgs-org-id-risks-risk-id-entities-createriskentitylink
title: "Risks: Create risk entity link"
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

### `POST /orgs/{org_id}/risks/{risk_id}/entities` — Create risk entity link

- **operationId:** `createRiskEntityLink`
- **Domínio(s):** Risks

Link entity to a risk.

> **Note**
> * Tagging a risk to an entity automatically tags a risk with all ancestor entities and descendant entities.
> * Request Get a risk with `entities` query param to get the whole list of entities linked to a risk.

Limitations:
  * You cannot tag the risk with entity if the objective it belongs to has been checked out using
  Offline Projects or the
  HighBond iPad app.
  * Only 1 entity can be sent in the request payload.

Learn more about tagging items with entities.

<details>
<summary><strong>Parâmetros</strong> (2)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `risk_id` | path | ✅ | integer | The ID of the risk. Ex.: `1` |

</details>

<details>
<summary><strong>Request body (payload)</strong></summary>

The data required to create a risk entity link.

**Body obrigatório.**

**Content-Type:** `application/vnd.api+json`

**Schema:** `CreateRiskEntityRequest`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | object | ✅ | The data associated with the resource. |
| `data.id` | string | ✅ | The ID of the risk. Ex.: `"1"` |
| `data.type` | string | ✅ | The classification of the object (`"entities"`). Ex.: `"entities"` |

</details>

<details>
<summary><strong>Respostas</strong> (7)</summary>

<details>
<summary>`201` — Created.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `CreateRiskEntityResponse`

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
