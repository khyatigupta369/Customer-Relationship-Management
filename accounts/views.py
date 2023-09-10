from django.shortcuts import render, redirect
from .models import *
from .forms import OrderForm
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


def createOrder(request):

    form = OrderForm()
    # action = "" means send the data in the form through post method to the same url
    if(request.method == 'POST'):
        # print('Printing the Form data: ' + request.POST)
        # if the received data matched the model form type, and the form is valid, then save it to database
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'form' : form
    }
    return render(request, 'accounts/order_form.html', context)

def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)

    if(request.method == 'POST'):
        # by passing instance, it edits the database rather than creating a new entry
        form = OrderForm(request.POST, instance = order)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'form' : form
    }

    return render(request, 'accounts/order_form.html', context)

def deleteOrder(request, pk):
    order = Order.objects.get(id = pk)
    if(request.method == 'POST'):
        order.delete()
        return redirect('/')

    context = {'item' : order}
    return render(request, 'accounts/delete.html', context)