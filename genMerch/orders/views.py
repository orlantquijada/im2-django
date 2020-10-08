from django.shortcuts import render,redirect,reverse
from genMerch import views as custom_views
#from django.http import HttpResponse

from products import models, forms
from orders import models as model, forms as form

from django.db.models import F
# Create your views here.

class OrderTemplateView(custom_views.CustomTemplateView):
    template_name = "order.html"
    queryset = models.Product.objects.all()  # pylint: disable=no-member
    default_form = form.CartForm

    def post(self,request):
        form = self.default_form(request.POST)
        if request.method == 'POST':
            product_ids = [int(id) for id in request.POST.getlist("id")]
            update_products = models.Product.objects.filter(id__in = product_ids) # pylint: disable=no-member
            #update_products.update(stocks=F('stocks') - 1)

            for product in update_products:
                form = model.Cart(product_id = product.id,price = product.price,quantity = 1,product_name= product.prod_name)
                form.save()
        #return HttpResponse("YES")
        return redirect(reverse("orders:orders"))

class CartTemplateView(custom_views.CustomTemplateView):
    template_name = "cart.html"
    queryset = model.Cart.objects.all() # pylint: disable=no-member
    default_form = form.OrderForm
    
    def post(self,request):
        form = self.default_form(request.POST)
        if request.method == 'POST':
            prod_ids = [int(id) for id in request.POST.getlist("sid")]
            update_prod = models.Product.objects.filter(id__in = prod_ids) # pylint: disable=no-member
            if 'purchase' in request.POST:
                update_prod.update(stocks=F('stocks') - 1)
                for product in update_prod:
                    form = model.OrderProduct(product_id = product.id, quantity = 1)
                    form.save()
            cart_ids = [int(id) for id in request.POST.getlist("cid")]
            update_cart = model.Cart.objects.filter(id__in = cart_ids)  # pylint: disable=no-member
            for prod in update_cart:
                model.Cart.objects.filter(id = prod.id).delete()  # pylint: disable=no-member
                
        return redirect(reverse("orders:orders"))