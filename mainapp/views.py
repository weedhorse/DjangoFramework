from django.shortcuts import render
from mainapp.models import Product, ProductCategory


def index(request):
    context = {
        "title": "Магазин от Django",
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    context = {
        'products': Product.objects.all(),
    }
    return render(request, 'mainapp/products.html', context=context)

def test_context(request):
    context = {
        'title': 'Hello dude',
        'username': 'Pavel',
        'products': [
            {'name': 'Black shirt', 'price': '2300$'},
            {'name': 'White jeans', 'price': '4100$'},
        ],
        'promotion_products': [
        ],
    }

    return render(request, 'mainapp/context.html', context)