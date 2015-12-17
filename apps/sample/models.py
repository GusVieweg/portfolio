from django.db import models

# Can create as many models here as you'd like
class Sample(models.Model):
    """
    Just an example model (entry in a database).
    """
    title = models.CharField(max_length=255)
    img_src = models.CharField(max_length=255)

