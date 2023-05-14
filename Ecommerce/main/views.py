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
    success_url = reverse_lazy('main:home')
    template_name = '/Ecommerce/template/accounts/signup.html'
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return render(request, 'home.html')
        return super().dispatch(request, *args, **kwargs)


def signin(request):
    error = ''
    if request.user.is_authenticated:
        return render(request, 'home.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'home.html')
        else:
            error = 'Invalid username or password.'
            
    ctx = {'error': error}
    return render(request, 'signin.html', ctx)


@login_required
def wishlist(request):
    wishlist = Wishlist.objects.get_or_create(user=request.user)[0]
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        if product_id:
            product = Product.objects.get(id=product_id)
            wishlist.products.add(product)
            return render(request, 'home.html')
    products = wishlist.products.all()
    return render(request, 'wishlist.html', {'products': products})


def home(request):
    products = Product.objects.all()
    context =  {'products': products}
    return render(request, 'home.html',context)



def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
