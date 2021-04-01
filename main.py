from Services.Pedido_Service import PedidoService

def painel():
    pedido_service = PedidoService()
    pedido = pedido_service\
        .fazerLancheComPaoRecheioMolhoValorQuantidade('Hot-Dog', 'Pure de Batata', 'Tomate', 7.50, 1)\
        .fazerLancheComPaoRecheioMolhoValorQuantidade('X-Salada', 'Cheddar', 'Maioneze', 15.52, 3)\
        .fazerSalgadoComRecheioMassaValorQuantidade('Frango', 'Italiana', 2.5, 1)\
        .fazerSalgadoComRecheioMassaValorQuantidade('Carne', 'Italiana', 5.20, 7)\
        .fazerPizzaComMolhoRecheioBordaValorQuantidade('Barbecue', 'Calabreza', False, 35.85, 1)\
        .fazerPizzaComMolhoRecheioBordaValorQuantidade('Azeite', 'Alho', False, 50.25, 3)\
        .fazerPizzaComMolhoRecheioBordaValorQuantidade('Branco', 'Dois Queijo', True, 45.23, 2)\
        .montarPratos()\
        .finalizar_pedido('Wagner Almeida', 10)

    pedido.exibir_pedido()

if __name__ == '__main__':
    painel()