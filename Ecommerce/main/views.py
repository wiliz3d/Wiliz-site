from django.contrib.auth import( authenticate, login )
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import *


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'signup.html'

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)


def signin(request):
    error = ''
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error = 'Invalid username or password.'
    return render(request, 'signin.html', {'error': error})


@login_required
def wishlist(request):
    wishlist = Wishlist.objects.get_or_create(user=request.user)[0]
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        if product_id:
            product = Product.objects.get(id=product_id)
            wishlist.products.add(product)
            return redirect('wishlist')
    products = wishlist.products.all()
    return render(request, 'wishlist.html', {'products': products})


def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})


