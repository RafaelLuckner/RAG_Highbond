---
id: endpoint-delete-orgs-org-id-metrics-id-deletemetric
title: "Metrics: Delete a metric"
tags: [endpoint, metrics]
source: openapi.json (HighBond API v1.1.0)
---

## Metrics

A metric is a calculation that you label as a specific type of key indicator. Key indicators are quantitative measurements of success (KPI, KCI) or risk (KRI) that are
associated with a company's objectives. Metrics monitor the data in a single column over a time period using an aggregate function such as average, count, or
percentage of total.

Your organization can have a maximum of 8,000 metrics.

Learn more about metrics.

### `DELETE /orgs/{org_id}/metrics/{id}` — Delete a metric

- **operationId:** `deleteMetric`
- **Domínio(s):** Metrics

If you no longer need a metric, you can delete it. Deleting a metric also removes it from any associated triggers and storyboards. It does not delete the table this metric exists in.

> **Note —**
If the metric is associated with an assessment driver in the Projects or Strategy app, deleting the metric disables the assessment automation in the relevant app.

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
