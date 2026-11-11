---
id: endpoint-get-orgs-org-id-strategy-risks-risk-id-strategy-comments-id-getstrategyriskcomme
title: "Strategy: Get a risk comment"
tags: [endpoint, strategy]
source: openapi.json (HighBond API v1.1.0)
---

## Strategy

You can use the Strategy app to identify, assess, and monitor strategic risks.

Learn more.

### `GET /orgs/{org_id}/strategy_risks/{risk_id}/strategy_comments/{id}` — Get a risk comment

- **operationId:** `getStrategyRiskComment`
- **Domínio(s):** Strategy

Get information about a comment and its attachments.

<details>
<summary><strong>Parâmetros</strong> (3)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `risk_id` | path | ✅ | integer | The ID of the risk. Ex.: `1` |
| `id` | path | ✅ | string | The ID of the requested resource. Ex.: `9999` |

</details>

<details>
<summary><strong>Respostas</strong> (5)</summary>

<details>
<summary>`200` — OK.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `GetStrategyRiskCommentResponse`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | object | ✅ | The data associated with the resource. |
| `data.id` | string | ✅ | The ID of the requested resource. Ex.: `"781"` |
| `data.type` | string | ✅ | The classification of the object (`"strategy_comments"`). Ex.: `"strategy_comments"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.text` | string |  | Content of the comment. Ex.: `"This risk requires more context."` |
| `data.attributes.user_id` | string |  | The identifier for the user who made the comment. Ex.: `"407188"` |
| `data.attributes.attachments` | array[object] |  | Attachments uploaded to the comment. |
| `data.attributes.attachments.id` | string |  | The ID of the attachment. Ex.: `"1507"` |
| `data.attributes.attachments.url` | string |  | The URL of the attached file. Ex.: `"https://risks.s3.amazonaws.com/uploads/attachment/file/1507/Screenshot..."` |
| `data.attributes.attachments.name` | string |  | The name of the file as it was uploaded. Ex.: `"Screenshot_2023-06-20_at_10.36.19.png"` |
| `data.attributes.attachments.created_at` | string |  | The timestamp identifying when the attachment was created. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.attributes.attachments.updated_at` | string |  | The timestamp identifying when the attachment was last updated. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.attributes.created_at` | string |  | The timestamp identifying when the comment was created. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.attributes.updated_at` | string |  | The timestamp identifying when the comment was last updated. Ex.: `"2019-02-09T13:17:26Z"` |

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
