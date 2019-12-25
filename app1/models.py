from django.conf import settings
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation
# Assign the User model in case it has been "swapped"
User = settings.AUTH_USER_MODEL
# Create your models here
class Post(models.Model):
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  title = models.CharField(max_length=75)
  slug = models.SlugField(unique=True)
  body = models.TextField(blank=True)
  comments = GenericRelation('Comment')


class Picture(models.Model):
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  image = models.ImageField()
  caption = models.TextField(blank=True)
  comments = GenericRelation('Comment')

class Comment(models.Model):
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  body = models.TextField(blank=True)
  content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
  object_id = models.PositiveIntegerField()
  content_object = GenericForeignKey()