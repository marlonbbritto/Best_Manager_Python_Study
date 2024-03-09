from django.contrib import admin
from django.urls import path, include

from user_data.views import index, register_admin,register_company

urlpatterns = [
    path('', index, name='index'),
    path('register_first_admin',register_admin, name='register_first_admin'),
    path('company_register',register_company,name='company_register')
]