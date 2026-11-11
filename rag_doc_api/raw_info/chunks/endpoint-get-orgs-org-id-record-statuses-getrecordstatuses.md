---
id: endpoint-get-orgs-org-id-record-statuses-getrecordstatuses
title: "Record statuses: Get record statuses"
tags: [endpoint, record-statuses]
source: openapi.json (HighBond API v1.1.0)
---

## Record statuses

A dictionary of table record statuses

### `GET /orgs/{org_id}/record_statuses` — Get record statuses

- **operationId:** `getRecordStatuses`
- **Domínio(s):** Record statuses

Get data for each record status of an organization

<details>
<summary><strong>Parâmetros</strong> (1)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |

</details>

<details>
<summary><strong>Respostas</strong> (4)</summary>

<details>
<summary>`200` — OK.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `MultiRecordStatusResponse`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | array[object] | ✅ |  |
| `data.id` | integer | ✅ | The ID of the record status Ex.: `"20"` |
| `data.type` | string | ✅ | The classification of the object (`"record_statuses"`) Ex.: `"record_statuses"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.name` | string |  | The name of the record status. Ex.: `"Open"` |
| `data.attributes.active` | boolean |  | Indicates whether the record status is active or not. Default: `True` Ex.: `true` |

</details>

- `401` — Bad credentials.

- `403` — Forbidden.

- `404` — Not found.

</details>
