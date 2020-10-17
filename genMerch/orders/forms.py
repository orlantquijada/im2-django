from django import forms
from orders import models


class CartForm(forms.ModelForm):

    class Meta:
        model = models.Cart
        fields = ('product_id',)
        
class OrderForm(forms.ModelForm):

    class Meta:
        model = models.OrderProduct
        fields = ('product_id',)