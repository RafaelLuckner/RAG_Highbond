---
id: endpoint-delete-orgs-org-id-related-requirements-id-deleterelatedrequirement
title: "Compliance Maps: Delete a link between requirements"
tags: [endpoint, compliance-maps]
source: openapi.json (HighBond API v1.1.0)
---

## Compliance Maps

You can use Compliance Maps to associate industry standards and regulations with your control frameworks.

Learn more.

### `DELETE /orgs/{org_id}/related_requirements/{id}` — Delete a link between requirements

- **operationId:** `deleteRelatedRequirement`
- **Domínio(s):** Compliance Maps

Once a relationship is established between requirements, you can delete that relationship. Use the related requirements feature at your discretion and risk. You are responsible to apply professional judgment to determine the appropriate procedures, tests, or controls for your own use. Learn more.

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
