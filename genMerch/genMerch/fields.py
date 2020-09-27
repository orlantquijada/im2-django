from django.db import models
from django.core.validators import MinLengthValidator

from genMerch import globals
from customers.validators import validate_phone_number


class TitleCaseCharfield(models.CharField):
    """
    Formats text to title case.
    """

    def get_prep_value(self, value):
        value = super().get_prep_value(value)
        if value:
            return value.title()

        return value


class PhoneNumberField(models.CharField):

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = globals.PHONE_NUMBER_MAX_LENGTH
        kwargs['validators'] = [
            MinLengthValidator(limit_value=globals.PHONE_NUMBER_MIN_LENGTH),
            validate_phone_number]

        super().__init__(*args, **kwargs)

    def get_prep_value(self, value):
        value = super().get_prep_value(value)
        if value and '-' not in value:
            return f'{value[0:4]}-{value[4:8]}-{value[8:11]}'

        return value
