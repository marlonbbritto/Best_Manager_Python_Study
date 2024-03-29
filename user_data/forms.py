from django import forms
from django.contrib.auth.models import User
from user_data.models import Employeer, Positions,Users_Data
from localflavor.br.forms import BRStateSelect


class UserForms(forms.Form):
    user_name = forms.CharField(
        label = 'User Name',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'type':"text",
                'class':"form-control", 
                'id':"floatingInput",
                'placeholder':"admin.xpto",
            }
        )
    )
    first_name = forms.CharField(
        label = 'Primeiro Nome',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'type':"text",
                'class':"form-control", 
                'id':"floatingInput",
                'placeholder':"João",
            }
        )
    )

    surname = forms.CharField(
        label = 'Sobrenome',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'type':"text",
                'class':"form-control", 
                'id':"floatingInput",
                'placeholder':"Silva Santos",
            }
        )
    )

    email = forms.EmailField(
        label='Email',
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'type':"email",
                'class':"form-control", 
                'id':"floatingInput",
                'placeholder':"xpto@gmail.com",
            }
        )
    )
    password=forms.CharField(
        label='Password', 
        required=True, 
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'type':"password",
                'class':"form-control", 
                'id':"floatingInput",
                'placeholder':"Password",
            }
        ),
    )
    password2=forms.CharField(
        label='Confirm your password', 
        required=True, 
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'type':"password",
                'class':"form-control", 
                'id':"floatingInput",
                'placeholder':"Password",
            }
        ),
    )

class EmployeerForms(forms.ModelForm):
    class Meta:
        model = Employeer
        fields = '__all__'
        labels = {
            'company_name':'Nome da Empresa',
            'admin_user':'Usuario Admin',
            'country': 'País',
            'state': 'Estado',
            'city': 'Cidade'
        }
        widgets = {
            'company_name': forms.TextInput(
                attrs={
                    'type':"text",
                    'class':"form-control", 
                    'id':"floatingInput",
                    'placeholder':"Empresa XPTO",
                }
            ),
            'admin_user': forms.Select(
                attrs={
                    'type':"select",
                    'class':"form-control", 
                    'id':"floatingInput",
                    'placeholder':"xpto_yz",
                }
            ),
            'country': forms.TextInput(
                attrs={
                    'type':"text",
                    'class':"form-control", 
                    'id':"floatingInput",
                    'placeholder':"País",
                }
            ),
            'state': BRStateSelect(
                attrs={
                    'class':"form-control", 
                    'id':"floatingInput",
                    'placeholder':"Estado",
                }
            ),
            'city': forms.TextInput(
                attrs={
                    'type':"text",
                    'class':"form-control", 
                    'id':"floatingInput",
                    'placeholder':"Cidade",
                }
            ),
        }

class PositionForm(forms.ModelForm):
    class Meta:
        model=Positions
        fields ='__all__'
        labels = {
            'company_name':'Nome da Empresa',
            'position':'Cargo',
            'level':'Nivel da Posição'
        }
        widgets = {
            'company_name':forms.Select(
                attrs={
                    'type':"text",
                    'class':"form-control", 
                    'id':"floatingInput",
                    'placeholder':"Empresa XPTO",
                }
            ),
            'position': forms.TextInput(
                attrs={
                    'type':"text",
                    'class':"form-control", 
                    'id':"floatingInput",
                    'placeholder':"Nome do Cargo",
                }
            ),
            'level': forms.NumberInput(
                attrs={
                    'type':"number",
                    'class':"form-control", 
                    'id':"floatingInput",
                    'placeholder':"Nome do Cargo",
                }
            ),
        }

class LoginForms(forms.Form):
    user_name = forms.CharField(
        label = 'User Name',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'type':"text",
                'class':"form-control mb-3", 
                'id':"floatingInput",
                'placeholder':"mokeyDLuffy",
            }
        )
    )
    password=forms.CharField(
        label='Password', 
        required=True, 
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'type':"password", 
                'class':"form-control",
                'id':"floatingPassword", 
                'placeholder':"Password",
            }
        ),
    )

class EmployeeForms(forms.ModelForm):
    class Meta:
        model = Users_Data
        fields = '__all__'
        labels = {
            'user':'Usuario',
            'born_date':'Data de nacimento', 
            'active':'Status',
            'admission_date':'Data de admissão na empresa', 
            'position': 'Cargo' ,
            'employeer':'Empresa' 
        }
        widgets = {        
            'user':forms.Select(
                    attrs={
                        'type':"text",
                        'class':"form-control", 
                        'id':"floatingInput",
                        'placeholder':"joaosilva",
                    }
                ),
            'born_date':forms.DateInput(
                attrs={
                    'type':"date",
                    'class':"form-control", 
                    'id':"floatingInput",
                    'placeholder':"Data de nacimento",
                }
            ),
            'active':forms.CheckboxInput(
                attrs={
                    'type':"checkbox",
                    'class':"form-control", 
                    'id':"floatingInput",
                    'placeholder':"Status do colaborador",
                }
            ),
            'admission_date':forms.DateInput(
                attrs={
                    'type':"date",
                    'class':"form-control", 
                    'id':"floatingInput",
                    'placeholder':"Data de admissão",
                }
            ),
            'position':forms.Select(
                attrs={
                    'type':"text",
                    'class':"form-control", 
                    'id':"floatingInput",
                    'placeholder':"Cargo",
                }
            ),
            'employeer':forms.Select(
                attrs={
                    'type':"text",
                    'class':"form-control", 
                    'id':"floatingInput",
                    'placeholder':"Empresa 1",
                }
            ),

        }
