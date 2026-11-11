---
id: endpoint-get-orgs-org-id-time-entries-id-gettimeentry
title: "Time entries: Get information about a time entry"
tags: [endpoint, time-entries]
source: openapi.json (HighBond API v1.1.0)
---

## Time entries

Use time entries to record time spent on projects, or on other tasks, for reporting purposes.

Learn more about time entries.

### `GET /orgs/{org_id}/time_entries/{id}` — Get information about a time entry

- **operationId:** `getTimeEntry`
- **Domínio(s):** Time entries

Get information about a time entry.

<details>
<summary><strong>Parâmetros</strong> (16)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `id` | path | ✅ | string | The ID of the requested resource. Ex.: `9999` |
| `include` | query |  | string | Requesting the API to return related resources. For more information, see Making requests Ex.: `target,project,objective,category,assigned_user` |
| `fields[time_entries]` | query |  | string | Requesting the API to return only the specified fields. For more information, see Making requests Ex.: `date,description,time,client_delay,created_at,updated_at,position,project,objective,target` |
| `fields[projects]` | query |  | string | Requesting the API to return only the specified fields. For more information, see Making requests Ex.: `name,state,status,created_at,updated_at,description,background,budget,position,header_alert_enabled,header_alert_text,certification,control_performance,risk_assurance,management_response,max_sample_size,number_of_testing_rounds,opinion,opinion_description,purpose,scope,start_date,target_date,tag_list,project_type,entities,collaborators,risk_assurance_data,collaborator_groups,time_spent,progress,planned_start_date,actual_start_date,planned_end_date,actual_end_date,planned_milestone_date,actual_milestone_date` |
| `fields[controls]` | query |  | string | Requesting the API to return only the specified fields. For more information, see Making requests Ex.: `title,description,control_id,owner,frequency,control_type,prevent_detect,method,status,position,created_at,updated_at,custom_attributes,objective,walkthrough,control_test_plan,control_tests,mitigations,owner_user,entities,framework_origin` |
| `fields[control_tests]` | query |  | string | Requesting the API to return only the specified fields. For more information, see Making requests Ex.: `assignee_name,testing_round_number,not_applicable,sample_size,testing_results,testing_conclusion,testing_conclusion_status,created_at,updated_at,control,assigned_user,actual_milestone_date,planned_milestone_date,preparer_signoff,detail_reviewer_signoff,general_reviewer_signoff,supplemental_reviewer,specialty_reviewer` |
| `fields[issues]` | query |  | string | Requesting the API to return only the specified fields. For more information, see Making requests Ex.: `title,description,creator_name,created_at,updated_at,position,owner,recommendation,deficiency_type,severity,published,identified_at,reference,reference_prefix,risk,scope,escalation,cause,effect,cost_impact,executive_summary,executive_owner,project_owner,closed,remediation_status,remediation_plan,remediation_date,actual_remediation_date,retest_deadline_date,actual_retest_date,retesting_results_overview,custom_attributes,project,entities,target,owner_user,executive_owner_user,project_owner_user,creator_user` |
| `fields[narratives]` | query |  | string | Requesting the API to return only the specified fields. For more information, see Making requests Ex.: `title,description,created_at,updated_at,objective,framework_origin` |
| `fields[objectives]` | query |  | string | Requesting the API to return only the specified fields. For more information, see Making requests Ex.: `title,description,reference,division_department,owner,executive_owner,created_at,updated_at,project,assigned_user,custom_attributes,position,risk_control_matrix_id,walkthrough_summary_id,testing_round_1_id,testing_round_2_id,testing_round_3_id,testing_round_4_id,entities,framework,framework_origin,risk_assurance_data,planned_start_date,actual_start_date,planned_end_date,actual_end_date,planned_milestone_date,actual_milestone_date` |
| `fields[risks]` | query |  | string | Requesting the API to return only the specified fields. For more information, see Making requests Ex.: `title,description,risk_id,owner,position,impact,likelihood,custom_attributes,custom_factors,created_at,updated_at,objective,mitigations,owner_user,entities,framework_origin,risk_assurance_data` |
| `fields[accounts]` | query |  | string | Requesting the API to return only the specified fields. For more information, see Making requests Ex.: `fy_end_day,fy_end_month` |
| `fields[control_test_plans]` | query |  | string | Requesting the API to return only the specified fields. For more information, see Making requests Ex.: `title,test_steps,sanitized_description,reference_prefix,self_link,update_linked_control_test_plans_link,preparer_signoff,detail_reviewer_signoff,general_reviewer_signoff,supplemental_reviewer,specialty_reviewer,sample_size,test_method,audit_name,sanitized_test_steps` |
| `fields[project_files]` | query |  | string | Requesting the API to return only the specified fields. For more information, see Making requests Ex.: `name,reference,file_type,is_editable,is_signed_off` |
| `fields[testing_rounds]` | query |  | string | Requesting the API to return only the specified fields. For more information, see Making requests Ex.: `round_number,full_title` |
| `fields[walkthroughs]` | query |  | string | Requesting the API to return only the specified fields. For more information, see Making requests Ex.: `walkthrough,control_verified,original_updated_at,preparer_signoff,detail_reviewer_signoff,general_reviewer_signoff,supplemental_reviewer,specialty_reviewer,control_performance_enabled,control_performance_readonly,signed_off,readonly,locked,enabled,planned_milestone_date,actual_milestone_date` |

