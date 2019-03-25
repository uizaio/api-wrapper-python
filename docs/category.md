## Category

This is client for calling to API category. Category has been splits into 3 types: folder, playlist and tag. These will make the management of entity more easier. See details [here](https://docs.uiza.io/#category).

We can use a `Category` to:

- **create()**
- **retrieve()**
- **list()**
- **update()**
- **delete()**
- **create_relation()**
- **delete_relation()**

### Create category

`create(**kwang)`

Function to create category for entity for easier management. Category use to group all the same entities into a group (like Folder/ playlist/or tag).

For example:

```python
import uiza

from uiza.api_resources.category import Category
from uiza.exceptions import ServerException

uiza.workspace_api_domain = "your-workspace-api-domain.uiza.co"
uiza.authorization = "your-authorization"

category_data = {
        "name": "Test name 1",
        "type": "folder",
    }

try:
    res, status_code = Category().create(**category_data)
    print("res ", res)
except ServerException as e:
    raise e
except Exception as e:
    raise e
```

#### Parameters

- **name** (*str*) - Name of category.
- **type** (*str*) - Has 3 types of category [ folder, playlist, tag ].
- **description** (*str*) - Description for category.
- **orderNumber** (*int*) - Order number for category, lower number is higher order.
- **icon** (*str*) - Small icon for each category.

#### Return type

- Tuple

#### Return

- Response data and status code

### Retrieve an category

`retrieve(id)`

Function to get detail of category.

For example:

```python
import uiza

from uiza.api_resources.category import Category
from uiza.exceptions import ServerException

uiza.workspace_api_domain = "your-workspace-api-domain.uiza.co"
uiza.authorization = "your-authorization"

try:
    res, status_code = Category().retrieve(id='33a86c18-f502-41a4-9c4c-d4e14efca238')
    print("res ", res)
except ServerException as e:
    raise e
except Exception as e:
    raise e
```

#### Parameters

- **id** (*str*) - Identifier of category.

#### Return type

- Tuple

#### Return

- Response data and status code

### Retrieve category list

`list(**params)`

Function to get list of categories including all detail.

For example:

```python
import uiza

from uiza.api_resources.category import Category
from uiza.exceptions import ServerException

uiza.workspace_api_domain = "your-workspace-api-domain.uiza.co"
uiza.authorization = "your-authorization"

try:
    res, status_code = Category().list()
    print("res ", res)
except ServerException as e:
    raise e
except Exception as e:
    raise e
```

#### Parameters

- N/A

#### Return type

- Tuple

#### Return

- Response data and status code

### Update category

`update(**data)`

Function to update category's information.

For example:

```python
import uiza

from uiza.api_resources.category import Category
from uiza.exceptions import ServerException

uiza.workspace_api_domain = "your-workspace-api-domain.uiza.co"
uiza.authorization = "your-authorization"

try:
    res, status_code = Category().update(id='33a86c18-f502-41a4-9c4c-d4e14efca238', name='Update title')
    print("res ", res)
except ServerException as e:
    raise e
except Exception as e:
    raise e
```

#### Parameters

- **id** (*str*) - Identifier of category.
- **name** (*str*) - Name of category.
- **type** (*str*) - Has 3 types of category [ folder, playlist, tag ].
- **description** (*str*) - Description for category.
- **orderNumber** (*int*) - Order number for category, lower number is higher order	.
- **icon** (*str*) - Small icon for each category.

#### Return type

- Tuple

#### Return

- Response data and status code

### Delete an category

`delete(id)`

Function to delete category.

For example:

```python
import uiza

from uiza.api_resources.category import Category
from uiza.exceptions import ServerException

uiza.workspace_api_domain = "your-workspace-api-domain.uiza.co"
uiza.authorization = "your-authorization"

try:
    res, status_code = Category().delete(id='ddf09dd0-b7a8-4f29-92df-14dafb97b2aa')
    print("res ", res)
except ServerException as e:
    raise e
except Exception as e:
    raise e
```

#### Parameters

- **id** (*str*) - Identifier of category.

#### Return type

- Tuple

#### Return

- Response data and status code

### Create category relation

`create_relation(**data)`

Function to add relation for entity and category.

For example:

```python
import uiza

from uiza.api_resources.category import Category
from uiza.exceptions import ServerException

uiza.workspace_api_domain = "your-workspace-api-domain.uiza.co"
uiza.authorization = "your-authorization"

try:
    res, status_code = Category().create_relation(
        entity_id="16ab25d3-fd0f-4568-8aa0-0339bbfd674f",
        metadata_ids=["095778fa-7e42-45cc-8a0e-6118e540b61d","e00586b9-032a-46a3-af71-d275f01b03cf"]
    )
    print("res ", res)
except ServerException as e:
    raise e
except Exception as e:
    raise e
```

#### Parameters

- **entityId** (*str*) - Identifier of entity.
- **metadataIds** (*array*) - Identifier of category.

#### Return type

- Tuple

#### Return

- Response data and status code

### Delete category relation

`delete_relation(**data)`

Function to delete relation for entity and category.

For example:

```python
import uiza

from uiza.api_resources.category import Category
from uiza.exceptions import ServerException

uiza.workspace_api_domain = "your-workspace-api-domain.uiza.co"
uiza.authorization = "your-authorization"

try:
    res, status_code = Category().delete_relation(
        entity_id="16ab25d3-fd0f-4568-8aa0-0339bbfd674f",
        metadata_ids=["095778fa-7e42-45cc-8a0e-6118e540b61d","e00586b9-032a-46a3-af71-d275f01b03cf"]
    )
    print("res ", res)
except ServerException as e:
    raise e
except Exception as e:
    raise e
```

#### Parameters

- **entityId** (*str*) - Identifier of entity.
- **metadataIds** (*array*) - Identifier of category.

#### Return type

- Tuple

#### Return

- Response data and status code
