---
id: endpoint-get-orgs-org-id-analyses-id-getanalysis
title: "Analyses: Get an analysis"
tags: [endpoint, analyses]
source: openapi.json (HighBond API v1.1.0)
---

## Analyses

An analysis is a second-level container. Analyses live in collections, and they are used to organize tables. Once you have created a collection, you can add one or
more analyses to that collection.

Your organization can have a maximum of 2,000 analyses.

Learn more about analyses.

### `GET /orgs/{org_id}/analyses/{id}` — Get an analysis

- **operationId:** `getAnalysis`
- **Domínio(s):** Analyses

Get information about an analysis.

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

**Schema:** `SingleAnalysisResponse`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | object | ✅ | The data associated with the resource. |
| `data.id` | string | ✅ | The ID of the requested resource. Ex.: `"20"` |
| `data.type` | string | ✅ | The classification of the object (`"analyses"`). Ex.: `"analyses"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.name` | string |  | The name of the analysis. Ex.: `"My first Analysis"` |
| `data.attributes.description` | string |  | The description of the analysis. Ex.: `"Description of My first Analysis"` |
| `data.attributes.created_at` | string |  | The date the analysis was created. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.attributes.updated_at` | string |  | The date the analysis was updated. Ex.: `"2019-03-18T22:02:05Z"` |
| `data.relationships` | object | ✅ | The relationships associated with the resource. Ex.: `{"collection": {"data": {"id": "1", "type": "collections"}}}` |
| `data.relationships.collection` | RelationshipObject |  |  |
| `data.relationships.collection.data` | object | ✅ | The data associated with the related object. |
| `data.relationships.collection.data.id` | string | ✅ | The ID of the related object. Ex.: `1` |
| `data.relationships.collection.data.type` | string | ✅ | The classification of the related object. Ex.: `"collection"` |

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
