---
id: endpoint-delete-orgs-org-id-robots-jobs-job-id-deleterobotjobs
title: "Robot task runs: Delete robot task run"
tags: [endpoint, robot-jobs]
source: openapi.json (HighBond API v1.1.0)
---

## Robot task runs

Robot task runs, also known as robot jobs, are individual executions of a robot task. For example, for any given robot task, you can schedule a task run once every 24 hours, or you can initiate a task run manually at any time.

### `DELETE /orgs/{org_id}/robots/jobs/{job_id}` — Delete robot task run

- **operationId:** `deleteRobotJobs`
- **Domínio(s):** Robot Jobs

Delete a single robot task run.

<details>
<summary><strong>Parâmetros</strong> (2)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `job_id` | path | ✅ | string | The ID of the robot job. Ex.: `2` |

</details>

<details>
<summary><strong>Respostas</strong> (5)</summary>

- `200` — OK.

- `401` — Bad credentials.

- `403` — Forbidden.

- `404` — Not found.

<details>
<summary>`422` — Unprocessable entity.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `RobotsError`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `errors` | array[object] | ✅ |  |
| `errors.status` | string |  | A HTTP response status code indicating an unprocessable entity. Valores: `422` Ex.: `"422"` |
| `errors.source` | object |  |  |
| `errors.source.pointer` | string |  | Indicates the specific source of the error. Ex.: `"/data/attributes/name"` |
| `errors.title` | string |  | A title of the error. Ex.: `"can't be blank"` |
| `errors.detail` | string |  | A descriptive statement of the error. Ex.: `"Name can't be blank"` |

</details>

</details>
