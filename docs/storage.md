## Storage

This is client for calling to API storage. You can add your storage (FTP, AWS S3) with UIZA. After synced, you can select your content easier from your storage to [create entity](https://docs.uiza.io/#create-entity).

We can use a `Storage` to:

- **create()**
- **retrieve()**
- **update()**
- **delete()**

### Create storage

`create(**kwang)`

Function to create storage.

For example:

```python

storage = Storage(connection)
storage_data = {
        "name":"FTP Uiza Test",
        "description":"FTP of Uiza, use for transcode",
        "storageType":"ftp",
        "host":"ftp-example.uiza.io"
    }

res, status_code = storage.create(**storage_data)

print("id: ", res.id)
print("status_code", status_code)
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
storage = Storage(connection)
storage_id = '33a86c18-f502-41a4-9c4c-d4e14efca238'

res, status_code = storage.retrieve(storage_id)

print("id: ", res.id)
print("status_code", status_code)
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
storage = Storage(connection)

res, status_code = storage.update(id='33a86c18-f502-41a4-9c4c-d4e14efca238', name='Update title')

print("id: ", res.id)
print("status_code", status_code)
```

#### Parameters

- **id** (*str*) - Identifier of the storage.
- **name** (*str*) - Name of storage.
- **host** (*str*) - Host name of the server or IP address.
- **port** (*int*) - Used port for FTP server. Normally will be 21.
- **storageType** (*str*) - Storage can be FTP or AWS S3. Allowed values: [S3, FTP].
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

`delete(id)`

Function to delete storage.

For example:

```python
storage = Storage(connection)

res, status_code = storage.delete('ddf09dd0-b7a8-4f29-92df-14dafb97b2aa')

print("id: ", res.id)
print("status_code", status_code)
```

#### Parameters

- **id** (*str*) - Identifier of storage.

#### Return type

- Tuple

#### Return

- Response data and status code
