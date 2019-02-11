from marshmallow import ValidationError


def validate_schema(schema):
    def validate(func):
        def wrapper(_, **kwargs):
            params, errors = schema.load(kwargs)
            if errors:
                raise ValidationError(errors)
            return func(_, params)
        return wrapper
    return validate
