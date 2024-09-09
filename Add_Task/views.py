from django.shortcuts import render,redirect,get_object_or_404
from .import forms
from .import models
# Create your views here.
def add_task(request):
    if request.method == 'POST':
        task_form = forms.TaskForm(request.POST)
        if task_form.is_valid():
            task_form.save()
            return redirect('add_task')
    
    else:   
        task_form = forms.TaskForm()
    return render(request, 'add_category.html', {'form' : task_form})

def edit_task(request,id):
    task=models.TaskModel.objects.get(pk=id)
    task_form=forms.TaskForm(instance=task)

    if request.method == 'POST':
        task_form = forms.TaskForm(request.POST,instance=task)
        if task_form.is_valid():
            task_form.save()
           
            return redirect('showpage')
    return render(request, 'add_category.html', {'form' : task_form})
def delete_task(request,id):
    task=models.TaskModel.objects.get(pk=id)
    task.delete()
    return redirect('showpage')

def completed_task(request, id):
    task = get_object_or_404(models.TaskModel, id=id)
    task.is_completed = not task.is_completed
    task.save()
    return redirect('showpage')
