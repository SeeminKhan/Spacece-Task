from django.shortcuts import render, redirect
from .models import Task

def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Task.objects.create(title=title)
            return redirect('view_tasks')
    return render(request, 'add_task.html')

def view_tasks(request):
    tasks = Task.objects.all()
    return render(request, 'view_tasks.html', {'tasks': tasks})

