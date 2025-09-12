from django.urls import path
from . import views
from .views import PostListView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    # path('lista/', views.lista_posts, name='lista_posts'),
    path('', PostListView.as_view(), name="lista_posts"),
    # path('novo/', views.criar_post, name="criar_post"),
    path('novo/', PostCreateView.as_view(), name="novo_post"),
    path('<int:pk>/detalhes', views.detalhes_post, name="detalhes_post"),
    path('<int:pk>/editar/', PostUpdateView.as_view(), name="editar_post"),
    path('<int:pk>/deletar/', PostDeleteView.as_view(), name="deletar_post"),
]

# Luiz Enrique