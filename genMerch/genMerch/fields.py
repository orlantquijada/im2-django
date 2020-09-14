from django.db import models


class TitleCaseCharfield(models.CharField):
    """
    Formats text to title case.
    """

    def get_prep_value(self, value):
        value = super().get_prep_value(value)
        if value:
            return value.title()

        return value
