
from django.urls import path
from .views import *


handler404 = f404

urlpatterns = [
    path('', home, name="home"),
    path('category/', category, name="category"),
    path('customer/<str:pk>/', customer, name="customer"),
    path('products/<str:pk>/', product, name="product"),
    path('product/<str:pk>/', single_product, name='single_product')
]