---
id: endpoint-get-orgs-org-id-signoffs-getsignoffs
title: "Sign-offs: Get organization's sign-offs"
tags: [endpoint, sign-offs]
source: openapi.json (HighBond API v1.1.0)
---

## Sign-offs

Sign-off on work you have prepared or reviewed, and assign another person as the next reviewer

Learn more about sign-offs.

### `GET /orgs/{org_id}/signoffs` — Get organization's sign-offs

- **operationId:** `getSignoffs`
- **Domínio(s):** Sign-offs

Get a list of all sign-offs within organization.

<details>
<summary><strong>Parâmetros</strong> (15)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `fields[signoffs]` | query |  | string | Requesting the API to return only the specified fields. For more information, see Making requests Ex.: `created_at,updated_at,prepared_at,detail_reviewed_at,general_reviewed_at,supplemental_reviewed_at,specialty_reviewed_at,project,target,preparer,detail_reviewer,general_reviewer,supplemental_reviewer,specialty_reviewer,next_reviewer` |
| `include` | query |  | string | Requesting the API to return related resources. Valores: `preparer`, `detail_reviewer`, `general_reviewer`, `supplemental_reviewer`, `specialty_reviewer`, `next_reviewer`, `target`, `project` Ex.: `preparer,project` |
| `filter[project.id]` | query |  | string | Requesting the API to filter results by project ID. For more information, see Making requests Ex.: `1` |
| `filter[project.state]` | query |  | string | Requesting the API to filter results by project state. For more information, see Making requests Ex.: `active` |
| `filter[target.id]` | query |  | string | Requesting the API to filter results by target ID. For more information, see Making requests Ex.: `1` |
| `filter[target.type]` | query |  | string | Requesting the API to filter results by target type. For more information, see Making requests Ex.: `narratives` |
| `filter[preparer.id]` | query |  | string | Requesting the API to filter results by preparer UID. For more information, see Making requests Ex.: `3NQ6XzAUxqJMnAQ7n4KF` |
| `filter[detail_reviewer.id]` | query |  | string | Requesting the API to filter results by detail reviewer UID. For more information, see Making requests Ex.: `3NQ6XzAUxqJMnAQ7n4KF` |
| `filter[general_reviewer.id]` | query |  | string | Requesting the API to filter results by general reviewer UID. For more information, see Making requests Ex.: `3NQ6XzAUxqJMnAQ7n4KF` |
| `filter[supplemental_reviewer.id]` | query |  | string | Requesting the API to filter results by supplemental reviewer UID. For more information, see Making requests Ex.: `3NQ6XzAUxqJMnAQ7n4KF` |
| `filter[specialty_reviewer.id]` | query |  | string | Requesting the API to filter results by specialty reviewer UID. For more information, see Making requests Ex.: `3NQ6XzAUxqJMnAQ7n4KF` |
| `filter[next_reviewer.id]` | query |  | string | Requesting the API to filter results by next reviewer UID. For more information, see Making requests Ex.: `3NQ6XzAUxqJMnAQ7n4KF` |
| `page[size]` | query |  | string | The number of items returned per page. Default is 50. Maximum is 100. Ex.: `25` |
| `page[number]` | query |  | string | The Base64-encoded page number of records to return. Ex.: `Mg==` |

</details>

<details>
<summary><strong>Respostas</strong> (6)</summary>

