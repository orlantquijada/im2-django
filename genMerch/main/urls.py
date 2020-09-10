from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.main_view, name="main"),
    path('2', views.main_view2, name='main2')
]