from django.shortcuts import get_object_or_404 , render , redirect
from .models import Task, TODO
from .forms import TaskForm , CategoryForm

def index(request):
    todos = TODO.objects.all()
    tasks = Task.objects.all()
    context = {'todos': todos, 'tasks': tasks}
    return render(request, 'main/cont.html', context)

def tasks_by_todo(request, todo_id):
    todo = get_object_or_404(TODO, id=todo_id)
    tasks = Task.objects.filter(TODO=todo)
    context = {'todo': todo, 'tasks': tasks}
    return render(request, 'main/todo_tasks.html', context)

def detailed_task(request, id):
    task = get_object_or_404(Task, id=id)
    context = {
        'task': task
    }
    return render(request, 'main/detailed.html', context)

def tasks_by_status(request, status):
    tasks = Task.objects.filter(status=status)
    context = {
        'tasks': tasks,
        'status': status
    }
    return render(request, 'main/todosstatus.html', context)

def Createtodo(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid() :
            form.save() #--> save the record in database            
            return redirect('home')
    else:  
        form = TaskForm()
    return render(request , 'main/create_todo.html' ,{'form' :form} )



def createCategory(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid() :
            form.save() #--> save the record in database            
            return redirect('home')
    else:  
        form = CategoryForm()
    return render(request , 'main/createcategory.html' ,{'form':form})



def update_task(request , id ):
    task = get_object_or_404(Task , id=id)
    if request.method == 'POST':
        form = TaskForm(request.POST , instance=task)
        if form.is_valid() :
            form.save() #--> save the record in database            
            return redirect('home')
    else:  
        form = TaskForm(instance=task)
    return render(request, 'main/updatetask.html' , {'form':form})

def delete_task(request , id):
    task = get_object_or_404(Task , id=id)
    task.delete()
    return redirect('home')