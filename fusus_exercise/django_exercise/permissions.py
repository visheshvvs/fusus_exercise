from rest_framework import permissions


class UserPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.groups.filter(name="Viewer").exists():
            return request.method in permissions.SAFE_METHODS
        elif request.user.groups.filter(name="Regular User").exists():
            return request.method not in ["DELETE"]
        return True


class OrgPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.groups.filter(name="Admin").exists():
            return request.method in ["PATCH", "PUT", "GET"]
        return False