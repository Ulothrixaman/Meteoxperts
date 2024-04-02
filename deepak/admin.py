from django.contrib import admin
from .models import *
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('prod_img', 'category', 'title', 'url')
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('cate_id','title',)
    
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name','email', 'product_url')
    
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Customer, CustomerAdmin)
    
