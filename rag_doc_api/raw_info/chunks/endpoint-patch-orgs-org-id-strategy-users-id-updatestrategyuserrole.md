---
id: endpoint-patch-orgs-org-id-strategy-users-id-updatestrategyuserrole
title: "Strategy: Update a user role"
tags: [endpoint, strategy]
source: openapi.json (HighBond API v1.1.0)
---

## Strategy

You can use the Strategy app to identify, assess, and monitor strategic risks.

Learn more.

### `PATCH /orgs/{org_id}/strategy_users/{id}` — Update a user role

- **operationId:** `updateStrategyUserRole`
- **Domínio(s):** Strategy

Make changes to a user's role.

The `role` attribute is required and must be one of the following values:
- `admin`
- `executive`
- `reviewer`
- `no_access`

<details>
<summary><strong>Parâmetros</strong> (2)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `id` | path | ✅ | string | The ID of the requested resource. Ex.: `9999` |

</details>

<details>
<summary><strong>Request body (payload)</strong></summary>

The data required to update a user role.

**Body obrigatório.**

**Content-Type:** `application/vnd.api+json`

**Schema:** `UpdateStrategyUserRoleRequest`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | object | ✅ | The data associated with the resource. |
| `data.type` | string | ✅ | The classification of the object (`"strategy_users"`). Ex.: `"strategy_users"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.role` | string |  | Valores: `admin`, `executive`, `reviewer`, `no_access` Ex.: `"admin"` |

</details>

<details>
<summary><strong>Respostas</strong> (7)</summary>

<details>
<summary>`200` — OK.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `UpdateStrategyUserRoleResponse`

_Apenas campos que diferem do request body. 4 campo(s) idênticos omitidos._

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data.attributes.name` | string |  | Full name of the user. Ex.: `"John Doe"` |
| `data.attributes.email` | string |  | The email address of the user. Ex.: `"johndoe@riskybusiness.com"` |
| `data.attributes.grc_role` | string |  | Ex.: `""` |
| `data.attributes.user_type` | string |  | The type of the user. Ex.: `"user"` |
| `data.attributes.subscription_type` | string |  | The type of user subscription in this HighBond instance.  Available codes are: `"grc_full"` for _Professional_, `"grc_lite"` for _Contributor_, `"grc_intermediate"` for _Oversight_, `"grc_results_cloud_admin"` for _Results Lite Professional_, `"grc_results_cloud_user"` for _Results Lite Contributor_, and `null` for _None_. Ex.: `"grc_full"` |
| `data.attributes.time_zone` | string |  | The time zone of the user. Ex.: `"Pacific Time (US & Canada)"` |
| `data.attributes.locale` | string |  | The two letter code representing the user's chosen locale in their HighBond profile. The available locales are `"de"`, `"en"`, `"es"`, `"fr"`, `"pt"`, `"ja"`, and `"zh"`. Ex.: `"en"` |
| `data.attributes.date_format` | string |  | The date format this user uses when they view timestamped fields in HighBond. Ex.: `"%m/%d/%Y"` |
| `data.attributes.created_at` | string |  | The timestamp identifying when the user was created. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.attributes.updated_at` | string |  | The timestamp identifying when the user was last updated. Ex.: `"2019-02-09T13:17:26Z"` |

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
