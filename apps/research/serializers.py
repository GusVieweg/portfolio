from rest_framework import serializers
from apps.research.models import Research


class ResearchSerializer(serializers.ModelSerializer):
    """
    Serializes information relating to projects.
    """
    class Meta:
        model = Research
        fields = ('id', 'title', 'img_src', 'description', 'date_added')
