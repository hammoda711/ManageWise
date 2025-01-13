from rest_framework import viewsets
from .models import Employee
from .serializers import EmployeeSerializer
from accounts.permissions import IsAdminOrManager 
# Create your views here.
from rest_framework.viewsets import ModelViewSet
from .models import Company, Department, Employee, Project
from .serializers import (
    CompanySerializer,
    DepartmentSerializer,
    EmployeeSerializer,
    ProjectSerializer,
)

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAdminOrManager]  # Restrict access based on role


