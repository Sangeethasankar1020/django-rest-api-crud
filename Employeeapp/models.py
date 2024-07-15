from django.db import models
from.myDb import*


class Department(models.Model):
    DepartmentId =models.AutoField(primary_key=True)
    DepartmentName=models.CharField(max_length=500)


class Employees(models.Model):
    EmployeeId =models.AutoField(primary_key=True)
    EmployeeName=models.CharField(max_length=500)
    Department=models.CharField(max_length=500)
    DateOfJoining=models.CharField(max_length=500)
    PhotoFileName=models.CharField(max_length=500)