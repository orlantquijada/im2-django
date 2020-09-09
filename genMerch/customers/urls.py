from django.urls import path
from . import views

app_name = 'customers'

urlpatterns = [
    path('index', views.CustomerIndexView.as_view(), name="index_view"),
    path('registration', views.CustomerRegView.as_view(), name="registration_view")
]