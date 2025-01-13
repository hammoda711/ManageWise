from rest_framework.permissions import BasePermission

class IsAdminOrManager(BasePermission):
    """
    Custom permission to allow access to Admin and Manager only.
    """

    def has_permission(self, request, view):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return False

        # Admin has access to everything
        if request.user.role == 'admin':
            return True

        # Manager has limited access
        if request.user.role == 'manager':
            return True

        # Employees can only access their own data
        if request.user.role == 'employee':
            if view.action in ['list', 'retrieve']:
                return True
            return False
        return False
