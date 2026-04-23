from django.apps import AppConfig

class CosmeticsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cosmetics'

    def ready(self):
        from .models import Categoria
        
        lista = [
            "Maquiagens", "Produtos de Limpeza Facial", "Cuidados com a Pele", 
            "Proteção Solar", "Banho", "Kids", "Séruns e Tratamentos", 
            "Hidratação Intensa", "Tonificação", "Esfoliantes", 
            "Cuidado com os Olhos", "Máscaras Faciais"
        ]

        try:
            for item in lista:
                Categoria.objects.get_or_create(nome=item)
        except:
            pass
