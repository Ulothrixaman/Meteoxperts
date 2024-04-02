from django.shortcuts import render, redirect,get_object_or_404
from deepak.models import *

# Create your views here.

def home(request):
    return render(request, 'home.html', {})


def category(request):
    category = Category.objects.all()
    data = {
        'categorys': category
    }
    return render(request, 'category.html', data)

def product(request, pk):
    category = Category.objects.get(cate_id=pk)
    tag = category.title
    print(tag)
    product = Product.objects.filter(category=category)
    data = {
        'tag': tag,
        'products': product
    }
    
    request.session['cate_id'] = pk
    
    return render(request, 'products.html', data)

def single_product(request, pk):
    product = get_object_or_404(Product, pro_id=pk) 
    product.price = int(product.price)
    product.dis_price = int(product.dis_price)
    data = {
        'product': product
    } 
    return render(request, 'product.html', data) 

def customer(request, pk):
    cate_id = request.session.get('cate_id')
    product = Product.objects.get(pro_id=pk)
    pro_id = product.pro_id
    pro_url = f'http://127.0.0.1:8000/product/{pro_id}/'
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        data = Customer(name=name, email=email, product_url=pro_url)
        data.save()
    if cate_id:
        return redirect('product', pk = cate_id)
    else:
        return redirect('home')

        
def f404(request, exception):
    return render(request, '404.html', {})