from django.db import models
from datetime import date

from genMerch import globals, fields as custom_fields

# Create your models here.


class Product(models.Model):
    date_registered = models.DateField(default=date.today)
    sku = models.PositiveIntegerField(default=0)

    category = custom_fields.TitleCaseCharfield(
        max_length=globals.DEFAULT_MAX_LENGTH)
    prod_name = custom_fields.TitleCaseCharfield(
        max_length=globals.DEFAULT_MAX_LENGTH)
    brand = custom_fields.TitleCaseCharfield(
        max_length=globals.DEFAULT_MAX_LENGTH)
    color = custom_fields.TitleCaseCharfield(
        max_length=globals.DEFAULT_MAX_LENGTH)

    size = models.FloatField()
    price = models.FloatField()
    stocks = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = 'Products'

    def __str__(self):
        # pylint: disable=no-member
        return f'{self.id} / {self.prod_name}'


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='product_images')
    image = models.ImageField(upload_to='images/products/prod_image/')

    class Meta:
        db_table = 'Product_Image'

    def __str__(self):
        # pylint: disable=no-member
        return f'{self.product_id} / {str(self.image)}'
