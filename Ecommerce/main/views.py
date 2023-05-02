from django.shortcuts import * 
from . models import *
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import(
                    SignupForm,
                    SignInForm
                  )
from django.contrib.auth import(
                                authenticate,
                                login
                                )


def Home(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, ('home.html'),context)


def Signup(request):
    if request.method =='POST':
        user_form = SignupForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return render(request,('home.html'),context)
        else:
            user_form = SignupForm()
        return HttpResponse('<h1>Error 404</h1>')
    context = {'user_form':user_form}
    return render(request, 'accounts/signup.html',context)



def Signin(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user=authenticate(request,
                              username=cd["username"],
                              password=cd['password']
                              )
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return HttpResponse("<h1>Wlcome</h2>")
                else:
                    return HttpResponse("<h1>DIssable<h1/>")
            else:
                return HttpResponse("<h1>INVALID<h1/>")
    else:
        form = SignInForm()            
    return render(request, 'accounts/signin.html',{"form"})



def About(request):
    return render(request, ('About.html'),{})

