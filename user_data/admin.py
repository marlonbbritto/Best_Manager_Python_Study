from django.contrib import admin
from user_data.models import Employeer,Positions,Users_Data

class ListEmployeer(admin.ModelAdmin):
    list_display = ('id',
                    'company_name',
                    'admin_user',
                    'country',
                    'state',
                    'city'                    
                    )
    list_display_links=(
        'id',
        'company_name',
        'admin_user'
    )
    list_filter = (
        'company_name',
    )
admin.site.register(Employeer,ListEmployeer)

class ListPositions(admin.ModelAdmin):
    list_display = (
        'id',
        'company_name',
        'position',
        'level'
    )
    list_display_links = (
        'id',
        'company_name',
        'position'
    )
    list_filter = (
        'company_name',
        'position'
    )
admin.site.register(Positions,ListPositions)

class ListUsers(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'born_date', 
        'active',
        'admission_date',
        'position',
        'employeer'
    )
    list_display_links = (
        'id',
        'user'
    )
    list_filter = (
        'employeer',
        'position',
        'active'
    )
admin.site.register(Users_Data,ListUsers)