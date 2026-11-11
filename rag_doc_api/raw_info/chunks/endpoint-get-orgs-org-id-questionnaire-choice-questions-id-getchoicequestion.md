---
id: endpoint-get-orgs-org-id-questionnaire-choice-questions-id-getchoicequestion
title: "Questionnaires: Get a choice question"
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

### `GET /orgs/{org_id}/questionnaire/choice_questions/{id}` — Get a choice question

- **operationId:** `getChoiceQuestion`
- **Domínio(s):** Questionnaires

Get information about a choice question.

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

**Schema:** `SingleChoiceQuestionResponse`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | object | ✅ | The data associated with the resource. |
| `data.id` | string | ✅ | The ID of the requested resource. Ex.: `"20"` |
| `data.type` | string | ✅ | The classification of the object (`"questions"`). Ex.: `"questionnaire_items"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.text` | string |  | The main text of the question. Ex.: `"What's the best pet in the world?"` |
| `data.attributes.instructions` | string |  | The instructions for answering the question. Ex.: `"Cat is the only right choice."` |
| `data.attributes.column_text` | string |  | The display name of the question when it appears in a table. Ex.: `"Best pet"` |
| `data.attributes.optional` | boolean |  | Specifies whether the question is optional. Default: `False` Ex.: `false` |
| `data.attributes.position` | integer |  | The position value determines the order of items within the questionnaire.  e.g. position value of 2 will place the choice question as the second item in the questionnaire.  If the value is not provided, the choice question will be appended to the end of the questionnaire. Ex.: `4` |
| `data.attributes.weight` | number |  | Adds importance weight to choice question. Ex.: `4.21` |
| `data.attributes.reference_id` | string |  | Unique identifier for the question within the questionnaire, and for the response option within the choice question. Ex.: `"Important-Questions"` |
| `data.attributes.other_value` | string |  | When spcified, respondents can provide an alternative answer if the available options do not apply to them. The text will be used as the label to this option. Ex.: `"None of the above"` |
| `data.attributes.options` | array[object] |  | The options available to choose.  Note:  1. When updating the options of a choice question, HighBond will replace all existing options and their follow up questions with the new options provided in the upload payload.  2. Follow-up questions must be existing (already created) questions.  3. Follow-up questions cannot be another choice question which has its own follow-up questions.  4. Follow-up questions cannot have more than one parent question.  5.The reference_id must be unique for each option, if the reference_id value is not null. Ex.: `[{"reference_id": "cat-option", "text": "cat", "weight": 2}, {"reference_id": "dog-option", "text": "dog", "weight": 1, "follow_up_questions": [1, ...` |
| `data.attributes.options.text` | string | ✅ | The text of an option. Ex.: `"cat"` |
| `data.attributes.options.follow_up_questions` | array[integer] |  | The IDs of the follow-up questions to an option Ex.: `[1, 2]` |
| `data.attributes.options.weight` | number |  | Adds importance weight to an option. Ex.: `4.12` |
| `data.attributes.options.reference_id` | string |  | Unique identifier for the response option within the choice question. Ex.: `"Important-Options"` |
| `data.attributes.question_id` | integer |  | Id of the question. Ex.: `77` |
| `data.attributes.item_type` | string |  | Specifies the type of the questionnaire item. Valores: `SingleChoiceQuestion`, `MultipleChoiceQuestion`, `DropdownQuestion` Ex.: `"SingleChoiceQuestion"` |
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
