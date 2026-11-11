---
id: endpoint-patch-orgs-org-id-related-requirements-id-updaterelatedrequirement
title: "Compliance Maps: Update a link between requirements"
tags: [endpoint, compliance-maps]
source: openapi.json (HighBond API v1.1.0)
---

## Compliance Maps

You can use Compliance Maps to associate industry standards and regulations with your control frameworks.

Learn more.

### `PATCH /orgs/{org_id}/related_requirements/{id}` — Update a link between requirements

- **operationId:** `updateRelatedRequirement`
- **Domínio(s):** Compliance Maps

Once a relationship is established between requirements, you can change any aspect of that relationship. To update a link, you need the id of the relationship that was generated when it was created. You also need the requirement ID for each requirement, whether the related requirement supports or overlaps the first requirement, the strength of the relationship, and whether the link should be active or not. Use the related requirements feature at your discretion and risk. You are responsible to apply professional judgment to determine the appropriate procedures, tests, or controls for your own use. Learn more.

<details>
<summary><strong>Parâmetros</strong> (3)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `id` | path | ✅ | string | The ID of the requested resource. Ex.: `9999` |
| `fields[related_compliance_requirements]` | query |  | string | Requesting the API to return only the specified fields. For more information, see Making requests Ex.: `relationship_type,relationship_strength,status,compliance_requirement,related_compliance_requirement` |

</details>

<details>
<summary><strong>Request body (payload)</strong></summary>

The data required to update a related requirement.

**Body obrigatório.**

**Content-Type:** `application/vnd.api+json`

**Schema:** `UpdateRelatedRequirementRequest`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | object | ✅ | The data associated with the resource. |
| `data.id` | string | ✅ | The ID of the requested resource. Ex.: `"1"` |
| `data.type` | string | ✅ | The classification of the object (`"related_compliance_requirements"`). Ex.: `"related_compliance_requirements"` |
| `data.attributes` | object |  | The attributes associated with the resource. |
| `data.attributes.relationship_type` | string |  | The type of the relationship between the requirements. Valores: `support`, `overlap` Ex.: `"support"` |
| `data.attributes.relationship_strength` | string |  | The strength of the relationship between the requirements. Valores: `equivalent`, `strongly_related`, `moderately_related`, `weakly_related` Ex.: `"equivalent"` |
| `data.attributes.status` | string |  | The status of the related requirement. Valores: `active`, `inactive` Ex.: `"active"` |
| `data.relationships` | object |  | The relationships associated with the resource. |
| `data.relationships.compliance_requirement` | object |  | Requirement object. |
| `data.relationships.compliance_requirement.data` | object |  | The data associated with the resource. |
| `data.relationships.compliance_requirement.data.id` | string |  | The ID of the requested resource. Ex.: `"11"` |
| `data.relationships.compliance_requirement.data.type` | string |  | The classification of the object (`"compliance_requirements"`). Ex.: `"compliance_requirements"` |
| `data.relationships.related_compliance_requirement` | object |  | Requirement object. |
| `data.relationships.related_compliance_requirement.data` | object |  | The data associated with the resource. |
| `data.relationships.related_compliance_requirement.data.id` | string |  | The ID of the requested resource. Ex.: `"22"` |
| `data.relationships.related_compliance_requirement.data.type` | string |  | The classification of the object (`"compliance_requirements"`). Ex.: `"compliance_requirements"` |

</details>

<details>
<summary><strong>Respostas</strong> (7)</summary>

<details>
<summary>`200` — OK.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `CreateRelatedRequirementResponse`

_Apenas campos que diferem do request body. 3 campo(s) idênticos omitidos._

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.relationship_type` | string | ✅ | The type of the relationship between the requirements. Valores: `support`, `overlap` Ex.: `"support"` |
| `data.attributes.relationship_strength` | string | ✅ | The strength of the relationship between the requirements. Valores: `equivalent`, `strongly_related`, `moderately_related`, `weakly_related` Ex.: `"equivalent"` |
| `data.attributes.status` | string | ✅ | The status of the related requirement. Valores: `active`, `inactive` Ex.: `"active"` |
| `data.relationships` | object | ✅ | The relationships associated with the resource. |
| `data.relationships.compliance_requirement` | object | ✅ | Requirement object. |
| `data.relationships.compliance_requirement.data` | object | ✅ | The data associated with the resource. |
| `data.relationships.compliance_requirement.data.id` | string | ✅ | The ID of the requested resource. Ex.: `"11"` |
| `data.relationships.compliance_requirement.data.type` | string | ✅ | The classification of the object (`"compliance_requirements"`). Ex.: `"compliance_requirements"` |
| `data.relationships.related_compliance_requirement` | object | ✅ | Requirement object. |
| `data.relationships.related_compliance_requirement.data` | object | ✅ | The data associated with the resource. |
| `data.relationships.related_compliance_requirement.data.id` | string | ✅ | The ID of the requested resource. Ex.: `"22"` |
| `data.relationships.related_compliance_requirement.data.type` | string | ✅ | The classification of the object (`"compliance_requirements"`). Ex.: `"compliance_requirements"` |

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
