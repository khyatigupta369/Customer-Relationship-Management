from django.forms import ModelForm 
from .models import Order


# names of classes starts with capital letters
class OrderForm(ModelForm):
    class Meta:
        model = Order
        # here, we could specify in a list ['customer', 'products'] the fields we want the form for
        fields = '__all__'