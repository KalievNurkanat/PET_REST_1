from rest_framework.permissions import  BasePermission, SAFE_METHODS
from datetime import timedelta
from django.utils import timezone

class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user
    

class IsGuest(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

    
class IsAuthenticated(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)
     

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.is_staff:
            return True
        
    def has_object_permission(self, request, view, obj):
        if request.user and request.user.is_staff:
            return True
        
class EditTime(BasePermission):
    def has_object_permission(self, request, view, obj):
        time_passed = timezone.now() - obj.created_at
        return time_passed <= timedelta(minutes=10)