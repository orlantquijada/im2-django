from django import forms
from products import models


class ProductForm(forms.ModelForm):

    img1 = forms.ImageField(required=False)
    img2 = forms.ImageField(required=False)
    img3 = forms.ImageField(required=False)

    class Meta:
        model = models.Product
        fields = ('date_registered', 'sku', 'category', 'prod_name', 'brand',
                  'color', 'size', 'price', 'stocks', 'img1', 'img2', 'img3')
