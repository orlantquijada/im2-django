from django.shortcuts import render

def customer_index_view(request):
    return render(request, 'customers/customers.html')

def customer_registration_view(request):
    return render(request, 'customers/customer_reg.html')