# 장고가 만든거
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# 우리가 만든거
from .forms import CustomUserCreationForm 


# Create your views here.
def signup(request):
    if request.method == "POST": # 사용자가 값을 입력했을 때,
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else: # Get일 때 => url에 접속했을 때
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user() # form에서 어떤 유저인지 가져오기
            auth_login(request, user)
            return redirect('todos:index')
    else:
        form = AuthenticationForm()
    
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


def logout(request):
    auth_logout(request)
    return redirect('todos:index')