# Generated by Django 4.2.2 on 2023-06-14 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Emp_management_app', '0007_alter_leave_halfday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='halfday',
            field=models.CharField(blank=True, choices=[('First', 'First'), ('Second', 'Second')], max_length=10, null=True),
        ),
    ]
