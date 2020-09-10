from django.shortcuts import render
from django.views.generic import View, TemplateView

# Create your views here.

class ProductIndexView(View):
    def get(self, request):
        return render(request, 'products/products.html')

    def post(self, request):
        return render(request, 'products/product_reg.html')

class ProductRegView(View):
    def get(self, request):
        return render(request, 'products/product_reg.html')
