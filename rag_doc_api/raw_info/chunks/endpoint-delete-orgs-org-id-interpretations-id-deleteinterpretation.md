---
id: endpoint-delete-orgs-org-id-interpretations-id-deleteinterpretation
title: "Interpretations: Delete an interpretation"
tags: [endpoint, interpretations]
source: openapi.json (HighBond API v1.1.0)
---

## Interpretations

An interpretation is a bundled collection of filters, visualizations, and statistics based on a table in a collection. Use them to interpret and visualize results to gain
a deeper understanding of the facts and insights hidden in the data.

Your organization can have a maximum of 4,000 interpretations.

Learn more about interpretations.

### `DELETE /orgs/{org_id}/interpretations/{id}` — Delete an interpretation

- **operationId:** `deleteInterpretation`
- **Domínio(s):** Interpretations

If you no longer need an interpretation, you can permanently delete it.

> **Caution —**
Deleting an interpretation also deletes any visualizations created from that interpretation and removes those visualizations from storyboards. It does not delete the table where the interpretation exists.

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
