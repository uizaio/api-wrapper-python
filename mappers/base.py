import re

from marshmallow import Schema, validates_schema, ValidationError
from marshmallow.fields import DateTime, Date


class BaseSchema(Schema):

    @validates_schema(pass_original=True)
    def check_unknown_fields(self, data, original_data):
        unknown = set(original_data) - set(self.fields)
        if unknown:
            raise ValidationError('Unknown field', unknown)


class DateTimeISO8601(DateTime):

    def validate_iso8601_format(self, value):
        iso8601_pattern = (
            r'^(?P<year>[0-9]{4})-(?P<month>1[0-2]|0[1-9])-(?P<day>3[01]|0[1-9]|[12][0-9])'
            'T(?P<hour>2[0-3]|[01][0-9]):(?P<minute>[0-5][0-9]):(?P<second>[0-5][0-9])'
            '[+-](?P<tz_hh>[0-9]{2}):(?P<tz_mm>[0-9]{2})$'
        )
        try:
            match = re.match(iso8601_pattern, value)
        except TypeError:
            return

        if not match:
            raise ValidationError('Not a valid datetime.')

    def _deserialize(self, value, attr, data):
        self.validate_iso8601_format(value)
        return super()._deserialize(value, attr, data)


class DateISO8601(Date):

    def validate_iso8601_format(self, value):
        iso8601_pattern = (
            r'^(?P<day>3[01]|0[1-9]|[12][0-9])/(?P<month>1[0-2]|0[1-9])/(?P<year>[0-9]{4})/$'
        )
        try:
            match = re.match(iso8601_pattern, value)
        except TypeError:
            return

        if not match:
            raise ValidationError('Not a valid date.')

    def _deserialize(self, value, attr, data):
        self.validate_iso8601_format(value)
        return super()._deserialize(value, attr, data)
