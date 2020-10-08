from django.db import models

# Create your models here.

class OrderProduct(models.Model):
    product_id = models.IntegerField()
    quantity = models.IntegerField(null=True)
    class Meta:
        db_table = 'OrderProduct'

class Cart(models.Model):
    product_id = models.IntegerField()
    price = models.IntegerField()
    quantity = models.IntegerField()
    product_name = models.CharField(max_length=100,null=True)
    class Meta:
        db_table = 'Cart'