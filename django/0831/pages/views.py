from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

def drink(request):
    return render(request, 'drink.html')