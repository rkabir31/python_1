
# Getting Started with MdNotesCCG

## Introduction

API for Markdown Notes app.

## Building

You must have Python `3 >=3.6, <= 3.9` installed on your system to install and run this SDK. This SDK package depends on other Python packages like nose, jsonpickle etc. These dependencies are defined in the `requirements.txt` file that comes with the SDK.To resolve these dependencies, you can use the PIP Dependency manager. Install it by following steps at [https://pip.pypa.io/en/stable/installing/](https://pip.pypa.io/en/stable/installing/).

Python and PIP executables should be defined in your PATH. Open command prompt and type `pip --version`. This should display the version of the PIP Dependency Manager installed if your installation was successful and the paths are properly defined.

* Using command line, navigate to the directory containing the generated files (including `requirements.txt`) for the SDK.
* Run the command `pip install -r requirements.txt`. This should install all the required dependencies.

![Building SDK - Step 1](https://apidocs.io/illustration/python?workspaceFolder=Mdnotesccg-Python&step=installDependencies)

## Installation

The following section explains how to use the mdnotesccg library in a new project.

### 1. Open Project in an IDE

Open up a Python IDE like PyCharm. The basic workflow presented here is also applicable if you prefer using a different editor or IDE.

![Open project in PyCharm - Step 1](https://apidocs.io/illustration/python?workspaceFolder=Mdnotesccg-Python&step=pyCharm)

Click on `Open` in PyCharm to browse to your generated SDK directory and then click `OK`.

![Open project in PyCharm - Step 2](https://apidocs.io/illustration/python?workspaceFolder=Mdnotesccg-Python&step=openProject0)

The project files will be displayed in the side bar as follows:

![Open project in PyCharm - Step 3](https://apidocs.io/illustration/python?workspaceFolder=Mdnotesccg-Python&projectName=mdnotesccg&step=openProject1)

### 2. Add a new Test Project

Create a new directory by right clicking on the solution name as shown below:

![Add a new project in PyCharm - Step 1](https://apidocs.io/illustration/python?workspaceFolder=Mdnotesccg-Python&projectName=mdnotesccg&step=createDirectory)

Name the directory as "test".

![Add a new project in PyCharm - Step 2](https://apidocs.io/illustration/python?workspaceFolder=Mdnotesccg-Python&step=nameDirectory)

Add a python file to this project.

![Add a new project in PyCharm - Step 3](https://apidocs.io/illustration/python?workspaceFolder=Mdnotesccg-Python&projectName=mdnotesccg&step=createFile)

Name it "testSDK".

![Add a new project in PyCharm - Step 4](https://apidocs.io/illustration/python?workspaceFolder=Mdnotesccg-Python&projectName=mdnotesccg&step=nameFile)

In your python file you will be required to import the generated python library using the following code lines

```python
from mdnotesccg.mdnotesccg_client import MdnotesccgClient
```

![Add a new project in PyCharm - Step 5](https://apidocs.io/illustration/python?workspaceFolder=Mdnotesccg-Python&projectName=mdnotesccg&libraryName=mdnotesccg.mdnotesccg_client&className=MdnotesccgClient&step=projectFiles)

After this you can write code to instantiate an API client object, get a controller object and  make API calls. Sample code is given in the subsequent sections.

### 3. Run the Test Project

To run the file within your test project, right click on your Python file inside your Test project and click on `Run`

![Run Test Project - Step 1](https://apidocs.io/illustration/python?workspaceFolder=Mdnotesccg-Python&projectName=mdnotesccg&libraryName=mdnotesccg.mdnotesccg_client&className=MdnotesccgClient&step=runProject)

## Test the SDK

You can test the generated SDK and the server with test cases. `unittest` is used as the testing framework and `nose` is used as the test runner. You can run the tests as follows:

Navigate to the root directory of the SDK and run the following commands

```
pip install -r test-requirements.txt
nosetests
```

## Initialize the API Client

**_Note:_** Documentation for the client can be found [here.](/doc/client.md)

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

## Authorization

The SDK will attempt to authorize by providing no scopes in case an endpoint requiring authentication is called. You can also authorize the client yourself.

The SDK uses *OAuth 2.0 Authorization* to authorize the client.

The `authorize()` method will exchange the OAuth client credentials for an *access token*. The access token is an object containing information for authorizing client requests and refreshing the token itself.

```python
try:
    client.auth.authorize()
except OAuthProviderException as ex:
    # handle exception
except APIException as ex:
    # handle exception
```

The client can now make authorized endpoint calls.

### Storing an access token for reuse

It is recommended that you store the access token for reuse.

```python
# store token
save_token_to_database(client.config.o_auth_token)
```

### Creating a client from a stored token

To authorize a client from a stored access token, just set the access token in Configuration along with the other configuration parameters before creating the client:

```python
client = MdnotesccgClient()
client.config.o_auth_token = load_token_from_database()
```

### Complete example

```python
from mdnotesccg.mdnotesccg.mdnotesccg_client import MdnotesccgClient
from mdnotesccg.exceptions.o_auth_provider_exception import OAuthProviderException

# function for storing token to database
def save_token_to_database(token):
    # code to save the token to database

# function for loading token from database
def load_token_from_database():
    # load token from database and return it (return None if no token exists)
    pass

from mdnotesccg.mdnotesccg_client import MdnotesccgClient
from mdnotesccg.configuration import Environment

client = MdnotesccgClient(
    o_auth_client_id='OAuthClientId',
    o_auth_client_secret='OAuthClientSecret',
    environment=Environment.PRODUCTION,)
# obtain access token, needed for client to be authorized
previous_token = load_token_from_database()
if previous_token:
    # restore previous access token
    client.config.o_auth_token = previous_token
else:
    # obtain new access token
    try:
        token = client.auth.authorize()
        save_token_to_database(token)
    except OAuthProviderException as ex:
        # handle exception
    except APIException as ex:
        # handle exception

# the client is now authorized and you can use controllers to make endpoint calls
```

## List of APIs

* [User](/doc/controllers/user.md)
* [Service](/doc/controllers/service.md)

## Classes Documentation

* [Utility Classes](/doc/utility-classes.md)
* [HttpResponse](/doc/http-response.md)
* [HttpRequest](/doc/http-request.md)

