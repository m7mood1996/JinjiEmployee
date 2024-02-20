from django.contrib import admin

from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'car_number', 'paycheck', '_advance_payment_calculate')
admin.site.register(Employee, EmployeeAdmin)