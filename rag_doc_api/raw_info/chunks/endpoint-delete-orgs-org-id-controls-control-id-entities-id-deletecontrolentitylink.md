---
id: endpoint-delete-orgs-org-id-controls-control-id-entities-id-deletecontrolentitylink
title: "Controls: Delete control entity link"
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

### `DELETE /orgs/{org_id}/controls/{control_id}/entities/{id}` — Delete control entity link

- **operationId:** `deleteControlEntityLink`
- **Domínio(s):** Controls

Permanently delete control entity link.

> **Note -**
Untagging a control from an entity automatically untags a control from all descendant entities.

Limitations:
  * You cannot untag a control from an entity if the objective it belongs to has been checked out using
  Offline Projects or the
  HighBond iPad app.
  * Inherited entity tags cannot be removed.

<details>
<summary><strong>Parâmetros</strong> (3)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `control_id` | path | ✅ | integer | The ID of the control. Ex.: `1` |
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
