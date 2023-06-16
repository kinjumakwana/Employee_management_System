from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from .forms import *
# Create your views here.
data = {}
def index(request):
    return render(request,"index.html")

########### Employeee#########
def all_employee_list(request):
    data['employee'] = Employee.objects.all()
    return render(request,"index.html", data)

def show_employee(request,pk):
    data['employee_detail'] = Employee.objects.get(id=pk)
    return render(request,"index.html", data)

def employee_add(request):
    if request.method == 'POST':
        # Name = request.POST['name']
        # Phone_number = request.POST['phone_number']
        # Whatsapp_number = request.POST['Whatsapp_number']
        # Email = request.POST['email']
        # Address = request.POST['address']

        # user = User.objects.create(Name=Name,
        #                                 Phone_number = Phone_number,
        #                                 Whatsappno = Whatsapp_number,
        #                                 Email = Email,
        #                                 Address = Address
        #                                 )
        # user.save()
        # return redirect(index)

        form_add = EmployeeForm(request.POST)
        if form_add.is_valid():
            form_add.save()
            return redirect('employee_list')
    else:
        form_add = EmployeeForm()
    return render(request, 'index.html', {'form_add': form_add})

def employee_edit(request,pk):
    employee = get_object_or_404(Employee, pk=pk)
    # if request.POST:
    #         employee.Name = request.POST['name']
    #         employee.Phone_number = request.POST['phone_number']
    #         employee.Whatsappno = request.POST['Whatsapp_number']
    #         employee.Email = request.POST['email']
    #         employee.Address = request.POST['address']
    #         employee.save()
    # return redirect(index)
    if request.method == 'POST':
        form_edit = EmployeeForm(request.POST, instance=employee)
        if form_edit.is_valid():
            form_edit.save()
            return redirect('employee_list')
    else:
        form_edit = EmployeeForm(instance=employee)
    return render(request, 'index.html', {'form_edit': form_edit})

def employee_delete(request,pk):
    employee = get_object_or_404(Employee, pk=pk)
    # employee.delete()
    # return redirect(request.META['HTTP_REFERER'])

    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')
    return render(request, 'index.html', {'employee': employee})

###### Holiday ##### 

def holiday_list(request):
    data['holiday'] = Holiday.objects.all()
    return render(request,"index.html",data)

def add_holiday(request):
    if request.method == 'POST':
        form_add_holiday = HolidayForm(request.POST)
        if form_add_holiday.is_valid():
            form_add_holiday.save()
            return redirect('holiday_list')
    else:
        form_add_holiday = HolidayForm()
    return render(request, 'index.html', {'form_add_holiday': form_add_holiday})

def edit_holiday(request,pk):
    holiday = get_object_or_404(Holiday, pk=pk)
    if request.method == 'POST':
        form_edit_holiday = HolidayForm(request.POST, instance=holiday)
        if form_edit_holiday.is_valid():
            form_edit_holiday.save()
            return redirect('holiday_list')
    else:
        form_edit_holiday = HolidayForm(instance=holiday)
    return render(request, 'index.html', {'form_edit_holiday': form_edit_holiday})

def delete_holiday(request,pk):
    holiday = get_object_or_404(Holiday, pk=pk)
    if request.method == 'POST':
        holiday.delete()
        return redirect('holiday_list')
    return render(request, 'index.html', {'holiday': holiday})

####  Attendence ####
def attendence_list(request):
    data['attendence'] = Attendance.objects.all()
    return render(request,"index.html",data)

def Emp_attendace_details(request,pk):
    data['Emp_attendace_details'] = Attendance.objects.get(id=pk)
    return render(request,"index.html", data)

def add_attendace(request,pk):
    if request.method == 'POST':
        form_add_attendace = AttendanceForm(request.POST)
        if form_add_attendace.is_valid():
            form_add_attendace.save()
            return redirect('attendence_list')
    else:
        form_add_attendace = AttendanceForm()
    return render(request,'index.html',{'form_add_attendace':form_add_attendace})

def edit_attendace(request,pk):
    attendence = get_object_or_404(Attendance,pk=pk)
    if request.method == 'POST':
        form_edit_attendace = AttendanceForm(request.POST, instance=attendence)
        if form_edit_attendace.is_valid():
            form_edit_attendace.save()
            return redirect("attendence_list")
    else:
        form_edit_attendace = AttendanceForm(instance=attendence)
    return render(request,'index.html',{'form_edit_attendace':form_edit_attendace})

def delete_attendace(request,pk):
    attendence = get_object_or_404(Attendance,pk=pk)
    if request.method == 'POST':
        attendence.delete()
        return redirect('attendence_list')
    return render(request, 'index.html', {'attendence': attendence})

## leave ### 

def leave_list(request):
    data['leave'] = Leave.objects.all()
    return render(request,"index.html",data)

def Emp_leave_details(request,pk):
    data['Emp_leave_details'] = Leave.objects.get(id=pk)
    return render(request,"index.html", data)

