from typing import Iterable

from rest_framework import permissions


class HasAccessToLesson(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.products.filter(productaccess__user=request.user).exists()