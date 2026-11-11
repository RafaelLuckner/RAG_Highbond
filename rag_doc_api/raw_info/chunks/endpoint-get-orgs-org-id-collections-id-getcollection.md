---
id: endpoint-get-orgs-org-id-collections-id-getcollection
title: "Collections: Get a collection"
tags: [endpoint, collections]
source: openapi.json (HighBond API v1.1.0)
---

## Collections

A collection is a container used to organize analyses that relate to different departments, business processes, or data sets. Collections are the highest level of
organization in the Results app.

Your organization can have a maximum of 2,000 collections.

Learn more about collections.

### `GET /orgs/{org_id}/collections/{id}` — Get a collection

- **operationId:** `getCollection`
- **Domínio(s):** Collections

Get information about a collection.

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

**Schema:** `SingleCollectionResponse`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | object | ✅ | The data associated with the resource. |
| `data.id` | string | ✅ | The ID of the requested resource. Ex.: `"1"` |
| `data.type` | string | ✅ | The classification of the object (`"collections"`). Ex.: `"collections"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.name` | string |  | The name of the collection. Ex.: `"My first Collection"` |
| `data.attributes.description` | string |  | The description of the collection. Ex.: `"Description of My first Collection"` |
| `data.attributes.workflow_id` | integer |  | The ID of the workflow associated with the collection. Ex.: `42` |
| `data.attributes.default` | boolean |  | Specifies if the collection is a default (system created) collection. Ex.: `false` |
| `data.attributes.archived` | boolean |  | Specifies if the collection is archived (in a read-only state). Ex.: `false` |
| `data.attributes.created_at` | string |  | The date the collection was created. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.attributes.updated_at` | string |  | The date the collection was updated. Ex.: `"2019-03-18T22:02:05Z"` |
| `data.attributes.collection_type` | string |  | The type of a collection Valores: `RegularProject`, `ProjectsAppIntegrationProject`, `ReportingProject`, `ReferenceProject`, `AssessmentProject` Ex.: `"RegularProject"` |

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
