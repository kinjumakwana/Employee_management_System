# Generated by Django 4.2.2 on 2023-06-13 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Emp_management_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='note',
            field=models.TextField(blank=True, null=True),
        ),
    ]