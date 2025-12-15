from rest_framework.routers import DefaultRouter
from django.urls import path, include
from resources.api_views import ResourceViewSet

router = DefaultRouter()
router.register("resources", ResourceViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
