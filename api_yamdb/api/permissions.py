from rest_framework import permissions


class AnonReadOnly(permissions.BasePermission):
    """
    Safe methods.

    For anonymous users.
    """

    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Safe methods.

    For authenticated users with admin.
    """

    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
            and request.user.is_admin
        )


class IsAdminOrOwnerOrReadOnly(permissions.BasePermission):
    """
    Safe methods.

    For authenticated users with admin rights or object's owners.
    """

    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_admin
            or request.user.is_moderator
            or obj.author == request.user
        )


class IsAdmin(permissions.BasePermission):
    """
    All methods methods.

    For authenticated users with admin rights.
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_admin
