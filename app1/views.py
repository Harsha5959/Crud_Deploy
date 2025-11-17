from django.shortcuts import render,redirect

# Create your views here.

from app1.models import employees
from app1.forms import employee_forms

def details(request):
    data = employees.objects.all()
    context = {
        'data' : data
    }
    return render(request,'frontend_app1/home.html',context)

def emp_forms(request):
    form = employee_forms()
    if request.method == 'POST':
        form = employee_forms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = employee_forms()
    context ={
        'form':form
    }
    return render(request,'frontend_app1/new_emp_form.html',context)