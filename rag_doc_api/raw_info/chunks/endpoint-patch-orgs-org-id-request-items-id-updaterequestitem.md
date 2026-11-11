---
id: endpoint-patch-orgs-org-id-request-items-id-updaterequestitem
title: "Request Items: Update a request item"
tags: [endpoint, request-items]
source: openapi.json (HighBond API v1.1.0)
---

## Request Items

A request item is used by Auditors to request documentation from business owners and other stakeholders to gather further information.

Learn more about request items.

### `PATCH /orgs/{org_id}/request_items/{id}` — Update a request item

- **operationId:** `updateRequestItem`
- **Domínio(s):** Request Items

Make changes to a request item.

<details>
<summary><strong>Parâmetros</strong> (2)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `id` | path | ✅ | string | The ID of the requested resource. Ex.: `9999` |

</details>

<details>
<summary><strong>Request body (payload)</strong></summary>

The data required to update a request item.

**Body obrigatório.**

**Content-Type:** `application/vnd.api+json`

**Schema:** `UpdateRequestItemRequest`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | object | ✅ |  |
| `data.id` | string | ✅ | The ID of the requested resource. Ex.: `"1"` |
| `data.type` | string | ✅ | The classification of the object (`"request_items"`). Ex.: `"request_items"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.description` | string | ✅ | Describes the requested information, such as the document name, version number, or department where you might expect to find the information. Ex.: `"<h1>Description heading</h1><p>Request item description.</p>"` |
| `data.attributes.owner` | string |  | Specifies the name of the person responsible for fulfilling the request. If the person is not a user or contact in a HighBond instance, you can provide a value in this field on create or update. This field becomes required if the `owner_user` relationship is not provided. Ex.: `"Owner name"` |
| `data.attributes.owner_email` | string |  | Specifies the email of the person responsible for fulfilling the request. If the person is not a user or contact in a HighBond instance, you can provide a value in this field on create or update. Ex.: `"owner_email@example.com"` |
| `data.attributes.due_date` | string |  | Specifies when the request should be fulfilled by. Ex.: `"2020-06-01"` |
| `data.attributes.send_recurrent_notifications` | boolean |  | Sends an email to the request owner and CC'ed persons on a specified recurring schedule. For more information about recurring reminders, see Sending recurring request reminders. Ex.: `false` |
| `data.attributes.email_subject` | string |  | Provides the ability to customize the email subject line. Ex.: `"Email subject"` |
| `data.attributes.email_message` | string |  | Provides the ability to customize the body of the email. Ex.: `"Email message"` |
| `data.attributes.position` | integer |  | The value that determines the order in which it is displayed. `position` must be a value between `1` and `2147483647`. Ex.: `1` |
| `data.attributes.received` | boolean |  | Specifies if the request item has been received (`true`) or if it is still open (`false`). The default is `false`.  >**Note**: Deprecated, please us the `request_item_status` instead of this. Ex.: `false` |
| `data.attributes.request_item_status` | string |  | Specifies the status of the request item. Ex.: `"Open"` |
| `data.attributes.cc_contacts` | array[string] |  | Specifies one or more people that can contribute to the request. A comma separated list of email addresses. Ex.: `["email_1@example.com", "email_2@example.com"]` |
| `data.attributes.contact_reference_name` | string |  | Specifies the name of the contact reference for fulfilling the request. Should be provided together with other contact reference fields. Values in contact reference fields will override any values provided in the `owner` and `owner_email`, but will not override owner relationship. Ex.: `"Contact User Name"` |
| `data.attributes.contact_reference_email` | string |  | Specifies the email of the contact reference for fulfilling the request. Should be provided together with other contact reference fields. Values in contact reference fields will override any values provided in the `owner` and `owner_email`, but will not override owner relationship. Ex.: `"email_1@example.com"` |
| `data.attributes.contact_reference_table_id` | string |  | Specifies the table_id of the contact reference for fulfilling the request. Should be provided together with other contact reference fields. Values in contact reference fields will override any values provided in the `owner` and `owner_email`, but will not override owner relationship. Ex.: `"13517676342454"` |
| `data.attributes.contact_reference_record_id` | string |  | Specifies the record_id of the contact reference for fulfilling the request. Should be provided together with other contact reference fields.  Values in contact reference fields will override any values provided in the `owner` and `owner_email`, but will not override owner relationship. Ex.: `"512356"` |
| `data.relationships` | object | ✅ | The relationships associated with the resource. |
| `data.relationships.target` | object |  | Specifies the resource that the request item is associated with. |
| `data.relationships.target.data` | object |  | The data associated with a project. |
| `data.relationships.target.data.id` | string |  | The ID of the resource. Ex.: `"1"` |
| `data.relationships.target.data.type` | string |  | The classification of the object.  A target can have one of the following types: `"projects"`, `"controls"`, `"control_tests"`, `"control_test_plans"`, `"issues"`, `"narratives"`, `"objectives"`, `"walkthrough_summaries"`, `"project_files"`, `"project_plannings"`, `"project_results"`, `"risks"`, `"risk_control_matrices"`, `"testing_rounds"`, `"walkthroughs"`. Ex.: `"objectives"` |
| `data.relationships.requestor_user` | object | ✅ | Specifies the user requesting the documentation. |
| `data.relationships.requestor_user.data` | object | ✅ | The data associated with the resource. |
| `data.relationships.requestor_user.data.id` | string | ✅ | The unique identifier (UID) of the user. For more information on obtaining this value, see Making requests. Ex.: `"3NQ6XzAUxqJMnAQ7n4KF"` |
| `data.relationships.requestor_user.data.type` | string | ✅ | The classification of the object (`"users"`). Ex.: `"users"` |
| `data.relationships.owner_user` | object |  | Specifies the user responsible for fulfilling the request. A value in this field will override any values provided in the `owner` and `owner_email` attributes or contact reference fields. This field becomes required if the `owner` attribute is not provided. |
| `data.relationships.owner_user.data` | object | ✅ | The data associated with the resource. |
| `data.relationships.owner_user.data.id` | string | ✅ | The unique identifier (UID) of the user. For more information on obtaining this value, see Making requests. Ex.: `"3NQ6XzAUxqJMnAQ7n4KF"` |
| `data.relationships.owner_user.data.type` | string | ✅ | The classification of the object (`"users"`). Ex.: `"users"` |
| `data.relationships.cc_users` | object |  | Specifies one or more users in a HighBond instance that can contribute to the request. |
| `data.relationships.cc_users.data` | array[object] | ✅ |  |
| `data.relationships.cc_users.data.id` | string | ✅ | The unique identifier (UID) of the user. For more information on obtaining this value, see Making requests. Ex.: `"3NQ6XzAUxqJMnAQ7n4KF"` |
| `data.relationships.cc_users.data.type` | string | ✅ | The classification of the object (`"users"`). Ex.: `"users"` |

</details>

<details>
<summary><strong>Respostas</strong> (7)</summary>

<details>
<summary>`200` — OK.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `GetRequestItemResponse`

_Apenas campos que diferem do request body. 33 campo(s) idênticos omitidos._

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | object | ✅ | The data associated with the resource. |
| `data.attributes.description` | string |  | Describes the requested information, such as the document name, version number, or department where you might expect to find the information. Ex.: `"<h1>Description heading</h1><p>Request item description.</p>"` |
| `data.attributes.created_at` | string |  | The timestamp identifying when the request item was created. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.attributes.updated_at` | string |  | The timestamp identifying when the request item was last updated. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.attributes.requestor` | string |  | Specifies the name of the person requesting the documentation. Ex.: `"Requestor name"` |
| `data.relationships.project` | object |  | Specifies the project that the request item is associated with. |
| `data.relationships.project.data` | object |  | The data associated with a project. |
| `data.relationships.project.data.id` | string |  | The ID of the project. Ex.: `"1"` |
| `data.relationships.project.data.type` | string |  | The classification of the object (`"projects"`). Ex.: `"projects"` |
| `data.relationships.requestor_user` | object |  | Specifies the user requesting the documentation. |

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
