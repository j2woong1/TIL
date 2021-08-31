from django.shortcuts import render
import random
from datetime import datetime

# Create your views here.
def index(request):
    return render(request, 'articles/index.html')

def introduce(request):
    return render(request, 'articles/introduce.html')

def greeting(request):
    foods = ['apple', 'banana', 'coconut',]
    info = {
        'name': 'woong'
    }

    context = {
        'info': info,
        'foods': foods,
    }

    return render(request, 'articles/greeting.html', context)

def dinner(request):
    foods = ['pizza', 'hamburger', '치킨', '초밥']
    pick = random.choice(foods)
    no = ''

    context = {
        'pick': pick,
        'foods': foods,
        'no': no,
    }

    return render(request, 'articles/dinner.html', context)

def image(request):

    return render(request, 'articles/image.html')


def template_language(request):
    menus = ['짜장면', '탕수육', '짬뽕', '양장피']
    my_sentence = 'Life is short, you need python'
    messages = ['apple', 'banana', 'coconut', 'mango']
    datetimenow = datetime.now()
    empty_list = []

    context = {
        'menus': menus,
        'my_sentence': my_sentence,
        'messages': messages,
        'datetimenow': datetimenow,
        'empty_list': empty_list,
    }

    return render(request, 'articles/template_language.html', context)


def throw(request):

    return render(request, 'articles/throw.html')


def catch(request):
    print(request)
    print(request.GET)
    message = request.GET.get('message')
    context = {
        'message': message
    }
    return render(request, 'articles/catch.html', context)


def hello(request, name):
    context = {
        'name': name
    }
    return render(request, 'articles/hello.html', context)