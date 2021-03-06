from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import UserChangeForm
from .forms import CustomUserChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

# Create your views here.
def signup(request): 
    if request.user.is_authenticated:
        return redirect('articles:index')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = UserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


def login(request): 
    if request.user.is_authenticated:
        return redirect('articles:index')
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST) 
        if form.is_valid(): 
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or'articles:index')
    else: 
        form = AuthenticationForm()
    context= {
        'form' : form,
    }
    return render(request, 'accounts/login.html',context)


def logout(request):
    auth_logout(request)
    return redirect('articles:index')


@login_required 
def update(request):
    if request.method =='POST':
        form = CustomUserChangeForm(request.POST, instance = request.user)
        if form.is_valid:
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance = request.user)
    context ={
        'form' : form,
    }
    return render(request, 'accounts/update.html', context)


def users(request):
    user_list = get_user_model().objects.all()
    context = {
        'user_list': user_list,
    }
    return render(request, 'accounts/users.html', context)