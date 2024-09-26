import time
from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Post
from .forms import PostForm

class PostListView(ListView):
    model = Post
    template_name = 'post/posts.html'
    context_object_name = 'posts'

    # def get_queryset(self):
    #     return Post.objects.all()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['play_sound'] = self.request.session.pop('sound_play', False)  
        return context


class PostCreateView(ListView): 
    def get(self, request):
        form = PostForm()  
        return render(request, 'post/create_post.html', {'form': form})

    def post(self, request):
        form = PostForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
            request.session['sound_play'] = True
            return redirect('posts') 
        return render(request, 'post/create_post.html', {'form': form})