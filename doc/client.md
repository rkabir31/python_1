
# Client Class Documentation

The following parameters are configurable for the API Client:

| Parameter | Type | Description |
|  --- | --- | --- |
| `o_auth_client_id` | `string` | OAuth 2 Client ID |
| `o_auth_client_secret` | `string` | OAuth 2 Client Secret |
| `environment` | Environment | The API environment. <br> **Default: `Environment.PRODUCTION`** |
| `timeout` | `float` | The value to use for connection timeout. <br> **Default: 60** |
| `max_retries` | `int` | The number of times to retry an endpoint call if it fails. <br> **Default: 0** |
| `backoff_factor` | `float` | A backoff factor to apply between attempts after the second try. <br> **Default: 2** |
| `retry_statuses` | `Array of int` | The http statuses on which retry is to be done. <br> **Default: [408, 413, 429, 500, 502, 503, 504, 521, 522, 524]** |
| `retry_methods` | `Array of string` | The http methods on which retry is to be done. <br> **Default: ['GET', 'PUT']** |
| `o_auth_token` | `OAuthToken` | Object for storing information about the OAuth token |

The API client can be initialized as follows:

```python
from mdnotesccg.mdnotesccg_client import MdnotesccgClient
from mdnotesccg.configuration import Environment

client = MdnotesccgClient(
    o_auth_client_id='OAuthClientId',
    o_auth_client_secret='OAuthClientSecret',
    environment=Environment.PRODUCTION,)
```

## MdNotesCCG Client

The gateway for the SDK. This class acts as a factory for the Controllers and also holds the configuration of the SDK.

## Controllers

| Name | Description |
|  --- | --- |
| user | Gets UserController |
| service | Gets ServiceController |
| o_auth_authorization | Gets OAuthAuthorizationController |

