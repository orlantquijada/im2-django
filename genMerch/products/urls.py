from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('index', views.ProductIndexTemplateView.as_view(), name="dashboard"),
    path('registration', views.ProductRegistrationTemplateView.as_view(), name="registration")
]