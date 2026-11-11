---
id: endpoint-get-orgs-org-id-event-reports-id-geteventreport
title: "Event Reports: Get an event report"
tags: [endpoint, event-reports]
source: openapi.json (HighBond API v1.1.0)
---

## Event Reports

A event report table stores responses to a questionnaire that are distributed through an anonymous link.

Each event report table can hold a maximum of 100,000 rows, 500 columns, and 256 characters per field, including blank characters.

### `GET /orgs/{org_id}/event_reports/{id}` — Get an event report

- **operationId:** `getEventReport`
- **Domínio(s):** Event Reports

Get information about an event report.

<details>
<summary><strong>Parâmetros</strong> (2)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `id` | path | ✅ | string | The ID of the requested resource. Ex.: `9999` |

</details>

<details>
<summary><strong>Respostas</strong> (5)</summary>

<details>
<summary>`200` — OK.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `SingleEventReportResponse`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | object | ✅ | The data associated with the resource. |
| `data.id` | string | ✅ | The ID of the event report. Ex.: `"300"` |
| `data.type` | string | ✅ | The classification of the object (`"event_reports"`). Ex.: `"event_reports"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.name` | string |  | The name of the event report. Ex.: `"My first event report"` |
| `data.attributes.description` | string |  | The description of the event report. Ex.: `"Description of My first Event Report"` |
| `data.attributes.event_report_url` | string |  | The url for answering the linked questionnaire. Ex.: `"https://example.results.highbond.com/survey_responses/KUdsQzTZGjRGmiiWA4s9/edit"` |
| `data.attributes.data_table_id` | integer |  | The data table ID of the event report table. Ex.: `123` |
| `data.attributes.created_at` | string |  | The date the event report was created. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.attributes.updated_at` | string |  | The date the event report was updated. Ex.: `"2019-03-18T22:02:05Z"` |
| `data.relationships` | object | ✅ | The relationships associated with the resource. Ex.: `{"analysis": {"data": {"id": "20", "type": "analyses"}}, "questionnaire": {"data": {"id": "29", "type": "questionnaires"}}}` |
| `data.relationships.analysis` | RelationshipObject | ✅ |  |
| `data.relationships.analysis.data` | object | ✅ | The data associated with the related object. |
| `data.relationships.analysis.data.id` | string | ✅ | The ID of the related object. Ex.: `1` |
| `data.relationships.analysis.data.type` | string | ✅ | The classification of the related object. Ex.: `"collection"` |
| `data.relationships.questionnaire` | RelationshipObject | ✅ |  |
| `data.relationships.questionnaire.data` | object | ✅ | The data associated with the related object. |
| `data.relationships.questionnaire.data.id` | string | ✅ | The ID of the related object. Ex.: `1` |
| `data.relationships.questionnaire.data.type` | string | ✅ | The classification of the related object. Ex.: `"collection"` |

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

</details>
