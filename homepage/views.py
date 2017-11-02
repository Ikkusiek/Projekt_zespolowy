from django.shortcuts import render
from product.models import Product


def index(request):
    products = Product.objects.filter(visible=True)
    return render(request, 'index.html', context={'products': products})
