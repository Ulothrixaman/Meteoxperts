from django.db import models
from django.utils.html import format_html
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    cate_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to='category/', null=True)
    description = models.TextField(null=True)
    
    def __str__(self):
        return self.title
    
class Customer(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    product_url = models.CharField(max_length=20, null=True)


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', null=True)
    pro_id = models.AutoField(primary_key=True)
    pro_img = models.ImageField(upload_to='products/')
    title = models.CharField(max_length=100)
    dis_price = models.CharField(max_length=20)
    price = models.CharField(max_length=20)
    model_name = models.CharField(max_length=20)
    make = models.CharField(max_length=20)
    datasheet = models.FileField(upload_to='datasheets/')
    manual = models.FileField(upload_to='manuals/')
    url = models.CharField(max_length=50)
    add_date = models.DateTimeField(auto_now_add=True, null=False)
    specification = models.TextField(null=True)
    description = models.TextField()
    about = models.TextField()

    def prod_img(self):
        return format_html(
            '<img src="/media/{}" style="height: 50px; width: 50px"/>'.format(self.pro_img)
        )

    def __str__(self):
        return str(self.title)

    def str(self):
        return str(self.description)


