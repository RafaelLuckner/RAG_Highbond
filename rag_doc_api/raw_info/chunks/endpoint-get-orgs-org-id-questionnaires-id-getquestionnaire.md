---
id: endpoint-get-orgs-org-id-questionnaires-id-getquestionnaire
title: "Questionnaires: Get a questionnaire"
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

### `GET /orgs/{org_id}/questionnaires/{id}` — Get a questionnaire

- **operationId:** `getQuestionnaire`
- **Domínio(s):** Questionnaires

Get information about a questionnaire.

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

**Schema:** `SingleQuestionnaireResponse`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | object | ✅ | The data associated with the resource. |
| `data.id` | string | ✅ | The ID of the requested resource. Ex.: `"20"` |
| `data.type` | string | ✅ | The classification of the object (`"questionnaires"`). Ex.: `"questionnaires"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.name` | string |  | The name of the questionnaire. Ex.: `"My first Questionnaire"` |
| `data.attributes.instruction` | string |  | Specifies the instructions for those individuals receiving your questionnaire. Ex.: `"Please complete the training before filling out this questionnaire."` |
| `data.attributes.position` | integer |  | The position of the questionnaire in a collection. Ex.: `55` |
| `data.attributes.resubmittable` | boolean |  | To allow users to submit updated responses to previously assigned questionnaires without supplying an explanatory comment. Default: `False` Ex.: `false` |
| `data.attributes.respondent_view` | string |  | Specifies whether recipients should see information about specific records. Valores: `all_records`, `select_records`, `no_records` Default: `all_records` |
| `data.attributes.email_subject` | string |  | The subject of the email notification to respondents when a questionnaire is sent. If an email_subject value is not specified, there will be a default email subject. Ex.: `"Respond to My first Questionnaire"` |
| `data.attributes.email_message` | string |  | The content of the email notification to respondents when a questionnaire is sent. If an email_message value is not specified, there will be a default email message body. Ex.: `"Test Collection has requested that you complete a questionnaire."` |
| `data.attributes.linked_tables_ids` | array[integer] |  | The IDs of the linked tables. Ex.: `[1, 3, 5]` |
| `data.attributes.linked_tables_only` | boolean |  | Specifies whether only allow this questionnaire to be sent from linked tables for all roles. Default: `False` Ex.: `false` |
| `data.attributes.weighting` | boolean |  | Specifies whether the questionnaire supports weighted questions and responses. Ex.: `false` |
| `data.attributes.reference_id` | string |  | Unique identifier for the questionnaire within the collection, for the question within the questionnaire, and for the response option within the choice question. Ex.: `"important-questionnaire"` |
| `data.attributes.locale` | string |  | A locale for questionnaire system labels. The available locales are `"en"`, `"de"`, `"es"`, `"fr"`, `"pt"`, `"ja"`, `"zh"`, `"el"`, `"it"`, `"pl"`, `"ro"`, `"ru"`, `"uk"` Ex.: `"pl"` |
| `data.attributes.surveys_ids` | array[integer] |  | The IDs of the surveys that use this questionnaire as the primary questionnaire. Ex.: `[1, 3]` |
| `data.attributes.created_at` | string |  | The date the questionnaire was created. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.attributes.updated_at` | string |  | The date the questionnaire was updated. Ex.: `"2019-03-18T22:02:05Z"` |
| `data.relationships` | object | ✅ | The relationships associated with the resource. Ex.: `{"collection": {"data": {"id": "1", "type": "collections"}}}` |
| `data.relationships.collection` | RelationshipObject | ✅ |  |
| `data.relationships.collection.data` | object | ✅ | The data associated with the related object. |
| `data.relationships.collection.data.id` | string | ✅ | The ID of the related object. Ex.: `1` |
| `data.relationships.collection.data.type` | string | ✅ | The classification of the related object. Ex.: `"collection"` |

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
