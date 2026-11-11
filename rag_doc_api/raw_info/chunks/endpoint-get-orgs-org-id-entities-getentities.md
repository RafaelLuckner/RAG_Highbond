---
id: endpoint-get-orgs-org-id-entities-getentities
title: "Entities: Get entities"
tags: [endpoint, entities]
source: openapi.json (HighBond API v1.1.0)
---

## Entities

Entities may be business units, departments, locations, or key initiatives that are within the scope of the organization. Entities have a hierarchical structure composed of parent and child entities. Once you have set up your organization's nested entity structure, you can tag different items with entities.

Learn more about entities.

### `GET /orgs/{org_id}/entities` — Get entities

- **operationId:** `getEntities`
- **Domínio(s):** Entities

Get all entities.

<details>
<summary><strong>Parâmetros</strong> (4)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `fields[entities]` | query |  | string | Requesting the API to return only the specified fields. For more information, see Making requests Ex.: `title,description,created_at,updated_at,parent,children_count,entity_category` |
| `page[size]` | query |  | string | The number of items returned per page. Default is 50. Maximum is 100. Ex.: `25` |
| `page[number]` | query |  | string | The Base64-encoded page number of records to return. Ex.: `Mg==` |

</details>

<details>
<summary><strong>Respostas</strong> (6)</summary>

<details>
<summary>`200` — OK.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `GetEntitiesResponse`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | array[object] | ✅ |  |
| `data.id` | string | ✅ | The ID of the requested resource. Ex.: `"2"` |
| `data.type` | string | ✅ | The type of resource (`"entities"`). Ex.: `"entities"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.title` | string | ✅ | The title of the entity. Ex.: `"Entity title"` |
| `data.attributes.description` | string |  | A detailed description of the entity. Ex.: `"Entity description"` |
| `data.attributes.children_count` | integer |  | A count of entity children. Ex.: `1` |
| `data.attributes.created_at` | string |  | The timestamp identifying when the entity was created. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.attributes.updated_at` | string |  | The timestamp identifying when the entity was last updated. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.relationships` | object | ✅ | The relationships associated with the resource. |
| `data.relationships.entity_category` | object |  | Each entity can be associated to the category. |
| `data.relationships.entity_category.data` | object | ✅ | The data associated with the resource. |
| `data.relationships.entity_category.data.id` | string | ✅ | The ID of the category. Ex.: `"54"` |
| `data.relationships.entity_category.data.type` | string | ✅ | The classification of the object (`"entity_categories"`). Ex.: `"entity_categories"` |
| `data.relationships.parent` | object |  | Each entity can be associated to the parent entity. |
| `data.relationships.parent.data` | object | ✅ | The data associated with the resource. |
| `data.relationships.parent.data.id` | string | ✅ | The ID of the entity. Ex.: `"1"` |
| `data.relationships.parent.data.type` | string | ✅ | The classification of the object (`"entities"`). Ex.: `"entities"` |
| `links` | object |  |  |
| `links.next` | string | ✅ | Next page url Ex.: `"/api/resource?page[number]=Mw=="` |
| `links.prev` | string | ✅ | Previous page url Ex.: `null` |

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
