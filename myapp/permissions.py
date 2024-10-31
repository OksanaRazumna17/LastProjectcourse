from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    """
    Пермишен, який дозволяє доступ тільки власнику об'єкта.
    """
    def has_object_permission(self, request, view, obj):
        # Перевіряє, чи є користувач власником об'єкта
        return obj.owner == request.user
