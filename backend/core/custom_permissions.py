from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return bool(request.user and request.user.is_staff)


class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            return (obj.user == request.user) | request.user.is_staff
        return False


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            return obj.user == request.user
        return False
