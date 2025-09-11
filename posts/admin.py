from django.contrib import admin
from .models import Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['autor', 'mensagem', 'criado_em']
    # list_filter = ['']
    # search_fields = ['']