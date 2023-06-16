from django import forms
from .models import *

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['user','gender','mobile_no','designation','department','address','date_of_birth','education','profile_pic','document']

class HolidayForm(forms.ModelForm):
    class Meta:
        model = Holiday
        fields = ['holiday_name','date','detials']

class LeaveForm(forms.ModelForm):
    class Meta:
        model = Leave
        fields = ['employee','leave_Title','leave_from','second_half','leave_to','first_half','no_of_days','status','reason','note']

class LeaveBalanceForm(forms.ModelForm):
    class Meta:
        model = Emp_Total_Leave
        fields = ['employee','year','leave']

class LeaveYearlyForm(forms.ModelForm):
    class Meta:
        model = Leave_yearly        
        fields = ['year','total_leave']

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['employee','check_in','break_in_time','break_out_time','check_out','total_hours']

class PayrollForm(forms.ModelForm):
    class Meta:
        model = Payroll
        fields = ['employee','salary','payslip']