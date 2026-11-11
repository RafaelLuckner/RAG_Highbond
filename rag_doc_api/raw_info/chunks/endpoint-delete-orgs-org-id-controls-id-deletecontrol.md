---
id: endpoint-delete-orgs-org-id-controls-id-deletecontrol
title: "Controls: Delete a control"
tags: [endpoint, controls]
source: openapi.json (HighBond API v1.1.0)
---

## Controls

A control is a program, policy, routine, or activity that is intended to mitigate a risk. Controls are organized by objectives, and can be associated with one or more risks.
The combination of identified risks and corresponding controls defines the Risk Control Matrix. Controls are also known as procedures.

> **Note:**
Controls located in such resources can be accessed using the API:
> * In projects that have an "active" state
> * In frameworks

Learn more about controls.

### `DELETE /orgs/{org_id}/controls/{id}` — Delete a control

- **operationId:** `deleteControl`
- **Domínio(s):** Controls

Permanently delete a control from an objective.

Limitations:
You cannot delete the control in the following scenarios:
* if the control is included in an existing certification program,
control performance schedule, or
assessment survey
* if the objective it belongs to has been checked out using
Offline Projects or the
HighBond iPad app

> **Caution —**
Deleting a control also removes associated data (including assessment drivers, to-dos, requests, issues, actions, time entries, etc.). Once deleted, you cannot access or restore the control.

<details>
<summary><strong>Parâmetros</strong> (2)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `id` | path | ✅ | string | The ID of the requested resource. Ex.: `9999` |

</details>

<details>
<summary><strong>Respostas</strong> (5)</summary>

- `204` — No content.

- `401` — Bad credentials.

- `403` — Forbidden.

- `404` — Not found.

<details>
<summary>`422` — Unprocessable entity.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `Errors`

Erro no formato padrão JSON:API: objeto `errors` (array) com `status` (código HTTP), `source.pointer` (JSON Pointer RFC6901 do campo com erro), `code`, `title` e `detail`.

</details>

</details>
