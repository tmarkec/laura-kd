from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("author_name", "body", "image")
    list_filter = ("author_name",)
