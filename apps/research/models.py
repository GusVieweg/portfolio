from django.db import models


class Research(models.Model):
    """
    Represents a post on something I've been studying.
    """
    title = models.CharField(max_length=255)
    img_src = models.URLField(max_length=255)
    description = models.TextField()
    last_modified = models.DateField(auto_now=True)
    date_added = models.DateField(auto_now_add=True)
    content_url = models.URLField(max_length=255)
