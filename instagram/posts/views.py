from django.shortcuts import render
from posts.models import Post
# Create your views here.
def Post_view(request):
    posts = Post.objects.all().order_by('-id')
    context = {
        'posts': posts
    }
    return render(request, 'index.html', context)
