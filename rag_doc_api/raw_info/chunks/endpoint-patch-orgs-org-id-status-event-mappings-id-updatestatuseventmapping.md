---
id: endpoint-patch-orgs-org-id-status-event-mappings-id-updatestatuseventmapping
title: "Workflows in Asset Inventory/Asset Manager: Update a status event mapping"
tags: [endpoint, workflows-in-asset-inventory-asset-manager]
source: openapi.json (HighBond API v1.1.0)
---

## Workflows in Asset Inventory/Asset Manager

Workflows contain a set of statuses that a certain item belonging to that workflow can be in. Any items in this workflow can move between certain statuses and the transition can trigger certain events which will execute their handlers.

Workflow statuses represent all possible states an item of the workflow can be in. Statuses can be associated with Events to allow transition from one status to another within the same workflow.

Every workflow must have exactly one "default" status. You can make a status the default status by setting or updating the default flag on that status. This default status cannot be deleted.

### `PATCH /orgs/{org_id}/status_event_mappings/{id}` — Update a status event mapping

- **operationId:** `updateStatusEventMapping`
- **Domínio(s):** Workflows in Asset Inventory/Asset Manager

Update the mapping between a status and an event.

<details>
<summary><strong>Parâmetros</strong> (2)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `id` | path | ✅ | string | The ID of the requested resource. Ex.: `296f9069-4e4a-42bf-ba8a-e372e8f9e724` |

</details>

<details>
<summary><strong>Request body (payload)</strong></summary>

The data required to update a status event mapping.

**Body obrigatório.**

**Content-Type:** `application/vnd.api+json`

**Schema:** `UpdateStatusEventMappingPayload`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | object | ✅ | The data associated with the resource |
| `data.id` | string | ✅ | The ID of the status event mapping. Ex.: `"317dc769-3e09-4501-a2fd-80908bea7a66"` |
| `data.type` | string | ✅ | The classification of the object (`"status_event_mappings"`). Ex.: `"status_event_mappings"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.status_id` | string |  | The ID of the status. Ex.: `"48943a00-43ae-4ea3-9824-09fbfb0574f3"` |
| `data.attributes.event_id` | string |  | The ID of the event. Ex.: `"d728af99-e55f-47fa-a47d-cc8dc2f74f46"` |

</details>

<details>
<summary><strong>Respostas</strong> (7)</summary>

<details>
<summary>`200` — Updated.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `SingleStatusEventMappingResponse`

_Apenas campos que diferem do request body. 2 campo(s) idênticos omitidos._

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | object |  | The data associated with the resource |
| `data.id` | string |  | The ID of the status event mapping. Ex.: `"317dc769-3e09-4501-a2fd-80908bea7a66"` |
| `data.type` | string |  | The classification of the object (`"status_event_mappings"`). Ex.: `"status_event_mappings"` |
| `data.attributes` | object |  | The attributes associated with the resource. |
| `data.attributes.created_at` | string |  | The date the status was created. Ex.: `"2020-08-11T07:42:42Z"` |
| `data.attributes.updated_at` | string |  | The date the status was updated. Ex.: `"2020-08-11T07:42:42Z"` |

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
