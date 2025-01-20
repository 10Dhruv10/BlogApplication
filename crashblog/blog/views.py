from django.shortcuts import render, get_object_or_404, redirect
from .models import PostBlog
from .forms import CommentForm

def detail(request, slug):
    post = get_object_or_404(PostBlog, slug = slug)
    
    if request.method == "POST":
        form =CommentForm(request.POST)
        
        if form.is_valid():
            comment = form.save(commit=False)      #doesnt save it to database
            comment.post = post
            comment.save()
            
            return redirect('post_detail', slug=slug)
    else:
        form = CommentForm()
        
    context = {'post': post, 'form': form}
    return render(request, 'blog/detail.html', context)

#we dont want to save comments to DB and just display them
#3 ways to add attribute data to model, 1. add directly into admin, 2. take input from user using form, 
# 3. initialize value inside code like comment.post = post_taken, comment is CommentForm object, post is its attribute, post_taken is something e.g. an object initialized in views.py