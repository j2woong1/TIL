from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_safe, require_POST, require_http_methods
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm

from .forms import CustomUserCreationForm

User = get_user_model()


@require_http_methods(['GET', 'POST'])
def signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                auth_login(request, user)
                return redirect('community:review_index')
        else:
            form = CustomUserCreationForm()

        context = {'form': form, }
        return render(request, 'accounts/signup.html', context=context)
    else:
        return redirect('community:review_index')


@require_http_methods(['GET', 'POST'])
def login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request, request.POST)
            if form.is_valid():
                user = form.get_user()
                auth_login(request, user)
                return redirect(request.GET.get('next') or 'community:review_index')
        else:
            form = AuthenticationForm()
        
        context = {'form': form, }
        return render(request, 'accounts/login.html', context=context)
    else:
        return redirect(request, 'community:review_index')


def logout(request):
    auth_logout(request)
    return redirect('community:review_index')


@require_safe
def profile(request, username):
    profile = get_object_or_404(User, username=username)
    is_following = profile.fans.filter(pk=request.user.pk).exists()
    context = {
        'profile': profile, 
        'is_following': is_following,
    }
    return render(request, 'accounts/profile.html', context)



@require_POST
def follow(request, username):
    fan = request.user
    star = get_object_or_404(User, username=username)
    if fan.stars.filter(pk=star.pk).exists():
        fan.stars.remove(star)
    else:
        fan.stars.add(star)
    return redirect('accounts:profile', star.username)