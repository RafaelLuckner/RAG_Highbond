---
id: endpoint-patch-orgs-org-id-import-data-session-id-updateimport
title: "Importer: Update import"
tags: [endpoint, importer]
source: openapi.json (HighBond API v1.1.0)
---

## Importer

Importer for HighBond, responsible for importing HighBond resources.

You can bulk import HighBond resources if you want to avoid time-consuming manual data entry associated with individually adding resources. You can bulk import resources such as requests, controls, risks, etc.

Learn more about importer.

### `PATCH /orgs/{org_id}/import/data/{session_id}` — Update import

- **operationId:** `updateImport`
- **Domínio(s):** Importer

Responsible for updating HighBond resources

<details>
<summary><strong>Parâmetros</strong> (2)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `session_id` | path | ✅ | string | The unique identifier for an import. Ex.: `58e559b1-31bf-4341-b761-c30364376adf` |

</details>

<details>
<summary><strong>Request body (payload)</strong></summary>

The data required to update a resource.

**Body obrigatório.**

**Content-Type:** `application/vnd.api+json`

**Schema:** `UpdateImporterPayload`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | object | ✅ | The data associated with the resource.  The payload must match the columns in the Excel template of the importer. The columns in the template are based on the type of resource you want to import. For more information, see Bulk importing HighBond resources. |
| `data.type` | string | ✅ | The classification of the object (`"importer"`). Ex.: `"importer"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |

</details>

<details>
<summary><strong>Respostas</strong> (7)</summary>

<details>
<summary>`200` — OK.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `ImporterResponse`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | array[object] | ✅ | The data associated with the resource. |
| `data.session_id` | string | ✅ | The Unique identifier for an import. Ex.: `"58e559b1-31bf-4341-b761-c30364376adf"` |
| `data.attributes` | string |  | Unique identifier for the resource. Ex.: `"58e559b1-31bf-4341-b761-c30364376adf"` |

</details>

<details>
<summary>`208` — Request already submitted.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `Errors`

Erro no formato padrão JSON:API: objeto `errors` (array) com `status` (código HTTP), `source.pointer` (JSON Pointer RFC6901 do campo com erro), `code`, `title` e `detail`.

</details>

<details>
<summary>`400` — Bad request.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `Errors`

Erro no formato padrão JSON:API: objeto `errors` (array) com `status` (código HTTP), `source.pointer` (JSON Pointer RFC6901 do campo com erro), `code`, `title` e `detail`.

</details>

- `401` — Bad credentials.

<details>
<summary>`403` — Forbidden.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `Errors`

Erro no formato padrão JSON:API: objeto `errors` (array) com `status` (código HTTP), `source.pointer` (JSON Pointer RFC6901 do campo com erro), `code`, `title` e `detail`.

</details>

<details>
<summary>`404` — Not Found.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `Errors`

Erro no formato padrão JSON:API: objeto `errors` (array) com `status` (código HTTP), `source.pointer` (JSON Pointer RFC6901 do campo com erro), `code`, `title` e `detail`.

</details>

<details>
<summary>`422` — Invalid import data.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `Errors`

Erro no formato padrão JSON:API: objeto `errors` (array) com `status` (código HTTP), `source.pointer` (JSON Pointer RFC6901 do campo com erro), `code`, `title` e `detail`.

</details>

</details>
