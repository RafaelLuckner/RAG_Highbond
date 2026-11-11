---
id: endpoint-delete-orgs-org-id-actions-id-deleteaction
title: "Actions: Delete an action"
tags: [endpoint, actions]
source: openapi.json (HighBond API v1.1.0)
---

## Actions

An action is a specific follow-up measure that is associated with an identified issue. You can add actions and assign action owners. You can also set up reminders for
yourself to retest issues or track hours spent on retesting by self-assigning actions.

> **Note —**
Only actions in projects that have an `"active"` state can be accessed using the API.

Learn more about actions.

### `DELETE /orgs/{org_id}/actions/{id}` — Delete an action

- **operationId:** `deleteAction`
- **Domínio(s):** Actions

Delete an action from an existing issue.

Limitations:
You cannot delete the action in the following scenarios:
* if the Follow-up & Remediation subtab of the associated issue is signed off
* if the action belongs to an objective that has been checked out using
Offline Projects or the
HighBond iPad app

> **Caution —**
Deleting an action is permanent. Once deleted, you cannot access or restore the action.

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
