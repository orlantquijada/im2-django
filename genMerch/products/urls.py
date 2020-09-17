from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('index', views.product_index_view, name="dashboard"),
   # path('registration', views.product_registration_view, name="registration")
    path('registration', views.ProductRegistrationView.as_view(), name="registration")
]