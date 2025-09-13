from rest_framework import permissions

class IsLibrarianOrReadOnly(permissions.BasePermission):
    """
    Custom permission:
    - Safe methods (GET, HEAD, OPTIONS) allowed for everyone
    - Librarians required for POST, PUT, PATCH, DELETE
    """

    def has_permission(self, request, view):
        # Safe methods are always allowed
        if request.method in permissions.SAFE_METHODS:
            return True
        # Only librarians can modify
        return request.user.is_authenticated and getattr(request.user, "role", "").lower() == "librarian"