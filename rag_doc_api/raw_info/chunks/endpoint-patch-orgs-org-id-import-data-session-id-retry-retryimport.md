---
id: endpoint-patch-orgs-org-id-import-data-session-id-retry-retryimport
title: "Importer: Retry import"
tags: [endpoint, importer]
source: openapi.json (HighBond API v1.1.0)
---

## Importer

Importer for HighBond, responsible for importing HighBond resources.

You can bulk import HighBond resources if you want to avoid time-consuming manual data entry associated with individually adding resources. You can bulk import resources such as requests, controls, risks, etc.

Learn more about importer.

### `PATCH /orgs/{org_id}/import/data/{session_id}/retry` — Retry import

- **operationId:** `retryImport`
- **Domínio(s):** Importer

Responsible for retrying a timed-out import session.

<details>
<summary><strong>Parâmetros</strong> (2)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `session_id` | path | ✅ | string | The unique identifier for an import. Ex.: `58e559b1-31bf-4341-b761-c30364376adf` |

</details>

<details>
<summary><strong>Respostas</strong> (8)</summary>

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
<summary>`412` — Precondition Failed.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `Errors`

Erro no formato padrão JSON:API: objeto `errors` (array) com `status` (código HTTP), `source.pointer` (JSON Pointer RFC6901 do campo com erro), `code`, `title` e `detail`.

</details>

<details>
<summary>`422` — Unprocessable Entity.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `Errors`

Erro no formato padrão JSON:API: objeto `errors` (array) com `status` (código HTTP), `source.pointer` (JSON Pointer RFC6901 do campo com erro), `code`, `title` e `detail`.

</details>

</details>
