from django.shortcuts import render
from . import forms
from firstapp.models import Employee


def  home(request):
    return render (request,'firstapp/home.html')

def login(request):
    form=forms.Employeeform()
    if request.method=='POST':
        form=forms.Employeeform(request.POST)
        if form.is_valid():
            form.save()
    return render (request,'firstapp/login.html',{'form':form})

def  show(request):
    list_emp=Employee.objects.all()
    return render (request,'firstapp/show.html',{'list_emp':list_emp})
