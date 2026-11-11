---
id: endpoint-get-orgs-org-id-extract-session-id-getextract
title: "Extract: Get extract information"
tags: [endpoint, extract]
source: openapi.json (HighBond API v1.1.0)
---

## Extract

Service to extract the resources from an organization based on resource ids.

### `GET /orgs/{org_id}/extract/{session_id}` — Get extract information

- **operationId:** `getExtract`
- **Domínio(s):** Extract

Get signed URL for generated terraform or json scripts.

<details>
<summary><strong>Parâmetros</strong> (2)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `session_id` | path | ✅ | string | The session_id of the extract. Ex.: `183dabb4-cf04-480e-94d7-8bc94f957ef6` |

</details>

<details>
<summary><strong>Respostas</strong> (4)</summary>

<details>
<summary>`200` — OK.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `GetExtractResponse`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | object | ✅ | The data associated with the resource. |
| `data.id` | string | ✅ | The session ID of the extraction. Ex.: `1` |
| `data.type` | string | ✅ | The classification of the object (`extract`). Ex.: `"extract"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.created_at` | string | ✅ | The timestamp specifying when the extract was created. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.attributes.status` | string | ✅ | The status of the extract.Can have one of the following values - success, inprogress, error Ex.: `"success"` |
| `data.attributes.signed_url` | string |  | The signed URL of the generated terraform scripts. Ex.: `"https://sdk-services-us-west-2-bucket.s3.us-west-2.amazonaws.com/17d16331-4c31-4068-a306-92d6802cf53c/output.zip?AWSAccessKeyId=ASIAQJYX73ZJPU4S7K...` |

</details>

<details>
<summary>`400` — Bad request.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `Errors`

Erro no formato padrão JSON:API: objeto `errors` (array) com `status` (código HTTP), `source.pointer` (JSON Pointer RFC6901 do campo com erro), `code`, `title` e `detail`.

</details>

- `401` — Bad credentials.

- `404` — Not found.

</details>
