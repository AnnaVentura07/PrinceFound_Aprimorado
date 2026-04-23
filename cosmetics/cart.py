# cart.py
from decimal import Decimal

class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart

    def add(self, produto, quantidade=1):
        produto_id = str(produto.id)
        if produto_id not in self.cart:
            self.cart[produto_id] = {
                'preco': str(produto.preco),
                'quantidade': 0,
                'nome': produto.nome
            }
        self.cart[produto_id]['quantidade'] += quantidade
        self.save()

    def save(self):
        self.session.modified = True

    def remove_by_id(self, produto_id):
        produto_id = str(produto_id)
        if produto_id in self.cart:
            del self.cart[produto_id]
            self.save()
            
    def __iter__(self):
        for produto_id, item in self.cart.items():
            item['id'] = produto_id  
            item['preco'] = Decimal(item['preco'])
            item['total'] = item['preco'] * item['quantidade']
            yield item

    def get_total_price(self):
        return sum(Decimal(item['preco']) * item['quantidade'] for item in self.cart.values())