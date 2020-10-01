from django.shortcuts import render, redirect, reverse
from django.db import transaction

from products import models, forms
from genMerch import views as custom_views


class ProductIndexTemplateView(custom_views.CustomTemplateView):
    template_name = "products/products.html"
    queryset = models.Product.objects.all()  # pylint: disable=no-member
    # default_form = forms.ProductForm

    def post(self, request):
        #  form = self.default_form(request.POST, request.FILES)

        if request.method == "POST":
            if "btnUpdate" in request.POST:
                print("update clicked")
                pid = request.POST.get("prodID")
                pname = request.POST.get("prod_name")
                pcat = request.POST.get("category")
                pbrand = request.POST.get("brand")
                pcolor = request.POST.get("color")
                psize = request.POST.get("size")
                pprice = request.POST.get("price")
                pstocks = request.POST.get("stocks")

                # imgs = request.POST.getlist("img")

                # pylint: disable=no-member
                update_product = models.Product.objects.filter(id=pid).update(
                    prod_name=pname,
                    category=pcat,
                    brand=pbrand,
                    color=pcolor,
                    size=psize,
                    price=pprice,
                    stocks=pstocks,
                )

                print(update_product)
                print("product updated")
            elif "btnDelete" in request.POST:
                print("delete clicked")
                pid = request.POST.get("prodID")

                # pylint: disable=no-member
                models.ProductImage.objects.filter(
                    product_id=pid
                ).delete()  # pylint: disable=no-member
                models.Product.objects.filter(
                    id=pid
                ).delete()  # pylint: disable=no-member
                print("product deleted")

        return redirect("products:dashboard")


class ProductRegistrationTemplateView(custom_views.CustomTemplateView):
    template_name = "products/product_reg.html"
    queryset = models.Product.objects.all()  # pylint: disable=no-member
    default_form = forms.ProductForm

    @transaction.atomic
    def post(self, request):
        form = self.default_form(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            img1 = form.cleaned_data.get("img1")
            img2 = form.cleaned_data.get("img2")
            img3 = form.cleaned_data.get("img3")

            instance = form.instance
            product_images = []
            for img in (img1, img2, img3):
                # images are not required
                if not img:
                    continue

                # pylint: disable=no-member
                product_image = models.ProductImage(product=instance, image=img)
                product_images.append(product_image)

            # pylint: disable=no-member
            models.ProductImage.objects.bulk_create(product_images)

            return redirect(reverse("products:dashboard"))
        return render(request, "products/product_reg.html")
