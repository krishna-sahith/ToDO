from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def add_task(request):
    form = TaskForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('task_list')  # Redirect to the task list after adding a task

    context = {'form': form}
    return render(request, 'tasks/add_task.html', context)

def task_list(request):
    tasks = Task.objects.filter(completed=False)  # Exclude completed tasks
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def completed_tasks(request):
    completed_tasks = Task.objects.filter(completed=True)
    return render(request, 'tasks/completed_tasks.html', {'completed_tasks': completed_tasks})

def mark_completed(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = not task.completed  # Toggle completion status
    task.save()
    return redirect('task_list')

def completed_tasks(request):
    completed_tasks = Task.objects.filter(completed=True)
    return render(request, 'tasks/completed_tasks.html', {'completed_tasks': completed_tasks})

def mark_completed(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('task_list')  # Redirect back to the updated task list

def delete_completed_tasks(request):
    if request.method == 'POST':
        completed_task_ids = request.POST.getlist('completed_tasks')
        Task.objects.filter(id__in=completed_task_ids).delete()
    return redirect('completed_tasks')


