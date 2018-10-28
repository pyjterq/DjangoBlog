from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from markdownx.models import MarkdownxField

# User.objects.create_user()

# Create your models here.

# class BlogUser(models):
class Category(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)

class Entry(models.Model):
    users = models.ManyToManyField(User)
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250) # TODO: użyj Slugify
    created_at = models.DateTimeField()
    posted_at = models.DateTimeField()
    # content = models.TextField()
    mk_content = MarkdownxField()
    is_archived = models.BooleanField(default=False)
    categories = models.ManyToManyField(Category)


    def save(self, *args, **kwargs):
        if not self.id:
            # not self.id oznacza, że obiekt nie nigdy nie był zapisany
            self.created_at = timezone.now()
        return super().save(*args, **kwargs)


    # def snippet(self):
    #     return self.mk_content[:300] + ' …'