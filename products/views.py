# from django contrid.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
class TitleMixin:
    pass
#from common.views import  TitleMixin
#from products.models import Basket, ProductCategory

class indexView(TitleMixin,TemplateView):
    template_name = 'products/index.html'
    title = 'Store'


class ProductsListView(TitleMixin,ListView):
    #model = Product
    template_name = 'products/products.html'
    paginate_by = 3
    title = 'Store-Каталог'


