from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsLecturer(BasePermission):
    """
    Permissions:
    - Anyone can READ (GET)
    - Only lecturers can CREATE, UPDATE, DELETE
    - Only the owner can UPDATE or DELETE
    """

    def has_permission(self, request, view):
        # Allow safe methods for everyone
        if request.method in SAFE_METHODS:
            return True

        # Only authenticated lecturers can write
        return (
            request.user.is_authenticated
            and getattr(request.user, "role", None) == "lecturer"
        )

    def has_object_permission(self, request, view, obj):
        # Read permissions allowed for everyone
        if request.method in SAFE_METHODS:
            return True

        # Write permissions only for the owner lecturer
        return (
            request.user.is_authenticated
            and getattr(request.user, "role", None) == "lecturer"
            and obj.uploaded_by == request.user
        )
