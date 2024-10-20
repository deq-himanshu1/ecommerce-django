from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category

# Create your views here.

def store(request, category_slug=None):
    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True) # this if condition is filtering products by categories
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True) # this will only show those product which are available
        product_count = products.count()

    context = {
        'products' : products,
        'product_count' : product_count,
    }
    return render(request, 'store/store.html',context)
    # by doing this these products will be availabe in our store.html in templates


def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
        # here two times __ is taken in category__slug , two time means it will bring category slug from category app model and matching with category slug that we are getting from urls
    except Exception as e:
        raise e
    
    context = {
        'single_product' : single_product,
    }
    return render(request, 'store/product_detail.html', context) # now we are having single product inside product.html