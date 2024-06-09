from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    """Для аутентифицированных пользователей имеющих статус администратора или
    персонала иначе только просмотр."""

    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
            and request.user.is_admin
        )


class IsAdminOrOwnerOrReadOnly(permissions.BasePermission):
    """Для аутентифицированных пользователей имеющих статус администратора или
    автора иначе только просмотр."""

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
    """Только для аутентифицированных пользователей имеющих статус
    администратора или суперюзера."""

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_admin
