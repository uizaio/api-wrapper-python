import unittest

class TestIntegration(unittest.TestCase):

    def __init__(self):
        super(TestIntegration, self).__init__()
        self.user_id = '37d6706e-be91-463e-b3b3-b69451dd4752'
        self.data = {
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

    # @unittest.mock
    # def test_get_user_valid(self):

