from application.validators import exception

def is_valid_put_req(req):
    if type(req) == dict:
        return True
    raise exception.BadRequestException()