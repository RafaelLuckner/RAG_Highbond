---
id: endpoint-get-orgs-org-id-storyboards-id-getstoryboard
title: "Storyboards: Get a storyboard"
tags: [endpoint, storyboards]
source: openapi.json (HighBond API v1.1.0)
---

## Storyboards

A storyboard is a communication platform that displays multiple visualizations and rich text content in rows and columns. You can use this API to create, configure,
update, and delete storyboards. However, to see your storyboards, you need to log in to HighBond or have someone send you a link to that storyboard.

Learn more about storyboards.

### `GET /orgs/{org_id}/storyboards/{id}` — Get a storyboard

- **operationId:** `getStoryboard`
- **Domínio(s):** Storyboards

Get information about a storyboard.

<details>
<summary><strong>Parâmetros</strong> (2)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `id` | path | ✅ | string | The ID of the requested resource. Ex.: `9999` |

</details>

<details>
<summary><strong>Respostas</strong> (6)</summary>

<details>
<summary>`200` — OK.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `SingleStoryboardResponse`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | object | ✅ | The data associated with the resource. |
| `data.id` | string | ✅ | The ID of the storyboard. Ex.: `"5"` |
| `data.type` | string | ✅ | The classification of the object (`"storyboards"`). Ex.: `"storyboards"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.name` | string |  | The name of the storyboard. Ex.: `"My first storyboard"` |
| `data.attributes.config` | string |  | A JSON string storing the configurations of a storyboard.  See the request sample for details. Ex.: `"{\n    \"globalFilters\": [\n        {\n            \"display_name\": \"City\",\n            \"field_format\": {},\n            \"field_type\": \"...` |
| `data.attributes.created_at` | string |  | The date when the storyboard was created. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.attributes.updated_at` | string |  | The date when the storyboard was updated. Ex.: `"2019-03-18T22:02:05Z"` |

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

</details>
