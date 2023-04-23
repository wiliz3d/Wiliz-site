from django.shortcuts import * 
from . models import *
import requests
from django.conf import settings
import xml.etree.ElementTree as ET
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

#/////////////////////////////////////////////////////////////////
#///                                                           //
#//  available at https://github.com/wiliz3d/       //
#//                          
#//                                                             //
#//                                                             //
#//                                                             //
#//                                                            ///
#/////////////////////////////////////////////////////////////////

# Create your views here.


def Home(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, ('home.html'),context)

def About(request):
    return render(request, ('About.html'),{})


def Signin(request):
    return render(request, 'signin.html', {})


def Signup(request):
    pass