from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self): return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=200)
    marca = models.CharField(max_length=100) 
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descricao = models.TextField(blank=True, null=True) 
    def __str__(self): return f"{self.marca} - {self.nome}"

class Ingrediente(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='ingredientes')
    nome_ativo = models.CharField(max_length=100) 
    porcentagem = models.CharField(max_length=10) 
    descricao = models.TextField(blank=True, null=True)
    def __str__(self): return self.nome_ativo

class Estoque(models.Model):
    produto = models.OneToOneField(Produto, on_delete=models.CASCADE, related_name='estoque')
    quantidade = models.IntegerField(default=0)
    data_validade = models.DateField(null=True, blank=True)
    # Removido o placeholder que causava o erro
    localizacao = models.CharField(max_length=50, blank=True, null=True, help_text="Ex: Prateleira 1")
    ultima_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self): 
        return f"Estoque de {self.produto.nome}"

class Dica(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    cor_borda = models.CharField(max_length=7, default="#6b0c22") 
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo