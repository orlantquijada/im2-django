from django.db import models


class Sex(models.TextChoices):
    MALE = ('M', 'Male')
    FEMALE = ('F', 'Female')


class Status(models.TextChoices):
    SINGLE = ('S', 'Single')
    MARRIED = ('M', 'Married')
    WIDOW = ('W', 'Widow/er')
    DIVORCED = ('D', 'Divorced')
