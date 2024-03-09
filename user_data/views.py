from django.shortcuts import redirect, render

from user_data.forms import UserForms,EmployeerForms
from django.contrib.auth.models import User
from django.contrib import messages, auth

from user_data.models import Employeer

def index(request):
    return render(request,'index.html')

def login(request):
    pass

def logout(request):
    pass

def register_admin(request):
    form=UserForms    
    if request.method == 'POST':
        form = UserForms(request.POST)        
        if form.is_valid():
            name = form['user_name'].value()

            if User.objects.filter(username=name).exists():
                messages.error(request,'Esse nome de usuario ja esta sendo utilizado')
                return redirect('register_first_admin')
            if form['password'].value() != form['password2'].value():
                messages.error(request,'As senhas devem ser identicas')
                return redirect('register_first_admin')
            
            user = User.objects.create_user(
                username=form['user_name'].value(),
                password=form['password'].value(),
                email=form['email'].value(),
                first_name=form['first_name'].value(),
                last_name=form['surname'].value()
            )
            user.save()            
            messages.success(request,'Admin cadastrado com sucesso')
            return redirect('company_register')
    return render(request,'register_admin.html',{'form':form})

def register_company(request):
    form = EmployeerForms
    if request.method == 'POST':
        form = EmployeerForms(request.POST)
        if form.is_valid():
            if Employeer.objects.filter(company_name=form['company_name']).exists():
                messages.error(request,'Uma empresa com esse nome ja esta cadastrada')
                return redirect('company_register')
            messages.success(request,'Empresa cadastrada com sucesso')
            form.save()
            return redirect('index')    
    return render(request,'company_register.html',{'form':form})
    

def register_employee(request):
    pass

def register_position(request):
    pass

def list_employees(request):
    pass

