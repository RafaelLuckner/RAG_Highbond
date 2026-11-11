---
id: endpoint-delete-orgs-org-id-projects-id-deleteproject
title: "Projects: Delete a project"
tags: [endpoint, projects]
source: openapi.json (HighBond API v1.1.0)
---

## Projects

A project is a management system that allows you to define objectives, risks, and controls, perform tests, and compile information for reporting purposes. Projects may also
be known as audits, compliance assessments, risk assessments, or another customized term.

Each project has a default system classification, called a "state". A project can have one of the following states:
* `"active"`— projects that are currently in progress
* `"archive"`— projects that are inactive and have been moved to the Project Library
* `"delete"`— previously deleted projects that are stored in the Project Library for 30 days, and then permanently deleted automatically after 30 days

Projects in a `"framework"` state cannot be accessed using the API.

Learn more about projects.

### `DELETE /orgs/{org_id}/projects/{id}` — Delete a project

- **operationId:** `deleteProject`
- **Domínio(s):** Projects

Delete a project that you no longer require. Projects in the state `"active"`, `"archived"` or `"delete"` can be deleted.

You can temporarily or permanently delete a project:
* By default, projects are temporarily deleted. The project is moved to a `"delete"` state and stored in the Project Library for 30 days. Project
Admins receive an email notification when a project has been temporarily deleted. After 30 days, the project is permanently deleted automatically.
* To request a permanent deletion of a project, you must specify `"delete"` using the `permanent` parameter. Project Admins do not receive
an email notification when a project is permanently deleted.

> **Caution —**
Once a project is permanently deleted, you cannot access or restore the project.

For more information, see Deleting
and restoring projects.

<details>
<summary><strong>Parâmetros</strong> (3)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `id` | path | ✅ | string | The ID of the requested resource. Ex.: `9999` |
| `permanent` | query |  | string | Specifies that the project and all associated data should be permanently deleted. Valores: `delete` |

</details>

<details>
<summary><strong>Respostas</strong> (8)</summary>

