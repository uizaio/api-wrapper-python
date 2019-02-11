from uiza.user.user import User
from uiza.base.connections import Connection

if __name__ == '__main__':
    data = {
        "status": 1,
        "username":"user_test",
        "email":"user_test@uiza.io",
        "fullname":"User Test",
        "avatar":"https://exemple.com/avatar.jpeg",
        "dob":"05/15/2018",
        "gender":0,
        "password":"FMpsr<4[dGPu?B#u",
        "isAdmin":1
    }

    connection = Connection(workspace_api_domain='localhost:5000',  api_key='abcd1234')
    user = User(connection) #.create(**data)
    x = user.create(**data)    # userservice = UserConnection(workspace_api_domain='localhost:5000',  api_key='abcd1234')
    # import pdb
    # pdb.set_trace()
    print(x)
