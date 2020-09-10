from django.urls import path
from . import views

app_name = 'customers'

urlpatterns = [
    path('index', views.customer_index_view, name='dashboard'),
    path('registration', views.customer_registration_view, name='customer_registration'),
]