from django.db import models
from datetime import date

from genMerch import globals, fields as custom_fields

# Create your models here.

class Product(models.Model):
    date_registered = models.DateField()
    # prod_name = models.CharField(max_length=100)
    # category = models.CharField(max_length=50)
    # brand = models.CharField(max_length=50)
    # color = models.CharField(max_length=50)
    prod_name = custom_fields.TitleCaseCharfield(
        max_length=globals.DEFAULT_MAX_LENGTH)
    
    category = custom_fields.TitleCaseCharfield(max_length=globals.DEFAULT_MAX_LENGTH)

    brand = custom_fields.TitleCaseCharfield(max_length=globals.DEFAULT_MAX_LENGTH)

    color = custom_fields.TitleCaseCharfield(max_length=globals.DEFAULT_MAX_LENGTH)

    size = models.FloatField()

    price = models.FloatField()

    stocks = models.IntegerField()

    class Meta:
        db_table = "Products"

class ProductImage(models.Model):
    product = models.ForeignKey(Product, null=False, blank=False,on_delete = models.CASCADE,related_name="Product")
    image = models.ImageField(
        upload_to='static/images/products/prod_image/')

    class Meta:
        db_table = "Product_Image"



