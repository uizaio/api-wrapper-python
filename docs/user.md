## User Management

You can manage user with APIs user. Uiza have 2 levels of user:

- Admin - This account will have the highest priority, can have permission to create & manage users.

- User - This account level is under Admin level. It only manages APIs that relates to this account.

We can use a `User` to:

- **retrieve()**
- **update()**
- **list()**
- **change_password()**
- **logout()**

### Retrieve an user

`retrieve(id)`

Function to retrieves the details of an existing user. You need only supply the unique userId that was returned upon user creation.

For example:

```python
import uiza
from uiza.api_resources.user import User

uiza.api_key = "<your-api-key>"
uiza.app_id = "<your-app-id>"

res, status_code = User().retrieve(id='33a86c18-f502-41a4-9c4c-d4e14efca238')

print("res: ", res)
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
import uiza
from uiza.api_resources.user import User

uiza.api_key = "<your-api-key>"
uiza.app_id = "<your-app-id>"

res, status_code = User().update(id='33a86c18-f502-41a4-9c4c-d4e14efca238', status=1)

print("res: ", res)
```

#### Parameters

- **id** (*str*) - Identifier of user wanted to update.
- **status** (*int*) - Status of account ( 0 = de-active, 1 = active).
- **name** (*str*) - Username of account (used for login instead of email).
- **email** (*str*) - Email (used for login instead of username).
- **password** (*str*) - Password (from A to x , 6 to 25 characters).
- **avatar** (*str*) - Link of avatar ( suggest 300x300).
- **fullname** (*str*) - Full name of user.
- **dob** (*str*) - Date of birth (MM-DD-YYYY).
- **gender** (*int*) - Gender ( 0 = Male, 1 = Female).
- **isAdmin** (*int*) - Set this account isAdmin or not (1 = Yes, 0 = No).

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
import uiza
from uiza.api_resources.user import User

uiza.api_key = "<your-api-key>"
uiza.app_id = "<your-app-id>"

res, status_code = User().list()

print("res: ", res)
```

#### Parameters

- N/A

#### Return type

- Tuple

#### Return

- Response data and status code

### Change password

`change_password(**data)`

Function to update password allows Admin or User update their current password.

For example:

```python
import uiza
from uiza.api_resources.user import User

uiza.api_key = "<your-api-key>"
uiza.app_id = "<your-app-id>"

res, status_code = User().change_password(
    user_id="9f1cd871-9244-48a1-a233-846a3b540741",
    old_password="S57Eb{:aMZhW=)G$",
    new_password="FMpsr<4[dGPu?B#u"
)

print("res: ", res)
```

#### Parameters

- **old_password** (*str*) - Current password.
- **new_password** (*str*) - New password (from a to Z, 6 to 25 characters).
- **user_id** (*str*) - Identifier of user need reset password.

#### Return type

- Tuple

#### Return

- Response data and status code

### Log Out

`logout()`

Function to log out an user. After logged out, token will be removed.

For example:

```python
import uiza
from uiza.api_resources.user import User

uiza.api_key = "<your-api-key>"
uiza.app_id = "<your-app-id>"

res, status_code = User().logout()

print("res: ", res)
```

#### Parameters

- N/A

#### Return type

- Tuple

#### Return

- Response data and status code
