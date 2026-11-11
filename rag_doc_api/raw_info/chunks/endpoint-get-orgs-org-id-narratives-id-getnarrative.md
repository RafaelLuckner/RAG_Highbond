---
id: endpoint-get-orgs-org-id-narratives-id-getnarrative
title: "Narratives: Get a narrative"
tags: [endpoint, narratives]
source: openapi.json (HighBond API v1.1.0)
---

## Narratives

A narrative is a description of a business process or area under review. Narratives are also known as policies, IT policies, process narratives, process descriptions, or control guides.

> **Note:**
> * To access narratives using the API, the narratives tab must be enabled in the project type associated with the project or framework.
>
> Narratives located in such resources can be accessed using the API:
> * In Internal Control workflow projects that have an "active" state
> * In frameworks

Learn more about narratives.

### `GET /orgs/{org_id}/narratives/{id}` — Get a narrative

- **operationId:** `getNarrative`
- **Domínio(s):** Narratives

Get information about a narrative.

Limitation:
Existing Citation Mode highlights and links are not displayed in the `description` field.

<details>
<summary><strong>Parâmetros</strong> (3)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `id` | path | ✅ | string | The ID of the requested resource. Ex.: `9999` |
| `fields[narratives]` | query |  | string | Requesting the API to return only the specified fields. For more information, see Making requests Ex.: `title,description,created_at,updated_at,objective,framework_origin` |

</details>

<details>
<summary><strong>Respostas</strong> (6)</summary>

<details>
<summary>`200` — OK.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `GetNarrativeResponse`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | object | ✅ | The data associated with the resource. |
| `data.id` | string | ✅ | The ID of the requested resource. Ex.: `"1"` |
| `data.type` | string | ✅ | The type of narrative (`"narratives"`). Ex.: `"narratives"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.title` | string | ✅ | The title of the narrative. Ex.: `"Narrative title"` |
| `data.attributes.description` | string |  | A detailed description of the narrative. Ex.: `"Narrative description"` |
| `data.attributes.position` | integer |  | The value that determines the order in which it is displayed in the index action. `position` must be a value between `1` and `2147483647`. Ex.: `1` |
| `data.attributes.created_at` | string |  | The timestamp identifying when the narrative was created. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.attributes.updated_at` | string |  | The timestamp identifying when the narrative was last updated. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.relationships` | object | ✅ | The relationships associated with the resource. |
| `data.relationships.objective` | object | ✅ | Each narrative has an associated objective. Objectives are the basis of a project or framework. They are also the organizing containers for the work done in a project or framework. |
| `data.relationships.objective.data` | object | ✅ | The data associated with the resource. |
| `data.relationships.objective.data.id` | string | ✅ | The ID of the objective. Ex.: `"1"` |
| `data.relationships.objective.data.type` | string | ✅ | The classification of the object (`"objectives"`). Ex.: `"objectives"` |
| `data.relationships.framework_origin` | object |  | In the Projects app, a project `narrative` can have a related counterpart in an associated framework. The `framework_origin` attribute allows you to associate an `narrative` in a project with its related counterpart in a framework. |
| `data.relationships.framework_origin.data` | object | ✅ | The data associated with the resource. |
| `data.relationships.framework_origin.data.id` | string | ✅ | The ID of the parent control. Ex.: `"1"` |
| `data.relationships.framework_origin.data.type` | string | ✅ | The classification of the object (`"narratives"`). Ex.: `"narratives"` |

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
