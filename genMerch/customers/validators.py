from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_phone_number(value: str):
    invalid = False

    if value[0:2] != '09':
        invalid = True

    # checks if phone number has - :0922-222-2222
    elif '-' in value:
        phone_number = value.split('-')

        if len(phone_number) != 3:
            invalid = True

        if not invalid:
            for num in phone_number:
                if not num.isnumeric():
                    invalid = True
                    break

    # value now must be 09222222222
    elif not value.isnumeric() or len(value) != 11:
        invalid = True

    if invalid:
        raise ValidationError(
            _(f'{value} is an invalid phone number'), params={'value': value})
