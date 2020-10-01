from django.shortcuts import render, redirect, reverse
from django.db import transaction
from django.contrib import messages

from products import models, forms
from genMerch import views as custom_views


class ProductIndexTemplateView(custom_views.CustomTemplateView):
    template_name = "products/products.html"
    queryset = models.Product.objects.all()  # pylint: disable=no-member
    default_form = forms.ProductForm

    def post(self, request):
        product_id = int(request.POST.get("id"))
        # pylint: disable=no-member
        product_instance = models.Product.objects.get(id=product_id)

        if "delete" in request.POST:
            product_instance.delete()
            messages.success(
                request, "Product successfully <b>removed</b>.", extra_tags="info"
            )

            return redirect("products:dashboard")

        product_images = product_instance.product_images.all()
        initial_product_images = {}

        for i in range(3):
            try:
                product_image = product_images[i]
            except:
                product_image = None

            initial_product_images[f"img{i+1}"] = product_image

        form = self.default_form(
            request.POST,
            request.FILES,
            instance=product_instance,
            initial=initial_product_images,
        )

        if form.is_valid():
            if "update" in request.POST:
                form.save()

                img1 = form.cleaned_data.get("img1")
                img2 = form.cleaned_data.get("img2")
                img3 = form.cleaned_data.get("img3")

                for form_image, product_image in zip(
                    (img1, img2, img3), product_images
                ):
                    if not isinstance(form_image, models.ProductImage):
                        product_image.image = form_image
                        product_image.save()

                messages.success(
                    request,
                    "Product successfully <b>updated</b>.",
                    extra_tags="primary",
                )

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

            messages.success(
                request, "Customer successfully <b>created</b>.", extra_tags="success"
            )

            return redirect(reverse("products:dashboard"))
        return render(request, "products/product_reg.html")
