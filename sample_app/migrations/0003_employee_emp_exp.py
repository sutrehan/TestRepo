# Generated by Django 2.2 on 2019-04-30 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample_app', '0002_employee_emp_salary'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='emp_exp',
            field=models.IntegerField(default=0),
        ),
    ]