from django.shortcuts import render,redirect
from Add_Task.models import TaskModel
def show(request):
    data=TaskModel.objects.all()
    return render(request,'show.html',{'data': data})
