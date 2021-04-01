from Models.Pizza import Pizza
from Models.Lanche import Lanche
from Models.Pedido import Pedido
from Models.Prato import Prato
from Models.Salgado import Salgado

class PedidoService:

    def __init__(self):
        self.itens = []
        self.pratos = []

    def adicionarItens(self, quantidade, item, valor):
        self.itens.append([quantidade, item, valor])

    def fazerLancheComPaoRecheioMolhoValorQuantidade(self, pao, recheio, molho, valor, quantidade):
        lanche = Lanche(pao, recheio, molho)
        self.adicionarItens(quantidade, lanche, valor)
        return self

    def fazerPizzaComMolhoRecheioBordaValorQuantidade(self, molho, recheio, borda, valor, quantidade):
        pizza = Pizza(molho, recheio, borda)
        self.adicionarItens(quantidade, pizza, valor)
        return self

    def fazerSalgadoComRecheioMassaValorQuantidade(self, recheio, massa, valor, quantidade):
        salgado = Salgado(recheio, massa)
        self.adicionarItens(quantidade, salgado, valor)
        return self

    def montarPratos(self):
        if len(self.itens) == 0:
            raise Exception("Escolha ao menos um item")
        for item in self.itens:
            prato = Prato(item[0], item[1], item[2])
            self.pratos.append(prato)
        return self

    def finalizar_pedido(self, nome_cliente, taxa_service):
        pedido = Pedido(nome_cliente, taxa_service, self.pratos)
        return pedido