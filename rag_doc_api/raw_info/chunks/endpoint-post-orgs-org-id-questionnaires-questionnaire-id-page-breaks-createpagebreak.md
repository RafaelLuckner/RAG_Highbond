---
id: endpoint-post-orgs-org-id-questionnaires-questionnaire-id-page-breaks-createpagebreak
title: "Questionnaires: Create a page break"
tags: [endpoint, questionnaires]
source: openapi.json (HighBond API v1.1.0)
---

## Questionnaires

Questionnaires are used to gather information from respondents and contextualize data. Each Collection can have one or more questionnaires that you deploy as surveys,
event reports, or as follow-up mechanisms when remediating records.

Your organization can have a maximum of 14,000 questionnaires and each questionnaire can hold a maximum of 900 questions, including page breaks and sections.

Learn more about questionnaires.

Questionnaires consist of a series of question and layout components. Please use the dedicated endpoints to manage these components:

- **Question Type**
  * `Numeric Scale` Question
  * Simple Question:
    - `Short Answer`
    - `Paragraph`
    - `Numeric`
    - `Date`
    - `Email`
    - `Attachment`
    - `Digital Signature`
  * Choice Question
    - `Single Choice`
    - `Dropdown`
    - `Multiple Choice`
- **Layout Type**
  * `Page Break`
  * `Section`

> **Note:**
>
> 1. Only not archived questionnaires can be managed by this set of APIs.
> 2. Only HighBond System Admins are authorized to manage questionnaires via this set of APIs.

### `POST /orgs/{org_id}/questionnaires/{questionnaire_id}/page_breaks` — Create a page break

- **operationId:** `createPageBreak`
- **Domínio(s):** Questionnaires

Create a new questionnaire page break in an existing questionnaire.

> **Note**: - Request body is **optional** when creating a Page Break.
>
> When absent, the new page break will be appended to bottom of the items in the questionnaire.
>
> When present, the `position` value must be provided according to the schema.

<details>
<summary><strong>Parâmetros</strong> (2)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `questionnaire_id` | path | ✅ | string | The ID of the questionnaire. Ex.: `10` |

</details>

<details>
<summary><strong>Request body (payload)</strong></summary>

The data required to create a page break.

**Content-Type:** `application/vnd.api+json`

**Schema:** `CreatePageBreakPayload`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | object | ✅ | The data associated with the resource. |
| `data.type` | string | ✅ | The classification of the object (`"page_breaks"`). Ex.: `"questionnaire_items"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.position` | integer | ✅ | The position value determines the order of items within the questionnaire.  e.g. position value of 2 will place the page break as the second item in the questionnaire.  If the value is not provided, the page break will be appended to the end of the questionnaire. Ex.: `2` |
| `data.attributes.reference_id` | string |  | Unique identifier for the Page Break within the questionnaire. Ex.: `"Important-Page-Break"` |

</details>

<details>
<summary><strong>Respostas</strong> (6)</summary>

<details>
<summary>`201` — Created.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `SinglePageBreakResponse`

_Apenas campos que diferem do request body. 4 campo(s) idênticos omitidos._

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data.id` | string | ✅ | The ID of the requested resource. Ex.: `"20"` |
| `data.attributes.position` | integer |  | The position value determines the order of items within the questionnaire.  e.g. position value of 2 will place the page break as the second item in the questionnaire.  If the value is not provided, the page break will be appended to the end of the questionnaire. Ex.: `2` |
| `data.attributes.item_type` | string |  | The type of the questionnaire item. Ex.: `"PageBreak"` |
| `data.attributes.created_at` | string |  | The date the page break was created. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.attributes.updated_at` | string |  | The date the page break was updated. Ex.: `"2019-03-18T22:02:05Z"` |
| `data.relationships` | object | ✅ | The relationships associated with the resource. Ex.: `{"questionnaire": {"data": {"id": "1", "type": "questionnaires"}}}` |
| `data.relationships.questionnaire` | RelationshipObject | ✅ |  |
| `data.relationships.questionnaire.data` | object | ✅ | The data associated with the related object. |
| `data.relationships.questionnaire.data.id` | string | ✅ | The ID of the related object. Ex.: `1` |
| `data.relationships.questionnaire.data.type` | string | ✅ | The classification of the related object. Ex.: `"collection"` |

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

<details>
<summary>`422` — Unprocessable entity.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `Errors`

Erro no formato padrão JSON:API: objeto `errors` (array) com `status` (código HTTP), `source.pointer` (JSON Pointer RFC6901 do campo com erro), `code`, `title` e `detail`.

</details>

</details>
