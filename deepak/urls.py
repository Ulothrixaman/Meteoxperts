
from django.urls import path
from .views import *


handler404 = f404

urlpatterns = [
    path('', home, name="home"),
    path('contact/', contact, name="contact"),
    path('about/', aboutus, name="about"),
    path('qhse/', qhse, name="qhse"),
    path('agro/', agro, name="agro"),
    path('qhsem/', qhsem, name="qhsem"),
    path('solar/', solar, name="solar"),
    path('wind/', wind, name="wind"),
    path('hydro/', hydro, name="hydro"),
    path('weather/', weather, name="weather"),
    path('electric/', electric, name="electric"),
    path('high/', high, name="high"),
    path('air/', air, name="air"),
    path('micro/', micro, name="micro"),
    path('land/', land, name="land"),
    path('alert/', alert, name="alert"),
    path('snow/', snow, name="snow"),
    path('sevices/', sevices, name="services"),
    path('safety/', safety, name="safety"),
    path('certificate/', certificate, name="certificate"),
    path('blog/', blog, name="blog"),
    path('category/', categorys, name="category"),
    path('customer/<str:pk>/', customer, name="customer"),
    path('products/<str:pk>/', product, name="product"),
    path('product/<str:pk>/', single_product, name='single_product')
]