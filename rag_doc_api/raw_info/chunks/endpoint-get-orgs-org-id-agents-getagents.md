---
id: endpoint-get-orgs-org-id-agents-getagents
title: "Robots Agents: Get a list of Robots Agents"
tags: [endpoint, robots-agents]
source: openapi.json (HighBond API v1.1.0)
---

## Robots Agents

A Robots Agent is the on-premise or cloud-based Robots component that uses the Analytics script engine to run scripts against data.

Learn more about the Robots Agent.

### `GET /orgs/{org_id}/agents` — Get a list of Robots Agents

- **operationId:** `getAgents`
- **Domínio(s):** Robots Agents

Get a list of all of the Robots Agents available to your organization.

<details>
<summary><strong>Parâmetros</strong> (1)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |

</details>

<details>
<summary><strong>Respostas</strong> (6)</summary>

<details>
<summary>`200` — OK.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `GetAgentsResponse`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | array[object] |  |  |
| `data.id` | string |  | The ID of the robot. Ex.: `1` |
| `data.type` | string |  | The classification of the object. Ex.: `"agent"` |
| `data.attributes` | object |  | The attributes associated with the resource. |
| `data.attributes.agent_type` | string |  | The type of the agent. Can be `cloud`, `default`, or `flow`. Valores: `cloud`, `default`, `flow` Ex.: `"cloud"` |
| `data.attributes.is_unicode` | boolean |  | If the agent is unicode or non-unicode. Ex.: `"cloud"` |

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
