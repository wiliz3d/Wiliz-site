from django.shortcuts import * 
from . models import *
import requests
import json
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

