from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.


class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Manager', 'Manager'),
        ('Employee', 'Employee'),
    ]
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    
        # Use unique related_name values to avoid conflicts
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_groups',  # Custom related_name
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_user_permissions',  # Custom related_name
        blank=True
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','role']

    def __str__(self):
        return self.email