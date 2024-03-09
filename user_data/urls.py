from django.contrib import admin
from django.urls import path, include

from user_data.views import index

urlpatterns = [
    path('', index, name='index'),
]