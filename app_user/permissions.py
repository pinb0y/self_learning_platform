from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """Класс для проверки доступа если пользователь владельца объекта"""

    def has_object_permission(self, request, view, obj):
        if hasattr(obj, 'user'):
            return request.user == obj.user
        elif hasattr(obj, 'email'):
            return request.user.email == obj.email
        return False


class IsTeacher(permissions.BasePermission):
    """Класс для проверки доступа если пользователь учитель"""

    def has_permission(self, request, view):
        return request.user.is_teacher


class IsAdmin(permissions.BasePermission):
    """Класс для проверки доступа если пользователь администратор"""

    def has_permission(self, request, view):
        return request.user.is_staff or request.user.is_superuser
