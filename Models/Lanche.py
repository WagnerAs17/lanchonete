class Lanche:

    def __init__(self, pao, recheio, molho):
        self.pao = pao
        self.recheio = recheio
        self.molho = molho

    def __str__(self):
        return "Lanche - Pão: {0} / Recheio: {1} / Molho: {2}".format(self.pao, self.recheio, self.molho)