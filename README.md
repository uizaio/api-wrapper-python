# Python Client for Uiza platform

## Introduction

The Uiza API is organized around RESTful standard. Our API has predictable, resource-oriented URLs, and uses HTTP response codes to indicate API errors. JSON is returned by all API responses, including errors, although our API libraries convert responses to appropriate language-specific objects.

## Documentation

See the [.Uiza API docs](https://docs.uiza.io/).

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

The first, needing create Uiza connection using `workspace_api_domain` and `authorization`:

```python
import uiza

uiza.workspace_api_domain = 'your-workspace-api-domain.uiza.co'
uiza.authorization = 'your-api-key'

``` 

After connection created, this is example search Entity:

```python
import uiza
from uiza.api_resources.entity import Entity
from uiza.exceptions import ServerException

uiza.workspace_api_domain = "your-workspace-api-domain.uiza.co"
uiza.authorization = "your-authorization"

try:
    entity_data, _ = Entity().search(keyword='Sample')
except ServerException as e:
    raise e
except Exception as e:
    raise e

...

```

Next steps, reading the [Client Library Documentation]() to see other available methods on the client.

- [Entity](https://github.com/uizaio/api-wrapper-python/blob/master/docs/entity.md)
- [Category](https://github.com/uizaio/api-wrapper-python/blob/master/docs/category.md)
- [Storage](https://github.com/uizaio/api-wrapper-python/blob/master/docs/storage.md)
- [Live Streaming](https://github.com/uizaio/api-wrapper-python/blob/master/docs/callback.md)
- [Callback](https://github.com/uizaio/api-wrapper-python/blob/master/docs/category.md)
- [User](https://github.com/uizaio/api-wrapper-python/blob/master/docs/user.md)
- [Analytic](https://github.com/uizaio/api-wrapper-python/blob/master/docs/analytic.md)

## Unittest

The first, you need install dependencies:

```bash
pip install -r requirements.txt
```

Run unittest:

```bash
python -m unittest discover tests
```

Coverage code:

```bash
coverage run -m unittest discover tests
coverage report
``` 


## Contributing

Bug reports and pull requests are welcome on GitHub at [https://github.com/uizaio/api-wrapper-python](https://github.com/uizaio/api-wrapper-python).

## License

The package is available as open source under the terms of the [MIT License](https://choosealicense.com/licenses/mit/).
