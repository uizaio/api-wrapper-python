## User Management

You can manage user with APIs user. Uiza have 2 levels of user:

- Admin - This account will have the highest priority, can have permission to create & manage users.

- User - This account level is under Admin level. It only manages APIs that relates to this account.

We can use a `User` to:

- **create()**
- **retrieve()**
- **update()**
- **list()**
- **delete()**
- **update_password()**
- **logout()**

### Create user

`create(**kwang)`

Function to create an user account for workspace.

For example:

```python

user = User(connection)
user_data = {
    "status": 1,
    "username": "test_admin_pythonvn",
    "email": "user_test@uiza.io",
    "fullname": "User Test",
    "avatar": "https://exemple.com/avatar.jpeg",
    "dob": "05/15/2018",
    "gender": 0,
    "password": "FMpsr<4[dGPu?B#u",
    "isAdmin": 1
}

res, status_code = user.create(**user_data)

print("id: ", res.id)
print("status_code", status_code)
```

#### Parameters

- **status** (*int*) - Status of account ( 0 = de-active, 1 = active).
- **username** (*str*) - Username of account (used for login instead of email).
- **email** (*str*) - Email (used for login instead of username).
- **password** (*str*) - Password (from A to x , 6 to 25 characters).
- **avatar** (*str*) - Link of avatar ( suggest 300x300).
- **fullname** (*str*) - Full name of user.
- **dob** (*str*) - Date of birth (MM/DD/YYYY).
- **gender** (*int*) - Gender ( 0 = Male, 1 = Female).
- **isAdmin** (*int*) - Set this account isAdmin or not (0 = Yes, 1 = No).

#### Return type

- Tuple

#### Return

- Response data and status code

### Retrieve an user

`retrieve(id)`

Function to retrieves the details of an existing user. You need only supply the unique userId that was returned upon user creation.

For example:

```python
user = User(connection)
user_id = '33a86c18-f502-41a4-9c4c-d4e14efca238'

res, status_code = user.retrieve(user_id)

print("id: ", res.id)
print("status_code", status_code)
```

#### Parameters

- **id** (*str*) - Identifier of user.

#### Return type

- Tuple

#### Return

- Response data and status code

### Update an user

`update(**data)`

Function to updates the specified user by setting the values of the parameters passed. Any parameters not provided will be left unchanged.

For example:

```python
user = User(connection)

res, status_code = user.update(id='33a86c18-f502-41a4-9c4c-d4e14efca238', status=1)

print("id: ", res.id)
print("status_code", status_code)
```

#### Parameters

- **id** (*str*) - Identifier of user wanted to update.
- **status** (*int*) - Status of account ( 0 = de-active, 1 = active).
- **username** (*str*) - Username of account (used for login instead of email).
- **email** (*str*) - Email (used for login instead of username).
- **password** (*str*) - Password (from A to x , 6 to 25 characters).
- **avatar** (*str*) - Link of avatar ( suggest 300x300).
- **fullname** (*str*) - Full name of user.
- **dob** (*str*) - Date of birth (MM/DD/YYYY).
- **gender** (*int*) - Gender ( 0 = Male, 1 = Female).
- **isAdmin** (*int*) - Set this account isAdmin or not (0 = Yes, 1 = No).

#### Return type

- Tuple

#### Return

- Response data and status code

### Delete an user

`delete(id)`

Function to delete an user. It cannot be undone. Also immediately cancels all token & information of this user.

For example:

```python
user = User(connection)

res, status_code = user.delete('ddf09dd0-b7a8-4f29-92df-14dafb97b2aa')

print("id: ", res.id)
print("status_code", status_code)
```

#### Parameters

- **id** (*str*) - Identifier of user want to delete.

#### Return type

- Tuple

#### Return

- Response data and status code

### List all users

`list(**params)`

Function to get list of users.The users are returned sorted by creation date, with the most recent user appearing first.

If you use Admin token, you will get all the user. If you use User token, you can only get the information of that user.

For example:

```python
user = User(connection)

res, status_code = user.list()

print("status_code", status_code)
```

#### Parameters

- N/A

#### Return type

- Tuple

#### Return

- Response data and status code

### Update password

`update_password(**data)`

Function to update password allows Admin or User update their current password.

For example:

```python
user = User(connection)
data_pw = {
    'id': "9f1cd871-9244-48a1-a233-846a3b540741",
    "oldPassword": "S57Eb{:aMZhW=)G$",
    "newPassword": "FMpsr<4[dGPu?B#u"
}
res, status_code = user.update_password(**data_pw)

print("id", res.id)
print("status_code", status_code)
```

#### Parameters

- **oldPassword** (*str*) - Current password.
- **newPassword** (*str*) - New password (from a to Z, 6 to 25 characters).
- **id** (*str*) - Identifier of user need reset password.

#### Return type

- Tuple

#### Return

- Response data and status code

### Log Out

`logout()`

Function to log out an user. After logged out, token will be removed.

For example:

```python
user = User(connection)
res, status_code = user.logout()

print("status_code", status_code)
```

#### Parameters

- N/A

#### Return type

- Tuple

#### Return

- Response data and status code
