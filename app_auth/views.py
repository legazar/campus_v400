from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import *

# Create your views here.
def login_blog(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('accueil')  
            else:
                messages.error(request,'Echec de l\'authentification')
                return render(request,'login.html',{'form':form})
        else:
            for field in form.errors:
                form[field].field.widget.attrs['class'] += 'is-valid'
            return render(request,"login.html",{"form":form})
    else:
        form = LoginForm()
        return render(request,'login.html',{'form':form})

def register_blog(request):
    if request.method == "POST":
        form = RegsiterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            for user in User.objects.all():
                if form.cleaned_data.get('username')==user.username or request.POST['username'].lower() in ['thibaut', 'gazari']:
                    messages.error(request,"Nom d'utilisateur déjà pris")
                    bad_username=True
                    break
            if 'bad_username' in locals():
                return render(request,'register.html',{'form':form})
            user = User.objects.create_user(username=username,email=email,password=password)
            if user is not None:
                return redirect('login_blog')
            else:
                messages.error(request,'Echec de la creation de compte')
                return render (request,'register.html',{'form':form})
        else:
            return render(request,'register.html',{'form':form})
        
    form = RegsiterForm()
    return render(request,'register.html',{'form':form})

def logout_blog(request):
    logout(request)
    return redirect('accueil')