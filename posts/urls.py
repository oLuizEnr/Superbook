from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.lista_posts, name='lista_posts'),
    path('cbv-lista/', views.PostListView.as_view(), name="cbv_lista_posts")
]

# Luiz Enrique