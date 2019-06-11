from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    message = 'Sorry, you don\'t have permissions to view this page'

    def has_object_permission(self, request, view, obj):
        if obj.author == request.user or request.user.is_superuser:
            return True
        return False
