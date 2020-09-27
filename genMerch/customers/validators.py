from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_phone_number(value: str):
    invalid = False

    if value[0:2] != '09':
        invalid = True

    # value format: 0922-222-2222
    elif '-' in value:
        while True:
            if len(value) != 13:
                invalid = True
                break

            # checks if - is in the correct position
            if value.find('-') != 4 and value.rfind('-') != 8:
                invalid = True
                break

            # checks if there are non numeric characters other than -
            for num in value.split('-'):
                if not num.isnumeric():
                    invalid = True
                    break
            break

    # value now must be 09222222222
    elif not value.isnumeric() or len(value) != 11:
        invalid = True

    if invalid:
        raise ValidationError(
            _(f'{value} is an invalid phone number'), params={'value': value})
