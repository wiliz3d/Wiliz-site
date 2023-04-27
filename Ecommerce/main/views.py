from django.shortcuts import * 
from . models import *
import requests
from django.conf import settings
import xml.etree.ElementTree as ET
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import UserCreationForm


def Home(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, ('home.html'),context)

def Signin(request):
    context = { }
    return render(request, 'accounts/signin.html',context)


def Signup(request):
    form = UserCreationForm()
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()    
    context = {
        "form":form
    }
    
    return render(request, 'accounts/signup.html',context)

def About(request):
    return render(request, ('About.html'),{})