---
id: endpoint-post-orgs-org-id-projects-project-id-issues-createissue
title: "Issues: Create an issue"
tags: [endpoint, issues]
source: openapi.json (HighBond API v1.1.0)
---

## Issues

An issue is a problem, control gap, or exception that has been identified within a project. Adding an issue involves recording basic information about the issue and assigning
the issue to an owner. Issues may also be known as deficiencies, findings, or another customized term.

> **Note —**
Only issues in projects that have an `"active"` state can be accessed using the API.

Learn more about issues.

### `POST /orgs/{org_id}/projects/{project_id}/issues` — Create an issue

- **operationId:** `createIssue`
- **Domínio(s):** Issues

Create a new issue in an existing project.

Limitations:
* There can be a maximum of 8000 issues per project.
* You cannot create an issue directly under individual objectives, risks, controls, walkthroughs, test plans, or testing rounds. Issues can only be created under a project.
* Issues created under a project do not display as part of assurance features in HighBond.
* Specifying a person's name or email in the following fields does not automatically notify them via email: `owner`, `project_owner`, `executive_owner`.

<details>
<summary><strong>Parâmetros</strong> (3)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `project_id` | path | ✅ | integer | The ID of the project. Ex.: `1` |
| `fields[issues]` | query |  | string | Requesting the API to return only the specified fields. For more information, see Making requests Ex.: `title,description,creator_name,created_at,updated_at,position,owner,recommendation,deficiency_type,severity,published,identified_at,reference,reference_prefix,risk,scope,escalation,cause,effect,cost_impact,executive_summary,executive_owner,project_owner,closed,remediation_status,remediation_plan,remediation_date,actual_remediation_date,retest_deadline_date,actual_retest_date,retesting_results_overview,custom_attributes,project,entities,target,owner_user,executive_owner_user,project_owner_user,creator_user` |

</details>

<details>
<summary><strong>Request body (payload)</strong></summary>

The data required to create an issue.

**Body obrigatório.**

**Content-Type:** `application/vnd.api+json`

