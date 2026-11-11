---
id: endpoint-get-orgs-org-id-robot-files-id-download-downloadfile
title: "ACL robot related files: Download an ACL robot related file"
tags: [endpoint, robot-files]
source: openapi.json (HighBond API v1.1.0)
---

## ACL robot related files

Related files in an ACL robot are non-Analytics files such as Excel or delimited that can be used as input for scripts in the robot.

Learn more about related files in ACL robots.

### `GET /orgs/{org_id}/robot_files/{id}/download` — Download an ACL robot related file

- **operationId:** `downloadFile`
- **Domínio(s):** Robot Files

Download a related file by ACL robot ID.

<details>
<summary><strong>Parâmetros</strong> (2)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `id` | path | ✅ | string | The ID of the requested resource. Ex.: `9999` |

</details>

<details>
<summary><strong>Respostas</strong> (6)</summary>

- `200` — OK.

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
