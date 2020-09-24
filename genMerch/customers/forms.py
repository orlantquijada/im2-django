from django.forms import ModelForm

from customers import models


class CustomerRegistrationModelForm(ModelForm):
    class Meta:
        model = models.Customer
        fields = '__all__'
