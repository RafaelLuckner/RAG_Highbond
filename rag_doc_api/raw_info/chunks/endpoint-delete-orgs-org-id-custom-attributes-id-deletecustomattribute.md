---
id: endpoint-delete-orgs-org-id-custom-attributes-id-deletecustomattribute
title: "Custom attributes: Delete a custom attribute"
tags: [endpoint, custom-attributes]
source: openapi.json (HighBond API v1.1.0)
---

## Custom attributes

Custom attributes are the customizable fields that are associated with supported objects.
Custom attributes are defined on the project type and used by the project and its children (i.e. objectives).

> **Note —**
No more than 5 custom attributes of one customizable_type can be created (no more than 8 if the customizable type is 'CustomRiskFactor').

Learn more about custom attributes.

### `DELETE /orgs/{org_id}/custom_attributes/{id}` — Delete a custom attribute

- **operationId:** `deleteCustomAttribute`
- **Domínio(s):** Custom attributes

Permanently delete a custom attribute from a project type.
> **Caution —**
Deleting a custom attribute permanently removes the field and all associated data from all relevant projects and frameworks.

<details>
<summary><strong>Parâmetros</strong> (2)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `id` | path | ✅ | string | The ID of the requested resource. Ex.: `9999` |

</details>

<details>
<summary><strong>Respostas</strong> (6)</summary>

- `204` — No content.

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
