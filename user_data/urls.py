from django.contrib import admin
from django.urls import path, include

from user_data.views import index, login, register_admin,register_company, register_position

urlpatterns = [
    path('', index, name='index'),
    path('register_first_admin',register_admin, name='register_first_admin'),
    path('company_register',register_company,name='company_register'),
    path('register_position',register_position,name='register_position'),
    path('login', login,name='login')
]