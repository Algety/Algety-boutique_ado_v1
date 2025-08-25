from .models import Product
from django.shortcuts import render

# Create your views here.

def all_products(request):
    """ A view to show all products, with search and sorting """

    products = Product.objects.all()
    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)