from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)  # Get the task or 404 if not found
    task.delete()  # Delete the task from the database
    return redirect('view_tasks')  # Redirect to the task list page after deletion


def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        Task.objects.create(title=title, description=description)
        return redirect('view_tasks')  # Redirect to the task list page
    return render(request, 'add_task.html')


def view_tasks(request):
    tasks = Task.objects.all()
    return render(request, 'view_tasks.html', {'tasks': tasks})

