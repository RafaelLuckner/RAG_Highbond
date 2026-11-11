---
id: endpoint-get-orgs-org-id-handlers-gethandlers
title: "Handlers: List Handlers"
tags: [endpoint, handlers]
source: openapi.json (HighBond API v1.1.0)
---

## Handlers

Handlers contain a set of conditions and actions that occur upon certain situation, e.g. an event fired, on scheduled time, a message received, etc.

### `GET /orgs/{org_id}/handlers` — List Handlers

- **operationId:** `getHandlers`
- **Domínio(s):** Handlers

List Handlers and their metadata for an organization. Does not include conditions, actions or events.

<details>
<summary><strong>Parâmetros</strong> (2)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `include_counts` | query |  | boolean | Include the number of conditions, actions and events for each handler. Default: `False` |

</details>

<details>
<summary><strong>Respostas</strong> (5)</summary>

<details>
<summary>`200` — OK.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `MultipleHandlersResponse`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | array[object] | ✅ | The data associated with the resource. |
| `data.id` | string | ✅ | The ID of the handler. Ex.: `"415dc769-3e49-4501-a2fd-80908bea7a32"` |
| `data.type` | string | ✅ | The classification of the object (`"handlers"`). Ex.: `"handlers"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.name` | string |  | The name of the handler. Ex.: `"My first Handler"` |
| `data.attributes.description` | string |  | The description of the handler. Ex.: `"Description of My first Handler"` |
| `data.attributes.shared` | boolean |  | Handlers can be marked as "shared". Only shared handlers can be reused across multiple events in different workflows. Default: `False` Ex.: `false` |
| `data.attributes.created_at` | string |  | The date the handler was created. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.attributes.updated_at` | string |  | The date the handler was updated. Ex.: `"2019-03-18T22:02:05Z"` |

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

</details>
