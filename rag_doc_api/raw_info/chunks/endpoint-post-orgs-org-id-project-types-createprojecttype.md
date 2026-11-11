---
id: endpoint-post-orgs-org-id-project-types-createprojecttype
title: "Project types: Create or copy a project type"
tags: [endpoint, project-types]
source: openapi.json (HighBond API v1.1.0)
---

## Project types

Project types define the structure of a project or framework, including the terminology used in the project or framework. Updates to project types apply to
all active projects, archived projects, temporarily deleted projects, and frameworks associated with the project type.

Each project type has an associated workflow: Workplan (`procedure`) or Internal Control (`control`). Workflows define the components available in a project
or framework.  The attributes `narrative_terms`, `control_test_terms`, and `test_plan_terms` are not available for a Workplan (`procedure`) workflow.

When creating a new project type, only the basic defining attributes are available. After creating the project type default customizable terms and toggles
are returned and available on PATCH requests for update.

### `POST /orgs/{org_id}/project_types` — Create or copy a project type

- **operationId:** `createProjectType`
- **Domínio(s):** Project types

Create or copy a new project type to define a customized project or framework structure.

Creating a project type:

When creating a new project type, only the basic defining attributes are available. After creating the project type default customizable terms and toggles
are returned and available on PATCH requests for update.

Copying a project type:

When copying an existing project type, you must define a `source_project_type_id` parameter in your request data, with its value being the ID of the
existing project type you want to copy. Do not include this if you wish to create a new project type. The `attributes` object must be included in the 
request data, however, it will be ignored when copying.

Limitations:
* There can be a maximum of 500 project types per HighBond instance.

<details>
<summary><strong>Parâmetros</strong> (2)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `fields[project_types]` | query |  | string | Requesting the API to return only the specified fields. For more information, see Making requests Ex.: `name,description,workflow,project_terms,certification_terms,control_terms,finding_terms,finding_retest_terms,finding_remediation_terms,control_test_terms,narrative_terms,objective_terms,planning_terms,results_terms,risk_terms,risk_control_matrix_terms,test_plan_terms,process_walkthrough_terms,walkthrough_terms,testing_round_terms,assigned_users` |

</details>

<details>
<summary><strong>Request body (payload)</strong></summary>

The data required to create a project type.

**Body obrigatório.**

**Content-Type:** `application/vnd.api+json`

**Schema:** `CreateProjectTypeRequest`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | object | ✅ | The data associated with the resource. |
| `data.type` | string | ✅ | The classification of the object (`"project_types"`). Ex.: `"project_types"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.name` | string | ✅ | The name of the project type. Ex.: `"Project type name"` |
| `data.attributes.description` | string |  | A detailed description of the project type. Ex.: `"Project type description."` |
| `data.attributes.workflow` | string | ✅ | The type of workflow associated with the project type. The workflow can be Workplan (`procedure`) or Internal Control (`control`).  `procedure` workflows are appropriate for straight-forward projects and frameworks, which consist of a set of steps or procedures that the assurance team will execute, and the documentation of the outcome of each step. The attributes `narrative_terms`, `control_test_terms`, and `test_plan_terms` are not available for this workflow.  `control` workflows are appropriate for more complex types of projects and frameworks, where narratives are defined, walkthroughs are performed to verify control design, and tests are performed to verify the operating effectiveness of controls.  For more information, see Workflows and project types. Ex.: `"control"` |
| `data.attributes.enable_creating_projects` | boolean | ✅ | Specifies if users with the appropriate permissions can create new projects and frameworks using this project type (`true`) or if they cannot (`false`).  Typically, you specify `true` when you have finalized your project type settings and you are ready for others to use the project type. If you want the project type to remain in draft mode, and prevent others from using it, specify `false`. Default: `True` Ex.: `true` |
| `data.source_project_type_id` | string |  | The ID of the resource to copy. Ex.: `"1"` |

</details>

<details>
<summary><strong>Respostas</strong> (7)</summary>

<details>
<summary>`201` — Created.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `GetProjectTypeResponse`

