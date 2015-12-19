from django.db import models


class Project(models.Model):
    """
    Represents a (potentially active) project I am working on.

    Each project refers to a new, dedicated project page, that describes
    the purpose of the project, potential API reference, etc.
    """
    title = models.CharField(max_length=255)
    img_src = models.CharField(max_length=255)
    git = models.URLField(max_length=255)
    description = models.TextField()
    date = models.DateField()
