from django.db import models
from django.contrib.auth.models import User

# User.objects.create_user()

# Create your models here.

# class BlogUser(models)


class Entry(models.Model):
    user = models.ManyToManyField(User)
    title = models.CharField(max_length=250)
    created_at = models.DateTimeField()
    content = models.TextField()
    is_archived = models.BooleanField()


class Category(models.Model):
    name = models.CharField(max_length=250)
    entry = models.ManyToManyField(Entry)





