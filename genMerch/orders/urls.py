from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('',views.OrderTemplateView.as_view(),name="orders"),
    path('cart',views.CartTemplateView.as_view(),name="cart"),
]