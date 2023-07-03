from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name="index"),
     path('emp/',EmpApi,name='EmpApi'),
    path('emp/<int:id>',EmpApi,name='EmpApi'),
    ## Employee API #####
    path('employees/', EmployeeList.as_view(), name='employee_list'),
    path('employees/add/', EmployeeList.as_view(), name='employee_add'),
    path('employees/<int:pk>/', EmployeeDetail.as_view(), name='employee_detail'),
    path('employees/edit/<int:pk>/', EmployeeDetail.as_view(), name='employee_edit'),
    path('employees/delete/<int:pk>/', EmployeeDetail.as_view(), name='employee_delete'),
    
    ##### Holiday API ########
    path('holiday/', Holidaylist.as_view(), name='holiday_list'),
    path('holiday/add/', Holidaylist.as_view(), name='holiday_add'),
    path('holiday/<int:pk>/', HolidayDetail.as_view(), name='holiday_detail'),
    path('holiday/edit/<int:pk>/', HolidayDetail.as_view(), name='holiday_edit'),
    path('holiday/delete/<int:pk>/', HolidayDetail.as_view(), name='holiday_delete'),
    
    ##### Leave API ########
    path('leave/', Leavelist.as_view(), name='leave_list'),
    path('leave/add/', Leavelist.as_view(), name='leave_add'),
    path('leave/<int:pk>/', LeaveDetail.as_view(), name='leave_detail'),
    path('leave/edit/<int:pk>/', LeaveDetail.as_view(), name='leave_edit'),
    path('leave/delete/<int:pk>/', LeaveDetail.as_view(), name='leave_delete'),
    
    #### Emp_Total_Leave API ###
    path('emp_Total_Leave/', Emp_Total_Leavelist.as_view(), name='emp_Total_Leave_list'),
    path('emp_Total_Leave/add/', Emp_Total_Leavelist.as_view(), name='emp_Total_Leave_add'),
    path('emp_Total_Leave/<int:pk>/', Emp_Total_LeaveDetail.as_view(), name='emp_Total_Leave_detail'),
    path('emp_Total_Leave/edit/<int:pk>/', Emp_Total_LeaveDetail.as_view(), name='emp_Total_Leave_edit'),
    path('emp_Total_Leave/delete/<int:pk>/', Emp_Total_LeaveDetail.as_view(), name='emp_Total_Leave_delete'),
    
    ##### Attendance API ########
    path('attendance/', Attendancelist.as_view(), name='attendance_list'),
    path('attendance/add/', Attendancelist.as_view(), name='attendance_add'),
    path('attendance/<int:pk>/', AttendanceDetail.as_view(), name='attendance_detail'),
    path('attendance/edit/<int:pk>/', AttendanceDetail.as_view(), name='attendance_edit'),
    path('attendance/delete/<int:pk>/', AttendanceDetail.as_view(), name='attendance_delete'),
    
    ##### Payroll API ########
    path('payroll/', Payrolllist.as_view(), name='payroll_list'),
    path('payroll/add/', Payrolllist.as_view(), name='payroll_add'),
    path('payroll/<int:pk>/', PayrollDetail.as_view(), name='payroll_detail'),
    path('payroll/edit/<int:pk>/', PayrollDetail.as_view(), name='payroll_edit'),
    path('payroll/delete/<int:pk>/', PayrollDetail.as_view(), name='payroll_delete'),
    
    ##### Leave_yearwise API ########
    path('leave_yearly/', Leave_yearwiselist.as_view(), name='leave_yearly_list'),
    path('leave_yearly/add/', Leave_yearwiselist.as_view(), name='leave_yearly_add'),
    path('leave_yearly/<int:pk>/', Leave_yearwiseDetail.as_view(), name='leave_yearly_detail'),
    path('leave_yearly/edit/<int:pk>/', Leave_yearwiseDetail.as_view(), name='leave_yearly_edit'),
    path('leave_yearly/delete/<int:pk>/', Leave_yearwiseDetail.as_view(), name='leave_yearly_delete'),
    
    ###  Employee ####
    path('all_employee_list/',all_employee_list,name="all_employee_list"),
    path('all_employee/',all_employee,name="all_employee"),
    path('employee/<int:pk>/',show_employee,name="show_employee"),
    path('add/', employee_add, name='employee_add'),
    path('edit/<int:pk>/', employee_edit, name='employee_edit'),
    path('delete/<int:pk>/', employee_delete, name='employee_delete'),
    
    #### Holiday #####
    path('holiday_list/', holiday_list, name='holiday_list'),
    path('add_holiday/', add_holiday, name='add_holiday'),
    path('edit_holiday/<int:pk>/', edit_holiday, name='edit_holiday'),
    path('delete_holiday/<int:pk>/', delete_holiday, name='delete_holiday'),
    
    ## Attendence #### 
    path('attendence_list', attendence_list, name='attendence_list'),
    path('Emp_attendace_details/<int:pk>/', Emp_attendace_details, name='Emp_attendace_details'),
    path('add_attendace/<int:pk>/', add_attendace, name='add_attendace'),
    path('edit_attendace/<int:pk>/', edit_attendace, name='edit_attendace'),
    path('delete_attendace/<int:pk>/', delete_attendace, name='delete_attendace'),
    
    ## leave ### 

    path('leave_list', leave_list, name='leave_list'),
    path('Emp_leave_details/<int:pk>/', Emp_leave_details, name='Emp_leave_details'),
    path('add_leave/<int:pk>/', add_leave, name='add_leave'),
    path('edit_leave/<int:pk>/', edit_leave, name='edit_leave'),
    path('delete_leave/<int:pk>/', delete_leave, name='delete_leave'),
    
    # leave Balance
    path('leave_balance_list', leave_balance_list, name='leave_balance_list'),
    path('leave_balance_add/', leave_balance_add, name='leave_balance_add'),
    path('leave_balance_edit/<int:pk>/', leave_balance_edit, name='leave_balance_edit'),
    path('leave_balance_delete/<int:pk>/', leave_balance_delete, name='leave_balance_delete'),
    path('Emp_leave_balance_details/<int:pk>/', Emp_leave_balance_details, name='Emp_leave_balance_details'),
    
    ### Leave_yearwise
    path('Leave_yearly_list', Leave_yearly_list, name='Leave_yearly_list'),
    path('Leave_year_add/', Leave_year_add, name='Leave_year_add'),
    path('Leave_year_edit/<int:pk>/', Leave_year_edit, name='Leave_year_edit'),
    path('Leave_year_delete/<int:pk>/', Leave_year_delete, name='Leave_year_delete'),
    
    ## payroll ###     
    path('Emp_salary_list', Emp_salary_list, name='Emp_salary_list'),
    path('Emp_salary_details/<int:pk>/', Emp_salary_details, name='Emp_salary_details'),
    path('add_Emp_salary/<int:pk>/', add_Emp_salary, name='add_Emp_salary'),
    path('edit_Emp_salary/<int:pk>/', edit_Emp_salary, name='edit_Emp_salary'),
    path('delete_Emp_salary/<int:pk>/', delete_Emp_salary, name='delete_Emp_salary'),
    path('generate_payslip/<int:pk>/', generate_payslip, name='generate_payslip'),
    
]