**Schema:** `CreateIssueRequest`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | object | ✅ | The data associated with the resource. |
| `data.type` | string | ✅ | The classification of the object (`"issues"`). Ex.: `"issues"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.description` | string | ✅ | A detailed description of the issue. Ex.: `"<h1>Description heading</h1><p>Issue description.</p>"` |
| `data.attributes.owner` | string | ✅ | The person responsible for the issue. Specifying a person's name or email does not automatically send them an email notification about the issue. This field becomes required if the `owner_user` relationship is not provided. Ex.: `"Payam Moghaddam"` |
| `data.attributes.deficiency_type` | string | ✅ | A user configurable classification of the issue. The options available depend on the configuration of the project type. Ex.: `"Deficiency"` |
| `data.attributes.recommendation` | string |  | A detailed description of the recommended actions to be taken based on the issue. Ex.: `"<h1>Issue recommendation heading</h1><p>Recommendation description.</p>"` |
| `data.attributes.title` | string |  | The title of the issue. Ex.: `"Title of issue"` |
| `data.attributes.severity` | string |  | A user configurable label that specifies the intensity of the issue. The options available depend on the configuration of the project type. Ex.: `"High"` |
| `data.attributes.published` | boolean |  | Specifies whether the issue is visible to all users (`true`), or hidden from users assigned the Contributor Tester, Contributor User, Oversight Executive, and Oversight Reviewer roles (`false`). An issue must be published to display in other related HighBond apps, such as Strategy. The default is `false`. Ex.: `true` |
| `data.attributes.identified_at` | string |  | The timestamp specifying when the issue was identified. The default is the current date and time. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.attributes.reference` | string |  | The ID of the issue. Ex.: `"ISS-01"` |
| `data.attributes.risk` | string |  | A detailed description of the risk or the impact the issue will have. Ex.: `"<h1>Risk heading</h1><p>Risk or impact description.</p>"` |
| `data.attributes.scope` | string |  | A user configurable label that specifies the extent to which the issue affects the organization. The options available depend on the configuration of the project type. Ex.: `"Local"` |
| `data.attributes.escalation` | string |  | A user configurable label that specifies the person, department, or organizational body that the issue should be brought to. The options available depend on the configuration of the project type. Ex.: `"Owner"` |
| `data.attributes.cause` | string |  | A detailed description of what caused the issue to occur. Ex.: `"<h1>Issue cause heading</h1><p>Issue cause description.</p>"` |
| `data.attributes.effect` | string |  | A detailed description of the effect the issue will have on the organization. Ex.: `"<h1>Issue effect heading</h1><p>Issue effect description.</p>"` |
| `data.attributes.cost_impact` | number |  | The estimated, or actual, monetary cost associated with the issue. Ex.: `4.2` |
| `data.attributes.executive_summary` | string |  | A high level overview of the issue that typically summarizes information from other related fields, such as risk/impact, cause, and effect. Ex.: `"<h1>Executive summary heading</h1><p>Executive summary description.</p>"` |
| `data.attributes.executive_owner` | string |  | The executive owner of the issue. Specifying a person's name or email does not automatically send them an email notification about the issue. Ex.: `"Max Powell"` |
| `data.attributes.project_owner` | string |  | The project owner of the issue. Specifying a person's name or email does not automatically send them an email notification about the issue. Ex.: `"Chris Rockwell"` |
| `data.attributes.closed` | boolean |  | Specifies whether the overall status of the issue is in an open (`false`) or closed state (`true`). The default is `false`. Ex.: `false` |
| `data.attributes.remediation_status` | string |  | A user configurable issue remediation status. The options available depend on the configuration of the project type. Ex.: `"Opened"` |
| `data.attributes.remediation_plan` | string |  | A detailed description of the remediation plan. Ex.: `"<h1>Remediation plan heading</h1><p>Remediation plan description.</p>"` |
| `data.attributes.remediation_date` | string |  | Specifies a deadline for the issue to be remediated by. Ex.: `"2019-02-09"` |
| `data.attributes.actual_remediation_date` | string |  | Specifies the date the issue was actually remediated. Ex.: `"2019-02-09"` |
| `data.attributes.retest_deadline_date` | string |  | Specifies a deadline for the issue to be retested by. Ex.: `"2019-02-09"` |
| `data.attributes.actual_retest_date` | string |  | Specifies the actual date when the issue was retested. Ex.: `"2019-02-09"` |
| `data.attributes.retesting_results_overview` | string |  | A detailed description that specifies whether or not the issue has truly been remediated. Ex.: `"<h1>Retesting results overview heading</h1><p>Retesting results overview description.</p>"` |
| `data.attributes.position` | integer |  | The value that determines the order in which it is displayed in the index action. `position` must be a value between `1` and `2147483647`. Ex.: `1` |
| `data.attributes.custom_attributes` | array[object] |  | An array of custom attributes defined by the user that are available on this object. |
| `data.attributes.custom_attributes.id` | string |  | The ID of the custom attribute that this custom attribute value is for. Optional if term is included. Ex.: `"42"` |
| `data.attributes.custom_attributes.term` | string |  | The user defined term used to identify the custom attribute. Optional if id is included. Ex.: `"Custom Issue Attribute"` |
| `data.attributes.custom_attributes.value` | array[string] |  | The value or values (for multiselect) to set this custom attribute to. Ex.: `["Custom Select Option Text"]` |
| `data.relationships` | object |  | The relationships associated with the resource. |
| `data.relationships.target` | object |  | Specifies the resource that the issue is associated with. If a target field wasn't passed, then an Issue will be linked to a Project by default. |
| `data.relationships.target.data` | object |  | The data associated with an issue. |
| `data.relationships.target.data.id` | string |  | The ID of the resource. Ex.: `"1"` |
| `data.relationships.target.data.type` | string |  | The classification of the object.  A target can have one of the following types: `"projects`", `"narratives`", `"objectives`", `"walkthrough_summaries`", `"project_plannings`", `"walkthroughs`", `"control_tests`", `"control_test_plans`", `"project_results`", `"project_files`", `"risk_control_matrices`", `"testing_rounds`", `"risks`", `"controls`" Ex.: `"objectives"` |
| `data.relationships.owner_user` | object |  | Specifies the user responsible for the issue. A value in this field will override any values provided in the `owner` attribute. This field becomes required if the `owner` attribute is not provided. |
| `data.relationships.owner_user.data` | object | ✅ | The data associated with the resource. |
| `data.relationships.owner_user.data.id` | string | ✅ | The unique identifier (UID) of the user. For more information on obtaining this value, see Making requests. Ex.: `"3NQ6XzAUxqJMnAQ7n4KF"` |
| `data.relationships.owner_user.data.type` | string | ✅ | The classification of the object (`"users"`). Ex.: `"users"` |

