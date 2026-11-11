---
id: endpoint-delete-orgs-org-id-collaborator-groups-encoded-uid-deletecollaboratorgroup
title: "Collaborators: Delete a collaborator group"
tags: [endpoint, collaborators]
source: openapi.json (HighBond API v1.1.0)
---

## Collaborators

A collaborator is a representation of user roles, which are associated with projects and frameworks, that you can manipulate. Collaborators are accessible both in project and framework resources.

The collaborator section has endpoints for both individuals and groups.

> **Note:**
> * Only users that have an assigned `effective_role` are returned in the response.
> * The `updated_at` field represents the date that the collaborator or collaborator group was last directly updated. Changes to the `effective_role` may occur as a result of assigning the user or group a `group_role`, but doing so won't update the `updated_at` field.

Learn more about roles and permissions.

### `DELETE /orgs/{org_id}/collaborator_groups/{encoded_uid}` — Delete a collaborator group

- **operationId:** `deleteCollaboratorGroup`
- **Domínio(s):** Collaborators

Remove a collaborator group from a project or framework.

Limitations:
* You can't unassign the `Default System Admins` group from a project.

<details>
<summary><strong>Parâmetros</strong> (2)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `encoded_uid` | path | ✅ | string | The IDs of the parent resource (project or framework) and Launchpad ID of the group, in the `parent_resource_id:group_lp_id` format, which then must be encoded into Base64.  For example, if the `parent_resource_id` is `11955` and the `group_lp_id` is `1337`, you would encode `11955:1337` into Base64. The result is `MTE5NTU6MTMzNw==`, which is the `id`. Ex.: `MTE5NTU6MTMzNw==` |

</details>

<details>
<summary><strong>Respostas</strong> (5)</summary>

- `202` — Accepted.

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
