from rest_framework import serializers
from apps.blog.models import Post


class PostSerializer(serializers.ModelSerializer):
    """
    Serializes information relating to my blog posts.
    """
    class Meta:
        model = Post
        fields = ('id', 'title', 'img_src', 'description', 'date')
