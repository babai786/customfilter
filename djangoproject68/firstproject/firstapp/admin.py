from django.contrib import admin
from firstapp.models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display=['name','number','sal']


admin.site.register(Employee,EmployeeAdmin)
