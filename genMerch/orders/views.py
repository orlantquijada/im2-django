from django.shortcuts import render, redirect, reverse
from django.db.models import F, Sum

from products import models as products_models
from orders import models as orders_models, forms as orders_forms
from genMerch import views as custom_views


class OrderTemplateView(custom_views.CustomTemplateView):
    template_name = "order.html"
    queryset = products_models.Product.objects.all()  # pylint: disable=no-member
    default_form = orders_forms.CartForm

    def post(self, request):
        form = self.default_form(request.POST)
        product_ids = [int(id) for id in request.POST.getlist("id")]

        update_products = products_models.Product.objects.filter(
            id__in=product_ids
        )  # pylint: disable=no-member

        for product in update_products:
            form = orders_models.Cart(
                product_id_id=product.id,
                price=product.price,
                quantity=1,
                product_name=product.prod_name,
            )
            form.save()
        return redirect(reverse("orders:orders"))


class CartTemplateView(custom_views.CustomTemplateView):
    template_name = "cart.html"
    queryset = orders_models.Cart.objects.all()  # pylint: disable=no-member
    default_form = orders_forms.OrderForm

    def get(self, request):
        context = self.get_context_data()
        context["total"] = self.queryset.aggregate(total=Sum("product_id__price")).get(
            "total", 0
        )

        return render(request, self.template_name, context=context)

    def post(self, request):
        form = self.default_form(request.POST)
        prod_ids = [int(id) for id in request.POST.getlist("sid")]

        # pylint: disable=no-member
        update_prod = products_models.Product.objects.filter(id__in=prod_ids)
        if "purchase" in request.POST:
            update_prod.update(stocks=F("stocks") - 1)
            for product in update_prod:
                form = orders_models.OrderProduct(product_id_id=product.id, quantity=1)
                form.save()

        cart_ids = [int(id) for id in request.POST.getlist("cid")]
        update_cart = orders_models.Cart.objects.filter(id__in=cart_ids)

        for prod in update_cart:
            orders_models.Cart.objects.filter(
                id=prod.id
            ).delete()  # pylint: disable=no-member

        return redirect(reverse("orders:orders"))
