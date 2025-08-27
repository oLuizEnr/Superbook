from django.shortcuts import render
from .models import Post
from django.views.generic import ListView

# Create your views here.
def lista_posts(request):
    posts = Post.objects.all()
    return render(request, "posts/lista_posts.html", {"postagens": posts})

class PostListView(ListView):
    model = Post
    template_name = "posts/lista_posts.html"
    context_object_name = "postagens"
    
# Luiz Enrique