---
id: endpoint-post-orgs-org-id-project-types-project-type-id-request-item-statuses-createreque
title: "Request item statuses: Create a request item status"
tags: [endpoint, request-item-statuses]
source: openapi.json (HighBond API v1.1.0)
---

## Request item statuses

Request statuses provide visibility into the progress of request resolutions. The number of available statuses, and the terms used for each status, can be customized by the organization.

Learn more about request item statuses.

### `POST /orgs/{org_id}/project_types/{project_type_id}/request_item_statuses` — Create a request item status

- **operationId:** `createRequestItemStatus`
- **Domínio(s):** Request item statuses

Create a new request item status in an existing project type.

<details>
<summary><strong>Parâmetros</strong> (3)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `project_type_id` | path | ✅ | integer | The ID of the project type. Ex.: `1` |
| `fields[request_item_statuses]` | query |  | string | Requesting the API to return only the specified fields. For more information, see Making requests Ex.: `status,action,default` |

</details>

<details>
<summary><strong>Request body (payload)</strong></summary>

The data required to create a request item status.

**Body obrigatório.**

**Content-Type:** `application/vnd.api+json`

**Schema:** `CreateRequestItemStatusRequest`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | object | ✅ | The data associated with the resource. |
| `data.type` | string | ✅ | The type of the request item status (`"request_item_statuses"`). Ex.: `"request_item_statuses"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.status` | string | ✅ | The displayed name of the request item status. Ex.: `"Open"` |
| `data.attributes.action` | string | ✅ | The action of the request item status. Valores: `nothing`, `warning` Ex.: `"warning"` |

</details>

<details>
<summary><strong>Respostas</strong> (7)</summary>

<details>
<summary>`201` — Created.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `GetRequestItemStatusResponse`

_Apenas campos que diferem do request body. 4 campo(s) idênticos omitidos._

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data.id` | string | ✅ | The ID of the requested resource. Ex.: `"1"` |
| `data.attributes.action` | string |  | The action of the request item status. Valores: `nothing`, `warning` Ex.: `"warning"` |
| `data.attributes.default` | boolean |  | Specifies if the request item status is default (`true`) or not (`false`). The default statuses can't be deleted. Ex.: `true` |
| `data.attributes.created_at` | string |  | The timestamp identifying when the narrative was created. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.attributes.updated_at` | string |  | The timestamp identifying when the narrative was last updated. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.relationships` | object | ✅ | The relationships associated with the resource. |
| `data.relationships.project_type` | object | ✅ | Each request item status has an associated project type. Project types define the structure of a project or framework, including the terminology used in the project or framework. |
| `data.relationships.project_type.data` | object | ✅ | The data associated with the resource. |
| `data.relationships.project_type.data.id` | string | ✅ | The ID of the project type that this request item status belongs to. Ex.: `"1"` |
| `data.relationships.project_type.data.type` | string | ✅ | The classification of the object (`"project_types"`). Ex.: `"project_types"` |

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
