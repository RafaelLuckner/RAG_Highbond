---
id: endpoint-get-orgs-org-id-compliance-requirements-id-getcompliancerequirement
title: "Compliance Maps: Get a compliance requirement"
tags: [endpoint, compliance-maps]
source: openapi.json (HighBond API v1.1.0)
---

## Compliance Maps

You can use Compliance Maps to associate industry standards and regulations with your control frameworks.

Learn more.

### `GET /orgs/{org_id}/compliance_requirements/{id}` — Get a compliance requirement

- **operationId:** `getComplianceRequirement`
- **Domínio(s):** Compliance Maps

Get information about a compliance requirement.

<details>
<summary><strong>Parâmetros</strong> (4)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `id` | path | ✅ | string | The ID of the requested resource. Ex.: `9999` |
| `fields[compliance_requirements]` | query |  | string | Requesting the API to return only the specified fields. For more information, see Making requests Ex.: `identifier,name,description,created_at,updated_at,external_id,external_parent_id,tags,rationale,applicable,covered,coverage,position,compliance_regulation,parent,compliance_mappings` |
| `fields[compliance_mappings]` | query |  | string | Requesting the API to return only the specified fields. For more information, see Making requests Ex.: `coverage,created_at,updated_at,compliance_requirement,control` |

</details>

<details>
<summary><strong>Respostas</strong> (6)</summary>

<details>
<summary>`200` — OK.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `GetComplianceRequirementResponseWithIncludes`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | object | ✅ | The data associated with the resource. |
| `data.id` | string | ✅ | The ID of the requested resource. Ex.: `"1"` |
| `data.type` | string | ✅ | The classification of the object (`"compliance_requirements"`). Ex.: `"compliance_requirements"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.name` | string |  | The name of the compliance requirement. Ex.: `"My requirement"` |
| `data.attributes.identifier` | string |  | The identifier of the compliance requirement. Ex.: `"REQ-1"` |
| `data.attributes.description` | string |  | The detailed description of the requirement. Ex.: `"Requirement details"` |
| `data.attributes.created_at` | string |  | The timestamp specifying when the requirement was created. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.attributes.updated_at` | string |  | The timestamp specifying when the requirement was updated. Ex.: `"2019-03-18T22:02:05Z"` |
| `data.attributes.external_id` | string |  | An optional identifier. Ex.: `"EXT-1"` |
| `data.attributes.external_parent_id` | string |  | An optional identifier of parent. Ex.: `"EXT-2"` |
| `data.attributes.tags` | array[string] |  | List of applied tags. Must use elements from regulation's `available_tags`. |
| `data.attributes.rationale` | string |  | Rationale. Ex.: `"Requirement rationale"` |
| `data.attributes.applicable` | boolean |  | Indicates whether requirement is covered/applicable. Ex.: `true` |
| `data.attributes.covered` | boolean |  | Indicates whether requirement is covered/applicable. Ex.: `true` |
| `data.attributes.coverage` | number |  | Coverage percentage. Ex.: `0.8` |
| `data.attributes.position` | integer |  | Position optional integer indicates position of compliance requirement in UI Ex.: `3` |
| `data.relationships` | object |  | The relationships associated with the resource. |
| `data.relationships.compliance_regulation` | object |  | Parent regulation object. |
| `data.relationships.compliance_regulation.data` | object | ✅ | The data associated with the resource. |
| `data.relationships.compliance_regulation.data.id` | string | ✅ | The ID of the requested resource. Ex.: `"1"` |
| `data.relationships.compliance_regulation.data.type` | string | ✅ | The classification of the object (`"compliance_regulations"`). Ex.: `"compliance_regulations"` |
| `data.relationships.parent` | object |  | Parent requirement object. |
| `data.relationships.parent.data` | object | ✅ | The data associated with the resource. |
| `data.relationships.parent.data.id` | string | ✅ | The ID of the requested resource. Ex.: `"1"` |
| `data.relationships.parent.data.type` | string | ✅ | The classification of the object (`"compliance_requirements"`). Ex.: `"compliance_requirements"` |
| `data.relationships.compliance_mappings` | object |  | Related control mappings. |
| `data.relationships.compliance_mappings.data` | array[object] | ✅ | The data associated with the resource. |
| `data.relationships.compliance_mappings.data.id` | string | ✅ | The ID of the requested resource. Ex.: `"1"` |
| `data.relationships.compliance_mappings.data.type` | string | ✅ | The classification of the object (`"compliance_mappings"`). Ex.: `"compliance_mappings"` |
| `data.links` | object |  | Resource links. |
| `data.links.ui` | string |  | Link to the requirement in UI. Ex.: `"https://test-org.compliance-maps.highbond.com/standard/1/requirement/2/edit"` |
| `included` | array[object] |  | Included resources. Ex.: `[{"id": 1, "type": "compliance_regulation", "attributes": {"name": "My regulation"}}, {"id": 2, "type": "compliance_requirements", "attributes": {"...` |

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