</details>

<details>
<summary><strong>Respostas</strong> (4)</summary>

<details>
<summary>`200` — OK.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `GetTimeEntryResponse`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | object | ✅ | The data associated with the resource. |
| `data.id` | string | ✅ | The ID of the requested resource. Ex.: `"1"` |
| `data.type` | string | ✅ | The classification of the object (`"time_entries"`). Ex.: `"time_entries"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.date` | string | ✅ | The date of the time entry. Ex.: `"2021-03-15"` |
| `data.attributes.time` | number |  | The time of the time entry. Ex.: `8` |
| `data.attributes.description` | string |  | A detailed description of the time entry. Ex.: `"TimeEntry description"` |
| `data.attributes.position` | integer |  | The value that determines the order in which it is displayed in the index action. `position` must be a value between `1` and `2147483647`. Ex.: `1` |
| `data.attributes.client_delay` | boolean |  | Specifies whether project was delayed. Default: `False` |
| `data.attributes.created_at` | string |  | The timestamp identifying when the time entry was created. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.attributes.updated_at` | string |  | The timestamp identifying when the time entry was last updated. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.relationships` | object | ✅ | The relationships associated with the resource. |
| `data.relationships.objective` | object |  | Time Entry can have an associated objective. Objectives are the organizing containers for the work done in a project or framework. |
| `data.relationships.objective.data` | object | ✅ | The data associated with the resource. |
| `data.relationships.objective.data.id` | string | ✅ | The ID of the objective. Ex.: `"1"` |
| `data.relationships.objective.data.type` | string | ✅ | The classification of the object (`"objectives"`). Ex.: `"objectives"` |
| `data.relationships.project` | object |  | Each time entry has an associated project or framework. Project/framework is a management system that allows you to define and compile information for reporting purposes. |
| `data.relationships.project.data` | object | ✅ | The data associated with the resource. |
| `data.relationships.project.data.id` | string | ✅ | The ID of the project. Ex.: `"1"` |
| `data.relationships.project.data.type` | string | ✅ | The classification of the object (`"projects"`). Ex.: `"projects"` |
| `data.relationships.project.links` | object | ✅ | Links associated with a project. |
| `data.relationships.project.links.ui` | string |  | URL of page providing user interface for project. Ex.: `"https://myorg.projects.highbond.com/audits/1/dashboard"` |
| `data.relationships.target` | object | ✅ | Specifies the resource that the time entry is associated with. |
| `data.relationships.target.data` | object | ✅ | The data associated with a time entry. |
| `data.relationships.target.data.id` | string |  | The ID of the resource. Ex.: `"1"` |
| `data.relationships.target.data.type` | string |  | The classification of the object.  A target can have one of the following types: `"projects`", `"narratives`", `"objectives`", `"walkthrough_summaries`", `"project_plannings`", `"walkthroughs`", `"control_tests`", `"control_test_plans`", `"project_results`", `"project_files`", `"risk_control_matrices`", `"testing_rounds`", `"risks`", `"controls`" Ex.: `"objectives"` |
| `data.relationships.target.links` | object | ✅ | Links associated with a target relationship. |
| `data.relationships.target.links.ui` | string |  | URL of page providing user interface for target resource. Ex.: `"https://myorg.projects.highbond.com/audits/1/dashboard"` |
| `data.relationships.category` | object |  | Time Entry can have a category, if target is NOT a project or project-related entity like Risk, Narrative, Control, etc. |
| `data.relationships.category.data` | object | ✅ | The data associated with the resource. |
| `data.relationships.category.data.id` | string | ✅ | The ID of the category. Ex.: `"1"` |
| `data.relationships.category.data.type` | string | ✅ | The classification of the object (`"time_entry_categories"`). Ex.: `"work_types"` |
| `data.relationships.assigned_user` | object |  | The person assigned to the time entry. Only the Professional Manager role user of the project is permitted to assign users, and only users of the Professional Manager, Professional User,  or Contributor Tester role within a project can be specified. The specified user has full read and write access to the time entry. The current user is assigned when the user is not specified on create action.  To return this field, you must specify the `fields[time_entry]=assigned_user` parameter in your request. For more information, see Making requests. |
| `data.relationships.assigned_user.data` | object | ✅ | The data associated with the resource. |
| `data.relationships.assigned_user.data.id` | string | ✅ | The unique identifier (UID) of the assigned user. For more information on obtaining this value, see Making requests. Ex.: `"3NQ6XzAUxqJMnAQ7n4KF"` |
| `data.relationships.assigned_user.data.type` | string | ✅ | The classification of the object (`"users"`). Ex.: `"users"` |

</details>

- `401` — Bad credentials.

- `403` — Forbidden.

- `404` — Not found.

</details>
