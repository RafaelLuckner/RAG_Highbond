---
id: endpoint-delete-orgs-org-id-events-id-deleteevent
title: "Events: Delete an Event"
tags: [endpoint, events]
source: openapi.json (HighBond API v1.1.0)
---

## Events

An Event links a status to handlers. When an event is fired, the associated handlers will be triggered.

### `DELETE /orgs/{org_id}/events/{id}` — Delete an Event

- **operationId:** `deleteEvent`
- **Domínio(s):** Events

Permanently delete an event.

<details>
<summary><strong>Parâmetros</strong> (2)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `id` | path | ✅ | string | The ID of the requested resource. Ex.: `296f9069-4e4a-42bf-ba8a-e372e8f9e724` |

</details>

<details>
<summary><strong>Respostas</strong> (5)</summary>

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

</details>
