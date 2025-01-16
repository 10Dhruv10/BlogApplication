from django.shortcuts import render
from blog.models import PostBlog

def frontpage(request):
    posts = PostBlog.objects.all()                  #queryset with all the rows
    context = {"posts": posts}
    return render(request, "core/frontpage.html", context)
def about(request):
    return render(request, "core/about.html")
