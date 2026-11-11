---
id: endpoint-post-orgs-org-id-entity-categories-createentitycategory
title: "Entities: Create an entity category"
tags: [endpoint, entities]
source: openapi.json (HighBond API v1.1.0)
---

## Entities

Entities may be business units, departments, locations, or key initiatives that are within the scope of the organization. Entities have a hierarchical structure composed of parent and child entities. Once you have set up your organization's nested entity structure, you can tag different items with entities.

Learn more about entities.

### `POST /orgs/{org_id}/entity_categories` — Create an entity category

- **operationId:** `createEntityCategory`
- **Domínio(s):** Entities

Create a new entity category.

Limitations:
* There can be a maximum of 500 entity categories per HighBond instance.

<details>
<summary><strong>Parâmetros</strong> (2)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `fields[entity_categories]` | query |  | string | Requesting the API to return only the specified fields. For more information, see Making requests Ex.: `title,description,position,entities_count,created_at,updated_at,entities` |

</details>

<details>
<summary><strong>Request body (payload)</strong></summary>

The data required to create an entity category.

**Body obrigatório.**

**Content-Type:** `application/vnd.api+json`

**Schema:** `CreateEntityCategoryRequest`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | object | ✅ | The data associated with the resource. |
| `data.type` | string | ✅ | The type of entity category (`"entity_categories"`). Ex.: `"entity_categories"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.title` | string | ✅ | the name of entity category Ex.: `"My new entity category"` |
| `data.attributes.description` | string |  | the description of entity category Ex.: `"My new description"` |

</details>

<details>
<summary><strong>Respostas</strong> (7)</summary>

<details>
<summary>`201` — Created.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `CreateEntityCategoryResponse`

_Apenas campos que diferem do request body. 5 campo(s) idênticos omitidos._

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data.id` | string | ✅ | The ID of the requested resource. Ex.: `"1"` |
| `data.attributes.position` | integer |  | The value that determines the order in which it is displayed in the index action. `position` must be a value between `1` and `2147483647`. Ex.: `1` |
| `data.attributes.entities_count` | integer |  | Related entities count, is a value between `1` and `2147483647`. Ex.: `1` |
| `data.attributes.created_at` | string |  | The timestamp identifying when the entity category was created. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.attributes.updated_at` | string |  | The timestamp identifying when the entity category was last updated. Ex.: `"2019-02-09T13:17:26Z"` |

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
