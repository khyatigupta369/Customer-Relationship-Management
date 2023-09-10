from django.contrib import admin
from django.urls import path, include

from . import views

# url patters 'customer/' is correct and '/customer' is wrong
# link name followed by slash
urlpatterns = [
    path('', views.home, name = 'home'),
    path('products/', views.products, name = 'products'),
    path('customer/<str:pk>/', views.customer, name = 'customer'),
]
