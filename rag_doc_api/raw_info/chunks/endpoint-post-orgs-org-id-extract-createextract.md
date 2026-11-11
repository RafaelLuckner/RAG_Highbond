---
id: endpoint-post-orgs-org-id-extract-createextract
title: "Extract: Create extraction request"
tags: [endpoint, extract]
source: openapi.json (HighBond API v1.1.0)
---

## Extract

Service to extract the resources from an organization based on resource ids.

### `POST /orgs/{org_id}/extract` — Create extraction request

- **operationId:** `createExtract`
- **Domínio(s):** Extract

Generate terraform or json scripts for resources existing in an organization.

<details>
<summary><strong>Parâmetros</strong> (2)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `output_format` | query |  | string | The output_format to extract. Valores: `tf`, `json` Default: `tf` |

</details>

<details>
<summary><strong>Request body (payload)</strong></summary>

The data required to create a extract.

**Body obrigatório.**

**Content-Type:** `application/vnd.api+json`

**Schema:** `CreateExtractRequest`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | object | ✅ | The data associated with the resource. |
| `data.type` | string | ✅ | The classification of the object (`extract`). Ex.: `"extract"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.resources` | object | ✅ | The resources associated to extract. |
| `data.attributes.resources.projects` | object |  | Projects to be extracted. Organization Ids or Project Ids are required. |
| `data.attributes.resources.projects.extractEntity` | boolean |  | Flag to extract entity ids. Default value is false. Can be used only with hierarchy true |
| `data.attributes.resources.projects.organizationIds` | array[string] |  | OrganizationIds as array to get all Projects under Organization |
| `data.attributes.resources.projects.hierarchy` | boolean |  | Flag to extract Hierarchy of all resources under Projects. Default value is true |
| `data.attributes.resources.projects.ids` | array[string] |  | Array of Project Ids. |
| `data.attributes.resources.projects.extractFrameworkOriginId` | boolean |  | Flag to extract Framework Origin ids. Default value is false. Can be used only with hierarchy true |
| `data.attributes.resources.controls` | object |  | Controls to be extracted. Project Ids or Framework Ids or Objective Ids or Control ids are required. |
| `data.attributes.resources.controls.objectiveIds` | array[string] |  | Array of Objective Ids. |
| `data.attributes.resources.controls.ids` | array[string] |  | Array of control Ids. |
| `data.attributes.resources.controls.projectIds` | array[string] |  | Array of Project Ids. |
| `data.attributes.resources.controls.frameworkIds` | array[string] |  | Array of Framework Ids. |
| `data.attributes.resources.frameworks` | object |  | Frameworks to be extracted. Organization Ids or Framework Ids are required. |
| `data.attributes.resources.frameworks.extractEntity` | boolean |  | Flag to extract entity ids. Default value is false. Can be used only with hierarchy true |
| `data.attributes.resources.frameworks.organizationIds` | array[string] |  | Array containing organization Id having frameworks. |
| `data.attributes.resources.frameworks.hierarchy` | boolean |  | Flag to extract Hierarchy of all resources under Frameworks. Default value is true |
| `data.attributes.resources.frameworks.ids` | array[string] |  | Array of framework Ids. |
| `data.attributes.resources.frameworks.extractFrameworkOriginId` | boolean |  | Flag to extract Framework Origin ids. Default value is false. Can be used only with hierarchy true |
| `data.attributes.resources.projectType` | object |  | Project Type to be extracted. Organization Ids or Project Ids or Framework Ids or Project Type Ids are required. |
| `data.attributes.resources.projectType.organizationIds` | array[string] |  | Array containing organization Id. |
| `data.attributes.resources.projectType.hierarchy` | boolean |  | Flag to extract Hierarchy of all resources under Project Type. Default value is true |
| `data.attributes.resources.projectType.ids` | array[string] |  | Array of projectType Ids. |
| `data.attributes.resources.projectType.projectIds` | array[string] |  | Array of Project Ids. |
| `data.attributes.resources.projectType.frameworkIds` | array[string] |  | Array of Framework Ids. |
| `data.attributes.resources.assetRecordRelationships` | object |  | Asset Records Relationships to be extracted. |
| `data.attributes.resources.assetRecordRelationships.ids` | array[object] | ✅ | Array of combinational ids of asset record id and asset record type Id and fieldName. |
| `data.attributes.resources.assetRecordRelationships.ids.fieldName` | string |  |  |
| `data.attributes.resources.assetRecordRelationships.ids.assetRecordTypeId` | string |  |  |
| `data.attributes.resources.assetRecordRelationships.ids.assetRecordId` | string |  |  |
| `data.attributes.resources.requestItems` | object |  | Request items to be extracted. Project Ids or request items ids are required |
| `data.attributes.resources.requestItems.ids` | array[string] |  | Array of Request Item Ids. |
| `data.attributes.resources.requestItems.projectIds` | array[string] |  | Array of Project Ids. |
| `data.attributes.resources.simpleQuestions` | object |  | Simple Questions to be extracted. |
| `data.attributes.resources.simpleQuestions.ids` | array[string] | ✅ | Array of simple question Ids. |
| `data.attributes.resources.issues` | object |  | Issues to be extracted. Either Project Ids or Ids are required. |
| `data.attributes.resources.issues.hierarchy` | boolean |  | Flag to extract Hierarchy of all resources under Issues. Default value is true |
| `data.attributes.resources.issues.ids` | array[string] |  | Array of Issue Ids. |
| `data.attributes.resources.issues.projectIds` | array[string] |  | Array of Project Ids. |
| `data.attributes.resources.mitigations` | object |  | Mitigations to be extracted. Project Ids or Framework Ids or Objective Ids or Mitigations Ids are required. |
| `data.attributes.resources.mitigations.objectiveIds` | array[string] |  | Array of Objective Ids. |
| `data.attributes.resources.mitigations.ids` | array[string] |  | Array of mitigation Ids. |
| `data.attributes.resources.mitigations.projectIds` | array[string] |  | Array of Project Ids. |
| `data.attributes.resources.mitigations.frameworkIds` | array[string] |  | Array of Framework Ids. |
| `data.attributes.resources.analyses` | object |  | Analyses to be extracted. Collection Ids or Analses Ids are required. |
| `data.attributes.resources.analyses.collectionIds` | array[string] |  | Array of Collection ids. |
| `data.attributes.resources.analyses.ids` | array[string] |  | Array of Analyses Ids. |
| `data.attributes.resources.tables` | object |  | Tables to be extracted. Analysis Ids or Collection Ids or Table Ids are required. |
| `data.attributes.resources.tables.analysisIds` | array[string] |  | Array of Analysis Ids. |
| `data.attributes.resources.tables.collectionIds` | array[string] |  | Array of Collection Ids. |
| `data.attributes.resources.tables.ids` | array[string] |  | Array of table Ids. |
| `data.attributes.resources.storyBoards` | object |  | Story boards to be extracted. |
| `data.attributes.resources.storyBoards.ids` | array[string] | ✅ | Array of storyboard Ids. |
| `data.attributes.resources.assets` | object |  | Assets to be extracted. Asset type Ids or Asset Ids are required. |
| `data.attributes.resources.assets.ids` | array[object] |  | Array of combinational ids of asset id and asset type Id. |
| `data.attributes.resources.assets.ids.assetTypeId` | string |  |  |
| `data.attributes.resources.assets.ids.assetId` | string |  |  |
| `data.attributes.resources.assets.assetTypeIds` | array[string] |  | Array of Asset Type Ids having assets. |
| `data.attributes.resources.collections` | object |  | Collections to be extracted. |
| `data.attributes.resources.collections.ids` | array[string] | ✅ | Array of collection Ids. |
| `data.attributes.resources.timeEntries` | object |  | Time Entries to be extracted. Organization Ids or Time Entries Ids are required. |
| `data.attributes.resources.timeEntries.organizationIds` | array[string] |  | OrganizationId passed as an array |
| `data.attributes.resources.timeEntries.ids` | array[string] |  | Array of time entry Ids. |
| `data.attributes.resources.collaborators` | object |  | Collaborators to be extracted. Project Ids or Framework Ids or Collaborators ids are required. |
| `data.attributes.resources.collaborators.ids` | array[string] |  | Array of collaborator Ids. |
| `data.attributes.resources.collaborators.projectIds` | array[string] |  | Array of Project Ids having collaborators. |
| `data.attributes.resources.collaborators.frameworkIds` | array[string] |  | Array of Framework Ids having collaborators. |
| `data.attributes.resources.robots` | object |  | Robots to be extracted. |
| `data.attributes.resources.robots.hierarchy` | boolean |  | Flag to extract Hierarchy of all resources under Robots. Default value is true |
| `data.attributes.resources.robots.ids` | array[string] | ✅ | Array of robot  Ids. |
| `data.attributes.resources.handlerTriggers` | object |  | Handler Triggers to be extracted. Organization Ids or Workflow Ids or Handler Ids are required. |
| `data.attributes.resources.handlerTriggers.workflowIds` | array[string] |  | Array of workflow ids having handler triggers. |
| `data.attributes.resources.handlerTriggers.organizationIds` | array[string] |  | Array containing organization Id having handler triggers. |
| `data.attributes.resources.handlerTriggers.handlerIds` | array[string] |  | Array of handler ids containing handler triggers. |
| `data.attributes.resources.roleAssignments` | object |  | Role Assignments to be extracted. Organization Ids or Role Ids are required. |
| `data.attributes.resources.roleAssignments.roleIds` | array[string] |  | Array of role ids containing roleAssignments. |
| `data.attributes.resources.roleAssignments.organizationIds` | array[string] |  | Array containing organization Id having roleAssignments. |
| `data.attributes.resources.interpretations` | object |  | Interpretations to be extracted. Table Ids or Interpretation Ids are required. |
| `data.attributes.resources.interpretations.ids` | array[string] |  | Array of interpretation Ids. |
| `data.attributes.resources.interpretations.tableIds` | array[string] |  | Array of Table Ids. |
| `data.attributes.resources.entityCategories` | object |  | Entity categories to be extracted. |
| `data.attributes.resources.entityCategories.ids` | array[string] | ✅ | Array of entity category Ids. |
| `data.attributes.resources.events` | object |  | Events to be extracted. Workflow Ids or Event Ids are required. |
| `data.attributes.resources.events.workflowIds` | array[string] |  | Array of workflow Ids having workflow status. |
| `data.attributes.resources.events.ids` | array[string] |  | Array of workflow status Ids. |
| `data.attributes.resources.impactReports` | object |  | Impact Reports to be extracted. Organization Ids or Impact Reports Ids are required. |
| `data.attributes.resources.impactReports.organizationIds` | array[string] |  | Array containing organization Id having impact reports. |
| `data.attributes.resources.impactReports.ids` | array[string] |  | Array of impact report Ids. |
| `data.attributes.resources.numericScales` | object |  | Numeric Scales to be extracted. |
| `data.attributes.resources.numericScales.ids` | array[string] | ✅ | Array of numeric scales Ids. |
| `data.attributes.resources.robotScriptVersion` | object |  | Robot Script Version to be extracted. Robot Ids or ids are required |
| `data.attributes.resources.robotScriptVersion.robotIds` | array[string] |  | Array of Robot Ids. |
| `data.attributes.resources.robotScriptVersion.ids` | array[object] |  | Array of combinational ids of robot and task id. |
| `data.attributes.resources.robotScriptVersion.ids.versionId` | string |  |  |
| `data.attributes.resources.robotScriptVersion.ids.robotId` | string |  |  |
| `data.attributes.resources.narratives` | object |  | Narratives to be extracted. Objective Ids or Project Ids or Framework Ids or Narrative Ids are required. |
| `data.attributes.resources.narratives.objectiveIds` | array[string] |  | Array of Objective Ids. |
| `data.attributes.resources.narratives.ids` | array[string] |  | Array of Narrative Ids. |
| `data.attributes.resources.narratives.projectIds` | array[string] |  | Array of Project Ids. |
| `data.attributes.resources.narratives.frameworkIds` | array[string] |  | Array of Framework Ids. |
| `data.attributes.resources.collaboratorGroups` | object |  | collaboratorGroups to be extracted. Project Ids or Framework Ids or Collaborator Group Ids are required. |
| `data.attributes.resources.collaboratorGroups.ids` | array[string] |  | Array of collaboratorGroups Ids. |
| `data.attributes.resources.collaboratorGroups.projectIds` | array[string] |  | Array of Project Ids containing Collaborator Groups. |
| `data.attributes.resources.collaboratorGroups.frameworkIds` | array[string] |  | Array of Framework Ids containing Collaborator Groups. |
| `data.attributes.resources.complianceRegulations` | object |  | Compliance Regulations to be extracted. |
| `data.attributes.resources.complianceRegulations.hierarchy` | boolean |  | Flag to extract Hierarchy of all resources under Compliance Regulations. Default value is true |
| `data.attributes.resources.complianceRegulations.ids` | array[string] | ✅ | Array of compliance regulation ids |
| `data.attributes.resources.workflowStatuses` | object |  | Workflow statuses to be extracted. Workflow Ids or Status Ids are required. |
| `data.attributes.resources.workflowStatuses.workflowIds` | array[string] |  | Array of workflow Ids having workflow status. |
| `data.attributes.resources.workflowStatuses.ids` | array[string] |  | Array of workflow status Ids. |
| `data.attributes.resources.assetTypeSections` | object |  | Asset type Sections to be extracted. Organization Ids or Asset Type Ids are required. |
| `data.attributes.resources.assetTypeSections.organizationIds` | array[string] |  | Array containing organization Id having assetTypeSections. |
| `data.attributes.resources.assetTypeSections.assetTypeIds` | array[string] |  | Array of asset Type Ids. |
| `data.attributes.resources.sections` | object |  | Sections to be extracted. |
| `data.attributes.resources.sections.ids` | array[string] | ✅ | Array of section Ids. |
| `data.attributes.resources.users` | object |  | Users to be extracted. Organization Ids or User Ids are required. |
| `data.attributes.resources.users.organizationIds` | array[string] |  | Array containing organization Id. |
| `data.attributes.resources.users.ids` | array[string] |  | Array of user Ids. |
| `data.attributes.resources.workflowStatusEvents` | object |  | Workflow Status Events to be extracted. Workflow Ids or Wrokflow Status Ids or Workflow Status event Ids are required. |
| `data.attributes.resources.workflowStatusEvents.workflowIds` | array[string] |  | Array of Workflow Ids having Wrokflow Status events. |
| `data.attributes.resources.workflowStatusEvents.workflowStatusIds` | array[string] |  | Array of Workflow Status Ids having Wrokflow Status events. |
| `data.attributes.resources.workflowStatusEvents.ids` | array[string] |  | Array of Workflow Status Event having Wrokflow Status events. |
| `data.attributes.resources.assetTypes` | object |  | Asset Types to be extracted. Organization Ids or Asset Types Ids are required. |
| `data.attributes.resources.assetTypes.organizationIds` | array[string] |  | Array containing organization Id. |
| `data.attributes.resources.assetTypes.hierarchy` | boolean |  | Flag to extract Hierarchy of all resources under Asset Types. Default value is true |
| `data.attributes.resources.assetTypes.ids` | array[string] |  | Array of asset type Ids. |
| `data.attributes.resources.rolePermissionAssignments` | object |  | Role Permission Assignments to be extracted. Organization Ids or Role Ids are required. |
| `data.attributes.resources.rolePermissionAssignments.roleIds` | array[string] |  | Array of role ids containing rolePermissionAssignments. |
| `data.attributes.resources.rolePermissionAssignments.organizationIds` | array[string] |  | Array containing organization Id having rolePermissionAssignments. |
| `data.attributes.resources.assetRecordTypeSections` | object |  | Asset Record type Sections to be extracted. Organization Ids or Asset Record Type Ids are required. |
| `data.attributes.resources.assetRecordTypeSections.organizationIds` | array[string] |  | Array containing organization Id having assetRecordTypeSections. |
| `data.attributes.resources.assetRecordTypeSections.assetRecordTypeIds` | array[string] |  | Array of asset Record Type Ids. |
| `data.attributes.resources.assetRecordTypeAttributes` | object |  | Asset Record Type Attributes to be extracted. |
| `data.attributes.resources.assetRecordTypeAttributes.assetRecordTypeIds` | array[string] | ✅ | Array of asset record type ids. |
| `data.attributes.resources.assetRelateRecordTypes` | object |  | Asset Record Type Attributes to be extracted. |
| `data.attributes.resources.assetRelateRecordTypes.assetRecordTypeIds` | array[string] | ✅ | Array of asset record type ids. |
| `data.attributes.resources.metrics` | object |  | Metrics to be extracted. |
| `data.attributes.resources.metrics.ids` | array[string] | ✅ | Array of metric Ids. |
| `data.attributes.resources.actions` | object |  | Actions to be extracted. Project Ids or Issue Ids or Action Ids are required. |
| `data.attributes.resources.actions.ids` | array[string] |  | Array of Action Ids. |
| `data.attributes.resources.actions.issueIds` | array[string] |  | Array of Issue Ids. |
| `data.attributes.resources.actions.projectIds` | array[string] |  | Array of Project Ids. |
| `data.attributes.resources.complianceRequirements` | object |  | Compliance Requirements to be extracted. Compliance Regulation Ids or Compliance requirement Ids are required. |
| `data.attributes.resources.complianceRequirements.complianceRegulationIds` | array[string] |  | Array containing complianceRegulationIds having compliance Requirements. |
| `data.attributes.resources.complianceRequirements.ids` | array[string] |  | Array of compliance Requirement Ids. |
| `data.attributes.resources.customAttributes` | object |  | Custom Attributes to be extracted. Project Type Ids or Project Ids or Framework Ids or Ids are required. |
| `data.attributes.resources.customAttributes.projectTypeIds` | array[string] |  | Array of ProjectTypeIds. |
| `data.attributes.resources.customAttributes.ids` | array[string] |  | Array of customAttribute Ids. |
| `data.attributes.resources.customAttributes.projectIds` | array[string] |  | Array of Project Ids. |
| `data.attributes.resources.customAttributes.frameworkIds` | array[string] |  | Array of Framework Ids. |
| `data.attributes.resources.attributeTypes` | object |  | Attribute Types to be extracted. Organization Ids or Asset Type Ids or Asset Record Type Ids or Ids are required. |
| `data.attributes.resources.attributeTypes.organizationIds` | array[string] |  | Array containing organization Id having attributeTypes. |
| `data.attributes.resources.attributeTypes.ids` | array[string] |  | Array of asset Type Ids. |
| `data.attributes.resources.attributeTypes.assetRecordTypeIds` | array[string] |  | Array of asset record type ids having assetRecordType Ids. |
| `data.attributes.resources.attributeTypes.assetTypeIds` | array[string] |  | Array of asset type ids containing attribute types. |
| `data.attributes.resources.assetTypeAttributes` | object |  | Asset Type Attributes to be extracted. |
| `data.attributes.resources.assetTypeAttributes.assetTypeIds` | array[string] | ✅ | Array of asset type ids having assetTypeAttributes. |
| `data.attributes.resources.columns` | object |  | Columns to be extracted. |
| `data.attributes.resources.columns.tableIds` | array[string] | ✅ | Array of column Ids. |
| `data.attributes.resources.roles` | object |  | Roles to be extracted. Organization Ids or Role Ids are required. |
| `data.attributes.resources.roles.organizationIds` | array[string] |  | Array containing organization Id. |
| `data.attributes.resources.roles.hierarchy` | boolean |  | Flag to extract Hierarchy of all resources under Roles. Default value is true |
| `data.attributes.resources.roles.ids` | array[string] |  | Array of role Ids. |
| `data.attributes.resources.surveys` | object |  | Surveys to be extracted. Analysis Ids or Collection Ids or Survey Ids are required. |
| `data.attributes.resources.surveys.analysisIds` | array[string] |  | Array of Analysis Ids. |
| `data.attributes.resources.surveys.collectionIds` | array[string] |  | Array of Collection Ids. |
| `data.attributes.resources.surveys.ids` | array[string] |  | Array of Survey Ids. |
| `data.attributes.resources.robotFiles` | object |  | Robot files to be extracted. |
| `data.attributes.resources.robotFiles.environment` | string |  | Either 'production' or 'development'. Default value is 'production' Valores: `production`, `development` |
| `data.attributes.resources.robotFiles.robotIds` | array[string] | ✅ | Array of robot file Ids. |
| `data.attributes.resources.tableIdentifiers` | object |  | Table Identifiers to be extracted. |
| `data.attributes.resources.tableIdentifiers.tableIds` | array[string] | ✅ | Array of table Ids. |
| `data.attributes.resources.workflows` | object |  | Workflows to be extracted. Organization Ids or Api Names or Workflow Ids are required. |
| `data.attributes.resources.workflows.organizationIds` | array[string] |  | Array containing organization Id having workflows. |
| `data.attributes.resources.workflows.hierarchy` | boolean |  | Flag to extract Hierarchy of all resources under Workflows. Default value is true |
| `data.attributes.resources.workflows.ids` | array[string] |  | Array of workflow Ids. |
| `data.attributes.resources.workflows.apiNames` | array[string] |  | Array of apiNames. |
| `data.attributes.resources.resultFiles` | object |  | Result files to be extracted. Project Ids or Result Files Ids are required. |
| `data.attributes.resources.resultFiles.ids` | array[string] |  | Array of Result file Ids. |
| `data.attributes.resources.resultFiles.projectIds` | array[string] |  | Array of Project Ids. |
| `data.attributes.resources.pageBreaks` | object |  | Pagebreaks to be extracted. |
| `data.attributes.resources.pageBreaks.ids` | array[string] | ✅ | Array of pagebreak Ids. |
| `data.attributes.resources.assetRelationships` | object |  | Asset Relationships to be extracted. |
| `data.attributes.resources.assetRelationships.ids` | array[object] | ✅ | Array of combinational ids of asset id and asset type Id and fieldName. |
| `data.attributes.resources.assetRelationships.ids.fieldName` | string |  |  |
| `data.attributes.resources.assetRelationships.ids.assetTypeId` | string |  |  |
| `data.attributes.resources.assetRelationships.ids.assetId` | string |  |  |
| `data.attributes.resources.planningFiles` | object |  | Planning files to be extracted. Project Ids or Framework Ids or Planning files Ids are required. |
| `data.attributes.resources.planningFiles.ids` | array[string] |  | Array of planning file Ids. |
| `data.attributes.resources.planningFiles.projectIds` | array[string] |  | Array of Project Ids. |
| `data.attributes.resources.planningFiles.frameworkIds` | array[string] |  | Array of Framework Ids. |
| `data.attributes.resources.robotTasks` | object |  | Robot tasks to be extracted. Robot Ids or Robot Task Ids are required |
| `data.attributes.resources.robotTasks.robotIds` | array[string] |  | Array of Robot Ids having robot tasks. |
| `data.attributes.resources.robotTasks.ids` | array[object] |  | Array of combinational ids of robot and task id. |
| `data.attributes.resources.robotTasks.ids.robotId` | string |  |  |
| `data.attributes.resources.robotTasks.ids.taskId` | string |  |  |
| `data.attributes.resources.assetRecords` | object |  | Asset Records to be extracted. Asset Record Type Ids or Asset record ids are required. |
| `data.attributes.resources.assetRecords.ids` | array[object] |  | Array of combinational ids of asset record id and asset record type Id. |
| `data.attributes.resources.assetRecords.ids.assetRecordTypeId` | string |  |  |
| `data.attributes.resources.assetRecords.ids.assetRecordId` | string |  |  |
| `data.attributes.resources.assetRecords.assetRecordTypeIds` | array[string] |  | Array of Asset Record Type Ids. |
| `data.attributes.resources.relatedComplianceRequirements` | object |  | RelatedComplianceRequirements to be extracted. |
| `data.attributes.resources.relatedComplianceRequirements.ids` | array[string] | ✅ | Array of relatedComplianceRequirements Ids. |
| `data.attributes.resources.complianceMaps` | object |  | Compliance Maps to be extracted. Compliance Requirement IDs or Compliance Requlation Ids or Compliance Maps Ids are required. |
| `data.attributes.resources.complianceMaps.complianceRegulationIds` | array[string] |  | Array containing compliance regulation ids having compliance maps. |
| `data.attributes.resources.complianceMaps.ids` | array[string] |  | Array of compliance maps Ids. |
| `data.attributes.resources.complianceMaps.complianceRequirementIds` | array[string] |  | Array containing compliance requirement ids having compliance maps. |
| `data.attributes.resources.assetRecordTypes` | object |  | Asset Record Types to be extracted. Organization Ids or Asset Record Type Ids are required. |
| `data.attributes.resources.assetRecordTypes.organizationIds` | array[string] |  | Array containing organization Id. |
| `data.attributes.resources.assetRecordTypes.hierarchy` | boolean |  | Flag to extract Hierarchy of all resources under Asset Record Types. Default value is true |
| `data.attributes.resources.assetRecordTypes.ids` | array[string] |  | Array of asset record type Ids. |
| `data.attributes.resources.nonProjectTimeCategories` | object |  | Non Project Time Category to be extracted. Organization Ids or Non Project Time Categories Ids are required. |
| `data.attributes.resources.nonProjectTimeCategories.organizationIds` | array[string] |  | Array containing Organization Id having nonProjectTimeCategory. |
| `data.attributes.resources.nonProjectTimeCategories.ids` | array[string] |  | Array containing Ids of nonProjectTimeCategory. |
| `data.attributes.resources.systemUsers` | object |  | System Users to be extracted. Organization Ids or User Ids are required. |
| `data.attributes.resources.systemUsers.organizationIds` | array[string] |  | Array containing organization Id. |
| `data.attributes.resources.systemUsers.ids` | array[string] |  | Array of system user Ids. |
| `data.attributes.resources.assetTypeRecordTypes` | object |  | Asset Type Record Type to be extracted. Asset type Ids or Asset record type ids are required. |
| `data.attributes.resources.assetTypeRecordTypes.assetRecordTypeIds` | array[string] |  | Array of asset record type ids having assettypeRecordType Relationship. |
| `data.attributes.resources.assetTypeRecordTypes.assetTypeIds` | array[string] |  | Array of asset type ids having assettypeRecordType Relationship. |
| `data.attributes.resources.choiceQuestions` | object |  | Choice Questions to be extracted. |
| `data.attributes.resources.choiceQuestions.ids` | array[string] | ✅ | Array of choice question Ids. |
| `data.attributes.resources.questionnaires` | object |  | Questionnaires to be extracted. Collection Ids or Questionnaire Id are required. |
| `data.attributes.resources.questionnaires.collectionIds` | array[string] |  | Array of Collection Ids. |
| `data.attributes.resources.questionnaires.ids` | array[string] |  | Array of Questionnaire Ids. |
| `data.attributes.resources.risks` | object |  | Risks to be extracted. Project Ids or Framework Ids or Objective Ids or Risk Ids are required. |
| `data.attributes.resources.risks.objectiveIds` | array[string] |  | Array of Objective Ids. |
| `data.attributes.resources.risks.ids` | array[string] |  | Array of Risk Ids. |
| `data.attributes.resources.risks.projectIds` | array[string] |  | Array of Project Ids. |
| `data.attributes.resources.risks.frameworkIds` | array[string] |  | Array of Framework Ids. |
| `data.attributes.resources.entities` | object |  | Entities to be extracted. |
| `data.attributes.resources.entities.ids` | array[string] | ✅ | Array of entity Ids. |
| `data.attributes.resources.handlers` | object |  | Handlers to be extracted. Organization Ids or Workflow Ids or Handler Ids are required. |
| `data.attributes.resources.handlers.workflowIds` | array[string] |  | Array of workflow ids having handlers. |
| `data.attributes.resources.handlers.organizationIds` | array[string] |  | Array containing organization Id having handlers. |
| `data.attributes.resources.handlers.ids` | array[string] |  | Array of handler Ids. |
| `data.attributes.resources.objectives` | object |  | Objectives to be extracted. Project Ids or Framework Ids or Objective Ids are represented |
| `data.attributes.resources.objectives.ids` | array[string] |  | Array of Objective Ids. |
| `data.attributes.resources.objectives.projectIds` | array[string] |  | Array of Project Ids. |
| `data.attributes.resources.objectives.frameworkIds` | array[string] |  | Array of Framework Ids. |
| `data.attributes.resources.todos` | object |  | Todos to be extracted |
| `data.attributes.resources.todos.organizationIds` | array[string] |  | OrganizationId passed as an array |
| `data.attributes.resources.todos.ids` | array[string] |  | Array of Todo Ids. |
| `data.attributes.resources.todos.projectIds` | array[string] |  | Array of Project Ids. |
| `data.attributes.resources.robotActivation` | object |  | Robot Activation to be extracted. Either Robot Ids or Ids are required |
| `data.attributes.resources.robotActivation.robotIds` | array[string] |  | Array of Robot Ids having robot activations. |
| `data.attributes.resources.robotActivation.ids` | array[RobotIdConfiguration] |  | Array of combinational ids of robot or robot and task id or robot and version id. |
| `data.attributes.resources.robotActivation.ids` | RobotIdConfiguration |  | ↩ *referência recursiva — ver schema* `RobotIdConfiguration` |
| `data.attributes.resources.robotApps` | object |  | Robot Apps to be extracted. Robot Ids or Robot App Ids are required. |
| `data.attributes.resources.robotApps.robotIds` | array[string] |  | Array of Robot Ids having robot apps. |
| `data.attributes.resources.robotApps.ids` | array[RobotAppConfiguration] |  | Array of combinational ids of robot or robot and task id or robot and version id. |
| `data.attributes.resources.robotApps.ids` | RobotAppConfiguration |  | ↩ *referência recursiva — ver schema* `RobotAppConfiguration` |
| `data.attributes.resources.impactReportTargets` | object |  | Impact Report Targets to be extracted. Report Target type or Report Target Ids are required. |
| `data.attributes.resources.impactReportTargets.reportTargetTypes` | array[ImpactReportTargetConfiguration] |  | Array containing combination of targetType and targetTypeId or targetType, targetTypeId, targetResource & targetResourceId |
| `data.attributes.resources.impactReportTargets.reportTargetTypes` | ImpactReportTargetConfiguration |  | ↩ *referência recursiva — ver schema* `ImpactReportTargetConfiguration` |
| `data.attributes.resources.impactReportTargets.ids` | array[string] |  | Array of impact Report Ids. |
| `data.attributes.resources.govMapOrganizationUnitTypes` | object |  | GovMap Organization Unit Types to be extracted. Organization Ids or GovMap Organization Unit Type Ids are required. |
| `data.attributes.resources.govMapOrganizationUnitTypes.organizationIds` | array[string] |  | Array of Organization Ids. |
| `data.attributes.resources.govMapOrganizationUnitTypes.ids` | array[string] |  | Array of GovMap Organization Unit Type Ids. |
| `data.attributes.resources.govMapOrganizationUnits` | object |  | GovMap Organization Unit to be extracted. Organization Ids or GovMap Organization Unit Ids are required. |
| `data.attributes.resources.govMapOrganizationUnits.organizationIds` | array[string] |  | Array of Organization Ids. |
| `data.attributes.resources.govMapOrganizationUnits.ids` | array[string] |  | Array of GovMap Organization Unit Ids. |
| `data.attributes.resources.requestItemStatus` | object |  | Request Item Statuses to be extracted. Project Type Ids or Request Item Status Ids are required. |
| `data.attributes.resources.requestItemStatus.projectTypeIds` | array[string] |  | Array of Project Type Ids. |
| `data.attributes.resources.requestItemStatus.ids` | array[string] |  | Array of Request Item Status Ids. |
| `data.attributes.resources.strategyRisks` | object |  | Strategy Risks to be extracted. Organization Ids or Strategy Risk Ids are required. |
| `data.attributes.resources.strategyRisks.organizationIds` | array[string] |  | OrganizationIds as array to get all Strategy Risks under Organization |
| `data.attributes.resources.strategyRisks.hierarchy` | boolean |  | Flag to extract Hierarchy of all resources under Strategy Risks. Default value is true |
| `data.attributes.resources.strategyRisks.ids` | array[string] |  | Array of Strategy Risk Ids. |
| `data.attributes.resources.strategyTags` | object |  | Strategy Tags to be extracted. Organization Ids or Strategy Tag Ids are required. |
| `data.attributes.resources.strategyTags.organizationIds` | array[string] |  | Array of Organization Ids. |
| `data.attributes.resources.strategyTags.ids` | array[string] |  | Array of Strategy Tag Ids. |
| `data.attributes.resources.strategySegments` | object |  | Strategy Segments to be extracted. Organization Ids or Strategy Segment Ids are required. |
| `data.attributes.resources.strategySegments.organizationIds` | array[string] |  | Array of Organization Ids. |
| `data.attributes.resources.strategySegments.ids` | array[string] |  | Array of Strategy Segment Ids. |
| `data.attributes.resources.strategyFactors` | object |  | Strategy Factors to be extracted. Organization Ids or Strategy Factor Ids are required. |
| `data.attributes.resources.strategyFactors.organizationIds` | array[string] |  | Array of Organization Ids. |
| `data.attributes.resources.strategyFactors.ids` | array[string] |  | Array of Strategy Factor Ids. |
| `data.attributes.resources.strategyObjectives` | object |  | Strategy Objectives to be extracted. Organization Ids or Objective Ids are required. |
| `data.attributes.resources.strategyObjectives.organizationIds` | array[string] |  | Array of Organization Ids. |
| `data.attributes.resources.strategyObjectives.ids` | array[string] |  | Array of Strategy Objective Ids. |
| `data.attributes.resources.strategyCustomAttributes` | object |  | Strategy Custom Attributes to be extracted. Organization Ids or Strategy Custom Attribute Ids are required. |
| `data.attributes.resources.strategyCustomAttributes.organizationIds` | array[string] |  | Array of Organization Ids. |
| `data.attributes.resources.strategyCustomAttributes.ids` | array[string] |  | Array of Strategy Custom Attribute Ids. |
| `data.attributes.resources.strategyRiskAssurances` | object |  | Strategy Risk Assurances to be extracted. Strategy Risk Ids or ids are required |
| `data.attributes.resources.strategyRiskAssurances.strategyRiskIds` | array[string] |  | Array of Strategy Risk Ids. |
| `data.attributes.resources.strategyRiskAssurances.ids` | array[object] |  | Array of combinational ids of strategy risk assurance Id and strategy risk Id. |
| `data.attributes.resources.strategyRiskAssurances.ids.strategyRiskAssuranceId` | string |  |  |
| `data.attributes.resources.strategyRiskAssurances.ids.strategyRiskId` | string |  |  |
| `data.attributes.resources.strategyRiskObjectives` | object |  | Strategy Risk Objectives to be extracted. Strategy Risk Ids or ids are required |
| `data.attributes.resources.strategyRiskObjectives.strategyRiskIds` | array[string] |  | Array of Strategy Risk Ids. |
| `data.attributes.resources.strategyRiskObjectives.ids` | array[object] |  | Array of combinational ids of Strategy Risk Id and Strategy Objective Id. |
| `data.attributes.resources.strategyRiskObjectives.ids.strategyRiskId` | string |  |  |
| `data.attributes.resources.strategyRiskObjectives.ids.strategyObjectiveId` | string |  |  |
| `data.attributes.resources.strategyRiskMetrics` | object |  | Strategy Risk Metrics to be extracted. Strategy Risk Ids or ids are required |
| `data.attributes.resources.strategyRiskMetrics.strategyRiskIds` | array[string] |  | Array of Strategy Risk Ids. |
| `data.attributes.resources.strategyRiskMetrics.ids` | array[object] |  | Array of combinational ids of strategy risk Id and strategy risk metric Id. |
| `data.attributes.resources.strategyRiskMetrics.ids.strategyRiskMetricId` | string |  |  |
| `data.attributes.resources.strategyRiskMetrics.ids.strategyRiskId` | string |  |  |
| `data.attributes.resources.strategyRiskComments` | object |  | Strategy Risk Comments to be extracted. Strategy Risk Ids or ids are required |
| `data.attributes.resources.strategyRiskComments.strategyRiskIds` | array[string] |  | Array of Strategy Risk Ids. |
| `data.attributes.resources.strategyRiskComments.ids` | array[object] |  | Array of combinational ids of strategy risk Id and strategy risk comment Id. |
| `data.attributes.resources.strategyRiskComments.ids.strategyRiskCommentId` | string |  |  |
| `data.attributes.resources.strategyRiskComments.ids.strategyRiskId` | string |  |  |
| `data.attributes.resources.strategyRiskTags` | object |  | Strategy Risk Tags to be extracted. |
| `data.attributes.resources.strategyRiskTags.strategyRiskIds` | array[string] | ✅ | Array of Strategy Risk Ids. |

</details>

<details>
<summary><strong>Respostas</strong> (4)</summary>

<details>
<summary>`202` — Extract Started.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `CreateExtractResponse`

_Apenas campos que diferem do request body. 3 campo(s) idênticos omitidos._

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data.id` | string | ✅ | The session ID of the extraction. Ex.: `1` |
| `data.attributes.created_at` | string | ✅ | The timestamp specifying when the extract was created. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.attributes.status` | string | ✅ | The status of the extract. Ex.: `"processing"` |

</details>

<details>
<summary>`400` — Bad request.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `Errors`

Erro no formato padrão JSON:API: objeto `errors` (array) com `status` (código HTTP), `source.pointer` (JSON Pointer RFC6901 do campo com erro), `code`, `title` e `detail`.

</details>

- `401` — Bad credentials.

- `404` — Not found.

</details>
