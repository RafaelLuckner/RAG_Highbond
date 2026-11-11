---
id: endpoint-get-orgs-org-id-projects-project-id-scheduled-users-getscheduledusers
title: "Scheduled Users: Get scheduled users"
tags: [endpoint, scheduled-users]
source: openapi.json (HighBond API v1.1.0)
---

## Scheduled Users

Get a list of all of the users currently scheduled for a project.

Learn more.

### `GET /orgs/{org_id}/projects/:project_id/scheduled_users` — Get scheduled users

- **operationId:** `getScheduledUsers`
- **Domínio(s):** Scheduled Users

Get a list of scheduled users in project

<details>
<summary><strong>Parâmetros</strong> (4)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `project_id` | path | ✅ | integer | The ID of the project. Ex.: `1` |
| `page[size]` | query |  | string | The number of items returned per page. Default is 50. Maximum is 100. Ex.: `25` |
| `page[number]` | query |  | string | The Base64-encoded page number of records to return. Ex.: `Mg==` |

</details>

<details>
<summary><strong>Respostas</strong> (6)</summary>

<details>
<summary>`200` — OK.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `GetScheduledUsersResponse`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | array[object] | ✅ |  |
| `data.id` | string | ✅ | The ID of the requested resource. Ex.: `"5q7ixBfSoYeZSCDS4YAU"` |
| `data.type` | string | ✅ | The classification of the object (`"scheduled_users"`). Ex.: `"scheduled_users"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.working_days` | array[integer] |  | The numbers of working days. Ex.: `[1, 3, 5]` |
| `data.attributes.hours_per_day` | number |  | Hours per day. Ex.: `6.5` |
| `data.attributes.hourly_rate` | number |  | Hourly rate. Ex.: `15.25` |
| `links` | object |  |  |
| `links.next` | string | ✅ | Next page url Ex.: `"/projects/:project_id/scheduled_users?page[size]=5&page[number]=Mg=="` |
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
