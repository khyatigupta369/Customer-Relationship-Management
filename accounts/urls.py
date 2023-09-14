from django.contrib import admin
from django.urls import path, include

from . import views

# url patters 'customer/' is correct and '/customer' is wrong
# link name followed by slash
urlpatterns = [
    path('', views.home, name = 'home'),
    path('products/', views.products, name = 'products'),
    path('customer/<str:pk>/', views.customer, name = 'customer'),

    path('create_order/<str:pk>/', views.createOrder, name = 'create_order'),
    path('update/<str:pk>/', views.updateOrder, name = 'update_order'),
    path('delete/<str:pk>/', views.deleteOrder, name = 'delete_order'),
]
