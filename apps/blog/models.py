from django.db import models


class PostCategory(models.Model):
    """

    """
    name = models.CharField(max_length=255)
    img_src = models.URLField(max_length=255)

    def __str__(self):
        """
        For display in dropdowns for Django Admin
        :return:
        """
        return self.name


class Post(models.Model):
    """
    Represents a blog post.

    The blog model is merely a reference to an HTML file to pull from.
    """
    title = models.CharField(max_length=255)
    category = models.ForeignKey(PostCategory, default=1)
    last_modified = models.DateField(auto_now=True)
    date_added = models.DateField(auto_now_add=True)
    description = models.TextField(null=True, blank=True)
    content = models.TextField()
