from django.urls import path
from . import views

app_name = 'customers'

urlpatterns = [
    path('index', views.CustomerIndexTemplateView.as_view(), name='dashboard'),
    path('registration', views.CustomerRegistrationTemplateView.as_view(),
         name='customer_registration'),
]
