from django.forms import ModelForm

from customers import models


class CustomerRegistrationModelForm(ModelForm):
    class Meta:
        model = models.Customer
        fields = ('date_registered', 'employee_id', 'first_name', 'middle_name',
                  'last_name', 'city', 'province', 'zip_code', 'country', 'birthdate',
                  'status', 'sex', 'spouse_name', 'spouse_occupation', 'number_of_children',
                  'father_name', 'father_occupation', 'mother_name', 'mother_occupation',
                  'height', 'weight', 'religion', 'profile_pic')
