---
id: endpoint-get-orgs-org-id-robots-folders-folder-id-robots-getrobotsinfolder
title: "Robots Folders: List Robots in a Folder"
tags: [endpoint, robots-folders]
source: openapi.json (HighBond API v1.1.0)
---

## Robots Folders

Folders to organize Robots.

### `GET /orgs/{org_id}/robots_folders/{folder_id}/robots` — List Robots in a Folder

- **operationId:** `getRobotsInFolder`
- **Domínio(s):** Robots Folders

List Robots in a Folder.

<details>
<summary><strong>Parâmetros</strong> (2)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `folder_id` | path | ✅ | number | The ID of the folder. Ex.: `2` |

</details>

<details>
<summary><strong>Respostas</strong> (4)</summary>

<details>
<summary>`200` — Success.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `ListRobotsInFolderResponse`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | array[object] |  | The data associated with the resource. |
| `data.id` | number |  | The Folder ID. Ex.: `1` |
| `data.type` | string |  | The classification of the object (`"robot"`). Ex.: `"robot"` |
| `data.attributes` | object |  | The attributes associated with the resource. |
| `data.attributes.active_app_version` | number |  | The active version of the robot. Ex.: `1` |
| `data.attributes.app_versions_count` | number |  | The number of script versions committed to the robot. Ex.: `1` |
| `data.attributes.automated` | boolean |  | Is the robot automated. Ex.: `false` |
| `data.attributes.category` | string |  | The category of the robot. Valores: `acl`, `highbond`, `workflow` Default: `acl` Ex.: `"workflow"` |
| `data.attributes.count` | number |  | The number of robots in the account. Ex.: `1` |
| `data.attributes.created_at` | string |  | Date when the robot was created. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.attributes.description` | string |  | The description of the robot. Ex.: `"Sample description"` |
| `data.attributes.delete_failed` | boolean |  | Specifies if the robot deletion failed. Ex.: `false` |
| `data.attributes.discarded_at` | string |  | Date when the robot was discarded. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.attributes.kept_tasks_count` | number |  | The number of tasks associated with the robot. Ex.: `1` |
| `data.attributes.last_committed_at` | string |  | Date when the robot was last committed. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.attributes.last_run_at` | string |  | Date when the robot was last run. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.attributes.name` | string |  | The name of the robot. Ex.: `"R2D2"` |
| `data.attributes.production_updated_at` | string |  | Date when the Production tab was last updated. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.attributes.share_tables_in_development` | boolean |  | Specifies if the robot shares tables in the Development tab. Ex.: `false` |
| `data.attributes.share_tables_in_production` | boolean |  | Specifies if the robot shares tables in the Production tab. Ex.: `false` |
| `data.relationships` | object |  |  |
| `data.relationships.folder` | object |  | The folder associated with the robot. |
| `data.relationships.folder.data` | object |  | The data associated with the resource. |
| `data.relationships.folder.data.id` | number |  | The Folder ID. Ex.: `1` |
| `data.relationships.folder.data.type` | string |  | The classification of the object (`"folder"`). Ex.: `"folder"` |

</details>

- `401` — Bad credentials.

- `403` — Forbidden.

- `404` — Not found.

</details>
