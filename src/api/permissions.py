from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True


class HasAccessToLesson(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.products.filter(productaccess__user=request.user).exists()
