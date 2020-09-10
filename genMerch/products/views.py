from django.shortcuts import render

def product_index_view(request):
    return render(request, 'products/products.html', {'is_customer': False})

def product_registration_view(request):
    return render(request, 'products/product_reg.html', {'is_customer': False})