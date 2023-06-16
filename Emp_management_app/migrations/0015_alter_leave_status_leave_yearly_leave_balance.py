# Generated by Django 4.1.7 on 2023-06-16 07:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Emp_management_app', '0014_remove_leave_my_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='status',
            field=models.CharField(choices=[('Approved', 'Approved'), ('Rejected', 'Rejected')], max_length=25),
        ),
        migrations.CreateModel(
            name='Leave_yearly',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.DateField()),
                ('total_leave', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Emp_management_app.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Leave_Balance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.DateField()),
                ('leave', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Emp_management_app.employee')),
            ],
        ),
    ]