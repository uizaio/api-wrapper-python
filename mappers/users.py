from marshmallow import fields, validate

from mappers.base import BaseSchema
from utility.utility import validate_password

DATE_FORMAT = 'MM/DD/YYYY'
DATE_FORMAT_REGEX = r'^(?P<month>1[0-2]|0[1-9])/(?P<day>3[01]|0[1-9]|[12][0-9])/(?P<year>[0-9]{4})$'

class CreateUserSchema(BaseSchema):
    status = fields.Int(required=True, validate=lambda n: n in [0, 1])
    username = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(required=True, validate=validate_password)
    avatar = fields.Str()
    fullname = fields.Str()
    dob = fields.Str(validate=validate.Regexp(regex=DATE_FORMAT_REGEX))
    gender = fields.Int(validate=lambda n: n in [0, 1])
    isAdmin = fields.Int(validate=lambda n: n in [0, 1])

    class Meta:
        strict = True


class UpdateUserSchema(BaseSchema):
    id = fields.Str(required=True)
    status = fields.Int(validate=lambda n: n in [0, 1])
    username = fields.Str()
    email = fields.Email()
    password = fields.Str()
    avatar = fields.Str()
    fullname = fields.Str()
    dob = fields.Str(validate=validate.Regexp(regex=DATE_FORMAT_REGEX))
    gender = fields.Int(validate=lambda n: n in [0, 1])
    isAdmin = fields.Int(validate=lambda n: n in [0, 1])

    class Meta:
        strict = True


class UpdatePasswordUserSchema(BaseSchema):
    id = fields.Str(required=True)
    oldPassword = fields.Str(required=True, validate=validate_password)
    newPassword = fields.Str(required=True, validate=validate_password)

    class Meta:
        strict = True


class GetUsersSchema(BaseSchema):
    id = fields.Str()
    isAdmin = fields.Int(validate=lambda n: n in [0, 1])
    username = fields.Str()
    email = fields.Email()
    createdAt = fields.Str()
    updatedAt = fields.Str()

    class Meta:
        strict = True
