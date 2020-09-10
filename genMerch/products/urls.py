from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('index', views.ProductIndexView.as_view(), name="index_view"),
    path('registration', views.ProductRegView.as_view(), name="registration_view")
]