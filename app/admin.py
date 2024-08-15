from django.contrib import admin
from .models import Product,Customer,cart
# Register your models here.
@admin.register(Product)
class modelproduct(admin.ModelAdmin):
    list_display=['id','title','discount_price','category','product_image']

@admin.register(Customer)
class customermodeladmin(admin.ModelAdmin):
    list_display=['id','user','locality','city','state','zipcode']



@admin.register(cart)
class cartmodeladmin(admin.ModelAdmin):
    list_display=['id','user','product','quantity']