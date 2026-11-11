---
id: endpoint-get-orgs-org-id-time-entry-categories-id-gettimeentrycategory
title: "Non-project time categories: Get information about a non-project time category."
tags: [endpoint, non-project-time-categories]
source: openapi.json (HighBond API v1.1.0)
---

## Non-project time categories

Use non-project time categories to divide non-project time entries by categories.

Learn more about non-project time categories.

### `GET /orgs/{org_id}/time_entry_categories/{id}` — Get information about a non-project time category.

- **operationId:** `getTimeEntryCategory`
- **Domínio(s):** Non-project time categories

<details>
<summary><strong>Parâmetros</strong> (2)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `id` | path | ✅ | string | The ID of the requested resource. Ex.: `9999` |

</details>

<details>
<summary><strong>Respostas</strong> (4)</summary>

<details>
<summary>`200` — OK.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `GetTimeEntryCategoryResponse`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | object | ✅ | The data associated with the resource. |
| `data.id` | string | ✅ | The ID of the requested resource. Ex.: `"1"` |
| `data.type` | string | ✅ | The classification of the object (`"time_entry_categories"`). Ex.: `"time_entry_categories"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.name` | string | ✅ | The name of the time entry category. Ex.: `"Administration"` |
| `data.attributes.position` | integer |  | The value that determines the order in which it is displayed in the index action. `position` must be a value between `1` and `2147483647`. Ex.: `1` |
| `data.attributes.active` | boolean |  | The value that determines if the time entry category is active. Ex.: `true` |
| `data.attributes.created_at` | string |  | The timestamp identifying when the time entry category was created. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.attributes.updated_at` | string |  | The timestamp identifying when the time entry category was last updated. Ex.: `"2019-02-09T13:17:26Z"` |

</details>

- `401` — Bad credentials.

- `403` — Forbidden.

- `404` — Not found.

</details>
