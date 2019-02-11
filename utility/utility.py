from marshmallow import ValidationError

PASSWORD_MIN_LENGTH = 6
PASSWORD_MAX_LENGTH = 25

API_CONCEPT = 'http://{workspace_api_domain}/{api_type}/{api_version}/{api_sub_url}'


def validate_password(password: str) -> bool or None:
    if len(password) < PASSWORD_MIN_LENGTH or len(password) > PASSWORD_MAX_LENGTH:
        raise ValidationError('Length of password is invalid')

    if ' ' in password:
        raise ValidationError('Not contain any whitespace')

    return True


def set_url(workspace_api_domain: str,
            api_type: str,
            api_version: str,
            api_sub_url: str):
    return API_CONCEPT.format(
            workspace_api_domain=workspace_api_domain,
            api_type=api_type,
            api_version=api_version,
            api_sub_url=api_sub_url
        )
