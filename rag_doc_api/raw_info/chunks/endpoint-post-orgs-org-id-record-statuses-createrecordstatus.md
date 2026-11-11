---
id: endpoint-post-orgs-org-id-record-statuses-createrecordstatus
title: "Record statuses: Create a record status"
tags: [endpoint, record-statuses]
source: openapi.json (HighBond API v1.1.0)
---

## Record statuses

A dictionary of table record statuses

### `POST /orgs/{org_id}/record_statuses` — Create a record status

- **operationId:** `createRecordStatus`
- **Domínio(s):** Record statuses

Create a new record status

<details>
<summary><strong>Parâmetros</strong> (1)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |

</details>

<details>
<summary><strong>Request body (payload)</strong></summary>

The data required to create a record status.

**Body obrigatório.**

**Content-Type:** `application/vnd.api+json`

**Schema:** `CreateRecordStatusPayload`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | object | ✅ | The data associated with the resource. |
| `data.type` | string | ✅ | The classification of the object (`"record_statuses"`). Ex.: `"record_statuses"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.name` | string | ✅ | The name of the record status. Ex.: `"Open"` |
| `data.attributes.active` | boolean |  | Indicates whether the record status is active or not. Default: `True` Ex.: `true` |
| `data.attributes.position` | integer |  | Specifies the order of statuses. Ex.: `5` |

</details>

<details>
<summary><strong>Respostas</strong> (7)</summary>

<details>
<summary>`201` — Created.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `SingleRecordStatusResponse`

_Apenas campos que diferem do request body. 3 campo(s) idênticos omitidos._

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data.id` | integer | ✅ | The ID of the record status Ex.: `"20"` |
| `data.type` | string | ✅ | The classification of the object (`"record_statuses"`) Ex.: `"record_statuses"` |
| `data.attributes.name` | string |  | The name of the record status. Ex.: `"Open"` |

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
