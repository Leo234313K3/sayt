# from django contrid.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect, render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

#from common.views import  TitleMixin
#from products.models import Basket, ProductCategory
#
# class indexView(TitleMixin,TemplateView):
#     template_name = 'products/index.html'
#     title = 'Store'
#
#
# class ProductsListView(TitleMixin,ListView):
#     #model = Product
#     template_name = 'products/products.html'
#     paginate_by = 3
#     title = 'Store-Каталог'


def index(request):
    context = {
        'title': 'Игровые воспоминания'
    }
    return render(request,'products/index.html',context)

def products(request):
    context = {
        'title': 'Каталог',
        'products' : [
        {
            'image':'static/vendor/img/products/Adidas-hoodie.png',
            'name': 'Игра HORIZON(ps5,ps4)',
            'price':4250,
            'description':"Игра для ps5 и ps4 Жанр игры - приключения, захватывающие сражения ! ",

        },
        {
            'image':'static/vendor/img/products/Adidas-hoodie.png',
            'name': 'Игра для ps4 SONIC FORCES',
            'price':1000,
            'description':" Игра с сюжетом ПРИКЛЮЧЕНИЯ !",
        },
        {
            'image':'static/vendor/img/products/Adidas-hoodie.png',
            'name': 'Игра для PS4 UFC',
            'price':3496,
            'description':" Сюжет игры: захватывающие сражения битвы и драки ",

        },
        {
            'image':'static/vendor/img/products/Adidas-hoodie.png',
            'name': 'Игра SPIDER-MAN (ps5)',
            'price':2649,
            'description':" Игра для консоли ps5. Жанр игры - приключения и немного боевика ",
        },
        {
            'image':'static/vendor/img/products/Adidas-hoodie.png',
            'name': 'Игра Второй сын (ps4)',
            'price':1250,
            'description':"Игра для консоли ps4. Жанр игры - приключения ",

        },
        {
            'image':'static/vendor/img/products/Adidas-hoodie.png',
            'name': 'Игра для PS4 FORTNITE',
            'price':1230,
            'description':"Отличная игра с хорошим сюжетом ! Сюжет игры заключается в том что нужно бегать по карте и убивать врагов ",
        }

    ]
    }
    return render(request,'products/index.html',context)