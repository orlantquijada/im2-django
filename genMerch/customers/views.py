from django.shortcuts import render, redirect, reverse

from customers import models, forms
from genMerch import views as custom_views


class CustomerIndexTemplateView(custom_views.CustomTemplateView):
    template_name = 'customers/customers.html'
    queryset = models.Customer.objects.all()  # pylint: disable=no-member
    default_context = {'is_customer': True}


class CustomerRegistrationTemplateView(custom_views.CustomTemplateView):
    template_name = 'customers/customer_reg.html'
    queryset = models.Customer.objects.all()  # pylint: disable=no-member
    default_form = forms.CustomerRegistrationModelForm
    default_context = {'is_customer': True}

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['form'] = self.default_form()

        return context

    def post(self, request):
        form = self.default_form(request.POST, request.FILES)
        context = self.get_context_data()

        if form.is_valid():
            form.save()

            return redirect(reverse('customers:dashboard'), kwargs=context)
        return render(request, self.template_name, context=context)
