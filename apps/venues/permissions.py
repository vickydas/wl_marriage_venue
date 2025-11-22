from rest_framework.permissions import BasePermission

class IsAdminUserRole(BasePermission):
    """
    Allows access only to users with admin role.
    Assumes the User model has a 'role' attribute.
    """

    def has_permission(self, request, view):
       return request.user.is_authenticated and request.user.role in ['ADMIN', 'SUPERADMIN']