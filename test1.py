from uiza.user.user import User
from uiza.base.connections import Connection

if __name__ == '__main__':
    data = {
        # "id": "9f1cd871-9244-48a1-a233-846a3b540741",
        "status": 1,
        "username":"user_test_admin",
        "email":"user_test@uiza.io",
        "fullname":"User Test",
        "avatar":"https://exemple.com/avatar.jpeg",
        "dob":"05/15/2018",
        "gender":0,
        "password":"FMpsr<4[dGPu?B#u",
        "isAdmin":1
    }

    data_pw = {
        'id': "9f1cd871-9244-48a1-a233-846a3b540741",
        "oldPassword": "S57Eb{:aMZhW=)G$",
        "newPassword": "FMpsr<4[dGPu?B#u"
    }

    workspace_api_domain = 'apiwrapper.uiza.co'
    api_key = 'uap-a2aaa7b2aea746ec89e67ad2f8f9ebbf-fdf5bdca'

    connection = Connection(workspace_api_domain=workspace_api_domain,  api_key=api_key)
    user = User(connection) #.create(**data)
    x = user.create(**data)
    # x = user.update(**data)
    # x = user.update_password(**data_pw)
    # x = user.remove('9f1cd871-9244-48a1-a233-846a3b540741')
    # x = user.logout()
    # x = user.get_users()
    # x = user.get_detail('9f1cd871-9244-48a1-a233-846a3b540741')
    print(x)
