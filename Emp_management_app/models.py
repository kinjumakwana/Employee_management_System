import math
from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.core.exceptions import ValidationError
from datetime import timedelta


# Create your models here.
# class Department(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()

#     def __str__(self):
#         return self.name

# class Designation(models.Model):
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name

# class Education(models.Model):
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name
    
class Employee(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    DEPARTMENT_CHOICES = [
        ('Development','Development'),
        ('Designing','Designing'),
        ('Testing','Testing'),
        ('HR','HR'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(choices=GENDER_CHOICES,max_length=1)
    # department = models.ForeignKey(Department, on_delete=models.CASCADE)
    # designation = models.ForeignKey(Designation, on_delete=models.CASCADE)
    mobile_no = models.CharField(max_length=12)
    designation = models.CharField(max_length=500)
    department = models.CharField(choices=DEPARTMENT_CHOICES,max_length = 25)
    address = models.TextField()
    date_of_birth = models.DateField()
    education = models.TextField()
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True)
    document = models.FileField(upload_to='documents/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'    

class Holiday(models.Model):
    holiday_name = models.CharField(max_length=500)
    date = models.DateField()
    detials = models.TextField()
    
    def __str__(self):
        return f'{self.holiday_name}'    
    
class Leave(models.Model):
    HALF_DAY = [
        ('First', 'First'),
        ('Second', 'Second'),
    ]
    LEAVE_TYPE = [
        ('Paid', 'Paid'),
        ('Unpaid', 'Unpaid'),
    ]
    STATUS = [
        ('Development','Development'),
        ('Designing','Designing'),
        ('Testing','Testing'),
        ('HR','HR'),
    ]
    
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    holiday = models.ForeignKey(Holiday, on_delete=models.SET_NULL, null= True, blank=True)
    leave_Title = models.CharField(max_length=500)
    leave_type = models.CharField(choices=LEAVE_TYPE, max_length = 10)
    leave_from = models.DateField()
    halfday_from = models.BooleanField(default=False, blank=True)
    # halfday_from = models.CharField(choices=HALF_DAY, max_length = 10, blank=True, null= True)
    leave_to = models.DateField()
    halfday_to = models.BooleanField(default=False, blank=True)
    # halfday_to = models.CharField(choices=HALF_DAY, max_length = 10, blank=True, null= True)
    no_of_days = models.CharField(max_length=12)
    status =models.CharField(choices=STATUS, max_length = 25)
    reason = models.TextField()
    note= models.TextField(null=True, blank=True)
    apply_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        self.working_hours = 8
        if self.leave_from and self.leave_to:
            if self.leave_from > self.leave_to:
                raise ValidationError("Leave 'from' date must be before the 'to' date.")
            
            if self.leave_from == self.leave_to:
                # If leave_from and leave_to are the same day
                if self.halfday_from and self.halfday_to:
                    raise ValidationError("Please select any one")
                self.no_of_days = 0.5
                print("half day is", self.no_of_days)
            
            if self.leave_from < self.leave_to:
                delta = self.leave_to - self.leave_from
                # Deduct holiday days
                holiday_days = Holiday.objects.filter(date__range=[self.leave_from, self.leave_to]).count()
                print("holidays",holiday_days)
                
                # get list of all days
                all_days = (self.leave_from + timedelta(days=x) for x in range((delta.days) + 1))
                # filter business days
                # weekday from 0 to 4. 0 is monday adn 4 is friday
                # increase counter in each iteration if it is a weekday
                count = sum(1 for day in all_days if day.weekday() < 5 and not Holiday.objects.filter(date=day).exists())
                print('Number of business days is:', count)
                
                if self.halfday_from and self.halfday_to :
                    # self.halfday = 'Second'
                    self.no_of_days = count - 1
                    print("Number of days is",self.no_of_days)
                    
                elif self.halfday_from or self.halfday_to :
                    self.half = self.working_hours/2
                    print("half day is", self.half) 
                    self.no_of_days = count - (self.half / self.working_hours)
                    print("Number of days is",self.no_of_days)

                else:
                    self.no_of_days = str(count)
                    print("Number of days is",self.no_of_days)
            
    def __str__(self):
        return f'{self.employee}'    
    
class Attendance(models.Model):
    STATUS = [('Present', 'Present'), ('Absent', 'Absent')]
    
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    break_in_time = models.DateTimeField(null=True, blank=True)
    break_out_time = models.DateTimeField(null=True, blank=True)
    check_out = models.DateTimeField(null=True, blank=True)
    total_hours = models.FloatField(null=True, blank=True)
    status = models.CharField(choices=STATUS, max_length = 10)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        if self.check_in and self.check_out:
            total_time = self.check_out - self.check_in

            # Subtract break time if available
            if self.break_in_time and self.break_out_time:
                break_time = self.break_out_time - self.break_in_time
                total_time -= break_time

            # Make sure total_time is not negative
            total_time = max(total_time, timedelta())
        
            total_hours = total_time.total_seconds() / 3600  # Convert seconds to hours
            self.total_hours = round(total_hours, 2)  # Round to two decimal places

        super().save(*args, **kwargs)
    
    def __str__(self):
        return f'{self.employee}'
    
class Payroll(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    attendance = models.ForeignKey(Attendance, on_delete=models.CASCADE)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    payslip = models.FileField(upload_to='payslips/',blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # Additional fields for the salary
    
    def __str__(self):
        return f'{self.employee}'