from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet
from .models import Company, Department, Employee #, Project
from .serializers import (
    CompanySerializer,
    DepartmentSerializer,
    EmployeeSerializer,
    #ProjectSerializer,
)
from accounts.permissions import IsAdminManagerOrEmployee, IsAdminOrManager
from rest_framework.permissions import IsAuthenticated


class CompanyViewSet(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated,IsAdminOrManager] 


class DepartmentViewSet(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated,IsAdminOrManager]  


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated,IsAdminManagerOrEmployee]

    def get_queryset(self):
        # Employees can only retrieve their own profile
        if self.request.user.role == 'employee':
            return Employee.objects.filter(user=self.request.user)
        return super().get_queryset()


# class ProjectViewSet(ModelViewSet):
#     queryset = Project.objects.all()
#     serializer_class = ProjectSerializer
