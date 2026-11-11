---
id: endpoint-patch-orgs-org-id-statuses-id-updateworkflowstatus
title: "Workflows in Asset Inventory/Asset Manager: Update a workflow status"
tags: [endpoint, workflows-in-asset-inventory-asset-manager]
source: openapi.json (HighBond API v1.1.0)
---

## Workflows in Asset Inventory/Asset Manager

Workflows contain a set of statuses that a certain item belonging to that workflow can be in. Any items in this workflow can move between certain statuses and the transition can trigger certain events which will execute their handlers.

Workflow statuses represent all possible states an item of the workflow can be in. Statuses can be associated with Events to allow transition from one status to another within the same workflow.

Every workflow must have exactly one "default" status. You can make a status the default status by setting or updating the default flag on that status. This default status cannot be deleted.

### `PATCH /orgs/{org_id}/statuses/{id}` — Update a workflow status

- **operationId:** `updateWorkflowStatus`
- **Domínio(s):** Workflows in Asset Inventory/Asset Manager

Make changes to an existing workflow status.

Notes regarding default statuses:
- updating a status to be the new default status will unset the previous default status
- the current default status cannot be unset directly since otherwise there would be no default status anymore

<details>
<summary><strong>Parâmetros</strong> (2)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `id` | path | ✅ | string | The ID of the requested resource. Ex.: `296f9069-4e4a-42bf-ba8a-e372e8f9e724` |

</details>

<details>
<summary><strong>Request body (payload)</strong></summary>

The data required to update a workflow status.

**Body obrigatório.**

**Content-Type:** `application/vnd.api+json`

**Schema:** `UpdateWorkflowStatusPayload`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | object | ✅ | The data associated with the resource. |
| `data.id` | string | ✅ | The ID of the workflow status. Ex.: `"317dc769-3e09-4501-a2fd-80908bea7a66"` |
| `data.type` | string | ✅ | The classification of the object (`"statuses"`). Ex.: `"statuses"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.name` | string |  | The name of the status. Names are case-insensitive and must be unique. Ex.: `"My first Status"` |
| `data.attributes.description` | string |  | The description of the status. Ex.: `"Description of My first Status"` |
| `data.attributes.position` | integer |  | Determines the visual order of statuses inside the workflow. Ex.: `8` |
| `data.attributes.default` | boolean |  | Specifies that this status is the default for items in the workflow. Every workflow must have exactly one default status. Default: `False` Ex.: `false` |
| `data.attributes.locked` | boolean |  | Indicates that this status cannot be deleted by the user. Default: `False` Ex.: `false` |
| `data.attributes.color` | string |  | Hexadecimal value to capture a color for the field, used in display and reporting Ex.: `"#7D00FF"` |
| `data.relationships` | object |  | The relationships associated with the resource. |
| `data.relationships.events` | object |  | The data associated with the resource. |
| `data.relationships.events.data` | array[object] | ✅ | Ex.: `[{"id": "2b8d8374-43a8-4124-b29e-bcfafd899cc5", "type": "events"}, {"id": "a5b5896c-0724-4460-9361-c2ea0bce92c9", "type": "events"}]` |
| `data.relationships.events.data.id` | string | ✅ | The ID of the event. Ex.: `"b125726f-ee4f-4ec9-9488-b6efa4ee1270"` |
| `data.relationships.events.data.type` | string | ✅ | The classification of the object (`"events"`). Ex.: `"events"` |

</details>

<details>
<summary><strong>Respostas</strong> (7)</summary>

<details>
<summary>`200` — Updated.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `SingleWorkflowStatusResponse`

_Apenas campos que diferem do request body. 13 campo(s) idênticos omitidos._

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data.id` | string | ✅ | The ID of the workflow. Ex.: `"9af02c4a-3c98-4283-8c5d-8dc47e3bf663"` |
| `data.attributes.created_at` | string |  | The date the status was created. Ex.: `"2020-08-11T07:42:42Z"` |
| `data.attributes.updated_at` | string |  | The date the status was updated. Ex.: `"2020-08-11T07:42:42Z"` |
| `data.attributes.system` | boolean |  | Indicates that this status cannot be modified by the user. Default: `False` Ex.: `false` |
| `data.relationships` | object | ✅ | The relationships associated with the resource. |
| `data.relationships.workflow` | object |  | The data associated with the resource. Ex.: `{"data": {"id": "5ca23d96-8c07-4c74-b7fd-1240e46a74ab", "type": "workflows"}}` |
| `data.relationships.workflow.data` | object | ✅ |  |
| `data.relationships.workflow.data.id` | string |  | The ID of the workflow. Ex.: `"5ca23d96-8c07-4c74-b7fd-1240e46a74ab"` |
| `data.relationships.workflow.data.type` | string |  | The classification of the object (`"workflows"`) Ex.: `"workflows"` |

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
