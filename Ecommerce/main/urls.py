from django.contrib import admin
from django.urls import path,include
from . views import *

app_name = 'main'

urlpatterns = [
    path('', Home,name='home'),
]



