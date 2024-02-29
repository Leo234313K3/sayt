
from django.contrib import admin
from django.contrib.sitemaps.views import index
from django.urls import path

import products

urlpatterns = [
    path("admin/",admin.site.urls),
    path("",index, name='index'),
    path('products/',products, name='products')

]