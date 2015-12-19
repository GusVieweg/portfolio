from rest_framework import serializers
from apps.projects.models import Project


class ProjectSerializer(serializers.ModelSerializer):
    """
    Serializes information relating to projects.
    """
    class Meta:
        model = Project
        fields = ('id', 'title', 'img_src', 'git', 'date', 'description')