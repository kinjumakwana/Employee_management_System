from django.contrib import admin
from .models import *
# Register your models here.
# register all class availavle in models.py file
# admin.site.register(District),
# admin.site.register([model for name, model in locals().items() if isinstance(model, type) and issubclass(model, models.Model)])
myModels = [Employee,Leave,Attendance,Payroll,Holiday, Leave_Balance,Leave_yearly]  # iterable list
admin.site.register(myModels)