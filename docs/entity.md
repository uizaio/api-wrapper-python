## Entity

This is client for calling to API take action with your media files (we called Entity) See details [here](https://docs.uiza.io/#video).

We can use a `Entity` to:

- **create()**
- **retrieve()**
- **list()**
- **update()**
- **delete()**
- **search()**
- **publish()**
- **get_status_publish()**
- **get_aws_upload_key()**

### Create entity

`create(**kwang)`

Function to create entity using full URL. Direct HTTP, FTP or AWS S3 link are acceptable.

For example:

```python
import uiza

from uiza.api_resources.entity import Entity
from uiza.exceptions import ServerException

uiza.workspace_api_domain = "your-workspace-api-domain.uiza.co"
uiza.authorization = "your-authorization"

entity_data = {
        "name": "Sample Video Python1",
        "url": "https://example.com/video.mp4",
        "inputType": "http",
        "description": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry'\''s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
    }

try:
    res, status_code = Entity().create(**entity_data)
    print("res ", res)
except ServerException as e:
    raise e
except Exception as e:
    raise e
```

#### Parameters

- **name** (*str*) - Name of entity.
- **url** (*str*) - Full URL of media file (direct public HTTP/HTTPS, FTP, AWS S3 acceptable). Send empty string in case of integration using SDK upload to AWS.
- **inputType** (*str*) - Type of URL (Allowed value: [ http, s3, ftp, s3-uiza ] ). In case url is empty string, this must be s3-uiza.
- **description** (*str*) - Full description for entity (without max-length).
- **metadataId** (*list*) - Add relation between entity and folder/playlist.
- **shortDescription** (*str*) - Short description of entity (250 characters).
- **poster** (*str*) - Poster of entity.
- **thumbnail** (*str*) - Thumbnail of entity.
- **metadataIds** (*list*) - List of category will be attached with entity.
- **extendMetadata** (*dict*) - Additional information of entity.
- **embedMetadata** (*dict*) - See [Embed Metadata](https://docs.uiza.io/#embed-metadata) for more information.

#### Return type

- Tuple

#### Return

- Response data and status code

### Retrieve an entity

`retrieve(id)`

Function to get detail of entity including all information of entity.

For example:

```python
import uiza

from uiza.api_resources.entity import Entity
from uiza.exceptions import ServerException

uiza.workspace_api_domain = "your-workspace-api-domain.uiza.co"
uiza.authorization = "your-authorization"

try:
    res, status_code = Entity().retrieve(id='33a86c18-f502-41a4-9c4c-d4e14efca238')
    print("res ", res)
except ServerException as e:
    raise e
except Exception as e:
    raise e
```

#### Parameters

- **id** (*str*) - Identifier of entity.

#### Return type

- Tuple

#### Return

- Response data and status code

### List all entities

`list(**params)`

Function to get list of entities including all detail.

For example:

```python
import uiza

from uiza.api_resources.entity import Entity
from uiza.exceptions import ServerException

uiza.workspace_api_domain = "your-workspace-api-domain.uiza.co"
uiza.authorization = "your-authorization"

try:
    res, status_code = Entity().list(name='Title')
    print("res ", res)
except ServerException as e:
    raise e
except Exception as e:
    raise e
```

#### Parameters

- **id** (*str*) - Identifier of entity.
- **name** (*str*) - Name of entity.
- **description** (*str*) - Full description for entity (without max-length).
- **shortDescription** (*str*) - Short description of entity (250 characters).
- **view** (*int*) - Total view of entity.
- **poster** (*str*) - Poster of entity.
- **thumbnail** (*str*) - Thumbnail of entity.
- **type** (*str*) - Has 2 types: VOD and AOD.
- **duration** (*str*) - Duration of entity in seconds.
- **publishToCdn** (*list*) - Status of publish task, include [ queue, not-ready, success, failed ].
- **embedMetadata** (*dict*) - See [Embed Metadata](https://docs.uiza.io/#embed-metadata) for more information.
- **extendData** (*dict*) - Additional information of entity that already input while creating entity.
- **createdAt** (*str*) - Time created entity.
- **updatedAt** (*str*) - Last edited time of entity.

#### Return type

- Tuple

#### Return

- Response data and status code

### Update an entity

`update(**data)`

Function to update entity's information.

For example:

```python
import uiza

from uiza.api_resources.entity import Entity
from uiza.exceptions import ServerException

uiza.workspace_api_domain = "your-workspace-api-domain.uiza.co"
uiza.authorization = "your-authorization"

try:
    res, status_code = Entity().update(id='33a86c18-f502-41a4-9c4c-d4e14efca238', name='Update title')
    print("res ", res)
except ServerException as e:
    raise e
except Exception as e:
    raise e
```

#### Parameters

- **id** (*str*) - Identifier of entity.
- **name** (*str*) - Name of entity.
- **description** (*str*) - Full description for entity (without max-length).
- **shortDescription** (*str*) - Short description of entity (250 characters).
- **poster** (*str*) - Poster of entity.
- **thumbnail** (*str*) - Thumbnail of entity.
- **extendData** (*dict*) - Additional information of entity that already input while creating entity.

#### Return type

- Tuple

#### Return

- Response data and status code

### Delete an entity

`delete(id)`

Function to delete entity.

For example:

```python
import uiza

from uiza.api_resources.entity import Entity
from uiza.exceptions import ServerException

uiza.workspace_api_domain = "your-workspace-api-domain.uiza.co"
uiza.authorization = "your-authorization"

try:
    res, status_code = Entity().delete(id='ddf09dd0-b7a8-4f29-92df-14dafb97b2aa')
    print("res ", res)
except ServerException as e:
    raise e
except Exception as e:
    raise e
```

#### Parameters

- **id** (*str*) - Identifier of entity.

#### Return type

- Tuple

#### Return

- Response data and status code

### Search entity

`search(**keyword)`

Function to search entity base on keyword entered.

For example:

```python
import uiza

from uiza.api_resources.entity import Entity
from uiza.exceptions import ServerException

uiza.workspace_api_domain = "your-workspace-api-domain.uiza.co"
uiza.authorization = "your-authorization"

try:
    res, status_code = Entity().search(keyword="Title")
    print("res ", res)
except ServerException as e:
    raise e
except Exception as e:
    raise e
```

#### Parameters

- **keyword** (*str*) - Identifier of entity.

#### Return type

- Tuple

#### Return

- Response data and status code

### Publish entity to CDN

`publish(id)`

Function to publish entity to CDN, use for streaming.

For example:

```python
import uiza

from uiza.api_resources.entity import Entity
from uiza.exceptions import ServerException

uiza.workspace_api_domain = "your-workspace-api-domain.uiza.co"
uiza.authorization = "your-authorization"

try:
    res, status_code = Entity().publish(id='ddf09dd0-b7a8-4f29-92df-14dafb97b2aa')
    print("res ", res)
except ServerException as e:
    raise e
except Exception as e:
    raise e
```

#### Parameters

- **id** (*str*) - Identifier of entity.

#### Return type

- Tuple

#### Return

- Response data and status code

### Get status publish

`get_status_publish(id)`

Function to get status publish.

For example:

```python
import uiza

from uiza.api_resources.entity import Entity
from uiza.exceptions import ServerException

uiza.workspace_api_domain = "your-workspace-api-domain.uiza.co"
uiza.authorization = "your-authorization"

try:
    res, status_code = Entity().get_status_publish(id='33a86c18-f502-41a4-9c4c-d4e14efca238')
    print("res ", res)
except ServerException as e:
    raise e
except Exception as e:
    raise e
```

#### Parameters

- **id** (*str*) - Identifier of entity.

#### Return type

- Tuple

#### Return

- Response data and status code

### Get AWS upload key

`get_aws_upload_key()`

Function to get AWS upload key.

For example:

```python
import uiza

from uiza.api_resources.entity import Entity
from uiza.exceptions import ServerException

uiza.workspace_api_domain = "your-workspace-api-domain.uiza.co"
uiza.authorization = "your-authorization"

try:
    res, status_code = Entity().get_aws_upload_key()
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
