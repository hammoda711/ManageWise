from rest_framework.permissions import BasePermission
from rest_framework.permissions import BasePermission

class IsAdminOrManager(BasePermission):
    """
    Custom permission to allow:
    - Admins: All actions
    - Managers: All actions except delete
    """

    def has_object_permission(self, request, view, obj):
        # Admins have full access
        if request.user.role == 'admin':
            return True

        # Managers have access to all actions except delete
        if request.user.role == 'manager':
            if view.action in ['list', 'retrieve', 'create', 'update', 'partial_update']:
                return True
            if view.action == 'destroy':
                return False

        return False


class IsAdminManagerOrEmployee(BasePermission):
    """
    Custom permission for the EmployeeViewSet:
    - Admins: All actions
    - Managers: All actions except delete
    - Employees: Can only view and update their own profile
    """

    def has_object_permission(self, request, view, obj):
        # Admins have full access
        if request.user.role == 'admin':
            return True

        # Managers have access to all actions except delete
        if request.user.role == 'manager':
            if view.action in ['list', 'retrieve', 'create', 'update', 'partial_update']:
                return True
            if view.action == 'destroy':
                return False

        # Employees can only view or update their own profile
        if request.user.role == 'employee':
            if view.action in ['retrieve', 'update', 'partial_update']:
                return obj.user == request.user
            return False

        return False
