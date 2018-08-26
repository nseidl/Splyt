import httplib


def server_response(code=httplib.OK, message="default message", information=None):
    return {
        "code": code,
        "message": message,
        "information": information
    }
