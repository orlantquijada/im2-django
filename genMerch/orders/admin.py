from django.contrib import admin

from orders import models


admin.site.register(models.Cart)
admin.site.register(models.OrderProduct)
admin.site.register(models.OrderItem)
admin.site.register(models.Order)
