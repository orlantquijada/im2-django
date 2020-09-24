from django.shortcuts import render, redirect, reverse

from customers import models, forms
from genMerch import views as custom_views


class CustomerIndexTemplateView(custom_views.CustomTemplateView):
    template_name = 'customers/customers.html'
    queryset = models.Customer.objects.all()  # pylint: disable=no-member
    default_form = forms.CustomerRegistrationModelForm
    default_context = {'is_customer': True}


class CustomerRegistrationTemplateView(custom_views.CustomTemplateView):
    template_name = 'customers/customer_reg.html'
    queryset = models.Customer.objects.all()  # pylint: disable=no-member
    default_form = forms.CustomerRegistrationModelForm
    default_context = {'is_customer': True}

    def post(self, request):
        form = self.default_form(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            return redirect(reverse('customers:dashboard'))
        return render(request, self.template_name)
