from django.urls import path
from .views import (
    signup_view,
    resource_list_view,
    resource_upload_view,
    resource_edit_view,
    resource_delete_view,
)

urlpatterns = [
    path("", resource_list_view, name="resource_list"),
    path("signup/", signup_view, name="signup"),

    path("upload/", resource_upload_view, name="resource_upload"),
    path("edit/<int:pk>/", resource_edit_view, name="resource_edit"),
    path("delete/<int:pk>/", resource_delete_view, name="resource_delete"),
]
