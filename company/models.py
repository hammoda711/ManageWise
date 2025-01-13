from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=255)
    
    @property
    def number_of_departments(self):
        return self.departments.count()

    @property
    def number_of_employees(self):
        return self.employees.count()

    @property
    def number_of_projects(self):
        return self.projects.count()

    def __str__(self):
        return self.name


class Department(models.Model):
    company = models.ForeignKey(Company, related_name='departments', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255)

    @property
    def number_of_employees(self):
        return self.employees.count()

    @property
    def number_of_projects(self):
        return self.projects.count()

    def __str__(self):
        return f"{self.name} ({self.company.name})"


class Employee(models.Model):
    user = models.OneToOneField('accounts.CustomUser', on_delete=models.CASCADE, related_name='employee')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='employees', null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='employees',null=True, blank=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    mobile_number = models.CharField(max_length=15)
    address = models.TextField()
    designation = models.CharField(max_length=255)
    hired_on = models.DateField(null=True, blank=True)

    @property
    def days_employed(self):
        if self.hired_on:
            from datetime import date
            return (date.today() - self.hired_on).days
        return None

    def __str__(self):
        return f"{self.user.username} ({self.company.name})"
    
class Project(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='projects', null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='projects')
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    assigned_employees = models.ManyToManyField(Employee, related_name='projects')