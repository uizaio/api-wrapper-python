from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/api/public/v3/admin/user', methods=['GET', 'POST', 'PUT', 'DELETE'])
def hello_world():
    data = {
        "status": 1,
        "username": "user_test",
        "email": "user_test@uiza.io",
        "fullname": "User Test",
        "avatar": "https://exemple.com/avatar.jpeg",
        "dob": "05/15/2018",
        "gender": 0,
        "password": "FMpsr<4[dGPu?B#u",
        "isAdmin": 1
    }

    if request.method  == 'GET':
        return "This is method GET"

    elif request.method == 'POST':
        return jsonify(**data)
    return "TEST"


if __name__ == '__main__':
    app.run()
