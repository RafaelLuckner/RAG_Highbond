---
id: endpoint-patch-orgs-org-id-record-statuses-id-updaterecordstatus
title: "Record statuses: Update a record status"
tags: [endpoint, record-statuses]
source: openapi.json (HighBond API v1.1.0)
---

## Record statuses

A dictionary of table record statuses

### `PATCH /orgs/{org_id}/record_statuses/{id}` — Update a record status

- **operationId:** `updateRecordStatus`
- **Domínio(s):** Record statuses

Make changes to a record status, like renaming it or activating/deactivating it.

<details>
<summary><strong>Parâmetros</strong> (2)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `id` | path | ✅ | string | The ID of the requested resource. Ex.: `9999` |

</details>

<details>
<summary><strong>Request body (payload)</strong></summary>

The data required to update a record status.

**Body obrigatório.**

**Content-Type:** `application/vnd.api+json`

**Schema:** `UpdateRecordStatusPayload`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | object | ✅ | The data associated with the resource. |
| `data.id` | string | ✅ | The ID of the record status that needs to be changed. Ex.: `"20"` |
| `data.type` | string | ✅ | The classification of the object (`"record_statuses"`). Ex.: `"record_statuses"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.name` | string |  | The name of the record status. Ex.: `"Open"` |
| `data.attributes.active` | boolean |  | Indicates whether the record status is active or not. Default: `True` Ex.: `true` |
| `data.attributes.position` | integer |  | Specifies the order of statuses. Ex.: `5` |

</details>

<details>
<summary><strong>Respostas</strong> (7)</summary>

<details>
<summary>`200` — OK.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `SingleRecordStatusResponse`

_Apenas campos que diferem do request body. 4 campo(s) idênticos omitidos._

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data.id` | integer | ✅ | The ID of the record status Ex.: `"20"` |
| `data.type` | string | ✅ | The classification of the object (`"record_statuses"`) Ex.: `"record_statuses"` |

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
