from django.contrib import admin
from foodOmeterApp.models import contact,Profile,Menu,Order,Cart,CartItems
# Register your models here.
admin.site.site_header="Food-O-Meter | Admin"


class ContactAdmin(admin.ModelAdmin):
    list_display=['id','name','email','mob_no','message','added_on','is_approved']
    
    
class MenuAdmin(admin.ModelAdmin):
    list_display=['id','item_name','item_price','item_img']

class CartAdmin(admin.ModelAdmin):
    list_display=['id','user','is_paid']
    
class CartItemAdmin(admin.ModelAdmin):
    list_display=['id','cart','user','product','qauntity','price','t_price']

admin.site.register(contact,ContactAdmin)
admin.site.register(Profile)
admin.site.register(Menu,MenuAdmin)
admin.site.register(Order)
admin.site.register(Cart,CartAdmin)
admin.site.register(CartItems,CartItemAdmin)

