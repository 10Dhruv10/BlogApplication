from django.url import path

urlpatterns = [
    path("<slug:slug>/", views.detail, name="post_detail" ),
]

#first slug is name in url, next slug is parameter passed in views.py in<slug:slug>