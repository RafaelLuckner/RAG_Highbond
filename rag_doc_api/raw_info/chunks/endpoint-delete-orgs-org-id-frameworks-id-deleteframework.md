---
id: endpoint-delete-orgs-org-id-frameworks-id-deleteframework
title: "Frameworks: Delete a framework"
tags: [endpoint, frameworks]
source: openapi.json (HighBond API v1.1.0)
---

## Frameworks

A framework is a management system that allows you to define objectives, risks, and controls, perform tests, and compile information for reporting purposes. Frameworks may also
be known as audits, compliance assessments, risk assessments, or another customized term.

Learn more about frameworks.

### `DELETE /orgs/{org_id}/frameworks/{id}` — Delete a framework

- **operationId:** `deleteFramework`
- **Domínio(s):** Frameworks

Delete a framework that you no longer require.

> **Caution —**
Once a framework is permanently deleted, you cannot access or restore the framework.

For more information, see Deleting frameworks.

<details>
<summary><strong>Parâmetros</strong> (2)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `id` | path | ✅ | string | The ID of the requested resource. Ex.: `9999` |

</details>

<details>
<summary><strong>Respostas</strong> (7)</summary>

- `202` — Accepted.

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
