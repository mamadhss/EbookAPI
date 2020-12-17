from rest_framework import permissions


class IsAdminUserOrReadOnly(permissions.IsAdminUser):
    def has_permission(self,request,view):
        is_admin = super().has_permission(request,view)
        return request.method in permissions.SAFE_METHODS or is_admin

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self,reqeust,view,obj):
        if reqeust.method in permissions.SAFE_METHODS:
            return True
        return obj.review_author == reqeust.user    