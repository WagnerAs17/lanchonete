class Pedido:

    def __init__(self, nomeCliente, taxaDeServico, itensConsumido):
        self.nomeCliente = nomeCliente
        self.taxaDeServico = taxaDeServico
        self.itensConsumido = itensConsumido

    def calcular(self):
        valorTotal = 0
        for prato in self.itensConsumido:
            valorTotal += prato.quantidade * prato.valor

        valor_taxa_final = valorTotal * self.taxaDeServico / 100
        valor_total_com_taxa = valorTotal + valor_taxa_final
        return valorTotal, valor_taxa_final, valor_total_com_taxa

    def exibir_pedido(self):
        informacoes_pedido = "Cliente: " + self.nomeCliente + "\n"
        informacoes_pedido += f"Taxa de Service: {self.taxaDeServico}%\n"
        for prato in self.itensConsumido:
            informacoes_pedido += str(prato) + "\n"

        valorTotal, taxa_calculada, valor_total_com_taxa = self.calcular()
        informacoes_pedido += f"Valor Total: {valorTotal} - Taxa Calculada: {taxa_calculada:.2f} " \
                              f"Valor Total + taxa calculada: {valor_total_com_taxa}"

        print(informacoes_pedido)