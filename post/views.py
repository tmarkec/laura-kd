from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Post
from .forms import PostForm

class PostListView(ListView):
    model = Post
    template_name = 'post/posts.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.all()


class PostCreateView(ListView): 
    def get(self, request):
        form = PostForm()  
        return render(request, 'post/create_post.html', {'form': form})

    def post(self, request):
        form = PostForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save() 
            return redirect('posts') 
        return render(request, 'post/create_post.html', {'form': form})