from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from .forms import *
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404, HttpResponse, JsonResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from .serializers import *


# Create your views here.
data = {}
def index(request):
    return render(request,"index.html")

@csrf_exempt
def EmpApi(request,id=0):
    if request.method=='GET':
        student = Employee.objects.all()
        student_serializer=EmployeeSerializer(student,many=True)
        return JsonResponse(student_serializer.data,safe=False)
    elif request.method=='POST':
        student_data=JSONParser().parse(request)
        student_serializer=EmployeeSerializer(data=student_data)
        if student_serializer.is_valid():
            student_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        student_data=JSONParser().parse(request)
        student=Employee.objects.get(id=id)
        student_serializer=EmployeeSerializer(student,data=student_data)
        if student_serializer.is_valid():
            student_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        student=Employee.objects.get(id=id)
        student.delete()
        return JsonResponse("Deleted Successfully",safe=False)

 ## Employee API #####
class EmployeeList(APIView):
    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response({"Message": "success", "data": serializer.data})
  
    def post(self, request):
        user_data = request.data.copy()
        # Extract user data from request
        print(user_data)
        user_data_dict = {
            'username': user_data.pop('username')[0],  # Get the first element of the list
            'first_name': user_data.pop('first_name')[0],
            'last_name': user_data.pop('last_name')[0],
            'email': user_data.pop('email')[0],  # Remove surrounding double quotes
            'password': user_data.pop('password')[0]
        }
        # user_data['user'] = user.id
        
        employee_data = {
                'user': user_data_dict,
                'gender': request.data['gender'],
                'mobile_no': request.data['mobile_no'],
                'designation': request.data['designation'],
                'department': request.data['department'],
                'address': request.data['address'],
                'date_of_birth': request.data['date_of_birth'],
                'education': request.data['education'],
                'profile_pic': request.FILES.get('profile_pic'),
                'document': request.FILES.get('document')
            }
        print(user_data_dict)
        print(employee_data)
        
        # Create User object
        user_serializer = UserSerializer(data=user_data_dict)
        if user_serializer.is_valid():
            employee_serializer = EmployeeSerializer(data=employee_data)
            if employee_serializer.is_valid():
                user = user_serializer.save()
                employee_serializer.save(user=user)
                return Response({"Message": "Employee created successfully"}, status=status.HTTP_201_CREATED)
            else:
                return Response({"Message": "Employee data validation failed", "errors": employee_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"Message": "User data validation failed", "errors": user_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class EmployeeDetail(APIView):
    def get_object(self, pk):
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        employee = self.get_object(pk)
        if not employee:
            return Response(
                {"Message": "Object with Employee id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

    def put(self, request, pk,*args, **kwargs):
        employee = self.get_object(pk)
        if not employee:
            return Response(
                {"Message": "Object with Employee id does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        user_data = request.data.copy()
        user_data_dict = {
            'username': user_data.pop('username', employee.user.username),
            'first_name': user_data.pop('first_name', employee.user.first_name),
            'last_name': user_data.pop('last_name', employee.user.last_name),
            'email': user_data.pop('email', employee.user.email),
            'password': user_data.pop('password', employee.user.password),
        }
        
        employee_data = {
            'user': user_data_dict,
            'gender': request.data.get('gender', employee.gender),
            'mobile_no': request.data.get('mobile_no', employee.mobile_no),
            'designation': request.data.get('designation', employee.designation),
            'department': request.data.get('department', employee.department),
            'address': request.data.get('address', employee.address),
            'date_of_birth': request.data.get('date_of_birth', employee.date_of_birth),
            'education': request.data.get('education', employee.education),
            'profile_pic': request.FILES.get('profile_pic', employee.profile_pic),
            'document': request.FILES.get('document', employee.document),
        }
        
        user_serializer = UserSerializer(employee.user, data=user_data_dict)
        if user_serializer.is_valid():
            employee_serializer = EmployeeSerializer(employee, data=employee_data)
            if employee_serializer.is_valid():
                user_serializer.save()
                employee_serializer.save()
                return Response({"Message": "Employee updated successfully"})
            else:
                return Response({"Message": "Employee data validation failed", "errors": employee_serializer.errors},
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"Message": "User data validation failed", "errors": user_serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)
        
    def patch(self, request, pk,*args, **kwargs):
        employee = self.get_object(pk)
        if not employee:
            return Response(
                {"Message": "Object with Employee id does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )

        user_data = request.data.copy()
        user_data_dict = {
            'username': user_data.pop('username', employee.user.username)[0],
            'first_name': user_data.pop('first_name', employee.user.first_name)[0],
            'last_name': user_data.pop('last_name', employee.user.last_name)[0],
            'email': user_data.pop('email', employee.user.email)[0],
            'password': user_data.pop('password', employee.user.password)[0],
        }
        print("userdata: ", user_data_dict)
        employee_data = {
            'user': user_data_dict,
            'gender': request.data.get('gender', employee.gender),
            'mobile_no': request.data.get('mobile_no', employee.mobile_no),
            'designation': request.data.get('designation', employee.designation),
            'department': request.data.get('department', employee.department),
            'address': request.data.get('address', employee.address),
            'date_of_birth': request.data.get('date_of_birth', employee.date_of_birth),
            'education': request.data.get('education', employee.education),
            'profile_pic': request.FILES.get('profile_pic', employee.profile_pic),
            'document': request.FILES.get('document', employee.document),
        }
        print("employee_data: ", employee_data)
        
        user_serializer = UserSerializer(employee.user, data=user_data_dict, partial=True)
        if user_serializer.is_valid():
            employee_serializer = EmployeeSerializer(employee, data=employee_data, partial=True)
            if employee_serializer.is_valid():
                user_serializer.save()  
                employee_serializer.save()
                return Response({"Message": "Employee updated successfully"})
            else:
                return Response({"Message": "Employee data validation failed", "errors": employee_serializer.errors},
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"Message": "User data validation failed", "errors": user_serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk,*args, **kwargs):
        employee = self.get_object(pk)
        if employee:
            user = employee.user
            if user:
                user.delete()  # Delete the associated user
            employee.delete()
            return Response({"Message": "Employee deleted!"},status=status.HTTP_200_OK)
        return Response(status=status.HTTP_204_NO_CONTENT)

##### Holiday API ########
class Holidaylist(APIView):
    def get(self,request):
        holiday = Holiday.objects.all()
        serializer = HolidaySerializer(holiday,many=True)
        return Response({"Message": "success", "data": serializer.data})
    
    def post(self,request):
        serializer = HolidaySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Message": "Add New Holiday Successfully!!","data":serializer.data, 'status':status.HTTP_201_CREATED})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class HolidayDetail(APIView):    
    def get_object(request,pk):
        try:
            return Holiday.objects.get(pk=pk)
        except Holiday.DoesNotExist:
            return Http404
        
    def get(self, request, pk):
        holiday = self.get_object(pk)
        if not holiday:
            return Response(
                {"Message": "Object with Holiday id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = HolidaySerializer(holiday)
        return Response(serializer.data)
    
    def put(self,request,pk,*args, **kwargs):
        holiday = self.get_object(pk)
        serializer = HolidaySerializer(instance = holiday, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Message": "Holiday Updated!",'data':serializer.data,'status':status.HTTP_200_OK})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request,pk,*args, **kwargs):
        holiday = self.get_object(pk)
        data = request.data.copy()  # Create a mutable copy of request.data
        data.pop('user', None)  # Remove the 'user' field if it exists

        serializer = HolidaySerializer(holiday, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Message": "Holiday Updated!",'data':serializer.data,'status':status.HTTP_200_OK})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk,*args, **kwargs):
        holiday = self.get_object(pk)
        if holiday:
            holiday.delete()
            return Response({"Message": "Holiday deleted!"},status=status.HTTP_200_OK)
        return Response(status=status.HTTP_204_NO_CONTENT)

##### Leave API ########
class Leavelist(APIView):
    def get(self,request):
        leave = Leave.objects.all()
        serializer = LeaveSerializer(leave,many=True)
        return Response({"Message": "success", "data": serializer.data})
    
    def post(self,request):
        serializer = LeaveSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Message": "Add New leave Successfully!!","data":serializer.data, 'status':status.HTTP_201_CREATED})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class LeaveDetail(APIView):  
    def get_object(request,pk):
        try:
            return Leave.objects.get(pk=pk)
        except Leave.DoesNotExist:
            return Http404
    
    def get(self, request, pk):
        leave = self.get_object(pk)
        if not leave:
            return Response(
                {"Message": "Object with Leave id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = LeaveSerializer(leave)
        return Response(serializer.data)
    
    def put(self,request,pk,*args, **kwargs):
        leave = self.get_object(pk)
        serializer = LeaveSerializer(instance = leave, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Message": "Leave Updated!",'data':serializer.data,'status':status.HTTP_200_OK})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request,pk,*args, **kwargs):
        leave = self.get_object(pk)
        data = request.data.copy()  # Create a mutable copy of request.data
        data.pop('user', None)  # Remove the 'user' field if it exists

        serializer = LeaveSerializer(leave, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Message": "Leave Updated!",'data':serializer.data,'status':status.HTTP_200_OK})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk,*args, **kwargs):
        leave = self.get_object(pk)
        if leave:
            leave.delete()
            return Response({"Message": "leave deleted!"},status=status.HTTP_200_OK)
        return Response(status=status.HTTP_204_NO_CONTENT)

##### Attendance API ########
class Attendancelist(APIView):
    def get(self,request):
        attendance = Attendance.objects.all()
        serializer = AttendanceSerializer(attendance,many=True)
        return Response({"Message": "success", "data": serializer.data})
    
    def post(self,request):
        serializer = AttendanceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Message": "Add New Attendance Successfully!!","data":serializer.data, 'status':status.HTTP_201_CREATED})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class AttendanceDetail(APIView):  
    def get_object(request,pk):
        try:
            return Attendance.objects.get(pk=pk)
        except Leave.DoesNotExist:
            return Http404
    
    def get(self, request, pk):
        attendance = self.get_object(pk)
        if not attendance:
            return Response(
                {"Message": "Object with Attendance id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = AttendanceSerializer(attendance)
        return Response(serializer.data)
    
    def put(self,request,pk,*args, **kwargs):
        attendance = self.get_object(pk)
        serializer = AttendanceSerializer(instance = attendance, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Message": "Attendance Updated!",'data':serializer.data,'status':status.HTTP_200_OK})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request,pk,*args, **kwargs):
        attendance = self.get_object(pk)
        data = request.data.copy()  # Create a mutable copy of request.data
        data.pop('user', None)  # Remove the 'user' field if it exists

        serializer = AttendanceSerializer(attendance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Message": "Attendance Updated!",'data':serializer.data,'status':status.HTTP_200_OK})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk,*args, **kwargs):
        attendance = self.get_object(pk)
        if attendance:
            attendance.delete()
            return Response({"Message": "Attendance deleted!"},status=status.HTTP_200_OK)
        return Response(status=status.HTTP_204_NO_CONTENT)

##### Payroll API ########

class Payrolllist(APIView):
    def get(self,request):
        payroll = Payroll.objects.all()
        serializer = PayrollSerializer(payroll,many=True)
        return Response({"Message": "success", "data": serializer.data})
    
    def post(self,request):
        serializer = PayrollSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Message": "Add New Payroll Successfully!!","data":serializer.data, 'status':status.HTTP_201_CREATED})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class PayrollDetail(APIView):  
    def get_object(request,pk):
        try:
            return Payroll.objects.get(pk=pk)
        except Payroll.DoesNotExist:
            return Http404
    
    def get(self, request, pk):
        payroll = self.get_object(pk)
        if not payroll:
            return Response(
                {"Message": "Object with Payroll id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = PayrollSerializer(payroll)
        return Response(serializer.data)
    
    def put(self,request,pk,*args, **kwargs):
        payroll = self.get_object(pk)
        serializer = PayrollSerializer(instance = payroll, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Message": "Payroll Updated!",'data':serializer.data,'status':status.HTTP_200_OK})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request,pk,*args, **kwargs):
        payroll = self.get_object(pk)
        data = request.data.copy()  # Create a mutable copy of request.data
        data.pop('user', None)  # Remove the 'user' field if it exists

        serializer = PayrollSerializer(payroll, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Message": "Payroll Updated!",'data':serializer.data,'status':status.HTTP_200_OK})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk,*args, **kwargs):
        payroll = self.get_object(pk)
        if payroll:
            payroll.delete()
            return Response({"Message": "Payroll deleted!"},status=status.HTTP_200_OK)
        return Response(status=status.HTTP_204_NO_CONTENT)

##### Leave_yearwise API ########

class Leave_yearwiselist(APIView):
    def get(self,request):
        payroll = Leave_yearly.objects.all()
        serializer = Leave_yearlySerializer(payroll,many=True)
        return Response({"Message": "success", "data": serializer.data})
    
    def post(self,request):
        serializer = Leave_yearlySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Message": "Add New Leave_yearwise Successfully!!","data":serializer.data, 'status':status.HTTP_201_CREATED})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class Leave_yearwiseDetail(APIView):  
    def get_object(request,pk):
        try:
            return Leave_yearly.objects.get(pk=pk)
        except Leave_yearly.DoesNotExist:
            return Http404
    
    def get(self, request, pk):
        leave_yearly = self.get_object(pk)
        if not leave_yearly:
            return Response(
                {"Message": "Object with Leave_yearwise id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = Leave_yearlySerializer(leave_yearly)
        return Response(serializer.data)
    
    def put(self,request,pk,*args, **kwargs):
        leave_yearly = self.get_object(pk)
        serializer = Leave_yearlySerializer(instance = leave_yearly, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Message": "Leave_yearwise Updated!",'data':serializer.data,'status':status.HTTP_200_OK})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request,pk,*args, **kwargs):
        leave_yearly = self.get_object(pk)
        data = request.data.copy()  # Create a mutable copy of request.data
        data.pop('user', None)  # Remove the 'user' field if it exists

        serializer = Leave_yearlySerializer(leave_yearly, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Message": "Leave_yearwise Updated!",'data':serializer.data,'status':status.HTTP_200_OK})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk,*args, **kwargs):
        leave_yearly = self.get_object(pk)
        if leave_yearly:
            leave_yearly.delete()
            return Response({"Message": "Leave_yearwise deleted!"},status=status.HTTP_200_OK)
        return Response(status=status.HTTP_204_NO_CONTENT)

##### Emp_Total_Leave API ########

class Emp_Total_Leavelist(APIView):
    def get(self,request):
        emp_Total_Leave = Emp_Total_Leave.objects.all()
        serializer = Emp_Total_LeaveSerializer(emp_Total_Leave,many=True)
        return Response({"Message": "success", "data": serializer.data})
    
    def post(self,request):
        serializer = Emp_Total_LeaveSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Message": "Add New Emp_Total_Leave Successfully!!","data":serializer.data, 'status':status.HTTP_201_CREATED})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class Emp_Total_LeaveDetail(APIView):  
    def get_object(request,pk):
        try:
            return Emp_Total_Leave.objects.get(pk=pk)
        except Emp_Total_Leave.DoesNotExist:
            return Http404
    
    def get(self, request, pk):
        emp_Total_Leave = self.get_object(pk)
        if not emp_Total_Leave:
            return Response(
                {"Message": "Object with Emp_Total_Leave id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = Emp_Total_LeaveSerializer(emp_Total_Leave)
        return Response(serializer.data)
    
    def put(self,request,pk,*args, **kwargs):
        emp_Total_Leave = self.get_object(pk)
        serializer = Emp_Total_LeaveSerializer(instance = emp_Total_Leave, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Message": "Emp_Total_Leave Updated!",'data':serializer.data,'status':status.HTTP_200_OK})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request,pk,*args, **kwargs):
        emp_Total_Leave = self.get_object(pk)
        data = request.data.copy()  # Create a mutable copy of request.data
        data.pop('user', None)  # Remove the 'user' field if it exists

        serializer = Emp_Total_LeaveSerializer(emp_Total_Leave, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Message": "Emp_Total_Leave Updated!",'data':serializer.data,'status':status.HTTP_200_OK})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk,*args, **kwargs):
        emp_Total_Leave = self.get_object(pk)
        if emp_Total_Leave:
            emp_Total_Leave.delete()
            return Response({"Message": "Emp_Total_Leave deleted!"},status=status.HTTP_200_OK)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
########### Employeee#########
def all_employee(request):
    employees = Employee.objects.all().values()
    return JsonResponse({'data': list(employees)})

def all_employee_list(request):
    employees = Employee.objects.all().values()
    return JsonResponse(list(employees), safe=False)

    # data['employee'] = Employee.objects.all()
    # return render(request,"employee.html", data)

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
    data['leave_balance'] = Emp_Total_Leave.objects.all()
    return render(request,"index.html",data)

def Emp_leave_balance_details(request,pk):
    data['Emp_leave_balance_details'] = Emp_Total_Leave.objects.get(id=pk)
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
    leave_balance = get_object_or_404(Emp_Total_Leave, pk=pk)
    if request.method == 'POST':
        form_balance_edit = LeaveBalanceForm(request.POST, instance=leave_balance)
        if form_balance_edit.is_valid():
            form_balance_edit.save()
            return redirect('leave_balance_list')
    else:
        form_balance_edit = LeaveBalanceForm(instance=leave_balance)
    return render(request,'index.html',{'form_balance_edit':form_balance_edit})

def leave_balance_delete(request, pk):
    leave_balance = get_object_or_404(Emp_Total_Leave, pk=pk)
    if request.method == 'POST':
        leave_balance.delete()
        return redirect('leave_balance_list')
    return render(request,'index.html',{'leave_balance':leave_balance})

### Leave_yearly
def Leave_yearly_list(request):
    data['Leave_yearly_list'] = Emp_Total_Leave.objects.all()
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


def generate_payslip(request, pk):
    salary = Payroll.objects.get(id=pk)
    template_path = 'payslip.html'
    context = {
        'salary': salary,
    }
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="Payslip.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response