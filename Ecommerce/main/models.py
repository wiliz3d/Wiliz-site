from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class User(models.Model):
    first_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=10)
    
    def __str__(self):
        return self.email

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wishlists')
    products = models.ManyToManyField(Product, related_name='wishlists')

    def __str__(self):
        return f"{self.user}'s Wishlist"

    
class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL,blank=True,null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)  
    transaction_id = models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return str(self.id)
    
    
class OrderItem(models.Model):
    product = models.ForeignKey(User, on_delete=models.SET_NULL,blank=True,null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL,blank=True,null=True)
    complete = models.IntegerField(default=0, null=True, blank=True)  
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.product.name
        
            
class ShippingAddress(models.Model):
    customer = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,null=True)
    address = models.CharField(max_length=200,null=False)
    city = models.CharField(max_length=200,null=False)
    state = models.CharField(max_length=200,null=False)
    zipcode = models.CharField(max_length=200,null=False)
    date_added = models.DateTimeField(auto_now_add=True)
    
   
