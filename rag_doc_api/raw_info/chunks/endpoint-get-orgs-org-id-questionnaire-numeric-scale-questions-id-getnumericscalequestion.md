---
id: endpoint-get-orgs-org-id-questionnaire-numeric-scale-questions-id-getnumericscalequestion
title: "Questionnaires: Get a numeric scale question"
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

### `GET /orgs/{org_id}/questionnaire/numeric_scale_questions/{id}` — Get a numeric scale question

- **operationId:** `getNumericScaleQuestion`
- **Domínio(s):** Questionnaires

Get information about a Numeric Scale question.

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

**Schema:** `SingleNumericScaleQuestionResponse`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | object | ✅ | The data associated with the resource. |
| `data.id` | string | ✅ | The ID of the requested resource. Ex.: `"20"` |
| `data.type` | string | ✅ | The classification of the object (`"questions"`). Ex.: `"questionnaire_items"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.text` | string |  | The main text of the question. Ex.: `"On a scale of 1 to 10, how much do you love cats?"` |
| `data.attributes.instructions` | string |  | The instructions for answering the question. Ex.: `"10 is the only right choice."` |
| `data.attributes.column_text` | string |  | The display name of the question when it appears in a table. Ex.: `"Cat love number"` |
| `data.attributes.optional` | boolean |  | Specifies whether the question is optional. Default: `False` Ex.: `false` |
| `data.attributes.scale_start` | integer |  | The start of the numeric scale. Ex.: `1` |
| `data.attributes.scale_end` | integer |  | The end of the numeric scale. Ex.: `10` |
| `data.attributes.label_left` | string |  | The label for the low end of the numeric scale. Ex.: `"This is the beginning of the scale."` |
| `data.attributes.label_center` | string |  | The label for the center of the numeric scale. Ex.: `"This is the center of the scale."` |
| `data.attributes.label_right` | string |  | The label for the high end of the numeric scale. Ex.: `"This is the end of the scale."` |
| `data.attributes.position` | integer |  | The position value determines the order of items within the questionnaire.  e.g. position value of 2 will place the numeric scale question as the second item in the questionnaire.  If the value is not provided, the numeric scale question will be appended to the end of the questionnaire. Ex.: `5` |
| `data.attributes.question_id` | integer |  | Id of the question. Ex.: `47` |
| `data.attributes.reference_id` | string |  | Unique identifier for the Numeric Scale question within the questionnaire. Ex.: `"Important-Questions"` |
| `data.attributes.weight` | number |  | Adds importance weight to numeric scale question. Ex.: `4.13` |
| `data.attributes.item_type` | string |  | The response type of the question. Ex.: `"NumericScaleQuestion"` |
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

</details>
