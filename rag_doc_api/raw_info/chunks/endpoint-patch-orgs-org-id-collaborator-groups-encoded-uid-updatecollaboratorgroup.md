---
id: endpoint-patch-orgs-org-id-collaborator-groups-encoded-uid-updatecollaboratorgroup
title: "Collaborators: Update a collaborator group"
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

### `PATCH /orgs/{org_id}/collaborator_groups/{encoded_uid}` — Update a collaborator group

- **operationId:** `updateCollaboratorGroup`
- **Domínio(s):** Collaborators

Make changes to a collaborator group in a project or framework, like changing its `project_role` attribute.

Limitations:
* You can't update a group that has a value of `none` assigned to the `project_role` attribute.
* You can't update the `Default System Admins` group.

<details>
<summary><strong>Parâmetros</strong> (4)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `encoded_uid` | path | ✅ | string | The IDs of the parent resource (project or framework) and Launchpad ID of the group, in the `parent_resource_id:group_lp_id` format, which then must be encoded into Base64.  For example, if the `parent_resource_id` is `11955` and the `group_lp_id` is `1337`, you would encode `11955:1337` into Base64. The result is `MTE5NTU6MTMzNw==`, which is the `id`. Ex.: `MTE5NTU6MTMzNw==` |
| `fields[collaborators_groups]` | query |  | string | Requesting the API to return only the specified fields. For more information, see Making requests Ex.: `project,framework,group_members,group,project_role,disabled,default,admin,created_at,updated_at` |
| `include` | query |  | string | Requesting the API to return related resources. For more information, see Making requests Ex.: `group,group_members,project,framework` |

</details>

<details>
<summary><strong>Request body (payload)</strong></summary>

The data required to update a collaborator group.

**Body obrigatório.**

**Content-Type:** `application/vnd.api+json`

**Schema:** `UpdateCollaboratorGroupRequest`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | object | ✅ | The data associated with the resource. |
| `data.id` | string | ✅ | The IDs of the parent resource (project or framework) and Launchpad ID of the group, in the `parent_resource_id:group_lp_id` format, which then must be encoded into Base64.  For example, if the `parent_resource_id` is `11955` and the `group_lp_id` is `yvqdNCtv8TeM47WQtzau`, you would encode `11955:yvqdNCtv8TeM47WQtzau` into Base64. The result is `MTE5NTU6eXZxZE5DdHY4VGVNNDdXUXR6YXU=`, which is the `id`. Ex.: `"MTE5NTU6eXZxZE5DdHY4VGVNNDdXUXR6YXU="` |
| `data.type` | string | ✅ | The classification of the object (`"collaborator_groups"`). Ex.: `"collaborator_groups"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.project_role` | string | ✅ | Assigned role for group within project or framework.  Available project roles are:   `"professional_manager"`, `"professional_user"`, `"oversight_executive"`, `"oversight_reviewer"`,   `"contributor_user"`, `"contributor_manager"`, `"contributor_tester"` Ex.: `"professional_manager"` |

</details>

<details>
<summary><strong>Respostas</strong> (7)</summary>

<details>
<summary>`200` — OK.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `GetCollaboratorGroupResponse`

_Apenas campos que diferem do request body. 4 campo(s) idênticos omitidos._

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data.attributes.project_role` | string |  | Assigned role for group within project or framework.  Available project roles are:   `"professional_manager"`, `"professional_user"`, `"oversight_executive"`, `"oversight_reviewer"`,   `"contributor_user"`, `"contributor_manager"`, `"contributor_tester"` Ex.: `"professional_manager"` |
| `data.attributes.admin` | boolean |  | Indicates if the group is assigned as the System Admin Group in Launchpad. Ex.: `false` |
| `data.attributes.disabled` | boolean |  | Indicates if the `project_role` attribute has a value assigned to it. Ex.: `false` |
| `data.attributes.default` | boolean |  | Indicates if the group was assigned by default to a project or framework. Ex.: `false` |
| `data.attributes.created_at` | string |  | The timestamp identifying when the collaborator group was created. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.attributes.updated_at` | string |  | The timestamp identifying when the collaborator group was last updated. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.relationships` | object | ✅ | The relationships associated with the resource. |
| `data.relationships.project` | object |  | Each collaborator group has an associated project or framework. A project/framework is a management system that allows you to define and compile information for reporting purposes. |
| `data.relationships.project.data` | object | ✅ | The data associated with the resource. |
| `data.relationships.project.data.id` | string | ✅ | The ID of the project. Ex.: `"1"` |
| `data.relationships.project.data.type` | string | ✅ | The classification of the object (`"projects"`). Ex.: `"projects"` |
| `data.relationships.framework` | object |  | Each collaborator group has an associated project or framework. A project/framework is a management system that allows you to define and compile information for reporting purposes. |
| `data.relationships.framework.data` | object | ✅ | The data associated with the resource. |
| `data.relationships.framework.data.id` | string | ✅ | The ID of the framework. Ex.: `"1"` |
| `data.relationships.framework.data.type` | string | ✅ | The classification of the object (`"frameworks"`). Ex.: `"frameworks"` |
| `data.relationships.group_members` | object |  | List of users assigned to the group. |
| `data.relationships.group_members.data` | array[object] | ✅ |  |
| `data.relationships.group_members.data.id` | string | ✅ | The unique identifier (UID) of the assigned user. For more information on obtaining this value, see Making requests. Ex.: `"yvqdNCtv8TeM47WQtzau"` |
| `data.relationships.group_members.data.type` | string | ✅ | The classification of the object (`"users"`). Ex.: `"users"` |
| `data.relationships.group` | object |  | Groups are a security feature in Launchpad that allow you to assign the same level of access to multiple users simultaneously. |
| `data.relationships.group.data` | object | ✅ | The data associated with the resource. |
| `data.relationships.group.data.id` | string | ✅ | The identifier of the assigned group. Ex.: `1` |
| `data.relationships.group.data.type` | string | ✅ | The classification of the object (`"groups"`). Ex.: `"groups"` |

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

<details>
<summary>`422` — Unprocessable entity.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `Errors`

Erro no formato padrão JSON:API: objeto `errors` (array) com `status` (código HTTP), `source.pointer` (JSON Pointer RFC6901 do campo com erro), `code`, `title` e `detail`.

</details>

</details>
