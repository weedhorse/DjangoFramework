from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
import datetime
from .models import ProductCategory, Product
from basketapp.models import Basket
import random, os, json


JSON_PATH = 'mainapp/json'


def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r') as infile:
        return json.load(infile)


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []

        
def get_hot_product():
    products = Product.objects.all()
    return random.sample(list(products), 1)[0]
    
    
def get_same_products(hot_product):
    same_products = Product.objects.filter(category=hot_product.category).exclude(pk=hot_product.pk)[:3]
    
    return same_products
        

        
def main(request):
    title = 'главная'  
    products = Product.objects.all()[:3]
    
    content = {
        'title': title,
        'products': products,
        'basket': get_basket(request.user),
    }
    
    return render(request, 'mainapp/index.html', content)
    

def products(request, pk=None, page=1):
    title = 'продукты'
    links_menu = ProductCategory.objects.all()
    basket = get_basket(request.user)

    if pk is not None:
        if pk == 0:
            category = {
                'name': 'все',
                'pk': 0
            }
            products = Product.objects.all().order_by('price')
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')

        paginator = Paginator(products, 2)

        try:
            products_paginator = paginator.page(request.GET.get('page', 1))
        except PageNotAnInteger:
            products_paginator = paginator.page(1)
        except EmptyPage:
            products_paginator = paginator.page(paginator.num_pages)
        content = {
            'title': title,
            'links_menu': links_menu,
            'category': category,
            'products': products_paginator,
            'basket': basket,
            'pages': range(1, paginator.num_pages)
        }
        
        return render(request, 'mainapp/products_list.html', content)
    
    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)
    
    content = {
        'title': title,
        'links_menu': links_menu, 
        'hot_product': hot_product,
        'same_products': same_products,
        'basket': basket,
    }
    
    return render(request, 'mainapp/products.html', content)
    
    
def product(request, pk):
    title = 'продукты'
    links_menu = ProductCategory.objects.all()

    product = get_object_or_404(Product, pk=pk)
    
    content = {
        'title': title, 
        'links_menu': links_menu, 
        'product': product, 
        'basket': get_basket(request.user),
    }
    return render(request, 'mainapp/product.html', content)
    

def contact(request):
    title = 'о нас'
    visit_date = datetime.datetime.now()
    
    locations = load_from_json('contact__locations')
    
    content = {
        'title': title,
        'visit_date':visit_date, 
        'locations': locations,
        'basket': get_basket(request.user),
    }
    
    return render(request, 'mainapp/contact.html', content)
    
    
