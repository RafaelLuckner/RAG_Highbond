---
id: endpoint-put-orgs-org-id-questionnaire-sections-id-updatesection
title: "Questionnaires: Update a section"
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

### `PUT /orgs/{org_id}/questionnaire/sections/{id}` — Update a section

- **operationId:** `updateSection`
- **Domínio(s):** Questionnaires

Make changes to a questionnaire section, like renaming it.

<details>
<summary><strong>Parâmetros</strong> (2)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `id` | path | ✅ | string | The ID of the requested resource. Ex.: `9999` |

</details>

<details>
<summary><strong>Request body (payload)</strong></summary>

The data required to update a questionnaire section.

**Body obrigatório.**

**Content-Type:** `application/vnd.api+json`

**Schema:** `UpdateSectionPayload`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | object | ✅ | The data associated with the resource. |
| `data.id` | string | ✅ | The ID of the requested resource. Ex.: `"20"` |
| `data.type` | string | ✅ | The classification of the object (`"questions"`). Ex.: `"questionnaire_items"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.name` | string |  | The name of the section. Ex.: `"Section One"` |
| `data.attributes.description` | string |  | The description of the section. Ex.: `"This section is related to health care."` |
| `data.attributes.position` | integer |  | The position value determines the order of items within the questionnaire.  e.g. position value of 2 will place the section as the second item in the questionnaire.  If the value is not provided, the section will be appended to the end of the questionnaire. Ex.: `8` |
| `data.attributes.reference_id` | string |  | Unique identifier for the Section within the questionnaire. Ex.: `"Important-Section-Headers"` |

</details>

<details>
<summary><strong>Respostas</strong> (7)</summary>

<details>
<summary>`200` — OK.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `SingleSectionResponse`

_Apenas campos que diferem do request body. 7 campo(s) idênticos omitidos._

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data.type` | string | ✅ | The classification of the object (`"sections"`). Ex.: `"questionnaire_items"` |
| `data.attributes.item_type` | string |  | The type of the questionnaire item. Ex.: `"SectionHeader"` |
| `data.attributes.created_at` | string |  | The date the section layout was created. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.attributes.updated_at` | string |  | The date the section layout was updated. Ex.: `"2019-03-18T22:02:05Z"` |
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
