from marshmallow import ValidationError


def validate_schema(schema):
    def validate(func):
        def wrapper(_, **kwargs):
            if not kwargs:
                return func(_)
            params, errors = schema.load(kwargs)
            if errors:
                raise ValidationError(errors)
            return func(_, params)
        return wrapper
    return validate
