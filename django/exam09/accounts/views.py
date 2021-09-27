from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.views.decorators.http import require_POST, require_http_methods


# Create your views here.
@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.user.is_authenticated:  # 이미 로그인 했으면
        return redirect('reservations:index')  # reservations redirect
    
    if request.method == 'POST':  # POST
        form = UserCreationForm(request.POST)
        if form.is_valid():  # 유효성 검사
            form.save()
            return redirect('accounts:login')  
    else:  # GET
        form = UserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)

@require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated:  # 로그인 했으면
        return redirect('reservations:index')

    if request.method == 'POST':  # POST
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():  # 유효성 검사
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'reservations:index')
    else:  # GET
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)

@require_POST  # 데코레이터
def logout(request):
    auth_logout(request)
    return redirect('accounts:login')