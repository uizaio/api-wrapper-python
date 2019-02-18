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

category = Category(connection)
category_data = {
        "name": "Test name 1",
        "type": "folder",
    }

res, status_code = category.create(**category_data)

print("id: ", res.id)
print("status_code", status_code)
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
category = Category(connection)
category_id = '33a86c18-f502-41a4-9c4c-d4e14efca238'

res, status_code = category.retrieve(category_id)

print("status_code", status_code)
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
category = Category(connection)

res, status_code = category.list()

print("status_code", status_code)
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
category = Category(connection)

res, status_code = category.update(id='33a86c18-f502-41a4-9c4c-d4e14efca238', name='Update title')

print("id: ", res.id)
print("status_code", status_code)
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
category = Category(connection)

res, status_code = category.delete('ddf09dd0-b7a8-4f29-92df-14dafb97b2aa')

print("id: ", res.id)
print("status_code", status_code)
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
category = Category(connection)
data = {
    "entityId":"16ab25d3-fd0f-4568-8aa0-0339bbfd674f",
    "metadataIds":["095778fa-7e42-45cc-8a0e-6118e540b61d","e00586b9-032a-46a3-af71-d275f01b03cf"]
}

res, status_code = category.create_relation(**data)

print("status_code", status_code)
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
category = Category(connection)
data = {
    "entityId":"16ab25d3-fd0f-4568-8aa0-0339bbfd674f",
    "metadataIds":["095778fa-7e42-45cc-8a0e-6118e540b61d","e00586b9-032a-46a3-af71-d275f01b03cf"]
}

res, status_code = category.delete_relation(**data)

print("status_code", status_code)
```

#### Parameters

- **entityId** (*str*) - Identifier of entity.
- **metadataIds** (*array*) - Identifier of category.

#### Return type

- Tuple

#### Return

- Response data and status code
