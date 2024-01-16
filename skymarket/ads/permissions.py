from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """
    Custom permission to checking the author.
    """
    message = 'Вы не являетесь владельцем.'

    def has_object_permission(self, request, view, obj):
        return request.user == obj.author


class IsAdmin(BasePermission):
    """
    Custom permission to check if the user is an administrator.
    """
    message = 'Данное действие доступно только администраторам проекта.'

    def has_permission(self, request, view):
        return request.user.is_admin
