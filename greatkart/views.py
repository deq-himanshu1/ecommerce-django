from django.shortcuts import render
from store.models import Product

# created views.py file manually here in project level app
def home(request):
    products = Product.objects.all().filter(is_available=True) # this will only show those product which are available

    context = {
        'products' : products,
    }
    return render(request,'home.html',context) # we are making contenxt dictionary so that it can be available in home.html