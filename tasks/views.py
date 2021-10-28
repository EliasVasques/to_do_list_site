from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Task

# Create your views here.

def tasks(request):
    all_tasks = Task.objects.all()
    search = request.GET.get('search')
    if search:  # SE FOI PESQUISADO ALGO
        filter_tasks = []
        for task in all_tasks:
            if search.lower() in task.title.lower():
                filter_tasks.append(task)
    else:
        filter_tasks = all_tasks
        search = ''
    return render(request, 'tasks.html', {'tasks': filter_tasks, 'search': search})

def task(request, id):
    task = get_object_or_404(Task, pk=id)
    return render(request, 'task.html', {'task': task})

def delete_task(request, id):
    task = get_object_or_404(Task, pk=id)
    messages.info(request, 'tarefa deletada com sucesso')
    Task.delete(task)
    return redirect('/')

def new_task(request):

    if request.method == 'POST': # (SALVAR)
        title = request.POST.get('title')
        description = request.POST.get('description')
        task = Task()
        task.title = title
        task.description = description 
        task.save()
        messages.info(request, 'tarefa criada com sucesso')
        return redirect('/')
    else: # (RENDER PARA PODER CRIAR)
        return render(request, 'add_task.html')

def edit_task(request, id):

    task = get_object_or_404(Task, pk=id)

    if request.method == 'POST': #(SALVAR MUDANÇAS)
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.situation = request.POST.get('situation')
        task.save()
        messages.info(request, 'tarefa editada com sucesso!')
        return redirect('/')
    else: # (CARREGAR PÁGINA)
        return render(request, 'edit_task.html', {'task': task})
