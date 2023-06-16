from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name="index"),
    ###  Employee ####
    path('all_employee_list/',all_employee_list,name="all_employee_list"),
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
    
    ## payroll ###     
    path('Emp_salary_list', Emp_salary_list, name='Emp_salary_list'),
    path('Emp_salary_details/<int:pk>/', Emp_salary_details, name='Emp_salary_details'),
    path('add_Emp_salary/<int:pk>/', add_Emp_salary, name='add_Emp_salary'),
    path('edit_Emp_salary/<int:pk>/', edit_Emp_salary, name='edit_Emp_salary'),
    path('delete_Emp_salary/<int:pk>/', delete_Emp_salary, name='delete_Emp_salary'),
    path('generate_payslip/<int:pk>/', generate_payslip, name='generate_payslip'),
    
]
