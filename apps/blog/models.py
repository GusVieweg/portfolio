from django.db import models


class PostCategory(models.Model):
    """
    Represents a category a post belongs too.

    If the Post object itself has a null img_src, it defaults to the img_src
    of the category the post belongs to.
    """
    name = models.CharField(max_length=255)

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
    img_src = models.URLField(max_length=255, null=True)
    category = models.ForeignKey(PostCategory, default=1)
    description = models.TextField(null=True, blank=True)
    content_url = models.URLField(max_length=255)
    date_added = models.DateField()
    last_modified = models.DateField(auto_now=True)
