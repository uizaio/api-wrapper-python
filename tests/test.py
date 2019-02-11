import urllib.request
import urllib.parse

if __name__ == '__main__':
    try:
        # Method POST
        body = {
            "status":1,
            "username":"user_test",
            "email":"user_test@uiza.io",
            "fullname":"User Test",
            "avatar":"https://exemple.com/avatar.jpeg",
            "dob":"05/15/2018",
            "gender":0,
            "password":"FMpsr<4[dGPu?B#u",
            "isAdmin":1
        }
        data = urllib.parse.urlencode(body).encode('utf-8')
        req = urllib.request.Request(
            url='http://localhost:5000/api/public/v3/admin/user',
            data = data,
            method='POST'
        )
        res = urllib.request.urlopen(req)
        print("Success: " + res.read().decode('utf8'))

    # # Method DELETE
        # req = urllib.request.Request(
        #     url='http://localhost:5000',
        #     method='DELETE'
        # )
        # res = urllib.request.urlopen(req)
        # print("Success: " + res.read().decode('utf8'))
        #
        # # Method PUT
        # req = urllib.request.Request(
        #     url='http://localhost:5000',
        #     method='PUT'
        # )
        # res = urllib.request.urlopen(req)
        # print("Success: " + res.read().decode('utf8'))

    except urllib.error.URLError as error:
        print("Success: " + error.read().decode('utf8'))
