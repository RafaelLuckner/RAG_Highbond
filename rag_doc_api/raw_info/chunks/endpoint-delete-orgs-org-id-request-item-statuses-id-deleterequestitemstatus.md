---
id: endpoint-delete-orgs-org-id-request-item-statuses-id-deleterequestitemstatus
title: "Request item statuses: Delete a request item status"
tags: [endpoint, request-item-statuses]
source: openapi.json (HighBond API v1.1.0)
---

## Request item statuses

Request statuses provide visibility into the progress of request resolutions. The number of available statuses, and the terms used for each status, can be customized by the organization.

Learn more about request item statuses.

### `DELETE /orgs/{org_id}/request_item_statuses/{id}` — Delete a request item status

- **operationId:** `deleteRequestItemStatus`
- **Domínio(s):** Request item statuses

Permanently delete a request item status from a project type.
> **Caution —**
Deleting a request item status permanently removes the field and all associated data from all relevant projects and frameworks.

<details>
<summary><strong>Parâmetros</strong> (2)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `id` | path | ✅ | string | The ID of the requested resource. Ex.: `9999` |

</details>

<details>
<summary><strong>Respostas</strong> (7)</summary>

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

<details>
<summary>`422` — Unprocessable entity.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `Errors`

Erro no formato padrão JSON:API: objeto `errors` (array) com `status` (código HTTP), `source.pointer` (JSON Pointer RFC6901 do campo com erro), `code`, `title` e `detail`.

</details>

</details>
