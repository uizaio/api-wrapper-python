## Storage

This is client for calling to API storage. You can add your storage (FTP, AWS S3) with UIZA. After synced, you can select your content easier from your storage to [create entity](https://docs.uiza.io/#create-entity).

We can use a `Storage` to:

- **add()**
- **retrieve()**
- **update()**
- **remove()**

### Create storage

`add(**kwang)`

Function to add storage.

For example:

```python

import uiza
from uiza.api_resources.storage import Storage

uiza.api_key = "<your-api-key>"
uiza.app_id = "<your-app-id>"

storage_data = {
    "name":"FTP Uiza Test",
    "description":"FTP of Uiza, use for transcode",
    "storageType":"ftp",
    "host":"ftp-example.uiza.io"
}

res, status_code = Storage().add(**storage_data)

print("res: ", res)
```

#### Parameters

- **name** (*str*) - Name of storage.
- **host** (*str*) - Host name of the server or IP address.
- **port** (*int*) - Used port for FTP server. Normally will be 21.
- **storageType** (*str*) - Storage can be FTP or AWS S3. Allowed values: [S3, FTP].
- **username** (*str*) - Account username.
- **password** (*str*) - Account password.
- **description** (*str*) - Storage's description.

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
from uiza.api_resources.storage import Storage

uiza.api_key = "<your-api-key>"
uiza.app_id = "<your-app-id>"

res, status_code = Storage().retrieve(id='33a86c18-f502-41a4-9c4c-d4e14efca238')

print("res: ", res)
```

#### Parameters

- **id** (*str*) - Identifier of storage.

#### Return type

- Tuple

#### Return

- Response data and status code

### Update storage

`update(**data)`

Function to update storage's information.

For example:

```python
import uiza
from uiza.api_resources.storage import Storage

uiza.api_key = "<your-api-key>"
uiza.app_id = "<your-app-id>"

res, status_code = Storage().update(id='33a86c18-f502-41a4-9c4c-d4e14efca238', name='Update title')

print("res: ", res)
```

#### Parameters

- **id** (*str*) - Identifier of the storage.
- **name** (*str*) - Name of storage.
- **host** (*str*) - Host name of the server or IP address.
- **port** (*int*) - Used port for FTP server. Normally will be 21.
- **storageType** (*str*) - Storage can be FTP or AWS S3. Allowed values: ["s3", "ftp", "s3-uiza", "s3-compatible"].
- **awsAccessKey** (*str*) - AWS Access key ID with storageType is S3.
- **awsSecretKey** (*str*) - AWS Secret key ID with storageType is S3.
- **prefix** (*str*) - Prefix for objects store in AWS S3 with storageType is S3.
- **bucket** (*str*) - Bucket data of AWS S3 with storageType is S3.
- **region** (*str*) - AWS S3 region with storageType is S3.
- **description** (*str*) - Storage's description.

#### Return type

- Tuple

#### Return

- Response data and status code

### Delete an storage

`remove(id)`

Function to remove storage.

For example:

```python
import uiza
from uiza.api_resources.storage import Storage

uiza.api_key = "<your-api-key>"
uiza.app_id = "<your-app-id>"

res, status_code = Storage().remove(id='ddf09dd0-b7a8-4f29-92df-14dafb97b2aa')

print("res: ", res)
```

#### Parameters

- **id** (*str*) - Identifier of storage.

#### Return type

- Tuple

#### Return

- Response data and status code
