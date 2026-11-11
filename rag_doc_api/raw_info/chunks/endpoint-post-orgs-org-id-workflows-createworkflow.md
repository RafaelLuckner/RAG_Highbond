---
id: endpoint-post-orgs-org-id-workflows-createworkflow
title: "Workflows in Asset Inventory/Asset Manager: Create a workflow"
tags: [endpoint, workflows-in-asset-inventory-asset-manager]
source: openapi.json (HighBond API v1.1.0)
---

## Workflows in Asset Inventory/Asset Manager

Workflows contain a set of statuses that a certain item belonging to that workflow can be in. Any items in this workflow can move between certain statuses and the transition can trigger certain events which will execute their handlers.

Workflow statuses represent all possible states an item of the workflow can be in. Statuses can be associated with Events to allow transition from one status to another within the same workflow.

Every workflow must have exactly one "default" status. You can make a status the default status by setting or updating the default flag on that status. This default status cannot be deleted.

### `POST /orgs/{org_id}/workflows` — Create a workflow

- **operationId:** `createWorkflow`
- **Domínio(s):** Workflows in Asset Inventory/Asset Manager

Create a new, empty workflow in an organization.

<details>
<summary><strong>Parâmetros</strong> (1)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |

</details>

<details>
<summary><strong>Request body (payload)</strong></summary>

The data required to create a workflow.

**Body obrigatório.**

**Content-Type:** `application/vnd.api+json`

**Schema:** `CreateWorkflowPayload`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | object | ✅ | The data associated with the resource. |
| `data.type` | string | ✅ | The classification of the object (`"workflows"`). Ex.: `"workflows"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.name` | string | ✅ | The name of the workflow. Names are case-insensitive and must be unique. Ex.: `"My first Workflow"` |
| `data.attributes.description` | string |  | The description of the workflow. Ex.: `"Description of My first Workflow"` |
| `data.attributes.locked` | boolean |  | Indicates that this workflow cannot be deleted by the user. Default: `False` Ex.: `false` |
| `data.attributes.api_name` | string |  | The API name of the workflow that is unique within the org, uneditable after creation, and must satisfy the following restrictions: - No uppercase letters - No whitespace (use `"_"` to separate words) - No special characters  Note: upon successful workflow creation a `"__c"` is appended to the provided api_name  Ex: my_api_name  -->  my_api_name__c Default: `None` Ex.: `"my_workflow_api_name__c"` |

</details>

<details>
<summary><strong>Respostas</strong> (7)</summary>

<details>
<summary>`201` — Created.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `SingleWorkflowResponse`

_Apenas campos que diferem do request body. 6 campo(s) idênticos omitidos._

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data.id` | string | ✅ | The ID of the workflow. Ex.: `"768cd1bc-d8af-4429-9aa0-8a4b477de42b"` |
| `data.attributes.name` | string |  | The name of the workflow. Names are case-insensitive and must be unique. Ex.: `"My first Workflow"` |
| `data.attributes.created_at` | string |  | The date the workflow was created. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.attributes.updated_at` | string |  | The date the workflow was updated. Ex.: `"2019-03-18T22:02:05Z"` |
| `data.attributes.system` | boolean |  | Indicates that this workflow cannot be modified by the user. Default: `False` Ex.: `false` |

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
