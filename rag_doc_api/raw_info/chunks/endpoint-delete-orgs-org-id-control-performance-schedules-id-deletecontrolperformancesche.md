---
id: endpoint-delete-orgs-org-id-control-performance-schedules-id-deletecontrolperformancesche
title: "Control performance schedules: Delete a Control Performance Schedule"
tags: [endpoint, control-performance-schedules]
source: openapi.json (HighBond API v1.1.0)
---

## Control performance schedules

A control performance schedule is a schedule of control tests that are performed on a recurring basis. Control performance schedules are associated with controls.

> **Note:**
Control performance schedules located in such resources can be accessed using the API:
> * In projects that have an "active" state
> * In frameworks

Learn more about control performance schedules.

### `DELETE /orgs/{org_id}/control_performance_schedules/{id}` — Delete a Control Performance Schedule

- **operationId:** `deleteControlPerformanceSchedule`
- **Domínio(s):** Control performance schedules

Delete a control performance schedule from a project or framework.

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
