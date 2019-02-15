# Python Client for Uiza platform

## Introduction

The Uiza API is organized around RESTful standard. Our API has predictable, resource-oriented URLs, and uses HTTP response codes to indicate API errors. JSON is returned by all API responses, including errors, although our API libraries convert responses to appropriate language-specific objects.

## Documentation

See the [.NET API docs](https://docs.uiza.io/).

## Installation

### Supported Python Versions
- Python 2.7.x. Python 2.7 support will be removed on January 1, 2020.
- Python 3.x
- Tested with Python 2.7.11, 3.4, 3.6.8

### Install uiza package via pip

Suggestion install this library using pip with [virtualenv](https://virtualenv.pypa.io/en/latest/). Because with virtualenv, it is possible to install this library without:
- Needing system install permission.
- Clashing with the installed system dependencies.

On Mac/Linux
```bash
pip install virtualenv
virtualenv <your-env>
source <your-env>/bin/activate
<your-env>/bin/pip install uiza
```

On Windows
```bash
pip install virtualenv
virtualenv <your-env>
<your-env>\Scripts\activate
<your-env>\Scripts\pip.exe install uiza
```

## Usage

The library needs to be configured with your account's `workspace_api_domain` and `authorization` (API key).
See details [here](https://docs.uiza.io/#authentication).

The first, needing create Uiza connection using `workspace_api_domain` and `api_key`:

```python
from uiza import Connection

connection = Connection(workspace_api_domain=<your-workspace-api-domain.uiza.co>, api_key=<your-api-key>)
``` 

After connection created, this is example search Entity:

```python
from uiza import Connection
from uiza.entity import Entity
from uiza.user import User
from uiza.exceptions import ServerException

connection = Connection(workspace_api_domain=<your-workspace-api-domain.uiza.co>, api_key=<your-api-key>)
entity = Entity(connection)

try:
    entity_data, _ = entity.search()
except ServerException as e:
    raise e
except Exception as e:
    raise e
    
user = User()
...

```

Next steps, reading the [Client Library Documentation]() to see other available methods on the client.

## Contributing
Bug reports and pull requests are welcome on GitHub at [https://github.com/uizaio/api-wrapper-python](https://github.com/uizaio/api-wrapper-python).

## License
The gem is available as open source under the terms of the [MIT License](https://choosealicense.com/licenses/mit/).

