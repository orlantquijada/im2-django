from django.contrib import admin

from customers import models

admin.site.register(models.Person)
admin.site.register(models.Customer)
