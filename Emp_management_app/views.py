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

