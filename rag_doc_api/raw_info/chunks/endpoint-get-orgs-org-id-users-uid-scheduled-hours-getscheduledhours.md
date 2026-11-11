---
id: endpoint-get-orgs-org-id-users-uid-scheduled-hours-getscheduledhours
title: "Scheduled Hours: Get scheduled hours"
tags: [endpoint, scheduled-hours]
source: openapi.json (HighBond API v1.1.0)
---

## Scheduled Hours

Get the hours a user is currently scheduled for.

Learn more.

### `GET /orgs/{org_id}/users/:uid/scheduled_hours` — Get scheduled hours

- **operationId:** `getScheduledHours`
- **Domínio(s):** Scheduled Hours

Get scheduled hours for the user

<details>
<summary><strong>Parâmetros</strong> (9)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `uid` | path | ✅ | string | The UID of the user. Ex.: `yvqdNCtv8TeM47WQtzau` |
| `filter[date][start]` | query |  | string | Requesting the API to filter results by start date. For more information, see Making requests Ex.: `2021-04-28` |
| `filter[date][end]` | query |  | string | Requesting the API to filter results by end date. For more information, see Making requests Ex.: `2021-04-30` |
| `filter[schedule_type]` | query |  | string | Requesting the API to filter results by schedule type. For more information, see Making requests Values can be:   * `project` - for getting project schedules   * `non_project` - for getting non project schedules Ex.: `project` |
| `filter[scheduled_project_id]` | query |  | string | Requesting the API to filter results by scheduled project IDs. For more information, see Making requests Ex.: `1,2,3` |
| `fields[scheduled_hours]` | query |  | string | Requesting the API to return only the specified fields. For more information, see Making requests Ex.: `schedule_type,time_category,hours_per_day,start_date,end_date,scheduled_project` |
| `page[size]` | query |  | string | The number of items returned per page. Default is 50. Maximum is 100. Ex.: `25` |
| `page[number]` | query |  | string | The Base64-encoded page number of records to return. Ex.: `Mg==` |

</details>

<details>
<summary><strong>Respostas</strong> (6)</summary>

<details>
<summary>`200` — OK.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `GetScheduledHoursResponse`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | array[object] | ✅ |  |
| `data.id` | string | ✅ | The ID of the requested resource. Ex.: `"1"` |
| `data.type` | string | ✅ | The classification of the object (`"scheduled_hours"`). Ex.: `"scheduled_hours"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.schedule_type` | string |  | Schedule type. Can be planning, fieldwork, results, non project Ex.: `"planning"` |
| `data.attributes.time_category` | string |  | Time entry category. Present only for non project schedules. Ex.: `"Leave/Vacation"` |
| `data.attributes.hours_per_day` | integer |  | Scheduled hours Ex.: `6` |
| `data.attributes.start_date` | string |  | The date specifying when the schedule for the project begins. Ex.: `"2021-11-16"` |
| `data.attributes.end_date` | string |  | The date specifying when the schedule for the project ends. Ex.: `"2021-12-01"` |
| `data.relationships` | object |  | The relationships associated with the resource. |
| `data.relationships.scheduled_project` | object |  | Scheduled project object. |
| `data.relationships.scheduled_project.data` | object | ✅ | The data associated with the resource. |
| `data.relationships.scheduled_project.data.id` | string | ✅ | The ID of the requested resource. Ex.: `"1"` |
| `data.relationships.scheduled_project.data.type` | string | ✅ | The classification of the object (`"scheduled_projects"`). Ex.: `"scheduled_projects"` |
| `links` | object |  |  |
| `links.next` | string | ✅ | Next page url Ex.: `"/users/:uid/scheduled_hours?page[size]=5&page[number]=Mg=="` |
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
