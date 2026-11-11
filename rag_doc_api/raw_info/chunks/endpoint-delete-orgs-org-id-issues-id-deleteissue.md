---
id: endpoint-delete-orgs-org-id-issues-id-deleteissue
title: "Issues: Delete an issue"
tags: [endpoint, issues]
source: openapi.json (HighBond API v1.1.0)
---

## Issues

An issue is a problem, control gap, or exception that has been identified within a project. Adding an issue involves recording basic information about the issue and assigning
the issue to an owner. Issues may also be known as deficiencies, findings, or another customized term.

> **Note —**
Only issues in projects that have an `"active"` state can be accessed using the API.

Learn more about issues.

### `DELETE /orgs/{org_id}/issues/{id}` — Delete an issue

- **operationId:** `deleteIssue`
- **Domínio(s):** Issues

Permanently delete an issue from a project.

Limitation:
If the issue belongs to an objective that has been checked out using
Offline Projects or the
HighBond iPad app, you cannot delete the issue.

> **Caution —**
Deleting an issue also removes any associated actions. Once deleted, you cannot access or restore the issue or associated actions.

<details>
<summary><strong>Parâmetros</strong> (2)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `id` | path | ✅ | string | The ID of the requested resource. Ex.: `9999` |

</details>

<details>
<summary><strong>Respostas</strong> (6)</summary>

- `204` — No content.

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
