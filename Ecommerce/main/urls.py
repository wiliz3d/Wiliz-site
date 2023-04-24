from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.Home,name='home'),
    path('about',views.About,name='abt'),
    path('signin/',views.Signin,name='signin'),
    path('signup/',views.Signup,name='signup'),
]



