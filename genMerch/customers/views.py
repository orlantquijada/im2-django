from django.shortcuts import render

def customer_index_view(request):
    return render(request, 'customers/customers.html', {'is_customer': True})

def customer_registration_view(request):
    return render(request, 'customers/customer_reg.html', {'is_customer': True})