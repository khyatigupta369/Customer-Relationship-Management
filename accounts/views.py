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

# primary key - pk same as that in the dynamic accounts/urls.py route
def customer(request, pk):
    customer = Customer.objects.get(id = pk)
    orders = customer.order_set.all()
    total_orders = orders.count()
    context = { 
        'customer' : customer,
        'total_orders' : total_orders,
        'orders' : orders
    }

    return render(request, 'accounts/customer.html', context)

def products(request):
    products = Product.objects.all()
    context = {
        'products' : products
    }
    return render(request, 'accounts/products.html', context)
