from django.shortcuts import render, redirect, reverse

from customers import models, forms
from genMerch import views as custom_views


class CustomerIndexTemplateView(custom_views.CustomTemplateView):
    template_name = "customers/customers.html"
    queryset = models.Customer.objects.all()  # pylint: disable=no-member
    default_form = forms.CustomerRegistrationModelForm
    default_context = {"is_customer": True}

    def post(self, request):
        customer_id = int(request.POST.get("id"))
        # pylint: disable=no-member
        customer_instance = models.Customer.objects.get(id=customer_id)

        if "delete" in request.POST:
            customer_instance.delete()

            return redirect("customers:dashboard")

        form = self.default_form(
            request.POST, request.FILES, instance=customer_instance
        )

        if form.is_valid():
            form.save()

        return redirect("customers:dashboard")


class CustomerRegistrationTemplateView(custom_views.CustomTemplateView):
    template_name = "customers/customer_reg.html"
    queryset = models.Customer.objects.all()  # pylint: disable=no-member
    default_form = forms.CustomerRegistrationModelForm
    default_context = {"is_customer": True}

    def post(self, request):
        form = self.default_form(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            return redirect(reverse("customers:dashboard"))

        context = self.get_context_data()
        context["has_error"] = True

        return render(request, self.template_name, context=context)
