from rest_framework import serializers
from apps.projects.models import Project

class SampleSerializer(serializers.ModelSerializer):
    """
    Used to serialize information based on REST endpoint.
    """
    class Meta:
        model = Project
        fields = ('id', 'title', 'img_src',)
