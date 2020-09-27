from django.shortcuts import render
from .forms import ProductForm,ProductImageForm
from .models import *
from django.views.generic import View
from django.http import HttpResponse

def product_index_view(request):
    return render(request, 'products/products.html', {'is_customer': False})

def product_registration_view(request):
    return render(request, 'products/product_reg.html', {'is_customer': False})

class ProductRegistrationView(View):
    def get(self, request):
        return render (request, 'products/product_reg.html')
    
    def post(self, request):
        form = ProductForm(request.POST,request.FILES)
        form2 = ProductImageForm(request.POST,request.FILES)
       # prodname = request.FILES["img1"]
       # print(prodname)
        if form.is_valid():
            date_reg = request.POST.get("date_reg")
            prodName = request.POST.get("prod_name")
            category = request.POST.get("category")
            brand = request.POST.get("prodbrand")
            size = request.POST.get("prodSize")
            color = request.POST.get("prodColor")
            price = request.POST.get("prodPrice")
            stock = request.POST.get("prodStocks")
            img1 = request.FILES["img1"]
            img2 = request.FILES["img2"]
            img3= request.FILES["img3"]

            form = Product(date_registered = date_reg, prod_name = prodName, category = category, brand = brand,
                                color = color, size = size, price = price, stocks = stock)
            form.save()

            form2 = ProductImage(product = form,image = img1)
            form2.save()
            form2 = ProductImage(product = form,image = img2)
            form2.save()
            form2 = ProductImage(product = form,image = img3)
            form2.save()

            return HttpResponse('Product Record Saved!')

        else:
            print(form.errors)
            return HttpResponse('not valid')

