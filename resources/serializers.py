from rest_framework import serializers
from .models import Resource


class ResourceSerializer(serializers.ModelSerializer):
    uploaded_by = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Resource
        fields = [
            "id",
            "title",
            "description",
            "file",
            "uploaded_by",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["uploaded_by", "created_at", "updated_at"]
