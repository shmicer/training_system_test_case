from typing import Iterable

from rest_framework import permissions

from .models import ProductAccess


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Пользователи могут редактировать свои собственные объекты,
    но создавать объекты могут только владельцы.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True


class HasAccessToLesson(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.products.filter(productaccess__user=request.user).exists()


class HasAccessToProduct(permissions.BasePermission):
    message = "У вас нет доступа к этому продукту."

    def has_object_permission(self, request, view, obj):
        user = request.user
        return obj.products.filter(productaccess__user=user).exists()
