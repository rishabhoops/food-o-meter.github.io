from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=254)
    mob_no=models.CharField(max_length=10)
    message=models.TextField()
    added_on=models.DateTimeField(auto_now_add=True)
    is_approved=models.BooleanField(default=True)


    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Contact Table"
        
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    profile_pic = models.ImageField(upload_to='profiles/%Y/%m/%d', null=True, blank=True)
    forget_password_token=models.CharField(max_length=50,null=True, blank=True)
    contact=models.IntegerField(null=True)
    address=models.TextField(blank=True)
    updated_on=models.DateTimeField(auto_now=True)
    
    def cart_count(self):
        cart = Cart.objects.get(user=self.user, is_paid=False)
        return CartItems.objects.filter(cart=cart).count()   
    
    def __str__(self):
        return self.user.first_name
    
    class Meta:
        verbose_name_plural = "Profile Table"
        
class Menu(models.Model):
    item_name=models.CharField(max_length=50)
    item_price=models.CharField(max_length=50)
    item_img=models.ImageField(upload_to='item_image')
    
    class Meta:
        verbose_name_plural = "Menu Table"
        


class Cart(models.Model):
    user=models.ForeignKey(Profile, on_delete=models.CASCADE,related_name='carts')
    is_paid=models.BooleanField(default=False)
    
    
class CartItems(models.Model):
    user=models.ForeignKey(Profile, on_delete=models.CASCADE)
    cart=models.ForeignKey(Cart, on_delete=models.CASCADE,related_name='cart_items')
    product=models.ForeignKey(Menu, on_delete=models.CASCADE)
    qauntity=models.IntegerField(default=0)
    price=models.IntegerField()
    t_price=models.IntegerField(null=True,blank=True)
    
    
    
class Order(models.Model):
    customer = models.ForeignKey(Profile, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    item=models.CharField(CartItems, max_length=50,null=True,blank=True)
    invoice_id = models.CharField(max_length=100, blank=True)
    payer_id = models.CharField(max_length=100, blank=True)
    instamojo_response=models.TextField(null=True,blank=True)
    ordered_on = models.DateTimeField(auto_now_add=True)

    
    def get_cart_count(self):
        c=CartItems.objects.filter(ChartItems__user=self.customer).count()
        return c
    
    def __str__(self):
        return self.customer.user.first_name

    class Meta:
        verbose_name_plural = "Order Table"
    
    