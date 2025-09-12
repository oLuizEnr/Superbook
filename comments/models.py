from django.db import models
from heroes.models import Hero
from posts.models import Post

# Create your models here.
class Comentario(models.Model):
    conteudo = models.CharField(max_length=200)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post")
    autor = models.ForeignKey(Hero, on_delete=models.CASCADE, related_name="autor")
    criado_em = models.DateTimeField(auto_now_add=True)

# Luiz Enrique