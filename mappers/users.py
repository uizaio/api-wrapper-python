from marshmallow import fields

from mappers.base import BaseSchema, DateISO8601
from utility.utility import validate_password

DATE_FORMAT = 'MM/DD/YYYY'


class CreateUserSchema(BaseSchema):
    status = fields.Int(required=True, validate=lambda n: n in [0, 1])
    username = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(required=True, validate=validate_password)
    avatar = fields.Str()
    fullname = fields.Str()
    dob = fields.Str(format=DATE_FORMAT)
    gender = fields.Int(validate=lambda n: n in [0, 1])
    isAdmin = fields.Int(validate=lambda n: n in [0, 1])

    class Meta:
        strict = True


class UpdateUserSchema(BaseSchema):
    status = fields.Int(validate=lambda n: n in [0, 1])
    username = fields.Str()
    email = fields.Email()
    password = fields.Str()
    avatar = fields.Str()
    fullname = fields.Str()
    dob = DateISO8601(format=DATE_FORMAT)
    gender = fields.Int(validate=lambda n: n in [0, 1])
    isAdmin = fields.Int(validate=lambda n: n in [0, 1])

    class Meta:
        strict = True


class UpdatePasswordUserSchema(BaseSchema):
    oldPassword = fields.Str(required=True, validate=validate_password)
    newPassword = fields.Int(required=True, validate=validate_password)

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
