---
id: endpoint-delete-orgs-org-id-robots-id-deleterobot
title: "Robots: Delete a robot"
tags: [endpoint, robots]
source: openapi.json (HighBond API v1.1.0)
---

## Robots

A robot is a tool that lets you automate repetitive tasks using scripts built in Analytics. Once you create the scripts, you upload them to a robot in the Robots app
and configure the task automation that you need. The robot then handles the recurring tasks according to your configuration.

Learn more about robots.

### `DELETE /orgs/{org_id}/robots/{id}` — Delete a robot

- **operationId:** `deleteRobot`
- **Domínio(s):** Robots

Permanently delete a robot.

> **Caution —**
Deleting a robot also permanently deletes any associated tasks.

<details>
<summary><strong>Parâmetros</strong> (2)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `id` | path | ✅ | string | The ID of the requested resource. Ex.: `9999` |

</details>

<details>
<summary><strong>Respostas</strong> (6)</summary>

<details>
<summary>`200` — Deleted.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `GetRobotResponse`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | Robot | ✅ |  |
| `data.id` | string | ✅ | The ID of the robot. Ex.: `1` |
| `data.type` | string | ✅ | The classification of the object (`"robot"`). Ex.: `"robot"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.active_app_version` | number |  | The active version of the robot. Ex.: `1` |
| `data.attributes.app_versions_count` | number |  | The number of script versions committed to the robot. Ex.: `1` |
| `data.attributes.automated` | boolean |  | Is the robot automated. Ex.: `false` |
| `data.attributes.category` | string |  | The category of the robot. Valores: `acl`, `highbond`, `workflow` Default: `acl` Ex.: `"workflow"` |
| `data.attributes.count` | number |  | The number of robots in the account. Ex.: `1` |
| `data.attributes.created_at` | string |  | Date when the robot was created. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.attributes.description` | string |  | The description of the robot. Ex.: `"Sample description"` |
| `data.attributes.delete_failed` | boolean |  | Specifies if the robot deletion failed. Ex.: `false` |
| `data.attributes.discarded_at` | string |  | Date when the robot was discarded. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.attributes.folder_id` | number |  | The Folder ID. Ex.: `1` |
| `data.attributes.kept_tasks_count` | number |  | The number of tasks associated with the robot. Ex.: `1` |
| `data.attributes.last_committed_at` | string |  | Date when the robot was last committed. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.attributes.last_run_at` | string |  | Date when the robot was last run. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.attributes.name` | string | ✅ | The name of the robot. Ex.: `"R2D2"` |
| `data.attributes.production_updated_at` | string |  | Date when the Production tab was last updated. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.attributes.share_tables_in_development` | boolean |  | Specifies if the robot shares tables in the Development tab. Ex.: `false` |
| `data.attributes.share_tables_in_production` | boolean |  | Specifies if the robot shares tables in the Production tab. Ex.: `false` |

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
