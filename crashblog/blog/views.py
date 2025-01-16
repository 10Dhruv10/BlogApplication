from django.shortcuts import render, get_object_or_404
from .models import PostBlog

def detail(request, slug):
    post = get_object_or_404(PostBlog, slug = slug)
    context = {'post': post}
    return render(request, 'blog/detail.html', context)
