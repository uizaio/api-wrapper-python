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

callback = Callback(connection)
callback_data = {
        "url":"https://callback-url-python.uiza.co",
        "method":"GET"
    }

res, status_code = callback.create(**callback_data)

print("id: ", res.id)
print("status_code", status_code)
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
callback = Callback(connection)
callback_id = '33a86c18-f502-41a4-9c4c-d4e14efca238'

res, status_code = callback.retrieve(callback_id)

print("id: ", res.id)
print("status_code", status_code)
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
callback = Callback(connection)

res, status_code = callback.update(id='33a86c18-f502-41a4-9c4c-d4e14efca238', method='POST')

print("id: ", res.id)
print("status_code", status_code)
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
callback = Callback(connection)

res, status_code = callback.delete('ddf09dd0-b7a8-4f29-92df-14dafb97b2aa')

print("id: ", res.id)
print("status_code", status_code)
```

#### Parameters

- **id** (*str*) - Identifier of storage.

#### Return type

- Tuple

#### Return

- Response data and status code
