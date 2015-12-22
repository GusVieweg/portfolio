from django.db import models


class Post(models.Model):
    """
    Represents a blog post.

    The blog model is merely a reference to an HTML file to pull from.
    """
    title = models.CharField(max_length=255)
    img_src = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)
    content = models.TextField()
