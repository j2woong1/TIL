from django.shortcuts import render

# Create your views here.
def dinner(request, menu, people):
    context = {
        'menu': menu,
        'people': people
    }
    return render(request, 'pages/dinner.html', context)