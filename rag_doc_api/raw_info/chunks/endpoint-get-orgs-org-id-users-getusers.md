---
id: endpoint-get-orgs-org-id-users-getusers
title: "Users: List users in an instance
"
tags: [endpoint, users]
source: openapi.json (HighBond API v1.1.0)
---

## Users

A user represents a member of HighBond. Users can belong to multiple instances.

Learn more about adding and managing users.

### `GET /orgs/{org_id}/users` — List users in an instance


- **operationId:** `getUsers`
- **Domínio(s):** Users

Get a list of users, excluding system and root users, who are part of a particular HighBond instance.

Note: System and root users are special types of users that act on behalf of the HighBond platform, like in automation tasks performed in the Robots app. Filters can be applied to query for them if needed.

<details>
<summary><strong>Parâmetros</strong> (5)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `filter[user_type]` | query |  | string | Requesting the API to filter Users by their type. Can only be one of the following types `"user"`, `"system"`, and `"root"` Ex.: `user` |
| `filter[query]` | query |  | string | Requesting the API to return only Users matching their name or email if it contains the search query string. Case-insensitive. Ex.: `diligent.com` |
| `page[size]` | query |  | number | The number of items returned per page. Default and maximum is 8000 to support backwards compatibility. Recommended best practice is to use 20-50 for user interface usage, and 100-500 for API usage. Ex.: `100` |
| `page[number]` | query |  | number | The page number of records to return. Default is 1. Ex.: `1` |

</details>

<details>
<summary><strong>Respostas</strong> (4)</summary>

<details>
<summary>`200` — OK.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `MultipleUsersResponse`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | array[object] | ✅ | An array of the users within this HighBond instance. |
| `data.id` | string | ✅ | The user ID for the user, used across all HighBond instances. Ex.: `"P2tuGWyTWxCAQgTd1XKx"` |
| `data.type` | string | ✅ | The classification of the object (`"users"`) for API schema serialization purposes. Ex.: `"users"` |
| `data.attributes` | object | ✅ |  |
| `data.attributes.email` | string |  | The user's email address, defined when that user was created. Ex.: `"john.smith.test@wegalvanize.com"` |
| `data.attributes.first_name` | string |  | First name for the user. The character limit is 40. Ex.: `"John"` |
| `data.attributes.last_name` | string |  | Last name for the user. The character limit is 40. Ex.: `"Smith"` |
| `data.attributes.title` | string |  | The user's professional title. The character limit is 255. Ex.: `"Prof."` |
| `data.attributes.initials` | string |  | The initials of this user's first and last names. The character limit is 255. Ex.: `"JS"` |
| `data.attributes.phone` | string |  | The user's phone number. This can be with or without hyphens. Ex.: `"555-555-5555"` |
| `data.attributes.phone_extension` | string |  | The user's phone extension. Ex.: `"555"` |
| `data.attributes.date_format` | string |  | The date format this user uses when they view timestamped fields in HighBond. Ex.: `"%m/%d/%Y"` |
| `data.attributes.timezone` | string |  | The user's timezone. Ex.: `"UTC"` |
| `data.attributes.locale` | string |  | The two letter code representing the user's chosen locale in their HighBond profile. The available locales are `"de"`, `"en"`, `"es"`, `"fr"`, `"pt"`, `"ja"`, and `"zh"`. Ex.: `"en"` |
| `data.attributes.created_at` | string |  | The date and time when the user was created. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.attributes.current_sign_in_at` | string |  | The date and time when the user last signed in. Ex.: `"2019-02-09T13:17:26Z"` |
| `data.attributes.name` | string |  | The user's full name. This value is system generated, based on `"first_name"` and `"last_name"`. Ex.: `"John Smith"` |
| `data.attributes.preferred_community_org` | string |  | The name of the user's preferred community instance. Ex.: `"Organization A"` |
| `data.attributes.preferred_community_org_id` | integer |  | The id of the preferred HighBond instance for the user to access community. Ex.: `12345` |
| `data.attributes.user_type` | string |  | The type of user in the HighBond instance, one of `"user"`, `"system"` or `"root"`. Ex.: `"user"` |
| `data.attributes.enabled` | boolean |  | Shows if the user is enabled or not in the platform. Ex.: `true` |
| `data.attributes.subscription` | string |  | The type of user subscription in this HighBond instance. This field will be returned to provide information, currently it cannot be updated via APIs. Available codes are: `"grc_full"` for _Professional_, `"grc_lite"` for _Contributor_, `"grc_intermediate"` for _Oversight_, `"grc_results_cloud_admin"` for _Results Lite Professional_, `"grc_results_cloud_user"` for _Results Lite Contributor_, and `null` for _None_. Ex.: `"grc_full"` |
| `data.attributes.is_system_admin` | boolean |  | Returns true when the user is a System Admin in this HighBond instance. Ex.: `false` |
| `data.attributes.is_external` | boolean |  | Returns true when the user is managed externally and synced into this HighBond instance. Ex.: `false` |
| `data.attributes.extended_attributes` | object |  | Set of key-value pairs containing up to 13 attributes defined externally in the user sync service. Ex.: `{"key1": "one", "key2": "two", "key3": "three", "key4": "four", "key5": "five", "key6": "six", "key7": "seven", "key8": "eight", "key9": "nine", "k...` |
| `links` | object |  | Links to the first, last, next, and previous pages. |
| `links.next` | string | ✅ | Next page url Ex.: `"/orgs/:org_id/users?page[number]=2&page[size]=10"` |
| `links.prev` | string | ✅ | Previous page url Ex.: `"/orgs/:org_id/users?page[number]=1&page[size]=10"` |
| `links.first` | string | ✅ | First page url Ex.: `"/orgs/:org_id/users?page[number]=1&page[size]=10"` |
| `links.last` | string | ✅ | Last page url Ex.: `"/orgs/:org_id/users?page[number]=1&page[size]=10"` |
| `links.self` | string | ✅ | Current page url Ex.: `"/orgs/:org_id/users?page[number]=1&page[size]=10"` |
| `meta` | object |  | Metadata about the users pagination. |
| `meta.total_pages` | integer | ✅ | Total number of pages Ex.: `1` |
| `meta.total_count` | integer | ✅ | Total number of users Ex.: `1` |

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
