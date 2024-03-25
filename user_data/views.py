from django.shortcuts import get_object_or_404, redirect, render

from user_data.forms import EmployeerForms, LoginForms, PositionForm, UserForms,EmployeeForms
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.db.models import ObjectDoesNotExist

from user_data.models import Employeer,Positions,Users_Data
from django.urls import reverse
from django.forms.utils import ErrorList


def index(request):
    user=request.user
    show_button = False
    if user.is_authenticated:
        user_obj = get_object_or_404(User, username=user.username)        
        if Employeer.objects.filter(admin_user=user_obj).exists():
            show_button=True         
    return render(request,'index.html',{'show_button':show_button})

def login(request):
    form = LoginForms
    if request.method =='POST':
        form = LoginForms(request.POST)
        if form.is_valid():
            name = form['user_name'].value()
            password = form['password'].value()
        user = auth.authenticate(
            request,
            username= name,
            password = password
        ) 
        if user is not None:
            auth.login(request,user)
            messages.success(request,f'{name} logado com sucesso')
            return redirect('index')
        else:
            messages.error(request,'Erro ao efetuar login')
            return redirect('login')
    return render(request,'login.html',{'form':form}) 

def logout(request):
    auth.logout(request)
    messages.success(request,"Logout efetuado")
    return redirect('index')

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
    form = EmployeerForms()
    if request.method == 'POST':
        form = EmployeerForms(request.POST)
        if form.is_valid():                   
            messages.success(request, 'Empresa cadastrada com sucesso')
            form.save()
            return redirect('login')  
        else:
            errors = form.errors.as_data()
            error_message = "O formulário contém os seguintes erros: "
            for field, error_list in errors.items():
                error_message += f"{field}: {error_list}"
            messages.error(request, error_message)
            return redirect('index')  
    return render(request, 'company_register.html', {'form': form})



    

def register_employee_user(request):
    form_user = UserForms()   

    if request.method == 'POST':
        form_user = UserForms(request.POST)
        

        if form_user.is_valid():
            print("Formulários são válidos")

            username = form_user.cleaned_data['user_name']

            if User.objects.filter(username=username).exists():
                messages.error(request, 'Este nome de usuário já está sendo utilizado')
                return redirect('employee_register_user')

            if form_user.cleaned_data['password'] != form_user.cleaned_data['password2']:
                messages.error(request, 'As senhas devem ser idênticas')
                return redirect('employee_register_user')

            # Criar usuário
            user = User.objects.create_user(
                username=username,
                password=form_user.cleaned_data['password'],
                email=form_user.cleaned_data['email'],
                first_name=form_user.cleaned_data['first_name'],
                last_name=form_user.cleaned_data['surname']
            )
            print("Usuário criado:", user)

            user.save()          
            messages.success(request, 'Usuário e funcionário cadastrados com sucesso')
            return redirect('employee_register_data')
            

    return render(request, 'employee_register_user.html', {'form_user': form_user})

def register_employee_data(request):
    form=EmployeeForms

    if request.method == 'POST':
        form=EmployeeForms(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request,'Dados do colaborador cadastrado com sucesso')
            return redirect('index')
    return render(request,'employee_register_data.html',{'form':form})


def register_position(request):
    if not request.user.is_authenticated:
        return redirect('login')  # Redirecionar para a página de login se o usuário não estiver autenticado
    
    form = PositionForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            employeer = Employeer.objects.filter(admin_user=request.user).first()
            if employeer is None or employeer.id != form.cleaned_data['company_name'].id:
                messages.error(request, 'Você não tem permissão para cadastrar um Cargo nesta Empresa')
            else:
                position = form.save(commit=False)
                position.company_name = employeer
                position.save()
                messages.success(request, "Cargo cadastrado com sucesso")
                return redirect('register_position')  # Redirecionar para a página inicial após o salvamento
        else:
            # Exibir erros do formulário na página
            errors = form.errors.as_data()
            for field, error in errors.items():
                messages.error(request, f"Erro no campo '{field}': {error[0]}")
    user_company = Employeer.objects.filter(admin_user=request.user).first()    
    company_positions = Positions.objects.filter(company_name=user_company)
    return render(request, 'position_register.html', {'form': form,'company_positions':company_positions})

def list_employees(request):
    if not request.user.is_authenticated:
        return redirect('login')  # Redirecionar para a página de login se o usuário não estiver autenticado
    
    user = request.user
    try:
        users_data = Users_Data.objects.get(user=user)
        company = users_data.employeer
    except ObjectDoesNotExist:
        try:
            users_data = Employeer.objects.get(admin_user=user)
            company = users_data.id
        except Employeer.DoesNotExist:
            messages.error(request, 'Nenhum dado de usuário ou empresa encontrado para este usuário.')
            return redirect('index')

    employees = Users_Data.objects.filter(employeer=company)
    
    return render(request, 'list_employees.html', {'employees': employees})

