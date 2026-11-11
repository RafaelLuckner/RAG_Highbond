---
id: endpoint-post-orgs-org-id-robots-robot-id-versions-createrobotscriptversion
title: "Robot script versions: Create a robot script version"
tags: [endpoint, robot-script-versions]
source: openapi.json (HighBond API v1.1.0)
---

## Robot script versions

A version of a robot that includes the hcl script in json.  You can upload new version of your hcl script to your highbond robot or workflow robot.

Flow json includes python script, variables and system token user uid.  See example of flow json in request body schema.

### `POST /orgs/{org_id}/robots/{robot_id}/versions` — Create a robot script version

- **operationId:** `createRobotScriptVersion`
- **Domínio(s):** Robot Script Versions

Create a new robot app version and flow.

<details>
<summary><strong>Parâmetros</strong> (3)</summary>

| Nome | Local | Obrigatório | Tipo | Descrição |
|------|-------|-------------|------|-----------|
| `org_id` | path | ✅ | string | The ID of the HighBond instance. Ex.: `1` |
| `robot_id` | path | ✅ | string | The ID of the robot. Ex.: `2` |
| `include` | query |  | string | If specified, the associated analytic scripts will be included in the `included` object Valores: `analytics` Ex.: `analytics` |

</details>

<details>
<summary><strong>Request body (payload)</strong></summary>

The below data are `required` to create a script for highbond robots or workflow robots.

**Body obrigatório.**

**Content-Type:** `application/vnd.api+json`

**Schema:** `CreateRobotScriptVersionRequest`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `comment` | string |  | An informative statement in the version history. Ex.: `"Example commit comment"` |
| `name` | string |  | Name of the flow |
| `raw` | object |  | Configuration object of the flow of a highbond robots or workflow robots.  It contains user python scripts and variables set up in flow builder.  See example of the flow structure in the sample response.  Version in json is required.  Initial version of flow json is `version: '2021-02-05'`.  environment is execution environments for user scripts. Each environment consists of a runtime (e.g. “python3.11”) and a list of packages (e.g. "hcl==3.0.*", "boxsdk==3.9.2")  environment for a robot should have `runtime: "python3.11"` and `requirements` should include `hcl==3.0.*`. For HighBond Robot, additional packages can be included, however they should match the versions as given below:  - Workflow Robot  ``` environment: {   runtime: "python3.11",   requirements: [     "hcl==3.0.*"   ] } ```  - HighBond Robot  ``` environment: {   runtime: "python3.11",    requirements: [     "hcl==3.0.*",     "boxsdk==3.9.2",     "openpyxl==3.1.2",     "Jinja2==3.1.3",     "simple-salesforce==1.12.5",     "jira==3.8.0"    ]  } ```  >In case `environment` is missing or the packages (e.g `boxsdk` and others mentioned above) does not match the specified versions, API will throw an error.  `id` in flow json needs to be unique.  Example shown are using uuidv4.  Note: For the `hcl` requirement, specify a version that is a valid HCL library version number using this format: `major.minor.*` (For example, `hcl==3.0.*`) Use an asterisk (`*`) rather than a specific patch number.   ``` {   version: '2021-02-05',   environment: {     runtime: "python3.11",     requirements: [       "hcl==3.0.*",        "boxsdk==3.9.2",       "openpyxl==3.1.2",       "Jinja2==3.1.3",       "simple-salesforce==1.12.5",       "jira==3.8.0"     ]   },   edges: []   nodes: [{     id: '7759ae53-a921-46b1-bc2f-49ac799e4882'     kind: 'script',     libraryNodeId: 'script-id',     name: 'Script',     config: {       cells: [         {           id: '41e1aa1b-ab74-43bc-8d07-8f5f76590ab1',           input: "print('demo')↵↵print('second line of demo')"         },         {           id: 'f3d4eaae-45e4-499e-833e-fb0ae77abf59',           input: "print('cell #2')↵↵print('another new line')"         }       ]     }   }]   variables: [     {       id: 'a9e0bc9d-6dcc-4d2d-943c-fd1c795667c5',       name: 'v_hb_token',       type: 'system_user_id',       value: '{the system user UID}'     },     {       id: 'c41c0c69-bec7-464e-a7c9-effd0a321706',       isTaskInput: false,       name: 'v_character',       type: 'character',       value: My variable value     },     {       id: '93674454-6a16-41a2-9e05-6f1f962d9a10',       isTaskInput: true,       name: 'v_password',       taskInputLabel: 'My Password Task Param Label',       type: 'password',       value: ''     }   ] } ``` |

</details>

<details>
<summary><strong>Respostas</strong> (7)</summary>

<details>
<summary>`200` — Created.</summary>

**Content-Type:** `application/vnd.api+json`

**Schema:** `GetRobotScriptVersionResponse`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `data` | RobotScriptVersion | ✅ |  |
| `data.id` | string | ✅ | The ID of the script version. Ex.: `1` |
| `data.type` | string | ✅ | The classification of the object (`"robot_apps"`). Ex.: `"analytics"` |
| `data.attributes` | object | ✅ | The attributes associated with the resource. |
| `data.attributes.comment` | string |  | An informative statement in the version history. Ex.: `"Example commit comment"` |
| `data.attributes.version` | integer |  | The version of the analytic Ex.: `10` |
| `data.relationships` | object |  | The resouces associated with this script version. |
| `data.relationships.analytics` | object |  | List of flows associated with the script version. |
| `data.relationships.analytics.data` | array[object] |  | An array of analytic IDs associated with the script version. |
| `data.relationships.analytics.data.id` | string |  | The ID of the analytic. |
| `data.relationships.analytics.data.type` | string |  | The classification of the object (`"analytic"`). |
| `included` | array[object] |  | All analytics related to the resource |
| `included.id` | string |  | The ID of the flow. |
| `included.type` | string |  | The classification of the object (`"analytics"`). |
| `included.attributes` | object |  | The attributes associated with the flow. |
| `included.attributes.name` | string |  | The name of the flow Ex.: `"Example Flow"` |
| `included.attributes.raw` | object |  | Configuration object of the flow of a highbond robots or workflow robots. |

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

**Schema:** `RobotsError`

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `errors` | array[object] | ✅ |  |
| `errors.status` | string |  | A HTTP response status code indicating an unprocessable entity. Valores: `422` Ex.: `"422"` |
| `errors.source` | object |  |  |
| `errors.source.pointer` | string |  | Indicates the specific source of the error. Ex.: `"/data/attributes/name"` |
| `errors.title` | string |  | A title of the error. Ex.: `"can't be blank"` |
| `errors.detail` | string |  | A descriptive statement of the error. Ex.: `"Name can't be blank"` |

</details>

</details>
