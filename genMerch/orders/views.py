from django.shortcuts import render
from genMerch import views as custom_views
from django.http import HttpResponse
from products import models, forms

from django.db.models import F
# Create your views here.

class OrderTemplateView(custom_views.CustomTemplateView):
    template_name = "order.html"
    queryset = models.Product.objects.all()  # pylint: disable=no-member

    def post(self,request):
        if request.method == 'POST':
            product_ids = [int(id) for id in request.POST.getlist("id")]
            update_products = models.Product.objects.filter(id__in = product_ids) # pylint: disable=no-member
            update_products.update(stocks=F('stocks') - 1)
        return HttpResponse("YES")