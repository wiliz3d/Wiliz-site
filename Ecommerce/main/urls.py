from django.contrib import admin
from django.urls import path,include
from .views import *
from . import views

app_name = 'main'

urlpatterns = [
    path('',SignUpView.as_view,name='base'),
    path('home/', views.home,name='home'),
   # path('about',views.About,name='about'),
    path('signin/',views.signup,name='signin'),
    path('signup/',views.signin,name='signup'),
    path('wishlist/',views.wishlist,name='wishlist'),
]