<details>
<summary>`200` — OK. [The project is temporarily deleted.]</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `GetProjectResponse`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | object | ✅ | The data associated with the resource. |
| `data.id` | string | ✅ | The ID of the requested resource. Ex.: `"1"` |
| `data.type` | string | ✅ | The classification of the object (`"projects"`). Ex.: `"projects"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.name` | string |  | The name of the project. Ex.: `"Example Application"` |
| `data.attributes.state` | string |  | A default system classification. A project can have one of the following states: `"active"`, `"archive"`, `"delete"`. When you create a project, the project is created in an `"active"` state. Projects with the state `"active"` or `"delete"` can be updated. Projects in the state `"active"`, `"archive"`, or `"delete"` can be deleted. Projects in the state `"framework"` cannot be accessed using the API. For more information, see Configuring project statuses. Ex.: `"active"` |
| `data.attributes.status` | string |  | A user configurable classification. Each project can have one status. Default statuses are: "draft", "proposed", "active", "completed". The default status is "active", if not specified. For more information, see Configuring project statuses. Ex.: `"active"` |
| `data.attributes.created_at` | string |  | The timestamp specifying when the project was created. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.attributes.updated_at` | string |  | The timestamp specifying when the project's settings were updated. Ex.: `"2019-03-18T22:02:05Z"` |
| `data.attributes.description` | string |  | A detailed description of the project. Ex.: `"Project description."` |
| `data.attributes.background` | string |  | The contextual circumstances of the project. Ex.: `"<h1>Heading</h1><p>Project background description.</p>"` |
| `data.attributes.budget` | integer |  | The budgeted hours that have been allocated for the project. `budget` must be a value between `0` and `2147483647`. Ex.: `1` |
| `data.attributes.certification` | boolean |  | Specifies if the Certifications feature has been enabled (`true`) or disabled (`false`) for the project. The default is `false`. You must be a System Admin with a Professional subscription to configure this field. For more information, see Creating certification programs. Ex.: `false` |
| `data.attributes.control_performance` | boolean |  | Specifies if the Control Performance feature has been enabled (`true`) or disabled (`false`) for the project. The default is `false`. You must be a System Admin with a Professional subscription to configure this field. For more information, see Scheduling Control Performance. Ex.: `false` |
| `data.attributes.risk_assurance` | boolean |  | Specifies if the Risk Assurance feature has been enabled (`true`) or disabled (`false`) for the project. The default is `false`. You must be a System Admin with a Professional subscription to configure this field. For more information, see Getting started with assurance for risk. Ex.: `false` |
| `data.attributes.management_response` | string |  | A description of management's response to the overall rating of the project. Ex.: `"<h1>Heading</h1><p>Management response description.</p>"` |
| `data.attributes.max_sample_size` | integer |  | The total sample size, split among testing rounds, defined in the project. The default is `0`. This field depends on `project_type`, which is dependent on workflow. For Workplan workflow projects, `max_sample_size` must be `0`. For Internal Control workflow projects, `max_sample_size` must be a value between `0` and `2147483647`. For more information, see Workflows and project types and Executing procedures and testing controls. Ex.: `25` |
| `data.attributes.number_of_testing_rounds` | integer |  | The number of testing rounds performed in the project. The default is `0`. This field depends on `project_type`, which is dependent on workflow. For Workplan workflow projects, `number_of_testing_rounds` must be `0`. For Internal Control workflow projects, `number_of_testing_rounds` must be one of the following values: `0`,`1`,`2`, or `4`. The number of testing rounds can only be set on create. This field cannot be updated. For more information, see Workflows and project types and Executing procedures and testing controls. Ex.: `4` |
| `data.attributes.opinion` | string |  | A user configurable final rating of the project outcome. Ex.: `"Excellent"` |
| `data.attributes.opinion_description` | string |  | A formal statement about the project outcome, including remarks or recommendations. Ex.: `"<h1>Heading</h1><p>Project opinion description.</p>"` |
| `data.attributes.purpose` | string |  | The intended results, aims, or goals of the project. Ex.: `"<h1>Heading</h1><p>Project purpose description.</p>"` |
| `data.attributes.scope` | string |  | What is, and is not, covered by this project. Ex.: `"<h1>Heading</h1><p>Project scope description.</p>"` |
| `data.attributes.start_date` | string |  | The date specifying when the project is scheduled to begin. Ex.: `"2019-02-01"` |
| `data.attributes.target_date` | string |  | The date specifying when the project is scheduled to be completed. Ex.: `"2019-04-01"` |
| `data.attributes.tag_list` | array[string] |  | A comma separated list of tags associated with the project. For more information, see Tagging projects. Ex.: `["tag 1", "tag 2", "tag 3"]` |
| `data.attributes.position` | integer |  | Legacy field that was used to determine the order in which it is displayed in the index action. This field is no longer supported and will always return 0. Ex.: `0` |
| `data.attributes.header_alert_enabled` | boolean |  | Specifies if the Header Alert feature has been enabled (`true`) or disabled (`false`) for the project. The default is `false`. Some of the projects have highly sensitive information. That data has restricted access and more controls apply to it. Ex.: `false` |
| `data.attributes.header_alert_text` | string |  | Custom message displayed at the top (header) of each project with sensitive data. Ex.: `"This Project is not authorized for sensitive data"` |
| `data.attributes.custom_attributes` | array[object] |  | An array of custom attributes defined on the project type used by this project. Learn more about project types. Make a PATCH request to modify the value of a custom attribute. Custom attributes can't be updated at the same time as the project type because the project type determines which custom attributes apply to the project and its resources. Custom attributes are not available on creation during a POST request, because the custom attributes are defined by the project type that is set when the project is created. |
| `data.attributes.custom_attributes.id` | string |  | The ID of this custom attribute. Optional if term is included. Ex.: `"42"` |
| `data.attributes.custom_attributes.term` | string |  | The user defined term used to identify this custom attribute. Optional if id is included. Ex.: `"Custom Project Planning Attribute"` |
| `data.attributes.custom_attributes.value` | array[string] |  | The value or values (for multiselect) for this custom attribute. Ex.: `["Custom Select Option Text"]` |
| `data.attributes.risk_assurance_data` | object |  | Fields that determines assurance values. Assurance is an expression of confidence that risk is effectively mitigated. Returns `null` if Risk Assurance feature is disabled. |
| `data.attributes.risk_assurance_data.inherent_risk` | number |  | The risk that an activity would pose if no controls or other mitigating factors were in place. Can also be referred to as the gross risk, or risks before controls, and can act as the baseline for your organization's risk tolerance or appetite. Ex.: `1.1` |
| `data.attributes.risk_assurance_data.residual_risk` | number |  | The risk that remains after controls are taken into account. Can also be referred to as the net risk or risk after controls. Ex.: `1.1` |
| `data.attributes.risk_assurance_data.assurance` | number |  | The level of assurance that the controls in place effectively mitigate risk to the business. Ex.: `0` |
| `data.attributes.time_spent` | number |  | The total time spent on the project. Ex.: `3.5` |
| `data.attributes.progress` | number |  | Project progress is calculated using the following formula: Sum of scores received per phase / Maximum score across all phases and objectives x 100. Ex.: `6.5` |
| `data.attributes.planned_start_date` | string |  | Planned start date Ex.: `"2019-02-09"` |
| `data.attributes.planned_end_date` | string |  | Planned end date. Ex.: `"2019-02-10"` |
| `data.attributes.actual_start_date` | string |  | Actual start date. Ex.: `"2019-02-09"` |
| `data.attributes.actual_end_date` | string |  | Actual end date. Ex.: `"2019-02-10"` |
| `data.attributes.actual_milestone_date` | string |  | Actual milestone date. Ex.: `"2019-02-10"` |
| `data.attributes.planned_milestone_date` | string |  | Planned milestone date. Ex.: `"2019-02-09"` |
| `data.relationships` | object | ✅ | The relationships associated with the resource. |
| `data.relationships.project_type` | object | ✅ | Each project has an associated project type. Project types define the structure of a project, including the terminology used in the project. The project type defines which workflow the project uses and which custom attributes are available on the project. Because of this dependency the project type can't be updated at the same time as the custom attributes. |
| `data.relationships.project_type.data` | object | ✅ | The data associated with the resource. |
| `data.relationships.project_type.data.id` | string | ✅ | The ID of the project type. Ex.: `"1"` |
| `data.relationships.project_type.data.type` | string | ✅ | The classification of the object (`"project_types"`). Ex.: `"project_types"` |
| `data.relationships.entities` | object |  | Each project has an associated project entities. |
| `data.relationships.entities.data` | array[object] | ✅ | The data associated with the resource. Ex.: `[]` |
| `data.relationships.entities.data.id` | string | ✅ | The ID of the entity. Ex.: `"1"` |
| `data.relationships.entities.data.type` | string | ✅ | The classification of the object (`"entities"`). Ex.: `"entities"` |
| `meta` | object |  |  |
| `meta.status_translations` | object | ✅ | Translations, or customized values for the project status states. |
| `meta.status_translations.draft` | string |  | Term to use when a project is in a draft state. Ex.: `"Draft"` |
| `meta.status_translations.proposed` | string |  | Term to use when a project is in a proposed state. Ex.: `"Proposed"` |
| `meta.status_translations.active` | string |  | Term to use when a project is in an active state. Ex.: `"Active"` |
| `meta.status_translations.completed` | string |  | Term to use when a project has been completed. Ex.: `"Completed"` |

</details>

- `202` — Accepted. [The project is queued for permanent deletion.]

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
