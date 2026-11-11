---
id: endpoint-post-orgs-org-id-issues-issue-id-actions-createaction
title: "Actions: Create an action"
tags: [endpoint, actions]
source: openapi.json (HighBond API v1.1.0)
---

## Actions

An action is a specific follow-up measure that is associated with an identified issue. You can add actions and assign action owners. You can also set up reminders for
yourself to retest issues or track hours spent on retesting by self-assigning actions.

> **Note —**
Only actions in projects that have an `"active"` state can be accessed using the API.

Learn more about actions.

### `POST /orgs/{org_id}/issues/{issue_id}/actions` — Create an action

- **operationId:** `createAction`
- **Domínio(s):** Actions

Create a new action in an existing issue.

Limitations:
* There can be a maximum of 500 actions per issue.
* You cannot create a new action in the following scenarios:
  * if the Follow-up & Remediation subtab of the associated issue is signed off
  * if the action belongs to an objective that has been checked out using
    Offline Projects or the
    HighBond iPad app

Specifying a person's name or email in the following fields does not immediately notify them via email: `owner_name`, `owner_email`.
Email notifications about actions are only sent if `send_recurring_reminder` is `true`.

<details>
<summary><strong>Parâmetros</strong> (3)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `issue_id` | path | ✅ | integer | The ID of the issue. Ex.: `1` |
| `fields[actions]` | query |  | string | Requesting the API to return only the specified fields. For more information, see Making requests Ex.: `title,created_at,updated_at,owner_name,owner_email,send_recurring_reminder,include_issue_details,include_remediation_details,description,due_date,priority,closed,completed_date,status,submitted_on,slug,custom_attributes,issue,assigned_by,cc_users` |

</details>

<details>
<summary><strong>Request body (payload)</strong></summary>

The data required to create an action.

**Body obrigatório.**

**Content-Type:** `application/vnd.api+json`

