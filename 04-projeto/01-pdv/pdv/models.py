from django.db.models import Model, CharField, DecimalField

class Produto(Model):
    nome = CharField(max_length=200)
    preco = DecimalField(decimal_places=2, max_digits=10)

    def __str__(self) -> str:
        return self.nome
    
    def obterIndex(self, produtos):
        return produtos.index(self)


