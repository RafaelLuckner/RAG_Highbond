---
id: endpoint-get-orgs-org-id-strategy-risks-risk-id-strategy-comments-getstrategyriskcomments
title: "Strategy: Get risk comments"
tags: [endpoint, strategy]
source: openapi.json (HighBond API v1.1.0)
---

## Strategy

You can use the Strategy app to identify, assess, and monitor strategic risks.

Learn more.

### `GET /orgs/{org_id}/strategy_risks/{risk_id}/strategy_comments` — Get risk comments

- **operationId:** `getStrategyRiskComments`
- **Domínio(s):** Strategy

Retrieves the list of comments on the discussion tab for the current risk from
Strategy.

Comments can have multiple file attachments. These can be retrieved via the
Comment resource.

The `user_id` points to the user's unique identifier who created the comment.
The User resource can be used to get information about
this user. It can be empty if the user has been removed from the organization.

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

**Schema:** `GetStrategyRiskCommentsResponse`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `links` | object | ✅ |  |
| `links.next` | string | ✅ | Next page url Ex.: `"/v1/orgs/1/strategy_risks/1/strategy_comments?page[number]=Mg=="` |
| `links.prev` | string | ✅ | Previous page url Ex.: `null` |
| `data` | array[object] | ✅ | Array of comments |
| `data.id` | string | ✅ | The ID of the requested resource. Ex.: `"781"` |
| `data.type` | string | ✅ | The classification of the object (`"strategy_comments"`). Ex.: `"strategy_comments"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.text` | string |  | Content of the comment Ex.: `"This risk requires more context."` |
| `data.attributes.user_id` | string |  | The identifier for the user who made the comment Ex.: `"407188"` |
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