def add_leave(request,pk):
    if request.method == 'POST':
        form_add_leave = LeaveForm(request.POST)
        if form_add_leave.is_valid():
            form_add_leave.save()
            return redirect('leave_list')
    else:
        form_add_leave = LeaveForm()
    return render(request,'index.html',{'form_add_leave':form_add_leave})

def edit_leave(request,pk):
    leave = get_object_or_404(Leave,pk=pk)
    if request.method == 'POST':
        form_edit_leave = LeaveForm(request.POST,instance = leave)
        if form_edit_leave.is_valid():
            form_edit_leave.save()
            return redirect('leave_list')
    else:
        form_edit_leave = LeaveForm(instance=leave)
    return render(request,'index.html',{'form_edit_leave':form_edit_leave})

def delete_leave(request,pk):
    leave = get_object_or_404(Leave,pk=pk)
    if request.method == 'POST':
        leave.delete()
        return redirect('leave_list')
    return render(request,'index.html',{'leave':leave})

def leave_balance_list(request):
    data['leave_balance'] = Leave_Balance.objects.all()
    return render(request,"index.html",data)

def Emp_leave_balance_details(request,pk):
    data['Emp_leave_balance_details'] = Leave_Balance.objects.get(id=pk)
    return render(request,"index.html", data)

def leave_balance_add(request):
    if request.method == 'POST':
        form_balance_add = LeaveBalanceForm(request.POST)
        if form_balance_add.is_valid():
            form_balance_add.save()
            return redirect('leave_balance_list')
    else:
        form_balance_add = LeaveBalanceForm()
    return render(request,'index.html',{'form_balance_add':form_balance_add})


def leave_balance_edit(request, pk):
    leave_balance = get_object_or_404(Leave_Balance, pk=pk)
    if request.method == 'POST':
        form_balance_edit = LeaveBalanceForm(request.POST, instance=leave_balance)
        if form_balance_edit.is_valid():
            form_balance_edit.save()
            return redirect('leave_balance_list')
    else:
        form_balance_edit = LeaveBalanceForm(instance=leave_balance)
    return render(request,'index.html',{'form_balance_edit':form_balance_edit})

def leave_balance_delete(request, pk):
    leave_balance = get_object_or_404(Leave_Balance, pk=pk)
    if request.method == 'POST':
        leave_balance.delete()
        return redirect('leave_balance_list')
    return render(request,'index.html',{'leave_balance':leave_balance})

### Leave_yearly
def Leave_yearly_list(request):
    data['Leave_yearly_list'] = Leave_Balance.objects.all()
    return render(request,"index.html", data)

def Leave_year_add(request):
    if request.method == 'POST':
        form_year_add = LeaveYearlyForm(request.POST)
        if form_year_add.is_valid():
            form_year_add.save()
            return redirect('Leave_yearly_list')
    else:
        form_year_add = LeaveBalanceForm()
    return render(request,'index.html',{'form_year_add':form_year_add})

def Leave_year_edit(request, pk):
    leave_year = get_object_or_404(Leave_yearly, pk=pk)
    if request.method == 'POST':
        form_year_edit = LeaveYearlyForm(request.POST, instance=leave_year)
        if form_year_edit.is_valid():
            form_year_edit.save()
            return redirect('Leave_yearly_list')
    else:
        form_year_edit = LeaveBalanceForm(instance=leave_year)
    return render(request,'index.html',{'form_year_edit':form_year_edit})

def Leave_year_delete(request, pk):
    leave_year = get_object_or_404(Leave_yearly, pk=pk)
    if request.method == 'POST':
        leave_year.delete()
        return redirect('Leave_yearly_list')
    return render(request,'index.html',{'Leave_yearly_list':Leave_yearly_list})

#### Payroll ### 
def Emp_salary_list(request):
    data['salary'] = Payroll.objects.all()
    return render(request,"index.html",data)

def Emp_salary_details(request,pk):
    data['Emp_salary_details'] = Payroll.objects.get(id=pk)
    return render(request,"index.html", data)

def generate_payslip(request,pk):
    pass

def add_Emp_salary(request,pk):
    if request.method == 'POST':
        form_add_Emp_salary = PayrollForm(request.POST)
        if form_add_Emp_salary.is_valid():
            form_add_Emp_salary.save()
            return redirect('Emp_salary_list')
    else:
        form_add_Emp_salary = PayrollForm()
    return render(request,'index.html',{'form_add_Emp_salary':form_add_Emp_salary})

def edit_Emp_salary(request,pk):
    salary = get_object_or_404(Payroll,pk=pk)
    if request.method == 'POST':
        form_edit_Emp_salary = PayrollForm(request.POST,instance = salary)
        if form_edit_Emp_salary.is_valid():
            form_edit_Emp_salary.save()
            return redirect('Emp_salary_list')
    else:
        form_edit_Emp_salary = PayrollForm(instance=salary)
    return render(request,'index.html',{'form_edit_Emp_salary':form_edit_Emp_salary})

def delete_Emp_salary(request,pk):
    salary = get_object_or_404(Payroll,pk=pk)
    if request.method == 'POST':
        salary.delete()
        return redirect('Emp_salary_list')
    return render(request,'index.html',{'salary':salary})


