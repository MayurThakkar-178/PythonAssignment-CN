from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOrganizerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return getattr(obj, 'organizer_id', None) == getattr(request.user, 'id', None)

class IsInvitedOrPublic(BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.is_public:
            return True
        if not request.user.is_authenticated:
            return False
        return obj.invited_users.filter(id=request.user.id).exists() or obj.organizer_id == request.user.id

    def has_permission(self, request, view):
        return True
