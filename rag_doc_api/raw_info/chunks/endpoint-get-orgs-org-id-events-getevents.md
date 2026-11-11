---
id: endpoint-get-orgs-org-id-events-getevents
title: "Events: List Events"
tags: [endpoint, events]
source: openapi.json (HighBond API v1.1.0)
---

## Events

An Event links a status to handlers. When an event is fired, the associated handlers will be triggered.

### `GET /orgs/{org_id}/events` — List Events

- **operationId:** `getEvents`
- **Domínio(s):** Events

List Events and their metadata for an organization. Does not include associated workflow statuses or handlers.

<details>
<summary><strong>Parâmetros</strong> (1)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |

</details>

<details>
<summary><strong>Respostas</strong> (5)</summary>

<details>
<summary>`200` — OK.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `MultipleEventsResponse`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | array[object] | ✅ | The data associated with the resource. |
| `data.id` | string | ✅ | The ID of the event. Ex.: `"415dc769-3e49-4501-a2fd-80908bea7a32"` |
| `data.type` | string | ✅ | The classification of the object (`"events"`). Ex.: `"events"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.admin_name` | string |  | The name of the event. This field is case-insensitive unique. Ex.: `"VRM: submit request review"` |
| `data.attributes.display_name` | string |  | The display name of the event.  > **Note —** If not provided, display_name will default to the admin_name of this event. Ex.: `"Submit request for review"` |
| `data.attributes.description` | string |  | The description of the event. Ex.: `"Description of the event."` |
| `data.attributes.type` | string |  | Configures the type of the event. It controls the appearance of interactable UI element for this event. Valores: `button`, `overflow`, `hidden` Ex.: `"button"` |
| `data.attributes.position` | integer |  | Each event is shown as a button in UI; this attribute determines the order of the button displayed among other events for statuses.  > **Note —** This ordering is global. Same order will be applied to Events used across all workflows for displaying of Event buttons on Statuses only. Ex.: `4` |
| `data.attributes.shared` | boolean |  | Events can be marked as "shared". Only shared events can be reused across multiple workflows. Default: `False` Ex.: `false` |
| `data.attributes.created_at` | string |  | The date the event was created. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.attributes.updated_at` | string |  | The date the event was updated. Ex.: `"2019-03-18T22:02:05Z"` |

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
