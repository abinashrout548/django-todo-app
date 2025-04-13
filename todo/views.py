from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def index(request):
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'index.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            # Check for duplicate tasks (case-insensitive)
            if Task.objects.filter(title__iexact=title).exists():
                form.add_error('title', 'A task with this name already exists.')
            else:
                form.save()
                return redirect('index')
    else:
        form = TaskForm()
    
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'index.html', {
        'form': form,
        'tasks': tasks
    })

def complete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = True
    task.save()
    return redirect('index')

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('index')