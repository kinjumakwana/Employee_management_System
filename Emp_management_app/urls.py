from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name="index"),
    path('all_employee_list',all_employee_list,name="all_employee_list"),
    path('all_employee_list/<int:pk>',show_employee,name="show_employee"),
    path('add/', employee_add, name='employee_add'),
    path('edit/<int:pk>/', employee_edit, name='employee_edit'),
    path('delete/<int:pk>/', employee_delete, name='employee_delete'),
    
]
