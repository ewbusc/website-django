from django.db import models
from ckeditor.fields import RichTextField

class Block(models.Model):
    name = models.CharField(max_length=50)
    content = RichTextField()
    class Meta(object):
        unique_together = ('name',)

