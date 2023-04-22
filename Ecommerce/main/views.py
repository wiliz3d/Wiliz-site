from django.shortcuts import * 
from . models import *
import requests
import json
#/////////////////////////////////////////////////////////////////
#/// getID3() by James Heinrich <info@getid3.org>               //
#//  available at https://github.com/wiliz3d/       //
#//                          
#//                                                             //
#// getid3.lib.php - part of getID3()                           //
#//  see readme.txt for more details                            //
#//                                                            ///
#/////////////////////////////////////////////////////////////////

# Create your views here.


def Home(request):
    return render(request, ('home.html'))

