from django import forms 
from app1.models import employees

class employee_forms(forms.ModelForm):
    class Meta:
        model = employees
        fields = '__all__'