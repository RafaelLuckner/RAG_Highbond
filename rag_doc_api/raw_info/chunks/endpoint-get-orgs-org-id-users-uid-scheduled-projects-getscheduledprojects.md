---
id: endpoint-get-orgs-org-id-users-uid-scheduled-projects-getscheduledprojects
title: "Scheduled Projects: Get scheduled projects"
tags: [endpoint, scheduled-projects]
source: openapi.json (HighBond API v1.1.0)
---

## Scheduled Projects

Get the list of projects a user is scheduled for, and the projects' start and end dates.

Learn more.

### `GET /orgs/{org_id}/users/:uid/scheduled_projects` — Get scheduled projects

- **operationId:** `getScheduledProjects`
- **Domínio(s):** Scheduled Projects

Get a list of scheduled projects for the user

<details>
<summary><strong>Parâmetros</strong> (7)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `uid` | path | ✅ | string | The UID of the user. Ex.: `yvqdNCtv8TeM47WQtzau` |
| `filter[date][start]` | query |  | string | Requesting the API to filter results by start date. For more information, see Making requests Ex.: `2021-04-28` |
| `filter[date][end]` | query |  | string | Requesting the API to filter results by end date. For more information, see Making requests Ex.: `2021-04-30` |
| `filter[scheduled_project_state]` | query |  | string | Requesting the API to filter results by scheduler project state. For more information, see Making requests Ex.: `active` |
| `page[size]` | query |  | string | The number of items returned per page. Default is 50. Maximum is 100. Ex.: `25` |
| `page[number]` | query |  | string | The Base64-encoded page number of records to return. Ex.: `Mg==` |

</details>

<details>
<summary><strong>Respostas</strong> (6)</summary>

<details>
<summary>`200` — OK.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `GetScheduledProjectsResponse`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | array[object] | ✅ |  |
| `data.id` | string | ✅ | The ID of the requested resource. Ex.: `"1"` |
| `data.type` | string | ✅ | The classification of the object (`"scheduled_projects"`). Ex.: `"scheduled_projects"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.start_date` | string |  | The date specifying when the schedule for the project begins. Ex.: `"2021-11-16"` |
| `data.attributes.end_date` | string |  | The date specifying when the schedule for the project ends. Ex.: `"2021-12-01"` |
| `links` | object |  |  |
| `links.next` | string | ✅ | Next page url Ex.: `"/users/:uid/scheduled_projects?page[size]=5&page[number]=Mg=="` |
| `links.prev` | string | ✅ | Previous page url Ex.: `null` |

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
