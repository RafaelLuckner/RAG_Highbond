---
id: endpoint-get-orgs-org-id-compliance-regulations-id-getcomplianceregulation
title: "Compliance Maps: Get a compliance regulation"
tags: [endpoint, compliance-maps]
source: openapi.json (HighBond API v1.1.0)
---

## Compliance Maps

You can use Compliance Maps to associate industry standards and regulations with your control frameworks.

Learn more.

### `GET /orgs/{org_id}/compliance_regulations/{id}` — Get a compliance regulation

- **operationId:** `getComplianceRegulation`
- **Domínio(s):** Compliance Maps

Get information about a compliance regulation.

> **Note —**
Only root users can read the `premium` and `subscription_types` attributes.

<details>
<summary><strong>Parâmetros</strong> (3)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `id` | path | ✅ | string | The ID of the requested resource. Ex.: `9999` |
| `fields[compliance_regulations]` | query |  | string | Requesting the API to return only the specified fields. For more information, see Making requests Ex.: `name,description,created_at,updated_at,external_id,source,disclaimer,report_disclaimer,requirement_disclaimer,available_tags,tags,locked,premium,subscription_types` |

</details>

<details>
<summary><strong>Respostas</strong> (6)</summary>

<details>
<summary>`200` — OK.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `GetComplianceRegulationResponse`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | object | ✅ | The data associated with the resource. |
| `data.id` | string | ✅ | The ID of the requested resource. Ex.: `"1"` |
| `data.type` | string | ✅ | The classification of the object (`"compliance_regulations"`). Ex.: `"compliance_regulations"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.name` | string |  | The unique name of the compliance regulation. Ex.: `"My regulation"` |
| `data.attributes.description` | string |  | The detailed description of the regulation. Ex.: `"Regulation details"` |
| `data.attributes.created_at` | string |  | The timestamp specifying when the regulation was created. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.attributes.updated_at` | string |  | The timestamp specifying when the regulation was updated. Ex.: `"2019-03-18T22:02:05Z"` |
| `data.attributes.external_id` | string |  | An optional identifier. Ex.: `"RG-1"` |
| `data.attributes.source` | string |  | Source of the regulation. Used for legal reasons. Ex.: `"Federal Trade Commission"` |
| `data.attributes.disclaimer` | string |  | Regulation disclaimer. Ex.: `"Example of disclaimer."` |
| `data.attributes.report_disclaimer` | string |  | Report disclaimer. Ex.: `"Example of disclaimer."` |
| `data.attributes.requirement_disclaimer` | string |  | Requirement disclaimer. Ex.: `"Example of disclaimer."` |
| `data.attributes.available_tags` | array[string] |  | List of available tags to be used inside the regulation. |
| `data.attributes.tags` | array[string] |  | List of applied tags. Must use elements from `available_tags`. |
| `data.attributes.locked` | boolean |  | Defines whether regulation is editable or not. Ex.: `false` |
| `data.attributes.premium` | boolean |  | Indicates whether content is only available for users who have premium edition subscriptions. Ex.: `false` |
| `data.attributes.subscription_types` | array[string] |  | Indicates the user's subscription type. |

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
