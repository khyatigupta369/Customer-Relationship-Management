from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    orders = Order.objects.all()

    

    total_orders = orders.count()
    delivered = orders.filter(status = 'Delivered').count()
    pending = orders.filter(status = 'Pending').count()

    customers = Customer.objects.all()

    orders = orders.order_by('-date_created')[:5]

    context ={
        'total_orders' : total_orders,
        'delivered' : delivered,
        'pending' : pending,
        'customers' : customers,
        'orders' : orders
    }
    return render(request, 'accounts/dashboard.html', context)

def customer(request):
    return render(request, 'accounts/customer.html')

def products(request):
    products = Product.objects.all()
    context = {
        'products' : products
    }
    return render(request, 'accounts/products.html', context)
