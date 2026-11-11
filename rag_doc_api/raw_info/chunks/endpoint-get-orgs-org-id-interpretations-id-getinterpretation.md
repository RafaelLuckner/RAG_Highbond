---
id: endpoint-get-orgs-org-id-interpretations-id-getinterpretation
title: "Interpretations: Get an interpretation"
tags: [endpoint, interpretations]
source: openapi.json (HighBond API v1.1.0)
---

## Interpretations

An interpretation is a bundled collection of filters, visualizations, and statistics based on a table in a collection. Use them to interpret and visualize results to gain
a deeper understanding of the facts and insights hidden in the data.

Your organization can have a maximum of 4,000 interpretations.

Learn more about interpretations.

### `GET /orgs/{org_id}/interpretations/{id}` — Get an interpretation

- **operationId:** `getInterpretation`
- **Domínio(s):** Interpretations

Get information about an interpretation.

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

**Schema:** `SingleInterpretationResponse`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | object | ✅ | The data associated with the resource. |
| `data.id` | string | ✅ | The ID of the interpretation. Ex.: `"4001"` |
| `data.type` | string | ✅ | The classification of the object (`"interpretations"`). Ex.: `"interpretations"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.title` | string |  | The name of the interpretation. Ex.: `"My first Interpretation"` |
| `data.attributes.raw` | string |  | A JSON string storing the configurations of an interpretation. See the response sample for details. Ex.: `"{\n    \"control_test_id\": 300,\n    \"filterConfig\": {\n        \"filtersOpen\": false,\n        \"myRecords\": false,\n        \"openStatuses\...` |
| `data.attributes.default` | boolean |  | Specifies if the interpretation is the default interpretation for the table.  **Note:** There is only one default interpretation allowed per table. Default: `False` Ex.: `false` |
| `data.attributes.created_at` | string |  | The date the interpretation was created. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.attributes.updated_at` | string |  | The date the interpretation was updated. Ex.: `"2019-03-18T22:02:05Z"` |
| `data.relationships` | object | ✅ | The relationships associated with the resource. Ex.: `{"table": {"data": {"id": "300", "type": "tables"}}}` |
| `data.relationships.table` | RelationshipObject |  |  |
| `data.relationships.table.data` | object | ✅ | The data associated with the related object. |
| `data.relationships.table.data.id` | string | ✅ | The ID of the related object. Ex.: `1` |
| `data.relationships.table.data.type` | string | ✅ | The classification of the related object. Ex.: `"collection"` |

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
