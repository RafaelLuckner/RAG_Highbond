---
id: endpoint-post-orgs-org-id-compliance-regulations-createcomplianceregulation
title: "Compliance Maps: Create a compliance regulation"
tags: [endpoint, compliance-maps]
source: openapi.json (HighBond API v1.1.0)
---

## Compliance Maps

You can use Compliance Maps to associate industry standards and regulations with your control frameworks.

Learn more.

### `POST /orgs/{org_id}/compliance_regulations` — Create a compliance regulation

- **operationId:** `createComplianceRegulation`
- **Domínio(s):** Compliance Maps

Create a new compliance regulation in an existing organization.

Limitations:
* There can be a maximum of 500 compliance regulations per HighBond instance.

> **Note —**
System and root users can edit the `disclaimer`, `report_disclaimer`, `requirement_disclaimer` and `locked` attributes. Only root users can edit the `premium` and `subscription_types` attributes.

<details>
<summary><strong>Parâmetros</strong> (2)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `fields[compliance_regulations]` | query |  | string | Requesting the API to return only the specified fields. For more information, see Making requests Ex.: `name,description,created_at,updated_at,external_id,source,disclaimer,report_disclaimer,requirement_disclaimer,available_tags,tags,locked,premium,subscription_types` |

</details>

<details>
<summary><strong>Request body (payload)</strong></summary>

The data required to create a regulation.

**Body obrigatório.**

**Content-Type:** `application/vnd.api+json`

**Schema:** `CreateComplianceRegulationRequest`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | object | ✅ | The data associated with the resource. |
| `data.type` | string | ✅ | The classification of the object (`"compliance_regulations"`). Ex.: `"compliance_regulations"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.name` | string | ✅ | The unique name of the compliance regulation. Ex.: `"My regulation"` |
| `data.attributes.description` | string |  | The detailed description of the regulation. Ex.: `"Regulation details"` |
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
<summary><strong>Respostas</strong> (7)</summary>

<details>
<summary>`201` — Created.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `GetComplianceRegulationResponse`

_Apenas campos que diferem do request body. 14 campo(s) idênticos omitidos._

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data.id` | string | ✅ | The ID of the requested resource. Ex.: `"1"` |
| `data.attributes.name` | string |  | The unique name of the compliance regulation. Ex.: `"My regulation"` |
| `data.attributes.created_at` | string |  | The timestamp specifying when the regulation was created. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.attributes.updated_at` | string |  | The timestamp specifying when the regulation was updated. Ex.: `"2019-03-18T22:02:05Z"` |

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
