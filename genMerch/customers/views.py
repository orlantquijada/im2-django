from django.shortcuts import render, redirect, reverse
from django.contrib import messages

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

            messages.success(
                request, "Customer successfully <b>removed</b>.", extra_tags="danger"
            )
            return redirect("customers:dashboard")

        form = self.default_form(
            request.POST, request.FILES, instance=customer_instance
        )

        if form.is_valid():
            form.save()
            messages.success(
                request, "Customer successfully <b>updated</b>.", extra_tags="primary"
            )

        context = self.get_context_data()
        context["has_errors"] = True

        fields_with_errors_list = []
        for error in form.errors.keys():
            fields_with_errors_list.append(f"<b>{ error }</b>")

        context["fields with errors"] = fields_with_errors_list

        if form.errors:
            messages.error(
                request,
                f"Incorrect fields: { ', '.join(fields_with_errors_list) }",
                extra_tags="danger",
            )

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

            messages.success(
                request, "Customer successfully <b>created</b>.", extra_tags="success"
            )
            return redirect(reverse("customers:dashboard"))

        context = self.get_context_data()
        context["has_errors"] = True

        fields_with_errors_list = []
        for error in form.errors.keys():
            fields_with_errors_list.append(f"<b>{ error }</b>")

        context["fields with errors"] = fields_with_errors_list

        messages.error(
            request,
            f"Incorrect fields: { ', '.join(fields_with_errors_list) }",
            extra_tags="danger",
        )

        return render(request, self.template_name, context=context)
