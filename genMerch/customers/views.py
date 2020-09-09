from django.shortcuts import render
from django.views.generic import View, TemplateView

# Create your views here.

class CustomerIndexView(View):
    def get(self, request):
        return render(request, 'customers/customers.html')

    def post(self, request):
        return render(request, 'customers/customer_reg.html')

class CustomerRegView(View):
    def get(self, request):
        return render(request, 'customers/customer_reg.html')
