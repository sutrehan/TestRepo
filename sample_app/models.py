from django.db import models

# Create your models here.

class Company(models.Model):
    company_name = models.CharField(max_length=100)
    company_loc = models.CharField(max_length=100)

    def __str__(self):
        return self.company_name

class Employee(models.Model):
    emp_name = models.CharField(max_length=100)
    emp_age = models.IntegerField()
    emp_salary = models.IntegerField()
    emp_exp = models.IntegerField(default=0)
    emp_company = models.ForeignKey(Company, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.emp_name

class User(models.Model):
    username = models.CharField(max_length=50)

    def __str__(self):
        return self.username

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_name = models.CharField(max_length=100)

    def __str__(self):
        return self.profile_name

class SampleModel(models.Model):
    pass
