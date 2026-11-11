---
id: endpoint-delete-orgs-org-id-compliance-regulations-id-deletecomplianceregulation
title: "Compliance Maps: Delete a compliance regulation"
tags: [endpoint, compliance-maps]
source: openapi.json (HighBond API v1.1.0)
---

## Compliance Maps

You can use Compliance Maps to associate industry standards and regulations with your control frameworks.

Learn more.

### `DELETE /orgs/{org_id}/compliance_regulations/{id}` — Delete a compliance regulation

- **operationId:** `deleteComplianceRegulation`
- **Domínio(s):** Compliance Maps

Permanently delete a compliance regulation from an organization.

<details>
<summary><strong>Parâmetros</strong> (2)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `id` | path | ✅ | string | The ID of the requested resource. Ex.: `9999` |

</details>

<details>
<summary><strong>Respostas</strong> (4)</summary>

- `204` — No content.

- `401` — Bad credentials.

- `403` — Forbidden.

- `404` — Not found.

</details>
