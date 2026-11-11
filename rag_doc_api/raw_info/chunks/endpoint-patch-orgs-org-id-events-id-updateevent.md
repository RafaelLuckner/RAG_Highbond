---
id: endpoint-patch-orgs-org-id-events-id-updateevent
title: "Events: Update an event"
tags: [endpoint, events]
source: openapi.json (HighBond API v1.1.0)
---

## Events

An Event links a status to handlers. When an event is fired, the associated handlers will be triggered.

### `PATCH /orgs/{org_id}/events/{id}` — Update an event

- **operationId:** `updateEvent`
- **Domínio(s):** Events

Make changes to metadata for an existing event, such as changing the admin_name or the description.

<details>
<summary><strong>Parâmetros</strong> (2)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `id` | path | ✅ | string | The ID of the requested resource. Ex.: `296f9069-4e4a-42bf-ba8a-e372e8f9e724` |

</details>

<details>
<summary><strong>Request body (payload)</strong></summary>

The data required to update a event.

**Body obrigatório.**

**Content-Type:** `application/vnd.api+json`

**Schema:** `UpdateEventPayload`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | object | ✅ | The data associated with the resource. |
| `data.id` | string | ✅ | The ID of the requested resource. Ex.: `"415dc769-3e49-4501-a2fd-80908bea7a32"` |
| `data.type` | string | ✅ | The classification of the object (`"events"`). Ex.: `"events"` |
| `data.attributes` | object |  | The attributes associated with the resource. |
| `data.attributes.admin_name` | string |  | The name of the event. This field is case-insensitive unique. Ex.: `"VRM: submit request review"` |
| `data.attributes.display_name` | string |  | The display name of the event.  > **Note —** If not provided, display_name will default to the admin_name of this event. Ex.: `"Submit request for review"` |
| `data.attributes.description` | string |  | The description of the event. Ex.: `"Description of the event."` |
| `data.attributes.type` | string |  | Configures the type of the event. It controls the appearance of interactable UI element for this event. Valores: `button`, `overflow`, `hidden` Ex.: `"button"` |
| `data.attributes.position` | integer |  | Each event is shown as a button in UI; this attribute determines the order of the button displayed among other events for statuses.  > **Note —** This ordering is global. Same order will be applied to Events used across all workflows for displaying of Event buttons on Statuses only. Ex.: `4` |
| `data.attributes.shared` | boolean |  | Events can be marked as "shared". Only shared events can be reused across multiple workflows. Default: `False` Ex.: `false` |
| `data.attributes.triggers` | array[object] |  | An array of triggers Ex.: `[{"name": "My Event Trigger", "trigger_type": "questionnaireResponded", "configuration": {"questionnaire_ids": ["1", "2"], "trigger_conjunction": "...` |
| `data.attributes.triggers.name` | string |  | The name of the event trigger |
| `data.attributes.triggers.trigger_type` | string |  | The trigger type of the event. Only one instance of a given triggerType is allowed in the triggers array. Valores: `fieldUpdated`, `questionnaireResponded` |
| `data.attributes.triggers.configuration` | object |  | Each trigger type requires its own set of configurations. |
| `data.attributes.triggers.configuration.field_names` | array[string] |  | The field names of an attribute that, when updated, will trigger the event. Required by the `fieldUpdated` trigger_type. |
| `data.attributes.triggers.configuration.questionnaire_ids` | array[string] |  | The questionnaire ids that trigger the handler. Required by the `questionnaireResponded` trigger_type. |
| `data.attributes.triggers.configuration.trigger_conjunction` | string |  | The conjunction used when performing the trigger check. Required by the `fieldUpdated` trigger_type, which supports both `anyOf` and `allOf`. For other trigger types, `anyOf` is implicitly used. Valores: `anyOf`, `allOf` |
| `data.relationships` | object |  | The relationships associated with the resource. |
| `data.relationships.handlers` | object |  | The data associated with the resource. |
| `data.relationships.handlers.data` | array[object] | ✅ | Ex.: `[{"id": "67880347-a683-4933-9b77-59a6997a9da6", "type": "handlers", "meta": {"scopes": ["self"]}}, {"id": "757ad0be-556b-434c-9abc-f4b39b5d7b57", "...` |
| `data.relationships.handlers.data.id` | string | ✅ | The ID of the handler. Ex.: `"e5079e91-3aed-40f0-b3d1-96b83a0bc159"` |
| `data.relationships.handlers.data.type` | string | ✅ | The classification of the object (`"handlers"`). Ex.: `"handlers"` |
| `data.relationships.handlers.data.meta` | object |  | The metadata for the eventhandler relationship |
| `data.relationships.handlers.data.meta.scopes` | array[string] |  | The relationship of the handler to the scope of the event Ex.: `["self"]` |
| `data.relationships.handlers.data.meta.position` | integer |  | The order in which the handler will be executed when an event is invoked Ex.: `1` |

</details>

<details>
<summary><strong>Respostas</strong> (7)</summary>

<details>
<summary>`200` — Updated.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `SingleEventCreateUpdateResponse`

_Apenas campos que diferem do request body. 21 campo(s) idênticos omitidos._

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data.id` | string | ✅ | The ID of the event. Ex.: `"415dc769-3e49-4501-a2fd-80908bea7a32"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.created_at` | string |  | The date the event was created. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.attributes.updated_at` | string |  | The date the event was updated. Ex.: `"2019-03-18T22:02:05Z"` |
| `data.attributes.invocation_context` | array[object] |  | The context information to invoke the event. Ex.: `[{"handler_id": "345a4117-ef52-473b-9af4-75347d28ea67", "context": [{"handler_action_type": "TransitionStatusAction", "context": [{"key": "object_t...` |
| `data.attributes.invocation_context.handler_id` | string |  | The ID of the handler |
| `data.attributes.invocation_context.context` | array[object] |  | The invocation context information of the handler |
| `data.attributes.invocation_context.context.handler_condition_type` | string |  | Type of the condition (only available when it is a condition) |
| `data.attributes.invocation_context.context.handler_action_type` | string |  | Type of the action (only available when it is a action) |
| `data.attributes.invocation_context.context.context` | array[object] |  | The invocation context information of the condition/action |
| `data.attributes.invocation_context.context.context.key` | string |  | Key of the context |
| `data.attributes.invocation_context.context.context.data_type` | string |  | Valores: `string`, `string[]` |
| `data.relationships` | object | ✅ | The relationships associated with the resource. |
| `data.relationships.statuses` | object |  | The data associated with the resource. |
| `data.relationships.statuses.data` | array[object] | ✅ | Ex.: `[{"id": "345a4117-ef52-473b-9af4-75347d28ea67", "type": "statuses"}, {"id": "568ee1e2-d7cc-4cb3-a1f9-95e085771121", "type": "statuses"}]` |
| `data.relationships.statuses.data.id` | string | ✅ | The ID of the status. Ex.: `"9d1c57e0-13a4-4cac-8374-b4b67836b0f0"` |
| `data.relationships.statuses.data.type` | string | ✅ | The classification of the object (`"statuses"`). Ex.: `"statuses"` |
| `data.relationships.handlers.data` | array[object] | ✅ | Ex.: `[{"id": "67880347-a683-4933-9b77-59a6997a9da6", "type": "handlers", "meta": {"scopes": ["self"], "position": 1}}, {"id": "757ad0be-556b-434c-9abc-f...` |

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
