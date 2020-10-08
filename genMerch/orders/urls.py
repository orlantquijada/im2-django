from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('',views.OrderTemplateView.as_view(),name="orders")
]