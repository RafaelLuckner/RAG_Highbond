---
id: endpoint-post-orgs-org-id-related-requirements-postrelatedrequirement
title: "Compliance Maps: Create a link between requirements"
tags: [endpoint, compliance-maps]
source: openapi.json (HighBond API v1.1.0)
---

## Compliance Maps

You can use Compliance Maps to associate industry standards and regulations with your control frameworks.

Learn more.

### `POST /orgs/{org_id}/related_requirements` — Create a link between requirements

- **operationId:** `postRelatedRequirement`
- **Domínio(s):** Compliance Maps

Organizations typically need to be compliant with multiple standards and regulations that may have related or overlapping requirements. Related requirements indicate that controls implemented for one requirement should effectively address another (related) requirement. To link two requirements, you need the requirement ID for each requirement, whether the related requirement supports or overlaps the first requirement, the strength of the relationship, and whether the link should be active or not. When you create a link, that link is tracked with a unique ID, which you can use again later to update or delete that relationship. Use the related requirements feature at your discretion and risk. You are responsible to apply professional judgment to determine the appropriate procedures, tests, or controls for your own use. Learn more.

<details>
<summary><strong>Parâmetros</strong> (2)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `fields[related_compliance_requirements]` | query |  | string | Requesting the API to return only the specified fields. For more information, see Making requests Ex.: `relationship_type,relationship_strength,status,compliance_requirement,related_compliance_requirement` |

</details>

<details>
<summary><strong>Request body (payload)</strong></summary>

The data required to create a link between requirements.

**Body obrigatório.**

**Content-Type:** `application/vnd.api+json`

**Schema:** `CreateRelatedRequirementRequest`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | object | ✅ | The data associated with the resource. |
| `data.type` | string | ✅ | The classification of the object (`"related_compliance_requirements"`). Ex.: `"related_compliance_requirements"` |
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
<summary><strong>Respostas</strong> (6)</summary>

<details>
<summary>`201` — Created.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `CreateRelatedRequirementResponse`

_Apenas campos que diferem do request body. 15 campo(s) idênticos omitidos._

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data.id` | string | ✅ | The ID of the requested resource. Ex.: `"1"` |

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