**Schema:** `CreateActionRequest`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | object | ✅ | The data associated with the resource. |
| `data.type` | string | ✅ | The classification of the object (`"actions"`). Ex.: `"actions"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.title` | string | ✅ | The title of the action. Ex.: `"Title of the action"` |
| `data.attributes.due_date` | string | ✅ | Specifies the date the action must be completed by. Ex.: `"2020-01-02"` |
| `data.attributes.owner_name` | string |  | The action owner. Specifying a person's name does not immediately send them an email notification about the action. However, if `send_recurring_reminder` is configured to `true`, recurring email reminders are sent to the action owner based on the frequency configured. This field becomes required if the `owner_user` relationship is not provided. For more information, see Sending recurring action reminders. Ex.: `"Tom Wachowski"` |
| `data.attributes.owner_email` | string |  | The action owner’s email address. Specifying a person's email does not immediately send them an email notification about the action. However, if `send_recurring_reminder` is configured to `true`, recurring email reminders are sent to the action owner based on the frequency configured. This field becomes required if the `owner_user` relationship is not provided. For more information, see Sending recurring action reminders. Ex.: `"tom.wachowski@greenhills.com"` |
| `data.attributes.created_at` | string |  | The timestamp identifying when the action was created. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.attributes.updated_at` | string |  | The timestamp identifying when the action was updated. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.attributes.send_recurring_reminder` | boolean |  | If `true`, a recurring email reminder about the action is sent to the owner. If `false`, a recurring email reminder is not sent. Recurring reminder frequencies are configurable. For more information, see Sending recurring action reminders. Ex.: `true` |
| `data.attributes.include_issue_details` | boolean |  | If `true`, the issue title and description fields are displayed to the action owner. Once the action owner clicks on the link to the action in the email, they can see the fields on the action page. If `false`, the fields are not displayed to the action owner. Ex.: `true` |
| `data.attributes.include_remediation_details` | boolean |  | If `true`, the remediation plan and remediation deadline fields are displayed to the action owner. Once the action owner clicks on the link to the action in the email, they can see the fields on the action page. If `false`, the fields are not displayed to the action owner. Ex.: `false` |
| `data.attributes.description` | string |  | A detailed description of the action. Ex.: `"<h1>Action heading</h1><p>Action description.</p>"` |
| `data.attributes.priority` | string |  | A user configurable classification that specifies the priority of the action. The options available depend on the configuration of the project type. Ex.: `"high"` |
| `data.attributes.closed` | boolean |  | Specifies the state of the action. An action can have one of the following states: `"open"` or `"closed"`. If `true`, the action is in a `"closed"` state. The action owner stops receiving recurring email notifications about the action. The link to the action in any previously sent email notifications also expires. If `false`, the action is in an `"open"` state. Recurring notifications about the action continue to be sent to the action owner. Ex.: `true` |
| `data.attributes.completed_date` | string |  | Specifies the date that the action was completed or addressed. This field is typically filled out by the issue owner. Ex.: `"2020-01-02"` |
| `data.attributes.status` | string |  | A user configurable classification that specifies the current status of the action. The options available depend on the configuration of the project type. This field is typically filled out by the action owner. Ex.: `"Audit Verifying"` |
| `data.attributes.submitted_on` | string |  | Specifies the date that the action was completed or addressed. This field is typically filled out by the action owner. Ex.: `"2020-01-02"` |
| `data.attributes.custom_attributes` | array[object] |  | An array of custom attributes defined by the user that are available on this object. |
| `data.attributes.custom_attributes.id` | string |  | The ID of the custom attribute that this custom attribute value is for. Optional if term is included. Ex.: `"42"` |
| `data.attributes.custom_attributes.term` | string |  | The user defined term used to identify the custom attribute. Optional if id is included. Ex.: `"Custom Action Attribute"` |
| `data.attributes.custom_attributes.value` | array[string] |  | The value or values (for multiselect) to set this custom attribute to. Ex.: `["Custom Select Option Text"]` |
| `data.attributes.cc_contacts` | array[string] |  | An array of user emails Ex.: `["user@company.com", "user1@company.com"]` |
| `data.relationships` | object | ✅ | The relationships associated with the resource. |
| `data.relationships.assigned_by` | object | ✅ | The person who created the action. You can only specify users with a Professional Manager or Professional User role in the project this action belongs to. |
| `data.relationships.assigned_by.data` | object | ✅ | The data associated with the resource. |
| `data.relationships.assigned_by.data.id` | string | ✅ | The unique identifier (UID) of the assigned user. For more information on obtaining this value, see Making requests. Ex.: `"3NQ6XzAUxqJMnAQ7n4KF"` |
| `data.relationships.assigned_by.data.type` | string | ✅ | The classification of the object (`"users"`). Ex.: `"users"` |
| `data.relationships.cc_users` | object |  | Specifies one or more users in a HighBond instance that are cc'ed on this action. |
| `data.relationships.cc_users.data` | array[object] | ✅ |  |
| `data.relationships.cc_users.data.id` | string | ✅ | The unique identifier (UID) of the user. For more information on obtaining this value, see Making requests. Ex.: `"3NQ6XzAUxqJMnAQ7n4KF"` |
| `data.relationships.cc_users.data.type` | string | ✅ | The classification of the object (`"users"`). Ex.: `"users"` |
| `data.relationships.owner_user` | object |  | Specifies the user in a HighBond instance that responsible for the action. |
| `data.relationships.owner_user.data` | object | ✅ | The data associated with the resource. |
| `data.relationships.owner_user.data.id` | string | ✅ | The unique identifier (UID) of the user. For more information on obtaining this value, see Making requests. Ex.: `"3NQ6XzAUxqJMnAQ7n4KF"` |
| `data.relationships.owner_user.data.type` | string | ✅ | The classification of the object (`"users"`). Ex.: `"users"` |

</details>

<details>
<summary><strong>Respostas</strong> (7)</summary>

<details>
<summary>`201` — Created.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `GetActionResponse`

_Apenas campos que diferem do request body. 34 campo(s) idênticos omitidos._

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data.id` | string | ✅ | The ID of the requested resource. Ex.: `1` |
| `data.attributes.title` | string |  | The title of the action. Ex.: `"Title of the action"` |
| `data.attributes.due_date` | string |  | Specifies the date the action must be completed by. Ex.: `"2020-01-02"` |
| `data.attributes.slug` | string |  | Specifies the secret token that is being used in an unauthenticated link that the free responders can use to access the action. Visible only to System Admins Ex.: `"a68c352c-3b2d-4ae8-9b78-b4d06b6bd5bd"` |
| `data.relationships.issue` | object | ✅ | The attributes associated with the resource. |
| `data.relationships.issue.data` | object | ✅ | The data associated with the resource. |
| `data.relationships.issue.data.id` | string | ✅ | The ID of the issue. Ex.: `"1"` |
| `data.relationships.issue.data.type` | string | ✅ | The classification of the object (`"issues"`). Ex.: `"issues"` |

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