</details>

<details>
<summary><strong>Respostas</strong> (7)</summary>

<details>
<summary>`201` — Created.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `GetIssueResponse`

_Apenas campos que diferem do request body. 39 campo(s) idênticos omitidos._

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data.id` | string | ✅ | The ID of the requested resource. Ex.: `"1"` |
| `data.attributes.description` | string |  | A detailed description of the issue. Ex.: `"<h1>Description heading</h1><p>Issue description.</p>"` |
| `data.attributes.creator_name` | string |  | The name of the person that created the issue. The default is the name of the current user. Ex.: `"Payam Moghaddam"` |
| `data.attributes.created_at` | string |  | The timestamp identifying when the issue was created. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.attributes.updated_at` | string |  | The timestamp identifying when the issue was last updated. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.attributes.owner` | string |  | The person responsible for the issue. Specifying a person's name or email does not automatically send them an email notification about the issue. This field becomes required if the `owner_user` relationship is not provided. Ex.: `"Payam Moghaddam"` |
| `data.attributes.deficiency_type` | string |  | A user configurable classification of the issue. The options available depend on the configuration of the project type. Ex.: `"Deficiency"` |
| `data.attributes.reference_prefix` | string |  | Specifies the ID if the issue is associated with an objective. Ex.: `"3"` |
| `data.relationships` | object | ✅ | The relationships associated with the resource. |
| `data.relationships.project` | object |  | Specifies the project that the issue is associated with. |
| `data.relationships.project.data` | object |  | The data associated with a project. |
| `data.relationships.project.data.id` | string |  | The ID of the project. Ex.: `"1"` |
| `data.relationships.project.data.type` | string |  | The classification of the object (`"projects"`). Ex.: `"projects"` |
| `data.relationships.entities` | object |  | Each issue has an associated issue entities. |
| `data.relationships.entities.data` | array[object] | ✅ | The data associated with the resource. Ex.: `[]` |
| `data.relationships.entities.data.id` | string | ✅ | The ID of the entity. Ex.: `"1"` |
| `data.relationships.entities.data.type` | string | ✅ | The classification of the object (`"entities"`). Ex.: `"entities"` |
| `data.relationships.executive_owner_user` | object |  | Specifies the executive owner responsible for the issue. |
| `data.relationships.executive_owner_user.data` | object | ✅ | The data associated with the resource. |
| `data.relationships.executive_owner_user.data.id` | string | ✅ | The unique identifier (UID) of the user. For more information on obtaining this value, see Making requests. Ex.: `"3NQ6XzAUxqJMnAQ7n4KF"` |
| `data.relationships.executive_owner_user.data.type` | string | ✅ | The classification of the object (`"users"`). Ex.: `"users"` |
| `data.relationships.project_owner_user` | object |  | Specifies the project owner responsible for the issue. |
| `data.relationships.project_owner_user.data` | object | ✅ | The data associated with the resource. |
| `data.relationships.project_owner_user.data.id` | string | ✅ | The unique identifier (UID) of the user. For more information on obtaining this value, see Making requests. Ex.: `"3NQ6XzAUxqJMnAQ7n4KF"` |
| `data.relationships.project_owner_user.data.type` | string | ✅ | The classification of the object (`"users"`). Ex.: `"users"` |
| `data.relationships.creator_user` | object |  | Specifies the user that created the issue. |
| `data.relationships.creator_user.data` | object | ✅ | The data associated with the resource. |
| `data.relationships.creator_user.data.id` | string | ✅ | The unique identifier (UID) of the user. For more information on obtaining this value, see Making requests. Ex.: `"3NQ6XzAUxqJMnAQ7n4KF"` |
| `data.relationships.creator_user.data.type` | string | ✅ | The classification of the object (`"users"`). Ex.: `"users"` |
| `data.relationships.objective` | object |  | Specifies the objective that the issue is associated with |
| `data.relationships.objective.data` | object | ✅ | The data associated with the resource. |
| `data.relationships.objective.data.id` | string | ✅ | The ID of the resource. Ex.: `"1"` |
| `data.relationships.objective.data.type` | string | ✅ | The classification of the object (`"objectives"`). Ex.: `"objectives"` |

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
