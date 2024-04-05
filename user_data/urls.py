from django.contrib import admin
from django.urls import path, include

from user_data.views import index, employee_information, list_employees, login, logout, register_admin,register_company, register_employee_data, register_employee_user, register_position

urlpatterns = [
    path('', index, name='index'),
    path('register_first_admin',register_admin, name='register_first_admin'),
    path('company_register',register_company,name='company_register'),
    path('register_position',register_position,name='register_position'),
    path('login', login,name='login'),
    path('logout',logout,name='logout'),
    path('employee_register_user',register_employee_user,name='employee_register_user'),
    path('employee_register_data',register_employee_data,name='employee_register_data'),
    path('list_employees',list_employees,name='list_employees'),
    path('list_employee_information/<int:user_id>/',employee_information,name='list_employee_information')

]