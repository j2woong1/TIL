from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def index(request):
    # todos = Todo.objects.all()
    # 이 코드의 문제 woong, student의 todo를 서로 볼 수 있음

    # 본인이 작성한 todo만 보이도록 설정
    todos = request.user.todo_set.all()

    context = {
        'todos': todos,
    }
    return render(request, 'todos/index.html', context)

@login_required
def new(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.author = request.user
            todo.save()
            return redirect('todos:index')
    else:
        form = TodoForm()
    context = {
        'form': form
    }
    return render(request, 'todos/new.html', context)
