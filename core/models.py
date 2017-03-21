from django.db import models
from ckeditor.fields import RichTextField

class Block(models.Model):
    content = RichTextField()