_Apenas campos que diferem do request body. 4 campo(s) idênticos omitidos._

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data.id` | string | ✅ | The ID of the requested resource. Ex.: `1` |
| `data.attributes.name` | string |  | The name of the project type. Ex.: `"Project type name"` |
| `data.attributes.workflow` | string |  | The type of workflow associated with the project type. The workflow can be Workplan (`procedure`) or Internal Control (`control`).  `procedure` workflows are appropriate for straight-forward projects and frameworks, which consist of a set of steps or procedures that the assurance team will execute, and the documentation of the outcome of each step. The attributes `narrative_terms`, `control_test_terms`, and `test_plan_terms` are not available for this workflow.  `control` workflows are appropriate for more complex types of projects and frameworks, where narratives are defined, walkthroughs are performed to verify control design, and tests are performed to verify the operating effectiveness of controls.  For more information, see Workflows and project types. Ex.: `"control"` |
| `data.attributes.enable_creating_projects` | boolean |  | Specifies if users with the appropriate permissions can create new projects and frameworks using this project type (`true`) or if they cannot (`false`).  Typically, you specify `true` when you have finalized your project type settings and you are ready for others to use the project type. If you want the project type to remain in draft mode, and prevent others from using it, specify `false`. Default: `True` Ex.: `true` |
| `data.attributes.project_terms` | object |  | The terms of the project. |
| `data.attributes.project_terms.term_for_project` | string |  | The term for the project. Ex.: `"Project"` |
| `data.attributes.project_terms.term_for_risk_control_matrix` | string |  | The term for Risk Control Matrix. Ex.: `"Risk Control Matrix"` |
| `data.attributes.project_terms.term_for_risk_control_matrix_short` | string |  | The short term for Risk Control Matrix. Ex.: `"RCM"` |
| `data.attributes.project_terms.term_for_fieldwork` | string |  | The term for fieldwork. Ex.: `"Fieldwork"` |
| `data.attributes.project_terms.term_for_planned_start_date` | string |  | Planned start date. Ex.: `"Planned start date"` |
| `data.attributes.project_terms.term_for_planned_end_date` | string |  | Planned end date. Ex.: `"Planned end date"` |
| `data.attributes.project_terms.planned_dates_enabled` | boolean |  | Planned dates enabled. Ex.: `true` |
| `data.attributes.project_terms.term_for_actual_start_date` | string |  | Actual start date. Ex.: `"Actual start date"` |
| `data.attributes.project_terms.term_for_actual_end_date` | string |  | Actual end date. Ex.: `"Actual end date"` |
| `data.attributes.project_terms.actual_dates_enabled` | boolean |  | Actual dates enabled. Ex.: `true` |
| `data.attributes.project_terms.term_for_planned_milestone_date` | string |  | Planned milestone date. Ex.: `"Planned milestone date"` |
| `data.attributes.project_terms.planned_milestone_date_enabled` | boolean |  | Planned milestone date enabled. Ex.: `true` |
| `data.attributes.project_terms.term_for_actual_milestone_date` | string |  | Term for actual milestone date. Ex.: `"Actual milestone date"` |
| `data.attributes.project_terms.actual_milestone_date_enabled` | boolean |  | Actual milestone date enabled. Ex.: `true` |
| `data.attributes.objective_terms` | object |  | The terms of the objective. |
| `data.attributes.objective_terms.term_for_objective` | string |  | The term for Section. Ex.: `"Section"` |
| `data.attributes.objective_terms.term_for_objectives` | string |  | The term for Sections. Ex.: `"Sections"` |
| `data.attributes.objective_terms.term_for_objective_reference` | string |  | The term for Objective Reference Ex.: `"Reference"` |
| `data.attributes.objective_terms.term_for_objective_location` | string |  | The term for Objective Location Ex.: `"Division/Department"` |
| `data.attributes.objective_terms.term_for_objective_owner` | string |  | The term for Owner. Ex.: `"Owner"` |
| `data.attributes.objective_terms.term_for_objective_executive_owner` | string |  | The term for executive owner. Ex.: `"Executive Owner"` |
| `data.attributes.objective_terms.term_for_planned_start_date` | string |  | Planned start date. Ex.: `"Planned start date"` |
| `data.attributes.objective_terms.term_for_planned_end_date` | string |  | Planned end date. Ex.: `"Planned end date"` |
| `data.attributes.objective_terms.planned_dates_enabled` | boolean |  | Planned dates enabled. Ex.: `true` |
| `data.attributes.objective_terms.term_for_actual_start_date` | string |  | Actual start date. Ex.: `"Actual start date"` |
| `data.attributes.objective_terms.term_for_actual_end_date` | string |  | Actual end date. Ex.: `"Actual end date"` |
| `data.attributes.objective_terms.actual_dates_enabled` | boolean |  | Actual dates enabled. Ex.: `true` |
| `data.attributes.objective_terms.term_for_planned_milestone_date` | string |  | Planned milestone date. Ex.: `"Planned milestone date"` |
| `data.attributes.objective_terms.planned_milestone_date_enabled` | boolean |  | Planned milestone date enabled. Ex.: `true` |
| `data.attributes.objective_terms.term_for_actual_milestone_date` | string |  | Term for actual milestone date. Ex.: `"Actual milestone date"` |
| `data.attributes.objective_terms.actual_milestone_date_enabled` | boolean |  | Actual milestone date enabled. Ex.: `true` |
| `data.attributes.process_walkthrough_terms` | object |  | The terms of process walkthrough. |
| `data.attributes.process_walkthrough_terms.term_for_preparer_signoff` | string |  | Ex.: `"Preparer"` |
| `data.attributes.process_walkthrough_terms.term_for_detail_reviewer_signoff` | string |  | Ex.: `"Detail Reviewer"` |
| `data.attributes.process_walkthrough_terms.term_for_general_reviewer_signoff` | string |  | Ex.: `"General Reviewer"` |
| `data.attributes.process_walkthrough_terms.term_for_supplemental_reviewer_signoff` | string |  | Ex.: `"Supplemental Reviewer"` |
| `data.attributes.process_walkthrough_terms.term_for_specialty_reviewer_signoff` | string |  | Ex.: `"Specialty Reviewer"` |
| `data.attributes.process_walkthrough_terms.detail_reviewer_signoff_enabled` | boolean |  | Ex.: `true` |
| `data.attributes.process_walkthrough_terms.general_reviewer_signoff_enabled` | boolean |  | Ex.: `true` |
| `data.attributes.process_walkthrough_terms.supplemental_reviewer_signoff_enabled` | boolean |  | Ex.: `true` |
| `data.attributes.process_walkthrough_terms.specialty_reviewer_signoff_enabled` | boolean |  | Ex.: `true` |
| `data.attributes.walkthrough_terms` | object |  | The terms of walkthrough. In a Workplan workflow project, a walkthrough is called an execute procedure. |
| `data.attributes.walkthrough_terms.term_for_walkthrough` | string |  | The term for Walkthrough. Ex.: `"Walkthrough"` |
| `data.attributes.walkthrough_terms.term_for_walkthroughs` | string |  | The term for Walkthroughs. Ex.: `"walkthroughs"` |
| `data.attributes.walkthrough_terms.term_for_walkthrough_walkthrough` | string |  | The term for Walkthrough Results. Ex.: `"Walkthrough Terms"` |
| `data.attributes.walkthrough_terms.term_for_walkthrough_control_verified` | string |  | The term for is the Control designed appropriately. Ex.: `"Is my control designed appropriately?"` |
| `data.attributes.walkthrough_terms.control_verified_values_true` | string |  | The term choices for Control Designed Appropriately. The exact values for this field (E.g. "Designed Appropriately" / "No Issues") depend on the configuration of the project type. Ex.: `"Designed Appropriately"` |
| `data.attributes.walkthrough_terms.control_verified_values_false` | string |  | The term choices for Control Design Failure. The exact values for this field (E.g. "Design Failure" / "Issue(s) Noted") depend on the configuration of the project type. Ex.: `"Designed Failure"` |
| `data.attributes.walkthrough_terms.walkthrough_enabled` | boolean |  | Whether the walkthrough terms are enabled Ex.: `true` |
| `data.attributes.walkthrough_terms.term_for_preparer_signoff` | string |  | Ex.: `"Preparer"` |
| `data.attributes.walkthrough_terms.term_for_detail_reviewer_signoff` | string |  | Ex.: `"Detail Reviewer"` |
| `data.attributes.walkthrough_terms.term_for_general_reviewer_signoff` | string |  | Ex.: `"General Reviewer"` |
| `data.attributes.walkthrough_terms.term_for_supplemental_reviewer_signoff` | string |  | Ex.: `"Supplemental Reviewer"` |
| `data.attributes.walkthrough_terms.term_for_specialty_reviewer_signoff` | string |  | Ex.: `"Specialty Reviewer"` |
| `data.attributes.walkthrough_terms.preparer_signoff_enabled` | boolean |  | Ex.: `true` |
| `data.attributes.walkthrough_terms.detail_reviewer_signoff_enabled` | boolean |  | Ex.: `true` |
| `data.attributes.walkthrough_terms.general_reviewer_signoff_enabled` | boolean |  | Ex.: `true` |
| `data.attributes.walkthrough_terms.supplemental_reviewer_signoff_enabled` | boolean |  | Ex.: `true` |
| `data.attributes.walkthrough_terms.specialty_reviewer_signoff_enabled` | boolean |  | Ex.: `true` |
| `data.attributes.walkthrough_terms.term_for_planned_milestone_date` | string |  | Planned milestone date. Ex.: `"Planned milestone date"` |
| `data.attributes.walkthrough_terms.planned_milestone_date_enabled` | boolean |  | Planned milestone date enabled. Ex.: `true` |
| `data.attributes.walkthrough_terms.term_for_actual_milestone_date` | string |  | Term for actual milestone date. Ex.: `"Actual milestone date"` |
| `data.attributes.walkthrough_terms.actual_milestone_date_enabled` | boolean |  | Actual milestone date enabled. Ex.: `true` |
| `data.attributes.control_terms` | object |  | The terms of control. |
| `data.attributes.control_terms.term_for_control` | string |  | The term for Control. Ex.: `"Control"` |
| `data.attributes.control_terms.term_for_controls` | string |  | The term for Control (plural). Ex.: `"Controls"` |
| `data.attributes.control_terms.term_for_control_id` | string |  | The term for Control Id. Ex.: `"Control ID"` |
| `data.attributes.control_terms.term_for_control_owner` | string |  | The term for Control Owner. Ex.: `"Control Owner"` |
| `data.attributes.control_terms.term_for_control_frequency` | string |  | The term for Control Frequency. Ex.: `"Frequency"` |
| `data.attributes.control_terms.term_for_control_control_type` | string |  | The term for Control Type. Ex.: `"Type"` |
| `data.attributes.control_terms.term_for_control_prevent_or_detect` | string |  | The term for Prevent or Detect. Ex.: `"Prevent or Detect?"` |
| `data.attributes.control_terms.term_for_control_method` | string |  | The term for Control Method. Ex.: `"Method"` |
| `data.attributes.control_terms.term_for_control_status` | string |  | The term for Control Status. Ex.: `"Status"` |
| `data.attributes.control_terms.control_prevent_or_detects` | array[string] |  | The term choices for Prevent or Detect. The options available depends on the configuration of the project type. Ex.: `["prevent", "detect", "n_a"]` |
| `data.attributes.control_terms.control_methods` | array[string] |  | The term choices for Method. The options available depends on the configuration of the project type. Ex.: `["Authorization", "Management Review", "Reconciliation"]` |
| `data.attributes.control_terms.control_states` | array[string] |  | The term choices for Control Status. The options available depends on the configuration of the project type. Ex.: `["Key Control", "Non Key Control", "Obsolete"]` |
| `data.attributes.control_terms.frequencies` | array[string] |  | The term choices for Control Frequency. The options available depends on the configuration of the project type. Ex.: `["Continuous", "Multiple Times Daily", "Daily"]` |
| `data.attributes.control_terms.control_types` | array[string] |  | The term choices for Control Type. The options available depends on the configuration of the project type. Ex.: `["Manual Control", "Application/System Control", "IT Dependent Manual Control"]` |
| `data.attributes.control_terms.frequency_enabled` | boolean |  | Whether frequency is enabled Ex.: `true` |
| `data.attributes.control_terms.type_enabled` | boolean |  | Whether control types are enabled Ex.: `true` |
| `data.attributes.control_terms.prevent_detect_enabled` | boolean |  | Whether control prevent or detect is enabled Ex.: `true` |
| `data.attributes.control_terms.control_method_enabled` | boolean |  | Whether control methods are enabled Ex.: `true` |
| `data.attributes.control_terms.control_status_enabled` | boolean |  | Whether control statuses are enabled Ex.: `true` |
| `data.attributes.risk_terms` | object |  | The terms of risks. |
| `data.attributes.risk_terms.term_for_risk` | string |  | The term for Risk. Ex.: `"Risk"` |
| `data.attributes.risk_terms.term_for_risk_id` | string |  | The term for Risk Id. Ex.: `"Risk ID"` |
| `data.attributes.risk_terms.term_for_risk_title` | string |  | The term for Risk Title. Ex.: `"Risk Title"` |
| `data.attributes.risk_terms.term_for_risk_description` | string |  | The term for Risk Description. Ex.: `"Risk Description"` |
| `data.attributes.risk_terms.term_for_risk_impact` | string |  | The term for Risk Impact. Ex.: `"Impact"` |
| `data.attributes.risk_terms.term_for_risk_likelihood` | string |  | The term for Risk Likelihood. Ex.: `"Likelihood"` |
| `data.attributes.risk_terms.risk_impacts` | array[string] |  | The options for Risk Impact. The options available depend on the configuration of the project type. Ex.: `["Low", "Medium", "High"]` |
| `data.attributes.risk_terms.risk_likelihoods` | array[string] |  | The options for Risk Likelihood. The options available depend on the configuration of the project type. Ex.: `["Low", "Medium", "High"]` |
| `data.attributes.risk_control_matrix_terms` | object |  | The terms of risk control matrix. |
| `data.attributes.risk_control_matrix_terms.term_for_preparer_signoff` | string |  | Ex.: `"Preparer"` |
| `data.attributes.risk_control_matrix_terms.term_for_detail_reviewer_signoff` | string |  | Ex.: `"Detail Reviewer"` |
| `data.attributes.risk_control_matrix_terms.term_for_general_reviewer_signoff` | string |  | Ex.: `"General Reviewer"` |
| `data.attributes.risk_control_matrix_terms.term_for_supplemental_reviewer_signoff` | string |  | Ex.: `"Supplemental Reviewer"` |
| `data.attributes.risk_control_matrix_terms.term_for_specialty_reviewer_signoff` | string |  | Ex.: `"Specialty Reviewer"` |
| `data.attributes.risk_control_matrix_terms.detail_reviewer_signoff_enabled` | boolean |  | Ex.: `true` |
| `data.attributes.risk_control_matrix_terms.general_reviewer_signoff_enabled` | boolean |  | Ex.: `true` |
| `data.attributes.risk_control_matrix_terms.supplemental_reviewer_signoff_enabled` | boolean |  | Ex.: `true` |
| `data.attributes.risk_control_matrix_terms.specialty_reviewer_signoff_enabled` | boolean |  | Ex.: `true` |
| `data.attributes.planning_terms` | object |  | The terms of planning. |
| `data.attributes.planning_terms.term_for_planning` | string |  | The term for Planning. Ex.: `"Planning"` |
| `data.attributes.planning_terms.term_for_planning_background` | string |  | The term for Planning background. Ex.: `"Background"` |
| `data.attributes.planning_terms.term_for_planning_scope` | string |  | The term for Planning scope. Ex.: `"Scope"` |
| `data.attributes.planning_terms.term_for_planning_purpose` | string |  | The term for Planning purpose. Ex.: `"Purpose"` |
| `data.attributes.planning_terms.term_for_planning_file` | string |  | The term for Planning file. Ex.: `"Planning File"` |
| `data.attributes.planning_terms.term_for_planning_files` | string |  | The term for Planning files. Ex.: `"Planning Files"` |
| `data.attributes.planning_terms.planning_enabled` | boolean |  | Whether planning is enabled Ex.: `true` |
| `data.attributes.planning_terms.term_for_preparer_signoff` | string |  | Ex.: `"Preparer"` |
| `data.attributes.planning_terms.term_for_detail_reviewer_signoff` | string |  | Ex.: `"Detail Reviewer"` |
| `data.attributes.planning_terms.term_for_general_reviewer_signoff` | string |  | Ex.: `"General Reviewer"` |
| `data.attributes.planning_terms.term_for_supplemental_reviewer_signoff` | string |  | Ex.: `"Supplemental Reviewer"` |
| `data.attributes.planning_terms.term_for_specialty_reviewer_signoff` | string |  | Ex.: `"Specialty Reviewer"` |
| `data.attributes.planning_terms.preparer_signoff_enabled` | boolean |  | Ex.: `true` |
| `data.attributes.planning_terms.detail_reviewer_signoff_enabled` | boolean |  | Ex.: `true` |
| `data.attributes.planning_terms.general_reviewer_signoff_enabled` | boolean |  | Ex.: `true` |
| `data.attributes.planning_terms.supplemental_reviewer_signoff_enabled` | boolean |  | Ex.: `true` |
| `data.attributes.planning_terms.specialty_reviewer_signoff_enabled` | boolean |  | Ex.: `true` |
| `data.attributes.planning_terms.term_for_planned_start_date` | string |  | Planned start date. Ex.: `"Planned start date"` |
| `data.attributes.planning_terms.term_for_planned_end_date` | string |  | Planned end date. Ex.: `"Planned end date"` |
| `data.attributes.planning_terms.planned_dates_enabled` | boolean |  | Planned dates enabled. Ex.: `true` |
| `data.attributes.planning_terms.term_for_actual_start_date` | string |  | Actual start date. Ex.: `"Actual start date"` |
| `data.attributes.planning_terms.term_for_actual_end_date` | string |  | Actual end date. Ex.: `"Actual end date"` |
| `data.attributes.planning_terms.actual_dates_enabled` | boolean |  | Actual dates enabled. Ex.: `true` |
| `data.attributes.planning_terms.term_for_planned_milestone_date` | string |  | Planned milestone date. Ex.: `"Planned milestone date"` |
| `data.attributes.planning_terms.planned_milestone_date_enabled` | boolean |  | Planned milestone date enabled. Ex.: `true` |
| `data.attributes.planning_terms.term_for_actual_milestone_date` | string |  | Term for actual milestone date. Ex.: `"Actual milestone date"` |
| `data.attributes.planning_terms.actual_milestone_date_enabled` | boolean |  | Actual milestone date enabled. Ex.: `true` |
| `data.attributes.results_terms` | object |  | The terms of results. |
| `data.attributes.results_terms.term_for_results` | string |  | The term for Results. Ex.: `"Results"` |
| `data.attributes.results_terms.term_for_results_conclusion` | string |  | The term for Results Conclusion. Ex.: `"Conclusion/Rating"` |
| `data.attributes.results_terms.term_for_results_management_response` | string |  | The term for Management Response. Ex.: `"Management Response"` |
| `data.attributes.results_terms.term_for_results_file` | string |  | The term for Result File. Ex.: `"Result File"` |
| `data.attributes.results_terms.term_for_results_files` | string |  | The term for Result Files. Ex.: `"Result Files"` |
| `data.attributes.results_terms.term_for_fieldwork_reports` | string |  | The term for Fieldwork Reports. Ex.: `"Fieldwork Reports"` |
| `data.attributes.results_terms.term_for_supporting_workpapers` | string |  | The term for Supporting Workpapers. Ex.: `"Supporting Workpapers"` |
| `data.attributes.results_terms.term_for_preparer_signoff` | string |  | Ex.: `"Preparer"` |
| `data.attributes.results_terms.term_for_detail_reviewer_signoff` | string |  | Ex.: `"Detail Reviewer"` |
| `data.attributes.results_terms.term_for_general_reviewer_signoff` | string |  | Ex.: `"General Reviewer"` |
| `data.attributes.results_terms.term_for_supplemental_reviewer_signoff` | string |  | Ex.: `"Supplemental Reviewer"` |
| `data.attributes.results_terms.term_for_specialty_reviewer_signoff` | string |  | Ex.: `"Specialty Reviewer"` |
| `data.attributes.results_terms.preparer_signoff_enabled` | boolean |  | Ex.: `true` |
| `data.attributes.results_terms.detail_reviewer_signoff_enabled` | boolean |  | Ex.: `true` |
| `data.attributes.results_terms.general_reviewer_signoff_enabled` | boolean |  | Ex.: `true` |
| `data.attributes.results_terms.supplemental_reviewer_signoff_enabled` | boolean |  | Ex.: `true` |
| `data.attributes.results_terms.specialty_reviewer_signoff_enabled` | boolean |  | Ex.: `true` |
| `data.attributes.results_terms.term_for_planned_start_date` | string |  | Planned start date. Ex.: `"Planned start date"` |
| `data.attributes.results_terms.term_for_planned_end_date` | string |  | Planned end date. Ex.: `"Planned end date"` |
| `data.attributes.results_terms.planned_dates_enabled` | boolean |  | Planned dates enabled. Ex.: `true` |
| `data.attributes.results_terms.term_for_actual_start_date` | string |  | Actual start date. Ex.: `"Actual start date"` |
| `data.attributes.results_terms.term_for_actual_end_date` | string |  | Actual end date. Ex.: `"Actual end date"` |
| `data.attributes.results_terms.actual_dates_enabled` | boolean |  | Actual dates enabled. Ex.: `true` |
| `data.attributes.results_terms.term_for_planned_milestone_date` | string |  | Planned milestone date. Ex.: `"Planned milestone date"` |
| `data.attributes.results_terms.planned_milestone_date_enabled` | boolean |  | Planned milestone date enabled. Ex.: `true` |
| `data.attributes.results_terms.term_for_actual_milestone_date` | string |  | Term for actual milestone date. Ex.: `"Actual milestone date"` |
| `data.attributes.results_terms.actual_milestone_date_enabled` | boolean |  | Actual milestone date enabled. Ex.: `true` |
| `data.attributes.results_terms.opinion_options` | array[string] |  | The options for Opinions. Ex.: `["Excellent", "Good", "Satisfactory", "Needs Improvement", "Unsatisfactory"]` |
| `data.attributes.finding_terms` | object |  | The terms of findings.  In a Workplan workflow project, a finding is called an action. |
| `data.attributes.finding_terms.term_for_finding` | string |  | The term for Issue. Ex.: `"Issue"` |
| `data.attributes.finding_terms.term_for_finding_risk_impact` | string |  | The term for Risk/Impact Ex.: `"Risk/Impact"` |
| `data.attributes.finding_terms.term_for_finding_id` | string |  | The term for Issue Id. Ex.: `"Issue ID"` |
| `data.attributes.finding_terms.term_for_finding_type` | string |  | The term for Type. Ex.: `"Type"` |
| `data.attributes.finding_terms.term_for_finding_severity` | string |  | The term for Severity. Ex.: `"Severity"` |
| `data.attributes.finding_terms.term_for_finding_cost_impact` | string |  | The term for Cost Impact. Ex.: `"Cost Impact"` |
| `data.attributes.finding_terms.term_for_finding_tab` | string |  | The term for Issues Tab. Ex.: `"Issues"` |
| `data.attributes.finding_terms.term_for_finding_description` | string |  | The term for Description. Ex.: `"Description"` |
| `data.attributes.finding_terms.term_for_finding_cause` | string |  | The term for Finding Cause. Ex.: `"Cause"` |
| `data.attributes.finding_terms.term_for_finding_effect` | string |  | The term for Effect. Ex.: `"Effect"` |
| `data.attributes.finding_terms.term_for_finding_scope` | string |  | The term for Scope. Ex.: `"Scope"` |
| `data.attributes.finding_terms.term_for_finding_action_status` | string |  | The term for Action Status. Ex.: `"Action Status"` |
| `data.attributes.finding_terms.term_for_finding_action_priority` | string |  | The term for Action Priority. Ex.: `"Priority"` |
| `data.attributes.finding_terms.term_for_finding_recommendation` | string |  | The term for Recommendation. Ex.: `"Recommendation"` |
| `data.attributes.finding_terms.term_for_finding_executive_summary` | string |  | The term for Executive Summary. Ex.: `"Executive Summary"` |
| `data.attributes.finding_terms.term_for_finding_escalation_level` | string |  | The term for Escalation Level. Ex.: `"Escalation Level"` |
| `data.attributes.finding_terms.term_for_finding_actual_remediation_date` | string |  | The term for Actual Remediation Date. Ex.: `"Actual Remediation Date"` |
| `data.attributes.finding_terms.term_for_finding_retest_deadline_date` | string |  | The term for Retest Deadline Date. Ex.: `"Retest Deadline Date"` |
| `data.attributes.finding_terms.term_for_finding_actual_retest_date` | string |  | The term for Actual Retest Date. Ex.: `"Actual Retest Date"` |
| `data.attributes.finding_terms.term_for_finding_remediation_date` | string |  | The term for Remediation Date. Ex.: `"Remediation Deadline"` |
| `data.attributes.finding_terms.term_for_finding_title` | string |  | The term for Title. Ex.: `"Title"` |
| `data.attributes.finding_terms.term_for_finding_owner` | string |  | The term for Owner. Ex.: `"Owner"` |
| `data.attributes.finding_terms.term_for_finding_date_identified` | string |  | The term for Date Identified. Ex.: `"Date Identified"` |
| `data.attributes.finding_terms.term_for_finding_executive_owner` | string |  | The term for Executive Owner. Ex.: `"Executive Owner"` |
| `data.attributes.finding_terms.term_for_finding_project_owner` | string |  | The term for Project Owner. Ex.: `"Project Owner"` |
| `data.attributes.finding_terms.term_for_finding_overall_status` | string |  | The term for Overall Status. Ex.: `"Overall Status"` |
| `data.attributes.finding_terms.term_for_finding_remediation_plan` | string |  | The term for Remediation Plan. Ex.: `"Remediation Plan"` |
| `data.attributes.finding_terms.finding_types` | array[string] |  | The options for Type. The options available depend on the configuration of the project type. Ex.: `["Finding", "Management Recommendation"]` |
| `data.attributes.finding_terms.severity_values` | array[string] |  | The options for Type. The options available depend on the configuration of the project type. Ex.: `["Low", "Medium", "High"]` |
| `data.attributes.finding_terms.scopes` | array[string] |  | The options for scope. The options available depend on the configuration of the project type. Ex.: `["Local", "Global"]` |
| `data.attributes.finding_terms.escalation_levels` | array[string] |  | The options for Escalation. The options available depend on the configuration of the project type. Ex.: `["Owner", "Executive", "Board"]` |
| `data.attributes.finding_terms.remediation_statuses` | array[string] |  | The options for Remediation Statuses. The options available depend on the configuration of the project type. Ex.: `["Opened", "Awaiting Management Response", "Management Remediating"]` |
| `data.attributes.finding_terms.action_statuses` | array[string] |  | The options for Action Status. The options available depend on the configuration of the project type. Ex.: `["Opened", "Awaiting Management Response", "Management Remediating"]` |
| `data.attributes.finding_terms.action_priorities` | array[string] |  | The options for Priority. The options available depend on the configuration of the project type. Ex.: `["low", "medium", "high"]` |
| `data.attributes.finding_terms.recommendation_enabled` | boolean |  | Whether recommendations are enabled Ex.: `true` |
| `data.attributes.finding_terms.severity_enabled` | boolean |  | Whether severity is enabled Ex.: `true` |
| `data.attributes.finding_terms.id_enabled` | boolean |  | Whether risk ID is enabled Ex.: `true` |
| `data.attributes.finding_terms.risk_impact_enabled` | boolean |  | Whether risk impact is enabled Ex.: `true` |
| `data.attributes.finding_terms.scope_enabled` | boolean |  | Whether scope is enabled Ex.: `true` |
| `data.attributes.finding_terms.escalation_enabled` | boolean |  | Whether escalation is enabled Ex.: `true` |
| `data.attributes.finding_terms.cause_enabled` | boolean |  | Whether cause is enabled Ex.: `true` |
| `data.attributes.finding_terms.effect_enabled` | boolean |  | Whether effect is enabled Ex.: `true` |
| `data.attributes.finding_terms.cost_impact_enabled` | boolean |  | Whether cost impact is enabled Ex.: `true` |
| `data.attributes.finding_terms.executive_summary_enabled` | boolean |  | Whether executive summary is enabled Ex.: `true` |
| `data.attributes.finding_terms.executive_owner_enabled` | boolean |  | Whether executive owner enabled Ex.: `true` |
| `data.attributes.finding_terms.project_owner_enabled` | boolean |  | Whether project owner is enabled Ex.: `true` |
| `data.attributes.finding_terms.term_for_preparer_signoff` | string |  | Ex.: `"Preparer"` |
| `data.attributes.finding_terms.term_for_detail_reviewer_signoff` | string |  | Ex.: `"Detail Reviewer"` |
| `data.attributes.finding_terms.term_for_general_reviewer_signoff` | string |  | Ex.: `"General Reviewer"` |
| `data.attributes.finding_terms.term_for_supplemental_reviewer_signoff` | string |  | Ex.: `"Supplemental Reviewer"` |
| `data.attributes.finding_terms.term_for_specialty_reviewer_signoff` | string |  | Ex.: `"Specialty Reviewer"` |
| `data.attributes.finding_terms.preparer_signoff_enabled` | boolean |  | Ex.: `true` |
| `data.attributes.finding_terms.detail_reviewer_signoff_enabled` | boolean |  | Ex.: `true` |
| `data.attributes.finding_terms.general_reviewer_signoff_enabled` | boolean |  | Ex.: `true` |
| `data.attributes.finding_terms.supplemental_reviewer_signoff_enabled` | boolean |  | Ex.: `true` |
| `data.attributes.finding_terms.specialty_reviewer_signoff_enabled` | boolean |  | Ex.: `true` |
| `data.attributes.finding_remediation_terms` | object |  | The terms of finding remediation. |
| `data.attributes.finding_remediation_terms.term_for_preparer_signoff` | string |  | Ex.: `"Preparer"` |
| `data.attributes.finding_remediation_terms.term_for_detail_reviewer_signoff` | string |  | Ex.: `"Detail Reviewer"` |
| `data.attributes.finding_remediation_terms.term_for_general_reviewer_signoff` | string |  | Ex.: `"General Reviewer"` |
| `data.attributes.finding_remediation_terms.term_for_supplemental_reviewer_signoff` | string |  | Ex.: `"Supplemental Reviewer"` |
| `data.attributes.finding_remediation_terms.term_for_specialty_reviewer_signoff` | string |  | Ex.: `"Specialty Reviewer"` |
| `data.attributes.finding_remediation_terms.preparer_signoff_enabled` | boolean |  | Ex.: `true` |
| `data.attributes.finding_remediation_terms.detail_reviewer_signoff_enabled` | boolean |  | Ex.: `true` |
| `data.attributes.finding_remediation_terms.general_reviewer_signoff_enabled` | boolean |  | Ex.: `true` |
| `data.attributes.finding_remediation_terms.supplemental_reviewer_signoff_enabled` | boolean |  | Ex.: `true` |
| `data.attributes.finding_remediation_terms.specialty_reviewer_signoff_enabled` | boolean |  | Ex.: `true` |
| `data.attributes.finding_retest_terms` | object |  | The terms of finding retest. |
| `data.attributes.finding_retest_terms.term_for_preparer_signoff` | string |  | Ex.: `"Preparer"` |
| `data.attributes.finding_retest_terms.term_for_detail_reviewer_signoff` | string |  | Ex.: `"Detail Reviewer"` |
| `data.attributes.finding_retest_terms.term_for_general_reviewer_signoff` | string |  | Ex.: `"General Reviewer"` |
| `data.attributes.finding_retest_terms.term_for_supplemental_reviewer_signoff` | string |  | Ex.: `"Supplemental Reviewer"` |
| `data.attributes.finding_retest_terms.term_for_specialty_reviewer_signoff` | string |  | Ex.: `"Specialty Reviewer"` |
| `data.attributes.finding_retest_terms.preparer_signoff_enabled` | boolean |  | Ex.: `true` |
| `data.attributes.finding_retest_terms.detail_reviewer_signoff_enabled` | boolean |  | Ex.: `true` |
| `data.attributes.finding_retest_terms.general_reviewer_signoff_enabled` | boolean |  | Ex.: `true` |
| `data.attributes.finding_retest_terms.supplemental_reviewer_signoff_enabled` | boolean |  | Ex.: `true` |
| `data.attributes.finding_retest_terms.specialty_reviewer_signoff_enabled` | boolean |  | Ex.: `true` |
| `data.attributes.certification_terms` | object |  | The terms of certifications. |
| `data.attributes.certification_terms.term_for_certification` | string |  | The term for certification. Ex.: `"Certification"` |
| `data.attributes.certification_terms.term_for_certifications` | string |  | The term for certifications. Ex.: `"Certifications"` |
| `data.attributes.narrative_terms` | object |  | The terms of narrative. This attribute and the associated terms are not available on a Workplan workflow project. |
| `data.attributes.narrative_terms.term_for_narrative` | string |  | The term for Narrative. Ex.: `"Narrative"` |
| `data.attributes.narrative_terms.term_for_narratives` | string |  | The term for Narratives. Ex.: `"Narratives"` |
| `data.attributes.narrative_terms.narrative_enabled` | boolean |  | Whether narratives are enabled Ex.: `true` |
| `data.attributes.narrative_terms.term_for_preparer_signoff` | string |  | Ex.: `"Preparer"` |
| `data.attributes.narrative_terms.term_for_detail_reviewer_signoff` | string |  | Ex.: `"Detail Reviewer"` |
| `data.attributes.narrative_terms.term_for_general_reviewer_signoff` | string |  | Ex.: `"General Reviewer"` |
| `data.attributes.narrative_terms.term_for_supplemental_reviewer_signoff` | string |  | Ex.: `"Supplemental Reviewer"` |
| `data.attributes.narrative_terms.term_for_specialty_reviewer_signoff` | string |  | Ex.: `"Specialty Reviewer"` |
| `data.attributes.narrative_terms.detail_reviewer_signoff_enabled` | boolean |  | Ex.: `true` |
| `data.attributes.narrative_terms.general_reviewer_signoff_enabled` | boolean |  | Ex.: `true` |
| `data.attributes.narrative_terms.supplemental_reviewer_signoff_enabled` | boolean |  | Ex.: `true` |
| `data.attributes.narrative_terms.specialty_reviewer_signoff_enabled` | boolean |  | Ex.: `true` |
| `data.attributes.test_plan_terms` | object |  | The terms of control test plan. This attribute and the associated terms are not available on a Workplan workflow project. |
| `data.attributes.test_plan_terms.term_for_test_plan` | string |  | The term for Test Plan. Ex.: `"Test Plan"` |
| `data.attributes.test_plan_terms.term_for_control_test_plan_test_method` | string |  | The term for Control Testing Method. Ex.: `"Testing Method"` |
| `data.attributes.test_plan_terms.term_for_control_test_plan_sample_size` | string |  | The term for Total Sample Size. Ex.: `"Total Sample Size"` |
| `data.attributes.test_plan_terms.term_for_control_test_plan_test_steps` | string |  | The term for Test Steps. Ex.: `"Test Steps/Test Attributes"` |
| `data.attributes.test_plan_terms.test_methods` | array[string] |  | The options for Test Methods The options available depend on the configuration of the project type. Ex.: `["Inspection", "Observation", "Inquiry", "Reperformance"]` |
| `data.attributes.test_plan_terms.test_plan_enabled` | boolean |  | Whether test plan is enabled Ex.: `true` |
| `data.attributes.test_plan_terms.test_method_enabled` | boolean |  | Whether control testing method enabled Ex.: `true` |
| `data.attributes.test_plan_terms.sample_size_enabled` | boolean |  | Whether total sample size enabled Ex.: `true` |
| `data.attributes.test_plan_terms.term_for_preparer_signoff` | string |  | Ex.: `"Preparer"` |
| `data.attributes.test_plan_terms.term_for_detail_reviewer_signoff` | string |  | Ex.: `"Detail Reviewer"` |
| `data.attributes.test_plan_terms.term_for_general_reviewer_signoff` | string |  | Ex.: `"General Reviewer"` |
| `data.attributes.test_plan_terms.term_for_supplemental_reviewer_signoff` | string |  | Ex.: `"Supplemental Reviewer"` |
| `data.attributes.test_plan_terms.term_for_specialty_reviewer_signoff` | string |  | Ex.: `"Specialty Reviewer"` |
| `data.attributes.test_plan_terms.detail_reviewer_signoff_enabled` | boolean |  | Ex.: `true` |
| `data.attributes.test_plan_terms.general_reviewer_signoff_enabled` | boolean |  | Ex.: `true` |
| `data.attributes.test_plan_terms.supplemental_reviewer_signoff_enabled` | boolean |  | Ex.: `true` |
| `data.attributes.test_plan_terms.specialty_reviewer_signoff_enabled` | boolean |  | Ex.: `true` |
| `data.attributes.control_test_terms` | object |  | The terms of control test. This attribute and the associated terms are not available on a Workplan workflow project. |
| `data.attributes.control_test_terms.term_for_control_test_test_results` | string |  | The term for Test Results. Ex.: `"Test Results"` |
| `data.attributes.control_test_terms.term_for_control_test_conclusion` | string |  | The term for Test Conclusion. Ex.: `"Did this control operate effectively?"` |
| `data.attributes.control_test_terms.term_for_control_test_testing` | string |  | The term for Control Test Testing Ex.: `"Testing"` |
| `data.attributes.control_test_terms.term_for_control_test_2_1` | string |  | The term for Interim Test. Ex.: `"Interim"` |
| `data.attributes.control_test_terms.term_for_control_test_2_2` | string |  | The term for Final Test. Ex.: `"Final"` |
| `data.attributes.control_test_terms.term_for_control_test_4_1` | string |  | The term for Q1 Test. Ex.: `"Q1"` |
| `data.attributes.control_test_terms.term_for_control_test_4_2` | string |  | The term for Q2 Test. Ex.: `"Q2"` |
| `data.attributes.control_test_terms.term_for_control_test_4_3` | string |  | The term for Q3 Test. Ex.: `"Q3"` |
| `data.attributes.control_test_terms.term_for_control_test_4_4` | string |  | The term for Q4 Test. Ex.: `"Q4"` |
| `data.attributes.control_test_terms.term_for_preparer_signoff` | string |  | Ex.: `"Preparer"` |
| `data.attributes.control_test_terms.term_for_detail_reviewer_signoff` | string |  | Ex.: `"Detail Reviewer"` |
| `data.attributes.control_test_terms.term_for_general_reviewer_signoff` | string |  | Ex.: `"General Reviewer"` |
| `data.attributes.control_test_terms.term_for_supplemental_reviewer_signoff` | string |  | Ex.: `"Supplemental Reviewer"` |
| `data.attributes.control_test_terms.term_for_specialty_reviewer_signoff` | string |  | Ex.: `"Specialty Reviewer"` |
| `data.attributes.control_test_terms.preparer_signoff_enabled` | boolean |  | Ex.: `true` |
| `data.attributes.control_test_terms.detail_reviewer_signoff_enabled` | boolean |  | Ex.: `true` |
| `data.attributes.control_test_terms.general_reviewer_signoff_enabled` | boolean |  | Ex.: `true` |
| `data.attributes.control_test_terms.supplemental_reviewer_signoff_enabled` | boolean |  | Ex.: `true` |
| `data.attributes.control_test_terms.specialty_reviewer_signoff_enabled` | boolean |  | Ex.: `true` |
| `data.attributes.control_test_terms.conclusion_values_true` | string |  | The term choices for Operating Effectively. The exact values for this field (E.g. "Operating Effectively") depend on the configuration of the project type. Ex.: `"Operating Effectively"` |
| `data.attributes.control_test_terms.conclusion_values_false` | string |  | The term choices for Exception(s) Noted. The exact values for this field (E.g. "Exception(s) Noted") depend on the configuration of the project type. Ex.: `"Exception(s) Noted"` |
| `data.attributes.control_test_terms.conclusion_status_options_true` | array[string] |  | The options for Conclusion Status (Passed). The options available depend on the configuration of the project type. Ex.: `["Operating Effectively"]` |
| `data.attributes.control_test_terms.conclusion_status_options_false` | array[string] |  | The options for Conclusion Status (Failing). The options available depend on the configuration of the project type. Ex.: `["Exception(s) Noted"]` |
| `data.attributes.control_test_terms.term_for_planned_milestone_date` | string |  | Planned milestone date. Ex.: `"Planned milestone date"` |
| `data.attributes.control_test_terms.planned_milestone_date_enabled` | boolean |  | Planned milestone date enabled. Ex.: `true` |
| `data.attributes.control_test_terms.term_for_actual_milestone_date` | string |  | Term for actual milestone date. Ex.: `"Actual milestone date"` |
| `data.attributes.control_test_terms.actual_milestone_date_enabled` | boolean |  | Actual milestone date enabled. Ex.: `true` |
| `data.attributes.testing_round_terms` | object |  | The terms of finding retest. |
| `data.attributes.testing_round_terms.term_for_preparer_signoff` | string |  | Ex.: `"Preparer"` |
| `data.attributes.testing_round_terms.term_for_detail_reviewer_signoff` | string |  | Ex.: `"Detail Reviewer"` |
| `data.attributes.testing_round_terms.term_for_general_reviewer_signoff` | string |  | Ex.: `"General Reviewer"` |
| `data.attributes.testing_round_terms.term_for_supplemental_reviewer_signoff` | string |  | Ex.: `"Supplemental Reviewer"` |
| `data.attributes.testing_round_terms.term_for_specialty_reviewer_signoff` | string |  | Ex.: `"Specialty Reviewer"` |
| `data.attributes.testing_round_terms.detail_reviewer_signoff_enabled` | boolean |  | Ex.: `true` |
| `data.attributes.testing_round_terms.general_reviewer_signoff_enabled` | boolean |  | Ex.: `true` |
| `data.attributes.testing_round_terms.supplemental_reviewer_signoff_enabled` | boolean |  | Ex.: `true` |
| `data.attributes.testing_round_terms.specialty_reviewer_signoff_enabled` | boolean |  | Ex.: `true` |
| `data.attributes.created_at` | string |  | The timestamp identifying when the project type was created. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.attributes.updated_at` | string |  | The timestamp identifying when the project type was updated. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.relationships` | object | ✅ | The relationships associated with the resource. |
| `data.relationships.assigned_users` | object |  |  |
| `data.relationships.assigned_users.data` | array[object] | ✅ | The data associated with the resource. |
| `data.relationships.assigned_users.data.id` | string | ✅ | The UID of the user. Ex.: `"6a69d46ba9bc4bf4"` |
| `data.relationships.assigned_users.data.type` | string | ✅ | The classification of the object (`"users"`). Ex.: `"users"` |

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
