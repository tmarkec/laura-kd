from django.shortcuts import render
from django.views.generic import ListView
from .models import Post  

class PostListView(ListView):
    model = Post
    template_name = 'post/posts.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.all()