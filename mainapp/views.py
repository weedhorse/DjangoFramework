from django.shortcuts import render


def index(request):
    context = {
        "title": "Магазин от Django",
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    context = {
        'title': 'ТОВАРЫ',
    }
    return render(request, 'mainapp/products.html', context)

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