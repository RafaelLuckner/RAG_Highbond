---
id: endpoint-patch-orgs-org-id-mitigations-id-updatemitigation
title: "Mitigations: Update a mitigation"
tags: [endpoint, mitigations]
source: openapi.json (HighBond API v1.1.0)
---

## Mitigations

> **Note —**
Only controls in projects that have an `"active"` state can be accessed using the API.

### `PATCH /orgs/{org_id}/mitigations/{id}` — Update a mitigation

- **operationId:** `updateMitigation`
- **Domínio(s):** Mitigations

Make changes to a mitigation.

Limitations:
* You cannot update the mitigation if the objective it belongs to has been checked out using
Offline Projects or the
HighBond iPad app.

<details>
<summary><strong>Parâmetros</strong> (2)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `id` | path | ✅ | string | The ID of the requested resource. Ex.: `9999` |

</details>

<details>
<summary><strong>Request body (payload)</strong></summary>

The data required to update a mitigation.

**Body obrigatório.**

**Content-Type:** `application/vnd.api+json`

**Schema:** `UpdateMitigationRequest`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | object | ✅ | The data associated with the resource. |
| `data.id` | string | ✅ | The ID of the requested resource. Ex.: `"1"` |
| `data.type` | string | ✅ | The type of mitigation (`"mitigations"`). Ex.: `"mitigations"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.weight` | integer | ✅ | the weight of mitigation. Must be > 0 and less than 100. Ex.: `99` |

</details>

<details>
<summary><strong>Respostas</strong> (7)</summary>

<details>
<summary>`200` — OK.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `GetMitigationResponse`

_Apenas campos que diferem do request body. 5 campo(s) idênticos omitidos._

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data.attributes.created_at` | string |  | The timestamp identifying when the mitigation was created. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.attributes.updated_at` | string |  | The timestamp identifying when the mitigation was last updated. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.relationships` | object | ✅ | The relationships associated with the resource. |
| `data.relationships.control` | object | ✅ | Each mitigation has an associated control. |
| `data.relationships.control.data` | object | ✅ | The data associated with the resource. |
| `data.relationships.control.data.id` | string | ✅ | The ID of the control. Ex.: `"1"` |
| `data.relationships.control.data.type` | string | ✅ | The classification of the object (`"controls"`). Ex.: `"controls"` |
| `data.relationships.risk` | object | ✅ | Each mitigation has an associated risk. |
| `data.relationships.risk.data` | object | ✅ | The data associated with the resource. |
| `data.relationships.risk.data.id` | string | ✅ | The ID of the risk. Ex.: `"1"` |
| `data.relationships.risk.data.type` | string | ✅ | The classification of the object (`"risks"`). Ex.: `"risks"` |

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
