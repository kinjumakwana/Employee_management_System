# Generated by Django 4.2.2 on 2023-06-14 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Emp_management_app', '0006_alter_leave_holiday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='halfday',
            field=models.CharField(choices=[('First', 'First'), ('Second', 'Second')], max_length=10),
        ),
    ]