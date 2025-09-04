from django.shortcuts import render, redirect
from .models import Post
from django.views.generic import ListView
from .forms import PostForm

# Create your views here.
def lista_posts(request):
    posts = Post.objects.all()
    return render(request,
                  "posts/lista_posts.html",
                  {"postagens": posts}
    )

class PostListView(ListView):
    model = Post
    template_name = "posts/lista_posts.html"
    context_object_name = "postagens"

def criar_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_posts')
    else:
        form = PostForm()

    return render(request,
                  "posts/form_post.html",
                  {"form": form}
    )
    
# Luiz Enrique