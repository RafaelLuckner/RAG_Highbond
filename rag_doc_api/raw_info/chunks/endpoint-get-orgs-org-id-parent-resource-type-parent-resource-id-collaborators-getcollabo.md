---
id: endpoint-get-orgs-org-id-parent-resource-type-parent-resource-id-collaborators-getcollabo
title: "Collaborators: Get collaborators"
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

### `GET /orgs/{org_id}/{parent_resource_type}/{parent_resource_id}/collaborators` — Get collaborators

- **operationId:** `getCollaborators`
- **Domínio(s):** Collaborators

Get all collaborators in a project or framework.

Note:
* Only users that have an assigned `project_role` are returned in the response.

<details>
<summary><strong>Parâmetros</strong> (5)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `parent_resource_type` | path | ✅ | string | The type of the parent resource. Valores: `projects`, `frameworks` Default: `projects` |
| `parent_resource_id` | path | ✅ | integer | The ID of the parent resource. Ex.: `1` |
| `fields[collaborators]` | query |  | string | Requesting the API to return only the specified fields. For more information, see Making requests Ex.: `project,framework,user,project_role,effective_role,organization_role,created_at,updated_at` |
| `include` | query |  | string | Requesting the API to return related resources. For more information, see Making requests Ex.: `project,framework,user` |

</details>

<details>
<summary><strong>Respostas</strong> (6)</summary>

<details>
<summary>`200` — OK.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `GetCollaboratorsResponse`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | array[object] | ✅ |  |
| `data.id` | string | ✅ | The IDs of the parent resource (project or framework) and user, in the `parent_resource_id:user_uid` format, which then must be encoded into Base64.  For example, if the `parent_resource_id` is `11955` and the `user_uid` is `yvqdNCtv8TeM47WQtzau`, you would encode `11955:yvqdNCtv8TeM47WQtzau` into Base64. The result is `MTE5NTU6eXZxZE5DdHY4VGVNNDdXUXR6YXU=`, which is the `id`. Ex.: `"MTE5NTU6eXZxZE5DdHY4VGVNNDdXUXR6YXU="` |
| `data.type` | string | ✅ | The classification of the object (`"collaborators"`). Ex.: `"collaborators"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.project_role` | string |  | Roles apply within an individual project or framework. A single user may have a different role for each project or framework.  Available project roles are:   `"professional_manager"`, `"professional_user"`, `"oversight_executive"`, `"oversight_reviewer"`,   `"contributor_user"`, `"contributor_manager"`, `"contributor_tester"` Ex.: `"professional_manager"` |
| `data.attributes.effective_role` | string |  | A user may be assigned to a project as an individual with a specific role, and also as a member of a group with a different role. If those roles conflict with each other, HighBond uses the effective_role. Ex.: `"client_manager"` |
| `data.attributes.organization_role` | string |  | Organization roles are user privileges that allow users to perform actions in projects and frameworks. Learn more about privileges in projects and frameworks.  Available account roles are:   `"sys_admin"`, `"project_creator"`, `"admin"`, `"project_type_admin"`, `"archivist"`, `"timesheets_admin"`,   `"compliance_maps_read"`, `"compliance_maps_write"`, `"compliance_maps_no_access"`, `"assurance_plan_admin"` Ex.: `"project_creator"` |
| `data.attributes.created_at` | string |  | The timestamp identifying when the collaborator was created. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.attributes.updated_at` | string |  | The timestamp identifying when the collaborator was last updated. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.relationships` | object | ✅ | The relationships associated with the resource. |
| `data.relationships.project` | object |  | Each collaborator has an associated project or framework. Project/framework is a management system that allows you to define and compile information for reporting purposes. |
| `data.relationships.project.data` | object | ✅ | The data associated with the resource. |
| `data.relationships.project.data.id` | string | ✅ | The ID of the project. Ex.: `"1"` |
| `data.relationships.project.data.type` | string | ✅ | The classification of the object (`"projects"`). Ex.: `"projects"` |
| `data.relationships.framework` | object |  | Each collaborator has an associated project or framework. Project/framework is a management system that allows you to define and compile information for reporting purposes. |
| `data.relationships.framework.data` | object | ✅ | The data associated with the resource. |
| `data.relationships.framework.data.id` | string | ✅ | The ID of the framework. Ex.: `"1"` |
| `data.relationships.framework.data.type` | string | ✅ | The classification of the object (`"frameworks"`). Ex.: `"frameworks"` |
| `data.relationships.user` | object |  | Details of the user nested in that endpoint. |
| `data.relationships.user.data` | object | ✅ | The data associated with the resource. |
| `data.relationships.user.data.id` | string | ✅ | The unique identifier (UID) of the assigned user. For more information on obtaining this value, see Making requests. Ex.: `"yvqdNCtv8TeM47WQtzau"` |
| `data.relationships.user.data.type` | string | ✅ | The classification of the object (`"users"`). Ex.: `"users"` |

</details>

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
