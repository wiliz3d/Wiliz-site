from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from . models import Customer
from django import forms
from django.contrib.auth.models import User



class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fidels = '__all__'
        
      
class CreateUserForm(UserCreationForm):
    class Meta:
        model= User
        fields = ['username','email','password1','password2']    
        
        