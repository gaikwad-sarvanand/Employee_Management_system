from .models import Employee ,Department,Role
from django import forms

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"
        

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = "__all__"
        
class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = "__all__"