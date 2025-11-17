from django.contrib import admin

# Register your models here.
from app1.models import employees
class employees_admin(admin.ModelAdmin):
    list_display = ['emp_name','emp_id','emp_email']
admin.site.register(employees,employees_admin)