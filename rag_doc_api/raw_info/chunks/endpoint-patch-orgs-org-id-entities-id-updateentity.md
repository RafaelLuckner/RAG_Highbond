---
id: endpoint-patch-orgs-org-id-entities-id-updateentity
title: "Entities: Update an entity"
tags: [endpoint, entities]
source: openapi.json (HighBond API v1.1.0)
---

## Entities

Entities may be business units, departments, locations, or key initiatives that are within the scope of the organization. Entities have a hierarchical structure composed of parent and child entities. Once you have set up your organization's nested entity structure, you can tag different items with entities.

Learn more about entities.

### `PATCH /orgs/{org_id}/entities/{id}` — Update an entity

- **operationId:** `updateEntity`
- **Domínio(s):** Entities

Make changes to an entity in account, like renaming the entity title or updating the entity description.

Limitations:
* Entity titles can be a maximum of 120 characters long.
* If you provide a parent relationship, none of the children can refer to any of their ancestors (parent, parent of parent, etc.).

<details>
<summary><strong>Parâmetros</strong> (3)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `id` | path | ✅ | string | The ID of the requested resource. Ex.: `9999` |
| `fields[entities]` | query |  | string | Requesting the API to return only the specified fields. For more information, see Making requests Ex.: `title,description,created_at,updated_at,parent,children_count,entity_category` |

</details>

<details>
<summary><strong>Request body (payload)</strong></summary>

The data required to update an entity.

**Body obrigatório.**

**Content-Type:** `application/vnd.api+json`

**Schema:** `UpdateEntityRequest`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | object | ✅ | The data associated with the resource. |
| `data.id` | string | ✅ | The ID of the requested resource. Ex.: `"2"` |
| `data.type` | string | ✅ | The type of resource (`"entities"`). Ex.: `"entities"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.title` | string | ✅ | The title of the entity. Ex.: `"Entity title"` |
| `data.attributes.description` | string |  | A detailed description of the entity. Ex.: `"Entity description"` |
| `data.relationships` | object |  | The relationships associated with the resource. |
| `data.relationships.entity_category` | object |  | Each entity can be associated to the category. |
| `data.relationships.entity_category.data` | object | ✅ | The data associated with the resource. |
| `data.relationships.entity_category.data.id` | string | ✅ | The ID of the category. Ex.: `"54"` |
| `data.relationships.entity_category.data.type` | string | ✅ | The classification of the object (`"entity_categories"`). Ex.: `"entity_categories"` |
| `data.relationships.parent` | object |  | Each entity can be associated to the parent entity. |
| `data.relationships.parent.data` | object | ✅ | The data associated with the resource. |
| `data.relationships.parent.data.id` | string | ✅ | The ID of the entity. Ex.: `"1"` |
| `data.relationships.parent.data.type` | string | ✅ | The classification of the object (`"entities"`). Ex.: `"entities"` |
| `data.relationships.children` | object |  | Each entity can have multiple associated entities. |
| `data.relationships.children.data` | array[object] | ✅ |  |
| `data.relationships.children.data.id` | string | ✅ | The ID of the entity. Ex.: `"3"` |
| `data.relationships.children.data.type` | string | ✅ | The classification of the object (`"entities"`). Ex.: `"entities"` |

</details>

<details>
<summary><strong>Respostas</strong> (7)</summary>

<details>
<summary>`200` — OK.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `GetEntityResponse`

_Apenas campos que diferem do request body. 14 campo(s) idênticos omitidos._

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data.attributes.children_count` | integer |  | A count of entity children. Ex.: `1` |
| `data.attributes.created_at` | string |  | The timestamp identifying when the entity was created. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.attributes.updated_at` | string |  | The timestamp identifying when the entity was last updated. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.relationships` | object | ✅ | The relationships associated with the resource. |

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
