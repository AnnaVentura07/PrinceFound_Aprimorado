from django.contrib import admin
from .models import Categoria, Dica, Estoque, Produto

admin.site.register(Categoria)
admin.site.register(Produto)
admin.site.register(Estoque)
admin.site.register(Dica)
