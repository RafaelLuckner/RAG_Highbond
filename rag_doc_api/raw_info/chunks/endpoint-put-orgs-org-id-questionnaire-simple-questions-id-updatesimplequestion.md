---
id: endpoint-put-orgs-org-id-questionnaire-simple-questions-id-updatesimplequestion
title: "Questionnaires: Update a simple question"
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

### `PUT /orgs/{org_id}/questionnaire/simple_questions/{id}` — Update a simple question

- **operationId:** `updateSimpleQuestion`
- **Domínio(s):** Questionnaires

Make changes to an existing simple question.

<details>
<summary><strong>Parâmetros</strong> (2)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `id` | path | ✅ | string | The ID of the requested resource. Ex.: `9999` |

</details>

<details>
<summary><strong>Request body (payload)</strong></summary>

The data required to update a simple question.

**Body obrigatório.**

**Content-Type:** `application/vnd.api+json`

**Schema:** `UpdateSimpleQuestionPayload`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | object | ✅ | The data associated with the resource. |
| `data.id` | string | ✅ | The ID of the requested resource. Ex.: `"20"` |
| `data.type` | string | ✅ | The classification of the object (`"questions"`). Ex.: `"questionnaire_items"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.text` | string |  | The simple question text. Ex.: `"What is your email?"` |
| `data.attributes.instructions` | string |  | The instructions for answering the question. Ex.: `"Please provide your work email."` |
| `data.attributes.column_text` | string |  | The column display name in linked tables. Ex.: `"email"` |
| `data.attributes.optional` | boolean |  | Specifies whether the question is optional. Default: `False` Ex.: `false` |
| `data.attributes.position` | integer |  | The position value determines the order of items within the questionnaire.  e.g. position value of 2 will place the simple question as the second item in the questionnaire.  If the value is not provided, the simple question will be appended to the end of the questionnaire. Ex.: `8` |
| `data.attributes.question_id` | integer |  | Id of the question. Ex.: `42` |
| `data.attributes.reference_id` | string |  | Unique identifier for the Simple question within the questionnaire. Ex.: `"Important-Questions"` |
| `data.attributes.weight` | number |  | Adds importance weight to simple question. Ex.: `4.13` |

</details>

<details>
<summary><strong>Respostas</strong> (7)</summary>

<details>
<summary>`200` — OK.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `SingleSimpleQuestionResponse`

_Apenas campos que diferem do request body. 12 campo(s) idênticos omitidos._

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data.attributes.item_type` | string |  | Specifies the type of the questionnaire item. Valores: `ParagraphTextQuestion`, `AttachmentQuestion`, `TextQuestion`, `EmailQuestion`, `NumericQuestion`, `DateQuestion`, `DigitalSignatureQuestion` Ex.: `"EmailQuestion"` |
| `data.attributes.created_at` | string |  | The date the question was created. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.attributes.updated_at` | string |  | The date the question was updated. Ex.: `"2019-03-18T22:02:05Z"` |
| `data.relationships` | object | ✅ | The relationships associated with the resource. Ex.: `{"questionnaire": {"data": {"id": "1", "type": "questionnaires"}}}` |
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
