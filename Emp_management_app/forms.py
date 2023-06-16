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
        fields = ['employee','holiday','leave_Title','leave_type','leave_from','halfday_from','leave_to','halfday_to','no_of_days','status','reason','note']

class LeaveBalanceForm(forms.ModelForm):
    class Meta:
        model = Leave_Balance
        fields = ['employee','Leave','Previous_Year','Current_Year','Total','Used','Accepted','Rejected','Expired','Carry_Over']

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['employee','check_in','break_in_time','break_out_time','check_out','total_hours','status']

class PayrollForm(forms.ModelForm):
    class Meta:
        model = Payroll
        fields = ['employee','attendance','salary','payslip']