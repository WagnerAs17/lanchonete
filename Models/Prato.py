class Prato:
    def __init__(self, quantidade, item, valor):
        self.quantidade = quantidade
        self.item = item
        self.valor = valor

    def __str__(self):
        return f"Item: {self.item} - Valor: {self.valor} - Quantidade: {self.quantidade}"