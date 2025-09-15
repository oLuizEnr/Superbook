from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm
from django.shortcuts import render, get_object_or_404, redirect
from comments.models import Comentario
from comments.forms import ComentarioForm

# Create your views here.
# def lista_posts(request):
#     posts = Post.objects.all()
#     return render(request,
#                   "posts/lista_posts.html",
#                   {"postagens": posts}
#     )

class PostListView(ListView):
    model = Post
    template_name = "posts/lista_posts.html"
    context_object_name = "posts"

# def criar_post(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('lista_posts')
#     else:
#         form = PostForm()

#     return render(request,
#                   "posts/form_post.html",
#                   {"form": form}
#     )

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/form_post.html'
    success_url = reverse_lazy('lista_posts')

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/form_post.html'
    success_url = reverse_lazy('lista_posts')

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'posts/confirmar_exclusao.html'
    success_url = reverse_lazy('lista_posts')

def detalhes_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.post = post
            comentario.save()
            return redirect('detalhes_post', pk=post.id)
    else:
        form = ComentarioForm()

    comments = Comentario.objects.filter(post=pk)

    return render(request, 'posts/detalhes_post.html', {'post': post,
                                                        'comments': comments,
                                                        'form': form})

# Luiz Enrique