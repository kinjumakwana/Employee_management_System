# Generated by Django 4.2.2 on 2023-06-13 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Emp_management_app', '0005_holiday_leave_holiday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='holiday',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Emp_management_app.holiday'),
        ),
    ]
