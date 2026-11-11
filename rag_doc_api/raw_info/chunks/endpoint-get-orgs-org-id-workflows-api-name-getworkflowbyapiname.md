---
id: endpoint-get-orgs-org-id-workflows-api-name-getworkflowbyapiname
title: "Workflows in Asset Inventory/Asset Manager: Get a workflow by api name"
tags: [endpoint, workflows-in-asset-inventory-asset-manager]
source: openapi.json (HighBond API v1.1.0)
---

## Workflows in Asset Inventory/Asset Manager

Workflows contain a set of statuses that a certain item belonging to that workflow can be in. Any items in this workflow can move between certain statuses and the transition can trigger certain events which will execute their handlers.

Workflow statuses represent all possible states an item of the workflow can be in. Statuses can be associated with Events to allow transition from one status to another within the same workflow.

Every workflow must have exactly one "default" status. You can make a status the default status by setting or updating the default flag on that status. This default status cannot be deleted.

### `GET /orgs/{org_id}/workflows/{api_name}` — Get a workflow by api name

- **operationId:** `getWorkflowByApiName`
- **Domínio(s):** Workflows in Asset Inventory/Asset Manager

Get information about a workflow, using api_name, including all of its statuses, events and handlers if requested.

<details>
<summary><strong>Parâmetros</strong> (3)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `api_name` | path | ✅ | string | The api name of the workflow Ex.: `my_workflow_api_name__c` |
| `include` | query |  | string | Include information about the associated resources. Valores: `statuses.events.handlers`, `statuses.events`, `statuses` Ex.: `statuses.events.handlers` |

</details>

<details>
<summary><strong>Respostas</strong> (4)</summary>

<details>
<summary>`200` — OK.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `SingleWorkflowResponseWithIncludes`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | object | ✅ | The data associated with the resource. |
| `data.id` | string | ✅ | The ID of the workflow. Ex.: `"768cd1bc-d8af-4429-9aa0-8a4b477de42b"` |
| `data.type` | string | ✅ | The classification of the object (`"workflows"`). Ex.: `"workflows"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.name` | string |  | The name of the workflow. Names are case-insensitive and must be unique. Ex.: `"My first Workflow"` |
| `data.attributes.description` | string |  | The description of the workflow. Ex.: `"Description of My first Workflow"` |
| `data.attributes.locked` | boolean |  | Indicates that this workflow cannot be deleted by the user. Default: `False` Ex.: `false` |
| `data.attributes.api_name` | string |  | The API name of the workflow that is unique within the org, uneditable after creation, and must satisfy the following restrictions: - No uppercase letters - No whitespace (use `"_"` to separate words) - No special characters  Note: upon successful workflow creation a `"__c"` is appended to the provided api_name  Ex: my_api_name  -->  my_api_name__c Default: `None` Ex.: `"my_workflow_api_name__c"` |
| `data.attributes.created_at` | string |  | The date the workflow was created. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.attributes.updated_at` | string |  | The date the workflow was updated. Ex.: `"2019-03-18T22:02:05Z"` |
| `data.attributes.system` | boolean |  | Indicates that this workflow cannot be modified by the user. Default: `False` Ex.: `false` |
| `data.relationships` | object |  | Each workflow has associated statuses. |
| `data.relationships.statuses` | object | ✅ | The data associated with the resource. |
| `data.relationships.statuses.data` | array[object] | ✅ |  |
| `data.relationships.statuses.data.id` | string | ✅ | The ID of the status. Ex.: `"b125726f-ee4f-4ec9-9488-b6efa4ee1270"` |
| `data.relationships.statuses.data.type` | string | ✅ | The classification of the object (`"statuses"`). Ex.: `"statuses"` |
| `included` | array[object] | ✅ | All the objects related to the resource Ex.: `[{"type": "statuses", "id": "9af02c4a-3c98-4283-8c5d-8dc47e3bf663", "attributes": {"name": "status 1", "description": "blahblah...", "locked": fals...` |

</details>

- `401` — Bad credentials.

- `403` — Forbidden.

- `404` — Not found.

</details>
