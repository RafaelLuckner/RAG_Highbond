---
id: endpoint-get-orgs-org-id-handlers-id-gethandler
title: "Handlers: Get a handler"
tags: [endpoint, handlers]
source: openapi.json (HighBond API v1.1.0)
---

## Handlers

Handlers contain a set of conditions and actions that occur upon certain situation, e.g. an event fired, on scheduled time, a message received, etc.

### `GET /orgs/{org_id}/handlers/{id}` — Get a handler

- **operationId:** `getHandler`
- **Domínio(s):** Handlers

Get information about a handler.

<details>
<summary><strong>Parâmetros</strong> (3)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `id` | path | ✅ | string | The ID of the requested resource. Ex.: `296f9069-4e4a-42bf-ba8a-e372e8f9e724` |
| `include` | query |  | string | If specified, the handler's associated events will be included in the `included` object Valores: `events` Ex.: `events` |

</details>

<details>
<summary><strong>Respostas</strong> (5)</summary>

<details>
<summary>`200` — OK.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `SingleHandlerWithEventsResponse`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | object | ✅ | The data associated with the resource. |
| `data.id` | string | ✅ | The ID of the handler. Ex.: `"e5079e91-3aed-40f0-b3d1-96b83a0bc159"` |
| `data.type` | string | ✅ | The classification of the object (`"handlers"`). Ex.: `"handlers"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.name` | string |  | The name of the handler. Ex.: `"My first Handler"` |
| `data.attributes.description` | string |  | The description of the handler. Ex.: `"Description of My first Handler"` |
| `data.attributes.shared` | boolean |  | Handlers can be marked as "shared". Only shared handlers can be reused across multiple events in different workflows. Default: `False` Ex.: `false` |
| `data.attributes.condition_conjunction` | string |  | Type of conditions Valores: `allOf`, `anyOf` Default: `allOf` Ex.: `"allOf"` |
| `data.attributes.conditions` | array[object] |  | An array of conditions Ex.: `[{"condition_type": "specificFieldsAreRequired", "configuration": {"field_names": ["reviewSummary", "reviewer"]}, "scopes": ["self"], "on_failure_a...` |
| `data.attributes.conditions.name` | string |  | The name of the handler condition Ex.: `"My first handler condition"` |
| `data.attributes.conditions.condition_type` | string |  | Determines conditions under which an asset or record can advance to the next workflow status.   * `allRequiredFieldsAreProvided` - All attributes (whose flag `is_required` = `true`) associated with an asset or record must have values.   * `specificFieldsAreRequired` - All attributes/fields specified must have values.   * `fieldValueComparison` -  Workflow advances if the condition/comparison is met for a `numeric`, `boolean`, or `text` attribute. Valores: `allRequiredFieldsAreProvided`, `specificFieldsAreRequired`, `fieldValueComparison` |
| `data.attributes.conditions.configuration` | HandlerConditionsConfigurationOptions |  | Configuration object differs depending on which `condition_type` is being used. |
| `data.attributes.conditions.configuration.field_names` | array[string] | ✅ | list of attributes that need to be checked. |
| `data.attributes.conditions.configuration.left_operand_field_name` | string | ✅ | The field of whom's value will be operated on (will be used to compare against right_operand_value). To reference a workflow status' name, use `metadata.workflow_status`. Ex.: `"risk_score"` |
| `data.attributes.conditions.configuration.right_operand_value` | array[string] |  | A list of values that `left_operand_field_name` will be compared against. The values can be number-like, boolean-like, or text. At this time, we only support one value passed in this list. This value is ignored when operators `is_blank` or `is_not_blank` is used, in all other cases this value is required. |
| `data.attributes.conditions.configuration.operator` | HandlerConditionsConfigurationOperatorOptions | ✅ | Operator represents an action to be performed on the values. Depending on the type of `right_operand_value` (can be `numeric`, `boolean`, or `text`), the set of allowed operators will change. Currently, we only support `numeric` type. |
| `data.attributes.conditions.configuration.operator` | HandlerConditionsConfigurationOperatorOptions |  | ↩ *referência recursiva — ver schema* `HandlerConditionsConfigurationOperatorOptions` |
| `data.attributes.conditions.scopes` | array[string] |  | Default: `['self']` |
| `data.attributes.conditions.on_failure_action` | string |  | Valores: `stopAllHandlersForThisEvent`, `stopThisHandlerForTheCurrentItem` |
| `data.attributes.conditions.on_failure_display_message` | boolean |  | Whether or not a custom error message is shown.  *This property will be deprecated* and replaced by `show_failure_message`. Only this boolean OR `show_failure_message` may be set in a single request Default: `False` |
| `data.attributes.conditions.show_failure_message` | boolean |  | Whether or not an error message is shown. If `on_failure_message` is defined a custom error message is shown. Default: `True` |
| `data.attributes.conditions.on_failure_message` | string |  | When `on_failure_message` is set, `show_failure_message` must be set to true. |
| `data.attributes.actions` | array[object] |  | An array of actions Ex.: `[{"action_type": "transitionStatus", "configuration": {"status_id": "317dc769-3e09-4501-a2fd-80908bea7a66"}, "scopes": ["self"], "show_success_mess...` |
| `data.attributes.actions.name` | string |  | The name of the handler action Ex.: `"My first handler action"` |
| `data.attributes.actions.action_type` | string |  | Valores: `notify`, `transitionStatus`, `runRobot`, `sendQuestionnaire` |
| `data.attributes.actions.configuration` | HandlerActionsConfigurationOptions |  | Configuration object differs depending on which `action_type` is being used. |
| `data.attributes.actions.configuration.emails` | array[string] | ✅ | The list of email addresses that the email notification will be sent to. |
| `data.attributes.actions.configuration.email_subject` | string | ✅ | The email subject of the email notification. |
| `data.attributes.actions.configuration.email_body` | string | ✅ | The email body of the email notification. |
| `data.attributes.actions.configuration.status_id` | string | ✅ | The ID of the Workflow Status to transition an Item to by this Handler Action. |
| `data.attributes.actions.configuration.task_id` | string | ✅ | The ID of the Workflow Robot task to run. |
| `data.attributes.actions.configuration.distribution_type` | string |  | Distribution type. When set to `manual`, this implies that the event is being invoked manually (i.e. through APIs or the UI). When set to `automated`, this implies that the event is being invoked asynchronously through triggers (currently, is only supported using the fieldUpdated trigger type). Valores: `manual`, `automated` Default: `manual` Ex.: `"manual"` |
| `data.attributes.actions.configuration.allowed_questionnaire_ids` | array[string] |  | The list of questionnaires that are going to be displayed in the UI dropdown, for the user to choose from. Used and required for the `manual` distribution_type. |
| `data.attributes.actions.configuration.email_attribute_field_name` | string |  | A field name that references a field containing an email address (which represents the questionnaire recipient). Text and user lookup fields can be used - at this time, only one email is supported (if there are multiple, only the first email in the field will be used). Used and required for the `automated` distribution_type. |
| `data.attributes.actions.configuration.sent_questionnaire_id` | string |  | The id of the questionnaire to be sent. Used and required for the `automated` distribution_type. |
| `data.attributes.actions.configuration.questionnaire_context_fields` | array[string] |  | A list of field names that the display name and value will be shown up in questionnaire responding page. |
| `data.attributes.actions.scopes` | array[string] |  | Default: `['self']` |
| `data.attributes.actions.show_success_message` | boolean |  | Default: `True` |
| `data.attributes.actions.on_success_message` | string |  | When `on_success_message` is set, `show_success_message` must be set to true. |
| `data.attributes.triggers` | array[object] |  | An array of triggers \| `DEPRECATED: Handlers with embedded triggers are not recommended. Please create an event to hold the trigger and link your handler to this event.` Ex.: `[{"name": "My Handler Trigger", "trigger_type": "fieldUpdated", "configuration": {"field_names": ["risk_score", "risk_appetite"], "trigger_conjunct...` |
| `data.attributes.triggers.name` | string |  | The name of the handler trigger |
| `data.attributes.triggers.trigger_type` | string |  | The trigger type of the handler. Only one instance of a given triggerType is allowed in the triggers array. Valores: `fieldUpdated`, `questionnaireResponded` |
| `data.attributes.triggers.configuration` | object |  | Each trigger type requires its own set of configurations. |
| `data.attributes.triggers.configuration.field_names` | array[string] |  | The field names of an attribute that, when updated, will trigger the handler. Required by the `fieldUpdated` trigger_type. |
| `data.attributes.triggers.configuration.questionnaire_ids` | array[string] |  | The questionnaire ids that trigger the handler. Required by the `questionnaireResponded` trigger_type. |
| `data.attributes.triggers.configuration.trigger_conjunction` | string |  | The conjunction used when performing the trigger check. Required by the `fieldUpdated` trigger_type, which supports both `anyOf` and `allOf`. For other trigger types, `anyOf` is implicitly used. Valores: `anyOf`, `allOf` |
| `data.attributes.created_at` | string |  | The date the handler was created. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.attributes.updated_at` | string |  | The date the handler was updated. Ex.: `"2019-03-18T22:02:05Z"` |
| `data.relationships` | object |  | The relationships associated with the resource. |
| `data.relationships.events` | object |  | The data associated with the resource. |
| `data.relationships.events.data` | array[object] | ✅ | Ex.: `[{"id": "415dc769-3e49-4501-a2fd-80908bea7a32", "type": "events", "meta": {"scopes": ["self"], "position": 1}}]` |
| `data.relationships.events.data.id` | string | ✅ | The ID of the event. Ex.: `"415dc769-3e49-4501-a2fd-80908bea7a32"` |
| `data.relationships.events.data.type` | string | ✅ | The classification of the object (`"events"`). Ex.: `"events"` |
| `data.relationships.events.data.meta` | object |  | The metadata for the handlerevent relationship |
| `data.relationships.events.data.meta.scopes` | array[string] |  | The relationship of the event to the scope of the handler Ex.: `["self"]` |
| `data.relationships.events.data.meta.position` | integer |  | The order in which the event will be executed when a handler is invoked Ex.: `1` |
| `included` | array[object] |  | The related entities included with the resource. |
| `included.id` | string |  | The ID of the included entity. Ex.: `"415dc769-3e49-4501-a2fd-80908bea7a32"` |
| `included.type` | string |  | The classification of the object (`"events"`). Ex.: `"events"` |
| `included.attributes` | EventPlainJsonWithoutId |  |  |
| `included.attributes.admin_name` | string |  | The name of the event. This field is case-insensitive unique. Ex.: `"VRM: submit request review"` |
| `included.attributes.display_name` | string |  | The display name of the event.  > **Note —** If not provided, display_name will default to the admin_name of this event. Ex.: `"Submit request for review"` |
| `included.attributes.description` | string |  | The description of the event. Ex.: `"Description of the event."` |
| `included.attributes.type` | string |  | Configures the type of the event. It controls the appearance of interactable UI element for this event. Valores: `button`, `overflow`, `hidden` Ex.: `"button"` |
| `included.attributes.position` | integer |  | Each event is shown as a button in UI; this attribute determines the order of the button displayed among other events for statuses.  > **Note —** This ordering is global. Same order will be applied to Events used across all workflows for displaying of Event buttons on Statuses only. Ex.: `4` |
| `included.attributes.shared` | boolean |  | Events can be marked as "shared". Only shared events can be reused across multiple workflows. Default: `False` Ex.: `false` |
| `included.attributes.created_at` | string |  | The date the event was created. Ex.: `"2019-02-09T13:17:26Z"` |
| `included.attributes.updated_at` | string |  | The date the event was updated. Ex.: `"2019-03-18T22:02:05Z"` |

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
