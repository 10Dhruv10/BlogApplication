from django.db import models
from django.utils import timezone

class PostBlog(models.Model):
    title = models.CharField(max_length=255)
    intro = models.TextField()
    body = models.TextField()
    slug = models.SlugField()    #those goofy ahh site url part 
    created_at = models.DateTimeField(default = timezone.now) #dont use timezone.now() i.e. callable function as parameters but use timezone.now i.e. without brackets
    
    class Meta:
        ordering = ("-created_at",)           #latest one is first i.e. descending
