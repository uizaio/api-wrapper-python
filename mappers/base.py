import re

from marshmallow import Schema, validates_schema, ValidationError
from marshmallow.fields import DateTime, Date


class BaseSchema(Schema):

    @validates_schema(pass_original=True)
    def check_unknown_fields(self, data, original_data):
        unknown = set(original_data) - set(self.fields)
        if unknown:
            raise ValidationError('Unknown field', unknown)
