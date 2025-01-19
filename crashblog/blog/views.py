from django.shortcuts import render, get_object_or_404
from .models import PostBlog
from .forms import CommentForm

def detail(request, slug):
    post = get_object_or_404(PostBlog, slug = slug)
    form = CommentForm()
    context = {'post': post, 'form': form}
    return render(request, 'blog/detail.html', context)
