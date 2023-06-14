from django import forms
from .models import *

class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ['user','gender','mobile_no','designation','department','address','date_of_birth','education','profile_pic','document']