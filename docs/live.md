## Live Streaming

These APIs used to create and manage live streaming event.

- When a Live is not start : it's named as Event
- When have an Event , you can start it : it's named as Feed

We can use a `Live Streaming` to:

- **create()**
- **retrieve()**
- **update()**
- **start_feed()**
- **stop_feed()**
- **get_view()**
- **list_recorded()**
- **convert_into_vod()**
- **delete()**

### Create live streaming

`create(**kwang)`

Function to create a live streaming and manage the live streaming input (output). A live stream can be set up and start later or start right after set up. Live Channel Minutes counts when the event starts..

For example:

```python
import uiza

from uiza.api_resources.live import Live
from uiza.exceptions import ServerException

uiza.workspace_api_domain = "your-workspace-api-domain.uiza.co"
uiza.authorization = "your-authorization"

live_data = {
    "name":"test event python 1",
    "mode":"push",
    "encode":1,
    "dvr":1,
    "linkStream":[
        "https://playlist.m3u8"
    ],
    "resourceMode":"single"
}
try:
    res, status_code = Live().create(**live_data)
    print("res ", res)
except ServerException as e:
    raise e
except Exception as e:
    raise e
```

#### Parameters

- **name** (*str*) - The event name (limit 100 characters).
- **mode** (*int*) - Type of event can be pull or push.
- **encode** (*str*) - Mode of live stream (0 = no encode, 1 = encode).
- **dvr** (*str*) - Feed after streamed will be recorded as a mp4 file.
- **description** (*str*) - Description of the live stream.
- **linkPublishSocial** (*str*) - Info to share live into social.
- **thumbnail** (*str*) - An Image link.
- **linkStream** (*str*) - Link streaming (if you choose mode = pull).
- **resourceMode** (*str*) - Resource mode ( single = only 1 feed & output), redundant = more than 1 feed & output to backup).

#### Return type

- Tuple

#### Return

- Response data and status code

### Retrieve an live streaming

`retrieve(id)`

Function to get detail of an existing event. You need only provide the unique identifier of event that was returned upon Live event creation.

For example:

```python
import uiza

from uiza.api_resources.live import Live
from uiza.exceptions import ServerException

uiza.workspace_api_domain = "your-workspace-api-domain.uiza.co"
uiza.authorization = "your-authorization"

try:
    res, status_code = Live().retrieve(id='33a86c18-f502-41a4-9c4c-d4e14efca238')
    print("res ", res)
except ServerException as e:
    raise e
except Exception as e:
    raise e
```

#### Parameters

- **id** (*str*) - Identifier of live event.

#### Return type

- Tuple

#### Return

- Response data and status code

### Update a live event

`update(**data)`

Function to update the specific Live event by edit values of parameter.

For example:

```python
import uiza

from uiza.api_resources.live import Live
from uiza.exceptions import ServerException

uiza.workspace_api_domain = "your-workspace-api-domain.uiza.co"
uiza.authorization = "your-authorization"

try:
    res, status_code = Live().update(id='33a86c18-f502-41a4-9c4c-d4e14efca238', name='Update title')
    print("res ", res)
except ServerException as e:
    raise e
except Exception as e:
    raise e
```

#### Parameters

- **id** (*str*) - Identifier of entity live.
- **name** (*str*) - The event name (limit 100 characters).
- **dvr** (*int*) - Feed after streamed will be recorded as a mp4 file .
- **mode** (*str*) - Type of event ( pull or push) .
- **encode** (*int*) - Mode of live stream (0 = no encode, 1 = encoded).
- **resourceMode** (*str*) - Resource mode ( single = only 1 feed & output), redundant = more than 1 feed & output to backup).

#### Return type

- Tuple

#### Return

- Response data and status code

### Start a live feed

`start_feed(id)`

Function to start a live event that has been create success. The Live channel minute start count whenever the event start success.

For example:

```python
import uiza

from uiza.api_resources.live import Live
from uiza.exceptions import ServerException

uiza.workspace_api_domain = "your-workspace-api-domain.uiza.co"
uiza.authorization = "your-authorization"

try:
    res, status_code = Live().start_feed(id='ddf09dd0-b7a8-4f29-92df-14dafb97b2aa')
    print("res ", res)
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

### Stop a live feed

`stop_feed(id)`

Function to stop live event.

For example:

```python
import uiza

from uiza.api_resources.live import Live
from uiza.exceptions import ServerException

uiza.workspace_api_domain = "your-workspace-api-domain.uiza.co"
uiza.authorization = "your-authorization"

try:
    res, status_code = Live().stop_feed(id='ddf09dd0-b7a8-4f29-92df-14dafb97b2aa')
    print("res ", res)
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

### Get view of live feed

`get_view(id)`

Function to get a live view status . This view only show when event has been started and being processing.

For example:

```python
import uiza

from uiza.api_resources.live import Live
from uiza.exceptions import ServerException

uiza.workspace_api_domain = "your-workspace-api-domain.uiza.co"
uiza.authorization = "your-authorization"

try:
    res, status_code = Live().get_view(id='ddf09dd0-b7a8-4f29-92df-14dafb97b2aa')
    print("res ", res)
except ServerException as e:
    raise e
except Exception as e:
    raise e
```

#### Parameters

- **id** (*str*) - EventId has been created.

#### Return type

- Tuple

#### Return

- Response data and status code

### List all recorded files

`list_recorded()`

Function to retrieves list of recorded file after streamed (only available when your live event has turned on Record feature).

For example:

```python
import uiza

from uiza.api_resources.live import Live
from uiza.exceptions import ServerException

uiza.workspace_api_domain = "your-workspace-api-domain.uiza.co"
uiza.authorization = "your-authorization"

try:
    res, status_code = Live().list_recorded()
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

### Delete a record file

`delete_recorded(id)`

Function to delete a recorded file.

For example:

```python
import uiza

from uiza.api_resources.live import Live
from uiza.exceptions import ServerException

uiza.workspace_api_domain = "your-workspace-api-domain.uiza.co"
uiza.authorization = "your-authorization"

try:
    res, status_code = Live().delete(id='ddf09dd0-b7a8-4f29-92df-14dafb97b2aa')
    print("res ", res)
except ServerException as e:
    raise e
except Exception as e:
    raise e
```

#### Parameters

- **id** (*str*) - Identifier of record (get from list record).

#### Return type

- Tuple

#### Return

- Response data and status code

### Convert into VOD

`convert_into_vod(id)`

Function to delete a recorded file.

For example:

```python
import uiza

from uiza.api_resources.live import Live
from uiza.exceptions import ServerException

uiza.workspace_api_domain = "your-workspace-api-domain.uiza.co"
uiza.authorization = "your-authorization"

try:
    res, status_code = Live().convert_into_vod(id='ddf09dd0-b7a8-4f29-92df-14dafb97b2aa')
    print("res ", res)
except ServerException as e:
    raise e
except Exception as e:
    raise e
```

#### Parameters

- **id** (*str*) - Identifier of record (get from list record).

#### Return type

- Tuple

#### Return

- Response data and status code
