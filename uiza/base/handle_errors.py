class Error(Exception):
    pass


class ServerException(Error):
    def __init__(self, message, code):
        self.message = message
        self.code = code

    def __str__(self):
        return self.message
