# company/admin.py
from django.contrib import admin
from .models import Company, Department, Employee, Project

admin.site.register(Company)


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'number_of_employees', 'number_of_projects')

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('user', 'company', 'department', 'designation', 'hired_on', 'days_employed')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'department', 'start_date', 'end_date')
    filter_horizontal = ('assigned_employees',)
