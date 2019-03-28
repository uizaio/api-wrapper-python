## Callback

This is client for calling to API callback. Callback used to retrieve an information for Uiza to your server, so you can have a trigger notice about an entity is upload completed.

We can use a `Callback` to:

- **create()**
- **retrieve()**
- **update()**
- **delete()**

### Create callback

`create(**kwang)`

Function to create a callback to your server when an entity is completed for upload or public.

For example:

```python
import uiza
from uiza.api_resources.callback import Callback
from uiza.exceptions import ServerException

uiza.authorization = "your-authorization"
uiza.app_id = "your-app-id"

callback_data = {
    "url":"https://callback-url-python.uiza.co",
    "method":"GET"
}

try:
    res, status_code = Callback().create(**callback_data)
    print("res: ", res)
except ServerException as e:
    raise e
except Exception as e:
    raise e

```

#### Parameters

- **url** (*str*) - Your server URL for callback.
- **method** (*str*) - Method of callback (get-post-put..).
- **jsonData** (*str*) - Extra data you want to attach in callback response	.
- **headersData** (*str*) - Add parameter to headers.

#### Return type

- Tuple

#### Return

- Response data and status code

### Retrieve a callback

`retrieve(id)`

Function to retrieves the details of an existing callback.

For example:

```python
import uiza
from uiza.api_resources.callback import Callback
from uiza.exceptions import ServerException

uiza.authorization = "your-authorization"
uiza.app_id = "your-app-id"

try:
    res, status_code = Callback().retrieve(id='33a86c18-f502-41a4-9c4c-d4e14efca238')
    print("res: ", res)
except ServerException as e:
    raise e
except Exception as e:
    raise e
```

#### Parameters

- **id** (*str*) - Id of callback setting.

#### Return type

- Tuple

#### Return

- Response data and status code

### Update a callback

`update(**data)`

Function to update callback's information.

For example:

```python
import uiza
from uiza.api_resources.callback import Callback
from uiza.exceptions import ServerException

uiza.authorization = "your-authorization"
uiza.app_id = "your-app-id"

try:
    res, status_code = Callback().update(id='33a86c18-f502-41a4-9c4c-d4e14efca238', method='POST')
    print("res: ", res)
except ServerException as e:
    raise e
except Exception as e:
    raise e
```

#### Parameters

- **id** (*str*) - Id of callback setting.
- **url** (*str*) - Your server URL for callback.
- **method** (*str*) - Method of callback (get-post-put..).
- **jsonData** (*str*) - Extra data you want to attach in callback response	.
- **headersData** (*str*) - Add parameter to headers.

#### Return type

- Tuple

#### Return

- Response data and status code

### Delete a callback

`delete(id)`

Function to delete an existing callback.

For example:

```python
import uiza
from uiza.api_resources.callback import Callback
from uiza.exceptions import ServerException

uiza.authorization = "your-authorization"
uiza.app_id = "your-app-id"

try:
    res, status_code = Callback().delete(id='ddf09dd0-b7a8-4f29-92df-14dafb97b2aa')
    print("res: ", res)
except ServerException as e:
    raise e
except Exception as e:
    raise e
```

#### Parameters

- **id** (*str*) - Identifier of storage.

#### Return type

- Tuple

#### Return

- Response data and status code
