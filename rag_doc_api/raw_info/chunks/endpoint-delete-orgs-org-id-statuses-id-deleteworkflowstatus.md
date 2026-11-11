---
id: endpoint-delete-orgs-org-id-statuses-id-deleteworkflowstatus
title: "Workflows in Asset Inventory/Asset Manager: Delete a workflow status"
tags: [endpoint, workflows-in-asset-inventory-asset-manager]
source: openapi.json (HighBond API v1.1.0)
---

## Workflows in Asset Inventory/Asset Manager

Workflows contain a set of statuses that a certain item belonging to that workflow can be in. Any items in this workflow can move between certain statuses and the transition can trigger certain events which will execute their handlers.

Workflow statuses represent all possible states an item of the workflow can be in. Statuses can be associated with Events to allow transition from one status to another within the same workflow.

Every workflow must have exactly one "default" status. You can make a status the default status by setting or updating the default flag on that status. This default status cannot be deleted.

### `DELETE /orgs/{org_id}/statuses/{id}` — Delete a workflow status

- **operationId:** `deleteWorkflowStatus`
- **Domínio(s):** Workflows in Asset Inventory/Asset Manager

Permanently delete a workflow status.

Locked workflow statuses cannot be deleted.

System workflow statuses cannot be deleted.

Statuses that are the default in the workflow cannot be deleted.

Statuses linked to an asset or asset record cannot be deleted.

<details>
<summary><strong>Parâmetros</strong> (3)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `id` | path | ✅ | string | The ID of the requested resource. Ex.: `296f9069-4e4a-42bf-ba8a-e372e8f9e724` |
| `force_delete` | query |  | boolean | If set to true, the status will be deleted regardless of default, locked, or linked items conditions. System statuses cannot be deleted, even with this set to true. Default: `False` |

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
