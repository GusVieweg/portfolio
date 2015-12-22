from rest_framework import serializers
from apps.blog.models import Post, PostCategory


class PostCategorySerializer(serializers.ModelSerializer):
    """
    Serializes information relating to post categories.
    """
    class Meta:
        model = PostCategory
        fields = ('id', 'name', 'img_src')


class PostSerializer(serializers.ModelSerializer):
    """
    Serializes information relating to my blog posts.
    """
    category = PostCategorySerializer(many=False)

    class Meta:
        model = Post
        fields = ('id', 'title', 'date_added', 'category', 'description')

