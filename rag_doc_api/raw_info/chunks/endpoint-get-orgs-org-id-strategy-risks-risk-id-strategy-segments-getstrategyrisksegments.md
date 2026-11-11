---
id: endpoint-get-orgs-org-id-strategy-risks-risk-id-strategy-segments-getstrategyrisksegments
title: "Strategy: Get risk segments"
tags: [endpoint, strategy]
source: openapi.json (HighBond API v1.1.0)
---

## Strategy

You can use the Strategy app to identify, assess, and monitor strategic risks.

Learn more.

### `GET /orgs/{org_id}/strategy_risks/{risk_id}/strategy_segments` — Get risk segments

- **operationId:** `getStrategyRiskSegments`
- **Domínio(s):** Strategy

Retrieves the full list of the risks's operating segments from
Strategy.

An operating segment is a region, business unit, division, location, or entity across which strategic risks are assessed.
The organization's operating segments can be accessed with the
Segments resource.

<details>
<summary><strong>Parâmetros</strong> (4)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `risk_id` | path | ✅ | integer | The ID of the risk. Ex.: `1` |
| `page[size]` | query |  | string | The number of items returned per page. Default is 20. Maximum is 100. Ex.: `10` |
| `page[number]` | query |  | string | The Base64-encoded page number of records to return. Ex.: `Mg==` |

</details>

<details>
<summary><strong>Respostas</strong> (5)</summary>

<details>
<summary>`200` — OK.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `GetStrategyRiskSegmentsResponse`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `links` | object | ✅ |  |
| `links.next` | string | ✅ | Next page url Ex.: `"/v1/orgs/1/strategy_risks/1/strategy_segments?page[number]=Mg=="` |
| `links.prev` | string | ✅ | Previous page url Ex.: `null` |
| `data` | array[object] | ✅ | Array of segments |
| `data.id` | string | ✅ | The ID of the requested resource. Ex.: `"101"` |
| `data.type` | string | ✅ | The classification of the object (`"strategy_segments"`). Ex.: `"strategy_segments"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.name` | string |  | The name of the segment. Ex.: `"EMEA"` |
| `data.attributes.created_at` | string |  | The timestamp identifying when the segment was created. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.attributes.updated_at` | string |  | The timestamp identifying when the segment was last updated. Ex.: `"2019-02-09T13:17:26Z"` |

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
