from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Resource
from .serializers import ResourceSerializer
from .permissions import IsLecturer


class ResourceViewSet(ModelViewSet):
    """
    API endpoints:
    GET    /api/resources/
    POST   /api/resources/        (lecturer only)
    PUT    /api/resources/<id>/   (owner lecturer only)
    DELETE /api/resources/<id>/   (owner lecturer only)
    """

    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer

    permission_classes = [
        IsAuthenticatedOrReadOnly,
        IsLecturer,
    ]

    def perform_create(self, serializer):
        serializer.save(uploaded_by=self.request.user)
