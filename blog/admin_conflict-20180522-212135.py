from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import Entry, Category
# Register your models here.
admin.site.register(Category)

class EntryModelAdmin(MarkdownxModelAdmin):
    list_display = ['id', 'title', 'posted_at']

# @admin.register(Author)
# class AuthorModelAdmin(ModelAdmin): pass

admin.site.register(Entry, EntryModelAdmin)
