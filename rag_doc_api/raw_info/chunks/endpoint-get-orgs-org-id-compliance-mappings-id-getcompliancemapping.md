---
id: endpoint-get-orgs-org-id-compliance-mappings-id-getcompliancemapping
title: "Compliance Maps: Get a compliance mapping"
tags: [endpoint, compliance-maps]
source: openapi.json (HighBond API v1.1.0)
---

## Compliance Maps

You can use Compliance Maps to associate industry standards and regulations with your control frameworks.

Learn more.

### `GET /orgs/{org_id}/compliance_mappings/{id}` — Get a compliance mapping

- **operationId:** `getComplianceMapping`
- **Domínio(s):** Compliance Maps

Get information about a compliance mapping in an organization.

<details>
<summary><strong>Parâmetros</strong> (3)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `id` | path | ✅ | string | The ID of the requested resource. Ex.: `9999` |
| `fields[compliance_mappings]` | query |  | string | Requesting the API to return only the specified fields. For more information, see Making requests Ex.: `coverage,created_at,updated_at,compliance_requirement,control` |

</details>

<details>
<summary><strong>Respostas</strong> (6)</summary>

<details>
<summary>`200` — OK.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `GetComplianceMappingResponseWithIncludes`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | object | ✅ | The data associated with the resource. |
| `data.id` | string | ✅ | The ID of the requested resource. Ex.: `"1"` |
| `data.type` | string | ✅ | The classification of the object (`"compliance_mappings"`). Ex.: `"compliance_mappings"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.coverage` | integer | ✅ | Coverage percentage. Ex.: `75` |
| `data.attributes.created_at` | string |  | The timestamp specifying when the mapping was created. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.attributes.updated_at` | string |  | The timestamp specifying when the mapping was updated. Ex.: `"2019-03-18T22:02:05Z"` |
| `data.relationships` | object |  | The relationships associated with the resource. |
| `data.relationships.compliance_requirement` | object |  | Requirement object. |
| `data.relationships.compliance_requirement.data` | object | ✅ | The data associated with the resource. |
| `data.relationships.compliance_requirement.data.id` | string | ✅ | The ID of the requested resource. Ex.: `"1"` |
| `data.relationships.compliance_requirement.data.type` | string | ✅ | The classification of the object (`"compliance_requirements"`). Ex.: `"compliance_requirements"` |
| `data.relationships.control` | object |  | Control object. |
| `data.relationships.control.data` | object | ✅ | The data associated with the resource. |
| `data.relationships.control.data.id` | string | ✅ | The ID of the requested resource. Ex.: `"1"` |
| `data.relationships.control.data.type` | string | ✅ | The classification of the object (`"controls"`). Ex.: `"controls"` |
| `included` | array[object] |  | Included resources. Ex.: `[{"id": 2, "type": "compliance_requirements", "attributes": {"name": "My requirement"}}]` |

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