<details>
<summary>`200` — OK.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `GetSignoffsResponse`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | array[object] | ✅ |  |
| `data.id` | string | ✅ | The ID of the requested resource. Ex.: `"1"` |
| `data.type` | string | ✅ | The classification of the object (`"signoffs"`). Ex.: `"signoffs"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.prepared_at` | string |  | The timestamp identifying when the signoff was prepared. Ex.: `"2021-01-18T13:17:26Z"` |
| `data.attributes.detail_reviewed_at` | string |  | The timestamp identifying when the signoff was detail reviewed. Ex.: `"2021-01-18T13:17:26Z"` |
| `data.attributes.general_reviewed_at` | string |  | The timestamp identifying when the signoff was general reviewed. Ex.: `"2021-01-18T13:17:26Z"` |
| `data.attributes.supplemental_reviewed_at` | string |  | The timestamp identifying when the signoff was supplemental reviewed. Ex.: `"2021-01-18T13:17:26Z"` |
| `data.attributes.specialty_reviewed_at` | string |  | The timestamp identifying when the signoff was specialty reviewed. Ex.: `"2021-01-18T13:17:26Z"` |
| `data.attributes.created_at` | string |  | The timestamp identifying when the signoff was created. Ex.: `"2021-01-18T13:17:26Z"` |
| `data.attributes.updated_at` | string |  | The timestamp identifying when the signoff was updated. Ex.: `"2021-01-18T13:17:26Z"` |
| `data.relationships` | object | ✅ | The relationships associated with the resource. |
| `data.relationships.preparer` | object |  | Specifies the user who signed-off as preparer |
| `data.relationships.preparer.data` | object | ✅ | The data associated with the resource. |
| `data.relationships.preparer.data.id` | string | ✅ | The unique identifier (UID) of the user. For more information on obtaining this value, see Making requests. Ex.: `"3NQ6XzAUxqJMnAQ7n4KF"` |
| `data.relationships.preparer.data.type` | string | ✅ | The classification of the object (`"users"`). Ex.: `"users"` |
| `data.relationships.detail_reviewer` | object |  | Specifies the user who signed-off as detail reviewer |
| `data.relationships.detail_reviewer.data` | object | ✅ | The data associated with the resource. |
| `data.relationships.detail_reviewer.data.id` | string | ✅ | The unique identifier (UID) of the user. For more information on obtaining this value, see Making requests. Ex.: `"3NQ6XzAUxqJMnAQ7n4KF"` |
| `data.relationships.detail_reviewer.data.type` | string | ✅ | The classification of the object (`"users"`). Ex.: `"users"` |
| `data.relationships.general_reviewer` | object |  | Specifies the user who signed-off as general reviewer |
| `data.relationships.general_reviewer.data` | object | ✅ | The data associated with the resource. |
| `data.relationships.general_reviewer.data.id` | string | ✅ | The unique identifier (UID) of the user. For more information on obtaining this value, see Making requests. Ex.: `"3NQ6XzAUxqJMnAQ7n4KF"` |
| `data.relationships.general_reviewer.data.type` | string | ✅ | The classification of the object (`"users"`). Ex.: `"users"` |
| `data.relationships.supplemental_reviewer` | object |  | Specifies the user who signed-off as supplemental reviewer |
| `data.relationships.supplemental_reviewer.data` | object | ✅ | The data associated with the resource. |
| `data.relationships.supplemental_reviewer.data.id` | string | ✅ | The unique identifier (UID) of the user. For more information on obtaining this value, see Making requests. Ex.: `"3NQ6XzAUxqJMnAQ7n4KF"` |
| `data.relationships.supplemental_reviewer.data.type` | string | ✅ | The classification of the object (`"users"`). Ex.: `"users"` |
| `data.relationships.specialty_reviewer` | object |  | Specifies the user who signed-off as specialty reviewer |
| `data.relationships.specialty_reviewer.data` | object | ✅ | The data associated with the resource. |
| `data.relationships.specialty_reviewer.data.id` | string | ✅ | The unique identifier (UID) of the user. For more information on obtaining this value, see Making requests. Ex.: `"3NQ6XzAUxqJMnAQ7n4KF"` |
| `data.relationships.specialty_reviewer.data.type` | string | ✅ | The classification of the object (`"users"`). Ex.: `"users"` |
| `data.relationships.next_reviewer` | object |  | Specifies the user who was assigned as next reviewer |
| `data.relationships.next_reviewer.data` | object | ✅ | The data associated with the resource. |
| `data.relationships.next_reviewer.data.id` | string | ✅ | The unique identifier (UID) of the user. For more information on obtaining this value, see Making requests. Ex.: `"3NQ6XzAUxqJMnAQ7n4KF"` |
| `data.relationships.next_reviewer.data.type` | string | ✅ | The classification of the object (`"users"`). Ex.: `"users"` |
| `data.relationships.project` | object |  | Each objective has an associated project or framework. Project/framework is a management system that allows you to define and compile information for reporting purposes. |
| `data.relationships.project.data` | object | ✅ | The data associated with the resource. |
| `data.relationships.project.data.id` | string | ✅ | The ID of the project. Ex.: `"1"` |
| `data.relationships.project.data.type` | string | ✅ | The classification of the object (`"projects"`). Ex.: `"projects"` |
| `data.relationships.target` | object |  | Specifies the resource which was signed-off. |
| `data.relationships.target.data` | object | ✅ | The data associated with a object. |
| `data.relationships.target.data.id` | string | ✅ | The ID of the resource. Ex.: `"1"` |
| `data.relationships.target.data.type` | string | ✅ | The classification of the object.  A target can have one of the following types: `"narratives"`, `"risk_control_matrices"`, `"walkthrough_summaries"`, `"walkthroughs"`, `"test_plans"`, `"testing_rounds"`, `"control_test_plans"`, `"control_tests"`, `"issues"`, `"project_plannings"`, `"project_results"`. Ex.: `"narratives"` |
| `links` | object |  |  |
| `links.next` | string | ✅ | Next page url Ex.: `"/api/resource?page[number]=Mw=="` |
| `links.prev` | string | ✅ | Previous page url Ex.: `null` |

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

</details>
